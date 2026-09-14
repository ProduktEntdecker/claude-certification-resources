# CCAR-F Practice Trainer

> Practice questions written by Florian Steiner for learning. Not affiliated with, endorsed by, or derived from the Anthropic certification exam.

170 scenario-based practice questions for the five domains of the Claude Certified Architect Foundations (CCAR-F) blueprint, plus a trainer page that runs in any browser without installation. Shared with participants of the session "Claude Certification Programme for Partners", Barcelona, 23 September 2026.

## Files

| File | Purpose |
|---|---|
| `index.html` | The trainer. Self-contained: no build step, no external scripts, no network calls. |
| `questions.json` | The question file. |
| `schema.json` | JSON Schema (draft 2020-12) for `questions.json`. |
| `PROVENANCE.md` | Where the questions come from, what was excluded, and why. |

## How to use

**Option 1: open the file.** Double-click `index.html`. Browsers block `fetch` for pages opened from `file://`, so the page uses the copy of the questions embedded in it. Works offline.

**Option 2: serve the folder.** The page then loads `questions.json` next to it:

```bash
cd trainer
python3 -m http.server 8000
# open http://localhost:8000/
```

If `questions.json` cannot be read, the page falls back to the embedded copy. Edits to `questions.json` show up only in option 2; the embedded copy is the state at build time.

### Modes

- **Practice by domain.** Pick one or more domains, optionally only unanswered questions or those you got wrong last time. After each answer you see whether it was right, the correct answer, and the explanation.
- **Mock exam.** N random questions (default 60) with a 120-minute timer, no feedback until you submit. By default the draw is balanced by domain share (27, 18, 20, 20, 15 percent). You get a score, a per-domain breakdown, and a review of every wrong or unanswered question, and can practice those again. An unfinished mock exam is saved and can be resumed.
- **Progress.** Answer history and recent mock results are stored in your browser's localStorage only. Nothing leaves your device. Use Reset progress to clear it.

Keyboard: `1` to `4` or `A` to `D` choose an answer, `Enter` checks or moves on, `N` next, `P` previous and `F` flag (mock exam). Options keep their letters when shuffled, so the letters in an explanation always match what you see.

## Question set

| Domain | Questions |
|---|---:|
| Agentic Architecture & Orchestration | 38 |
| Tool Design & MCP Integration | 32 |
| Claude Code Configuration & Workflows | 39 |
| Prompt Engineering & Structured Output | 33 |
| Context Management & Reliability | 28 |
| **Total** | **170** |

159 single-choice and 11 multiple-response items. Ids come from the author's source bank; gaps in the numbering are items that were left out (see `PROVENANCE.md`).

## JSON format

```json
{
  "version": "1.0.0",
  "generated": "YYYY-MM-DD",
  "certification": "CCAR-F",
  "disclaimer": "...",
  "license_note": "...",
  "questions": [
    {
      "id": "d1-mc-001",
      "domain": "Agentic Architecture & Orchestration",
      "scenario": "...",
      "question": "...",
      "options": [{ "key": "A", "text": "..." }],
      "answer": ["A"],
      "explanation": "...",
      "difficulty": "medium",
      "tags": ["task 1.1", "Agentic Loop Design", "single-choice"],
      "source": "self-written by Florian Steiner"
    }
  ]
}
```

| Field | Meaning |
|---|---|
| `id` | Stable id `d<domain>-<mc or mr>-<number>`; `mc` single choice, `mr` multiple response. |
| `domain` | One of the five domain names in the table above. |
| `scenario`, `question` | Context and the actual question. Inline code is marked with backticks. |
| `options` | Answer options with letter `key` and `text`. |
| `answer` | Keys of all correct options. Multiple-response items are scored as an exact match, no partial credit. |
| `explanation` | Why the answer is right and the others are not. Letters refer to option keys. |
| `difficulty` | Coarse heuristic: multiple-response `hard`, single-choice `medium`. Not calibrated. |
| `tags` | Task number and name, anti-pattern name where relevant, answer format. |
| `source` | Always `self-written by Florian Steiner`. |

Validate a modified file:

```bash
pip install jsonschema
python3 -c "import json, jsonschema; jsonschema.validate(json.load(open('questions.json')), json.load(open('schema.json'))); print('valid')"
```

## Disclaimer

Practice questions written by Florian Steiner for learning. Not affiliated with, endorsed by, or derived from the Anthropic certification exam. They are practice material, not real exam questions, and a score here does not predict a result on any real exam.

Shared for session participants. Ask the author before republishing.
