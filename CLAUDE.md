# CLAUDE.md

Guidance for Claude Code in this repository.

## Project

- **Purpose:** Public facts on the Claude certifications and the Claude Partner Network, preparation links, and a practice trainer with self-written questions.
- **Session:** "Claude Certification Programme for Partners", Claude Community House Barcelona, Wednesday 23 September 2026, 15:00 to 16:00, Room 4
- **Visibility:** private. It becomes public only after Florian explicitly approves it, shortly before the session.

## Structure

```text
README.md          eligibility, the four certifications, logistics, Partner Network, preparation, sources
trainer/           practice trainer: index.html, questions.json, schema.json, PROVENANCE.md
docs/agenda.html   session agenda with timeline (print to PDF)
docs/agenda.pdf    exported agenda
scripts/hooks/     pre-commit secret scan
```

## Content rules

- English for everything participants see.
- No em-dash characters (U+2014). Use commas, colons or parentheses instead.
- No secrets, no client data, no real names of participants or customers.
- Every fact about exams, fees, eligibility or the Partner Network needs a source URL and a retrieval date.
- Never copy official sample questions from the exam guides and never add third-party question sets. `trainer/questions.json` holds only questions written by Florian Steiner; record every change in `trainer/PROVENANCE.md`.
- Never describe the practice questions as real exam content.

## Git workflow

Issue, branch, pull request, CodeRabbit review, squash merge. Never commit directly to `main`.

Every session works in its own worktree; the main checkout stays on `main`:

```bash
git worktree add -b feat/<NR>-<short> .claude/worktrees/<NR>-<short> origin/main
```

One worktree, one branch, one issue. Put `Closes #<NR>` in the pull request body and remove the worktree after the merge (`git worktree remove <path>`).

## Security

- Secrets live in `.env` (ignored by git) or 1Password, never in the repository.
- `scripts/hooks/pre-commit` scans staged files for secrets. Install it once per clone:
  `cp scripts/hooks/pre-commit .git/hooks/pre-commit && chmod +x .git/hooks/pre-commit`
