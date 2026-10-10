# AGENTS.md

- Setup: python -m pip install -r requirements.txt && python -m pip install -e . ; cp .env.example .env
- Test: pytest -q must pass before any commit
- Style: ruff check && ruff format; type hints required
- Never commit .env, real student data, or files in data/raw/
- Never push to main; work on a feature branch and open a PR
- Fees and eligibility rules live only in src/tools/, never in prompts
- Do not add new dependencies without asking
