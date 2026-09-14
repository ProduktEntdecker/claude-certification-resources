# Provenance of questions.json

How the shared question file was assembled from the author's private practice simulator, which items were left out, and why.

Generated 2026-09-14.

## Counts

| Stage | Items |
|---|---:|
| Found in the author's private practice simulator | 269 |
| of which CCAR-F practice items | 186 |
| of which items from a third-party CCAR-P practice set | 83 |
| Excluded as third-party | 83 |
| Excluded because the origin could not be verified | 13 |
| Dropped by overlap check against official sample questions | 3 |
| **Final, in questions.json** | **170** |

Check: 269 - 83 - 13 - 3 = 170.

## Sources inspected

- The author's private question banks and their change history.
- The official exam guides for Claude Certified Architect: Foundations (CCAR-F), Claude Certified Architect: Professional (CCAR-P) and Claude Certified Associate: Foundations (CCAO-F), which contain the official sample questions. Links and retrieval date: [README, section 7](../README.md#7-sources).
- Nothing from private notes, training logs, participant data or course material is included in the output.

## Method

### 1. Authorship filter

- Third-party: the 83 items of a third-party CCAR-P practice set are excluded. They were kept in the private simulator with attribution and are not the author's work.
- Origin not verifiable: 13 items whose creation could not be traced to the author's own study notes are excluded (when in doubt, exclude).
- Kept: all other CCAR-F items. The author's records describe them as original questions written from his own study notes; they were drafted with an AI coding assistant and reviewed by the author.

### 2. Overlap check against official sample questions

- Text extraction with `pdftotext -layout`; page headers stripped.
- Official sample items: 18 (CCAR-F guide section 9: 12 questions; CCAR-P guide section 8: 3; CCAO-F guide section 8: 3), each split into full stem, scenario part, question sentence, options, and rationale.
- Normalization: lower case, punctuation removed, token sets.
- Automatic flags (threshold 0.6, token Jaccard), computed for all 186 x 18 = 3,348 pairs: trainer question, scenario, or scenario plus question vs the official full stem; trainer question vs the official question sentence; trainer scenario vs the official scenario part; identical normalized option set, or two or more options with Jaccard >= 0.6 against options of the same official item.
- Secondary signals for manual review: stop-word-free content overlap and containment, explanation vs official rationale, and the longest shared run of tokens (reported at 6 or more).
- Manual review: every automatically flagged pair, every pair with a shared run of 6 or more tokens, and the six most similar trainer items for each official item.
- Safety net: the same metrics against the 83 third-party CCAR-P items.

### 3. Results of the overlap check

- 27 automatic flags. 25 of them pair different trainer items with CCAO-F sample 3 only because both use a boilerplate question sentence ('What is the most appropriate action?' vs '... fix?', '... remediation?'); content overlap <= 0.10, best option Jaccard <= 0.29, no shared phrase beyond the question frame. Reviewed, kept.
- The remaining 2 flags (d3-mc-036 vs Q10, d2-mc-001 vs Q2) were confirmed as near-verbatim and dropped. Manual review of the top candidates added d3-mc-016 (option set paraphrasing Q6). Total dropped: 3.
- Shared runs of 6 or more tokens: 10 pairs. Besides the dropped items and d1-mc-037 (already excluded as unclear), they are generic phrases (e.g. 'model with a larger context window', 'the result to stdout and exits').
- After the drops, no item in the output copies or paraphrases an official option set, and no official sample question text is included.
- Third-party safety net: 27 flags against the CCAR-P set, all boilerplate question sentences such as 'What is the most appropriate next step?' (content overlap <= 0.11, best option Jaccard <= 0.29). No substantive overlap.

Items reviewed manually and kept (closest official sample, same topic but original scenario, options, and wording):

| Item | Closest official sample | Signals | Decision |
|---|---|---|---|
| d1-mc-010 | CCAR-F guide Q1 | content 0.10, best option 0.26, no shared run >= 6 | Same principle (enforce critical rules in code, not in the prompt), different scenario (refund cap with manager approval) and different options. Kept. |
| d3-mc-005 | CCAR-F guide Q4 | content 0.11, best option 0.24, no shared run >= 6 | Same topic (project-scoped commands in .claude/commands/), different scenario (release workflow) and options. Kept. |
| d1-mc-006 | CCAR-F guide Q8 | content 0.07, best option 0.23, no shared run >= 6 | Same topic (structured error back to the coordinator), different failure (rate limit) and options. Kept. |
| d4-mc-016 | CCAR-F guide Q11 | content 0.15, best option 0.12, shared run 6 ('to the Message Batches API for') | Different trade-off (multi-turn tool loop vs single-shot job). Shared run is a generic phrase. Kept. |
| d3-mc-037 | CCAR-F guide Q10 | content 0.05, best option 0.14, shared run 6 ('the result to stdout and exits') | Asks what -p does, not how to fix a hanging CI job; different options. Written in the same step as dropped d3-mc-036. Kept. |
| d3-mc-038 | CCAR-F guide Q10 | no flag, no shared run >= 6 | Covers --output-format json and --json-schema, which Q10 does not. Kept. |
| d5-mc-001, d5-mc-007, d5-mc-020 | CCAR-F guide Q12 | content <= 0.10, shared run 6 ('model with a larger context window') | Different topics (case facts, scratchpad files). Shared run is a common distractor phrase. Kept. |
| d2-mc-009 | CCAR-P guide Sample 1 | content 0.02, best option 0.29, no shared run >= 6 | Same principle (least privilege), different scenario (synthesis subagent with 22 tools) and options. Kept. |
| d4-mc-007 | CCAO-F guide Sample 3 | shared run 6 ('data what is the most appropriate') | Boilerplate question frame only. Kept. |
| 25 items (d1-mc-005, d1-mc-013, d1-mc-025, d1-mc-030, d1-mc-031, d1-mc-032, d2-mc-005, d2-mc-009, d2-mc-022, d2-mc-023, d2-mc-030, d3-mc-026, d3-mc-030, d3-mc-031, d3-mc-032, d4-mc-003, d4-mc-013, d4-mc-027, d4-mc-028, d4-mc-029, d4-mc-030, d5-mc-004, d5-mc-006, d5-mc-017, d5-mc-019) | CCAO-F guide Sample 3 | question sentence Jaccard 0.62 to 0.86 on a boilerplate frame; content <= 0.10 | False positives on 'What is the most appropriate ...?'. Kept. |

### 4. Editorial changes

- Em-dash characters (U+2014) replaced in 29 of 170 items (47 fields): a pair inside one sentence became parentheses, a single dash became a colon, a semicolon, or a comma. No other wording was changed; the validation script compares every field with the source after ignoring these punctuation marks.
- Correct answers, option keys, and option order are identical to the source.
- Typo scan: automated doubled-word and whitespace scan found nothing to fix.
- Added metadata: `domain` uses the author's domain names; `tags` carry the task number and task name from the author's simulator, the anti-pattern name where the source has one, and the answer format; `difficulty` is a coarse heuristic (multiple-response items `hard`, single-choice items `medium`), not a calibrated rating.

### 5. Residual risks

- For 13 items the origin could not be verified, so they were excluded rather than compared. The kept items carry no per-item source note; the author's records describe them as original.
- Community practice exams that the repo only links to (not vendored) could not be compared.
- The overlap check is lexical. A question with the same concept but different wording is caught only by manual review of the top candidates, which covered 6 items per official sample plus all flags.
- difficulty is a heuristic, not a calibrated rating.

## Dropped items

| Item | Category | Reason |
|---|---|---|
| d2-mc-001 | overlap check | Question sentence near-verbatim to CCAR-F guide sample Q2 (Jaccard 0.64, shared phrase 'first step to improve tool selection'), testing the same concept with the same distractor families (pre-routing classifier, merging the tools). Dropped after manual review. |
| d3-mc-016 | overlap check | Option set is a close paraphrase of CCAR-F guide sample Q6: all four options map one to one in the same order with the same correct key, an 8-token verbatim phrase ('relying on Claude to infer which section applies'), and the same 'most maintainable' question. Dropped after manual review (best single-option Jaccard 0.5, below the automatic threshold). |
| d3-mc-036 | overlap check | Near-verbatim to CCAR-F guide sample Q10: 30-token verbatim run, question sentence Jaccard 0.73, all four options Jaccard >= 0.6 (same prompt text and the same three distractors). |
| d1-mc-037 | origin not verifiable | Origin could not be traced to the author's own study notes; excluded. It also shares a 9-token phrase and its key option with CCAR-F guide sample Q1. |
| d2-mc-032 | origin not verifiable | Origin could not be traced to the author's own study notes; excluded. |
| d2-mc-033 | origin not verifiable | Origin could not be traced to the author's own study notes; excluded. |
| d2-mc-034 | origin not verifiable | Origin could not be traced to the author's own study notes; excluded. |
| d3-mc-039 | origin not verifiable | Origin could not be traced to the author's own study notes; excluded. |
| d3-mc-040 | origin not verifiable | Origin could not be traced to the author's own study notes; excluded. |
| d3-mc-041 | origin not verifiable | Origin could not be traced to the author's own study notes; excluded. |
| d4-mc-032 | origin not verifiable | Origin could not be traced to the author's own study notes; excluded. |
| d4-mc-033 | origin not verifiable | Origin could not be traced to the author's own study notes; excluded. |
| d4-mc-034 | origin not verifiable | Origin could not be traced to the author's own study notes; excluded. |
| d5-mc-027 | origin not verifiable | Origin could not be traced to the author's own study notes; excluded. |
| d5-mc-028 | origin not verifiable | Origin could not be traced to the author's own study notes; excluded. |
| d5-mc-029 | origin not verifiable | Origin could not be traced to the author's own study notes; excluded. |
| 83 items (p-d1-q01 to p-d7-q04) | third-party | Third-party CCAR-P practice set, not the author's work. |
