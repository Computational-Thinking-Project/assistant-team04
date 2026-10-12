# Security & Secret Audit Report

This document records the repository security audit conducted for Lab 02, fulfilling the requirements of **Issue #50** (`Security: review repo for personal data and secrets`).

---

## 1. Audit Metadata & Scope

| Attribute | Details |
| :--- | :--- |
| **Auditor** | Truong Thanh Dat (`@Thanhdat3010`) |
| **Date** | 2026-10-12 |
| **Checked Revision** | `7610839214c22049d72a83f59de2bff3af3a6ccc` (and current `main` HEAD) |
| **Scope** | All 82 tracked repository files, complete Git commit history across branches, documentation, sample datasets, and Python bootcamp submissions. |
| **Objective** | Verify zero committed secrets (API keys, tokens, credentials, private keys) and zero unauthorized private personal data. |

---

## 2. Tools and Inspection Methodology

### A. Automated Pattern Scan (Gitleaks / High-Entropy Rules)
An automated rule-based regex scanner was executed across all tracked files and the entire commit log (`git log -p --all`), checking for standard credential patterns:
* **OpenAI Secret Keys**: `sk-[a-zA-Z0-9]{20,}`
* **GitHub Tokens**: `ghp_[a-zA-Z0-9]{36}`, `gho_[a-zA-Z0-9]{36}`
* **AWS Access Keys**: `AKIA[0-9A-Z]{16}`
* **GitLab Tokens**: `glpat-[a-zA-Z0-9\-]{20,}`
* **Generic API Keys & Passwords**: `(?i)(api[_-]?key|password)\s*[:=]\s*["'][^"']+["']`
* **Private Key Headers**: `-----BEGIN [A-Z]+ PRIVATE KEY-----`

### B. Manual Verification
* Verified that `.env` is uncommitted and listed in `.gitignore`.
* Inspected `.env.example` to ensure only dummy placeholders (`changeme`, `sqlite:///dev.db`) exist.
* Inspected `data/` folder to ensure sample datasets (`offices.csv`, `tasks.csv`) contain no confidential student information.
* Reviewed `docs/team.md` and `PROGRESS.md` to ensure only standard, syllabus-mandated academic identifiers (student ID, institutional email, GitHub handle) are present.

---

## 3. Findings & Audit Results

| Category | Checked Items | Findings | Status |
| :--- | :--- | :---: | :---: |
| **API Keys & Tokens** | OpenAI, GitHub, AWS, Generic keys | 0 leaks detected | **PASS** |
| **Private Keys & Certificates** | RSA, OpenSSH, PGP headers | 0 leaks detected | **PASS** |
| **Passwords & DB Credentials** | Connection strings, plaintext credentials | 0 leaks detected | **PASS** |
| **Environment Files** | `.env`, `.env.local`, `.env.production` | Completely untracked; ignored by `.gitignore` | **PASS** |
| **Private Personal Data** | Phone numbers, personal home addresses, IDs | 0 violations detected | **PASS** |

**Conclusion:** The repository is clean and compliant with the course security policies. No remediation or key revocation is required.

---

## 4. Ongoing Preventive Measures

To maintain this security posture throughout the semester:
1. **Local Credentials Only**: Keep real API keys exclusively in local `.env` files.
2. **Pre-Commit Verification**: Run `git status` before committing to confirm no untracked secrets are staged.
3. **Emergency Protocol**: If an API key is ever committed, immediately revoke/rotate the key at the provider, remove it from Git history, and inform the Tech Lead per Section 13.2 of the Git Tutorial.
