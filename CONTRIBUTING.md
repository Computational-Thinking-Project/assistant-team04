# Contributing to assistant-team04

## Workflow
1. Every change starts as an issue on the board.
2. Branch from main: feat/<issue>-<short-name> (fix/, docs/, test/, chore/).
3. Small commits in Conventional Commits style.
4. Open a PR using the template; link the issue ("Closes #12").
5. At least 1 approval from another member; CI must be green.
6. Squash and merge; delete the branch.

## Rules
- Never push to main. Never force-push shared branches.
- No secrets, no real personal data, no files > 5 MB.
- Review requested PRs within 24 hours.
- Record AI use in the PR and in docs/ai-use-log.md.
- Pair work: add Co-authored-by trailers.

## Secrets & Configuration
- **Local Credentials**: Real API keys, tokens, and credentials belong **only** in a local `.env` file (`cp .env.example .env`).
- **Never Commit Secrets**: Never commit `.env`, private keys, passwords, database credentials, or real personal/student data to Git.
- **Gitignore Protection**: `.env` and `.env.*` are ignored by `.gitignore` (with `!.env.example` kept tracked as a template). Always verify with `git status` that `.env` is never staged.
- **Placeholders in Examples**: `.env.example` must contain only safe dummy values (e.g., `changeme`, `sqlite:///dev.db`).
- **Accidental Leak Protocol**: If a secret is accidentally committed and pushed:
  1. Immediately revoke and rotate the secret with the provider.
  2. Remove the secret from code history and notify the Tech Lead and team immediately (see Git Tutorial Chapter 13).