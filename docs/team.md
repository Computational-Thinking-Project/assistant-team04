# Team Roster & Roles — Team 04

CSC10014 — Smart Virtual Assistant, HCMUS.

Names, student IDs, and GitHub usernames were supplied by the team.
Nguyễn Bá Duy is the project manager. The roles below organize the seven
skeleton tasks, with Phạm Khánh Tâm responsible for documentation.

| No | Full Name | Student ID | GitHub Username | Role |
|:---|:---|:---|:---|:---|
| 1 | Nguyễn Bá Duy | 25127040 | [@johannguyen015](https://github.com/johannguyen015) | Project Manager / Config |
| 2 | Trương Thành Đạt | 25127035 | [@Thanhdat3010](https://github.com/Thanhdat3010) | Backend Engineer |
| 3 | Nguyễn Nhật Quỳnh | 25127131 | [@nhatquynh1107](https://github.com/nhatquynh1107) | DevOps / Tooling |
| 4 | Hà Trần Bội Anh | 25127013 | [@htbaax](https://github.com/htbaax) | Data Specialist |
| 5 | Nguyễn Đình Hùng | 25127194 | [@benalexx007](https://github.com/benalexx007) | QA / Test Engineer |
| 6 | Dương Trung Anh | 25127012 | [@philip-trkk](https://github.com/philip-trkk) | UI/UX Designer |
| 7 | Phạm Khánh Tâm | 25127135 | [@AI-WFox](https://github.com/AI-WFox) | Documentation Lead |

## Branches and ownership

Member numbers match the roster above and the seven-task skeleton plan.

| Member | Branch | Assigned files |
|:---|:---|:---|
| 1 | `feat/config` | `.gitignore`, `requirements.txt`, `pyproject.toml` |
| 2 | `feat/backend` | `src/assistant/__init__.py`, `src/assistant/rules.py`, `src/assistant/__main__.py` |
| 3 | `feat/scripts` | `scripts/check_env.py` |
| 4 | `feat/data` | `data/offices.csv`, `data/README.md` |
| 5 | `feat/tests` | `tests/test_smoke.py` |
| 6 | `feat/ui` | `ui/README.md` |
| 7 | `feat/docs` | `README.md`, `docs/README.md`, `docs/team.md` |

This table records the planned skeleton assignment. The corresponding files
are delivered through their owners' separate PRs.

## Review and milestone responsibilities

Each member opens a PR from their branch into the team repository's `main`.
A teammate or the project manager reviews the change before merging. The
recommended merge order is config, backend, scripts, data, tests, UI, then docs.
After all seven PRs are merged and setup checks pass, Member 1 creates and
pushes the `v0.1-setup` tag.
