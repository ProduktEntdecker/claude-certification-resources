#!/usr/bin/env python3
"""Validate questions.json.

Runs the JSON Schema check when the jsonschema package is installed, then the
rules a schema cannot express: unique ids, unique option keys, every answer key
is an option, answer count per type (mc exactly one, mr at least two), and the
copy embedded in index.html matches questions.json.

Usage: python3 validate.py [questions.json] [schema.json] [index.html]
"""
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent


def main() -> int:
    args = sys.argv[1:]
    qpath = pathlib.Path(args[0]) if len(args) > 0 else HERE / "questions.json"
    spath = pathlib.Path(args[1]) if len(args) > 1 else HERE / "schema.json"
    hpath = pathlib.Path(args[2]) if len(args) > 2 else HERE / "index.html"
    data = json.loads(qpath.read_text(encoding="utf-8"))
    errors = []

    try:
        import jsonschema
    except ImportError:
        print("note: jsonschema is not installed, schema check skipped (pip install jsonschema)")
    else:
        schema = json.loads(spath.read_text(encoding="utf-8"))
        validator = jsonschema.Draft202012Validator(schema)
        for err in sorted(validator.iter_errors(data), key=lambda e: list(e.path)):
            where = "/".join(str(p) for p in err.path) or "(root)"
            errors.append(f"schema: {where}: {err.message}")

    seen = set()
    for index, question in enumerate(data.get("questions", [])):
        qid = question.get("id", f"#{index}")
        if qid in seen:
            errors.append(f"{qid}: duplicate id")
        seen.add(qid)
        keys = [option.get("key") for option in question.get("options", [])]
        if len(keys) != len(set(keys)):
            errors.append(f"{qid}: duplicate option keys {keys}")
        answer = question.get("answer", [])
        missing = [key for key in answer if key not in keys]
        if missing:
            errors.append(f"{qid}: answer keys not among the options: {missing}")
        kind = re.search(r"-(mc|mr)-", qid)
        if not kind:
            errors.append(f"{qid}: id must contain -mc- or -mr-")
        elif kind.group(1) == "mc" and len(answer) != 1:
            errors.append(f"{qid}: single choice needs exactly one answer, has {len(answer)}")
        elif kind.group(1) == "mr" and len(answer) < 2:
            errors.append(f"{qid}: multiple response needs at least two answers, has {len(answer)}")

    if hpath.exists():
        html = hpath.read_text(encoding="utf-8")
        block = re.search(r'<script type="application/json" id="questions-data">(.*?)</script>', html, re.S)
        if not block:
            errors.append(f"{hpath.name}: embedded questions-data block not found")
        elif json.loads(block.group(1)) != data:
            errors.append(f"{hpath.name}: embedded copy differs from {qpath.name}, rebuild the page")

    if errors:
        print(f"INVALID: {len(errors)} problem(s)")
        for error in errors:
            print(f" - {error}")
        return 1
    print(f"valid: {len(data['questions'])} questions")
    return 0


if __name__ == "__main__":
    sys.exit(main())
