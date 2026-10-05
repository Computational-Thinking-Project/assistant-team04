# Smart Virtual Assistant — Team 04

A CSC10014 student project at HCMUS. The planned starter helps students find
university office locations and opening hours through a Python command-line
interface using deterministic rules and a CSV office directory.

## Skeleton status

The team is assembling the project through seven separate pull requests.
This documentation contribution adds only the root README and `docs/`.
Configuration, backend, scripts, data, tests, and UI planning belong to the
other members' branches. The setup and usage instructions below apply **after
those skeleton contributions are merged**; this documentation PR alone does
not provide an executable assistant. AI integration and a web UI are future
work.

See the [team roster and assignments](docs/team.md) and the
[documentation index](docs/README.md).

## Requirements

- Python 3.10 or newer.
- Git.
- Internet access to clone the repository and install dependencies.

## Setup (after the skeleton PRs are merged)

Clone the repository and enter its root directory:

```sh
git clone https://github.com/Computational-Thinking-Project/assistant-team04.git
cd assistant-team04
```

Create and activate a virtual environment for your platform.

**Windows PowerShell:**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If activation is blocked by PowerShell, allow local scripts for the current
terminal session, then retry:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
.\.venv\Scripts\Activate.ps1
```

**macOS/Linux:**

```sh
python3 -m venv .venv
source .venv/bin/activate
```

With the environment activated, install the dependencies and package:

```sh
python -m pip install -r requirements.txt
python -m pip install -e .
```

The editable installation makes the `src/assistant/` package importable.
Keep the root-level `data/offices.csv` inside the cloned repository.
Run the following commands from the repository root. Use `deactivate` when
finished.

## Run

Ask a single question:

```sh
python -m assistant "hi"
python -m assistant "Where is the Training Office?"
```

The reference starter responds:

```text
Hello! Ask me where an office is, or when it opens.
Training Office: room I.101, open Mon-Fri 07:30-16:30.
```

These examples assume the backend and data owners retain the reference
starter's rules and dataset; update them if the merged implementation changes.

Start an interactive session:

```sh
python -m assistant
```

Type a question at the prompt. Type `quit` or `exit` to leave.

## Tests and environment checks

```sh
python -m pytest -q
python scripts/check_env.py
```

The reference smoke suite has four tests: greeting, office lookup, unknown
question, and empty input. A successful run reports `4 passed`.
Run these checks again on the assembled team repository.

The environment checker verifies Python, the virtual environment, pytest, Git,
repository metadata, `.gitignore`, README completeness, Git email, and a greeting
response. Run the smoke tests as well to verify office lookup. If a required
file is missing, first confirm that its owner's skeleton PR has been merged.

Set your own commit identity inside the repository if it is missing:

```sh
git config user.name "Your Name"
git config user.email "your-email@example.com"
```

Stage only intended source files. The configuration contribution should ignore
`.venv/`, Python caches, and generated package metadata.

## Planned project structure

The final skeleton should contain the following files. Only `README.md` and
the two `docs/` files are added by Member 7.

```text
assistant-team04/
|-- LICENSE                  # Repository license
|-- README.md                # Project and developer guide
|-- .gitignore               # Generated-file exclusions
|-- pyproject.toml           # Packaging and pytest configuration
|-- requirements.txt         # Dependencies
|-- src/assistant/
|   |-- __init__.py          # Package version
|   |-- __main__.py          # CLI entry point
|   `-- rules.py             # Rule-based replies and CSV loading
|-- scripts/check_env.py     # Developer environment checks
|-- data/
|   |-- offices.csv          # Office names, rooms, and hours
|   `-- README.md            # Dataset source and maintenance notes
|-- tests/test_smoke.py      # Baseline behavior tests
|-- ui/README.md             # Future UI plan
`-- docs/
    |-- README.md            # Documentation index
    `-- team.md              # Roster and task ownership
```

## Baseline behavior and limitations

The reference responder normalizes input, checks greetings, loads the CSV, and
returns the first office whose full name occurs in the question. An unmatched
question receives a fallback response. It provides no fuzzy matching or
language-model integration. Confirm starter rooms and hours with the university
before presenting them as authoritative information.

For CSV size `B`, `N` offices, question length `L`, and maximum office-name
length `K`, CSV loading costs O(B) time and space. A conservative substring
search bound is O(NLK) time. A non-greeting reply that loads its own data uses
O(B + NLK) time and O(B + L) space; the reference starter reloads data for each
such question. Update these bounds if the backend changes.

Before adding AI or a web UI, validate that students can obtain accurate office
information and that campus staff can maintain the dataset.

## Contribution workflow

Work on the branch assigned in `docs/team.md`, commit only your contribution,
and open a PR into this repository's `main`. Contributors without write access
can use a personal fork. A teammate or the project manager reviews each PR.

Member 7 uses `feat/docs` for `README.md`, `docs/README.md`, and `docs/team.md`.
After all seven PRs are merged and setup checks pass, Member 1 can create the
`v0.1-setup` milestone tag.
