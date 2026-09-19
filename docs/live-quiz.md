# Live quiz: run of show

Facilitator notes for the 15 minute block at 15:25 in "Claude Certification Programme for Partners".

Goal: show what the exam actually asks, without reproducing exam content. Official sample questions stay in the official guides; we show them from the source and never copy them into slides, handouts or the practice trainer.

## Before the session

- [ ] Download the exam guide PDFs (links in README section 2) and keep local copies. The venue network is unknown.
- [ ] Open the CCAR-F guide at its sample questions section in one window.
- [ ] Open `trainer/index.html` in a second window and paste the three ids into Presenter mode, so the run is one click away on stage.
- [ ] Keep README section 1 (who can take the exams) at hand, the question comes up every time.

## Part 1: two official sample questions, 6 minutes

Show them from the guide PDF on screen.

1. Read the scenario out loud, then the question, then the four options.
2. Show of hands per option before revealing anything.
3. Reveal the official rationale from the guide, then name the pattern: scenario first, one question, four options of which two look plausible.

## Part 2: three questions from the practice trainer, 7 minutes

Paste these ids into **Presenter mode** on the trainer home screen and press Start presenter run. They run in exactly this order, without shuffling:

```text
d1-mc-010, d1-mc-006, d2-mc-009
```


| Id | What it tests |
|---|---|
| d1-mc-010 | Enforce a critical rule in code, not in the prompt |
| d1-mc-006 | Return a structured error to the coordinator instead of retrying blindly |
| d2-mc-009 | Least privilege when a subagent gets too many tools |

Say plainly what these are: practice questions written by the host, close in shape to the official ones, not exam content.

## Part 3: the difference, 2 minutes

- The trainer has 170 practice questions and no official material. Provenance is documented in `trainer/PROVENANCE.md`.
- Eligibility: the exams are open to people at Claude Partner Network organisations with a company email address, membership is free. (Sources: Anthropic Partner Academy, Certification FAQ, https://anthropic-partners.skilljar.com/page/faq-certifications, and https://claude.com/partners, both retrieved 14 September 2026. Full wording in README section 1.)
- Where to start: README sections 1 and 5.

## If something fails

- No network: the trainer runs from the local file, it carries an embedded copy of the questions.
- No projector: run Part 2 as a spoken quiz, the questions work read out loud.
- Short on time: drop Part 2 to one question, never drop Part 3.
