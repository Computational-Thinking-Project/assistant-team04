# Security & Secret Audit Report

This document records the comprehensive repository security audit conducted for Lab 02, fulfilling the acceptance criteria of **Issue #50** (`Security: review repo for personal data and secrets`).

---

## 1. Audit Metadata & Scope

| Attribute | Details |
| :--- | :--- |
| **Auditor** | Truong Thanh Dat (`@Thanhdat3010`) |
| **Audit Date** | 2026-10-13 |
| **Audit Revision / Cutoff** | `61663ee9af617990d77ae563618b3c9821e5429b` (`origin/main`) |
| **Scope** | All 88 tracked repository files, complete Git commit history across branches (56 commits), sample datasets, documentation, and Python bootcamp submissions. |
| **Objective** | Verify zero committed credentials (API keys, secret tokens, private keys, passwords) and zero unauthorized private personal data. |

---

## 2. Tools and Inspection Methodology

### A. Dedicated Secret Scanner: Gitleaks

The audit executed **Gitleaks** directly against the repository's active workspace and complete git revision history.

* **Tool Version**: `Gitleaks v8.24.0` (windows_x64)
* **Execution Commands**:
  ```sh
  # Scan active workspace and full Git commit history
  gitleaks detect --source . --verbose --report-format json --report-path docs/gitleaks-report.json
  ```
* **Sanitized Execution Output**:
  ```text
      ○
      │╲
      │ ○
      ○ ░
      ░    gitleaks

  INF 56 commits scanned.
  INF scanned ~115593 bytes (115.59 KB) in 429ms
  INF no leaks found
  ```
* **Scan Result**: Exit code `0`, finding count: `0` (empty JSON result `[]`). Zero credentials or high-entropy tokens detected in history.

---

### B. Secondary Automated Pattern Scan (Regex Audit)

A supplementary regex pattern audit was executed across all 88 tracked files and git diffs, checking for common credential formats and private personal data:

* **OpenAI & Anthropic Secret Keys**: `sk-[a-zA-Z0-9]{20,}`
* **GitHub Personal Access Tokens**: `gh[pousr]_[A-Za-z0-9_]{16,}`
* **AWS Access Keys**: `AKIA[0-9A-Z]{16}`
* **GitLab Tokens**: `glpat-[a-zA-Z0-9\-]{20,}`
* **Generic API Keys & Secrets**: `(?i)(api[_-]?key|secret|token|password|auth)\s*[:=]\s*["'][^"']+["']`
* **Private Key Headers**: `-----BEGIN [A-Z ]*PRIVATE KEY-----`
* **Vietnamese Phone Numbers**: `(?<!\d)(?:0|\+84)(?:3|5|7|8|9)\d{8}(?!\d)`
* **Vietnamese Citizen ID (CCCD)**: `(?<!\d)\d{12}(?!\d)`

*All detected dummy placeholders (`changeme`, `sqlite:///dev.db`) in `.env.example` were manually inspected and confirmed to be non-sensitive template values.*

---

### C. Manual Repository & Privacy Review

1. **Environment & Ignore Rules**:
   - Verified that `.env` is uncommitted and properly ignored by `.gitignore`.
   - Confirmed `.env.example` contains only descriptive comments and safe placeholder values (`changeme`).
2. **Datasets (`data/` folder)**:
   - Audited `data/offices.csv` and `data/README.md`: confirmed only publicly available HCMUS campus office locations, rooms, and working hours are listed.
   - Zero student personal information or confidential university records present.
3. **Documentation & Roster (`docs/team.md`, `PROGRESS.md`)**:
   - Confirmed only standard, syllabus-mandated academic identifiers (student full name, student ID, institutional email, GitHub handle) are included.
   - Zero private phone numbers, home addresses, or citizen identity numbers.

---

## 3. Findings & Audit Summary

| Category | Checked Items / Rules | Finding Summary | Status |
| :--- | :--- | :--- | :---: |
| **Gitleaks Scan** | 56 commits, all branches, active tree | 0 secret leaks found | **PASS** |
| **API Keys & Tokens** | OpenAI, GitHub, AWS, Generic credentials | 0 leaks detected | **PASS** |
| **Private Keys & Certificates** | RSA, OpenSSH, PGP headers | 0 leaks detected | **PASS** |
| **Passwords & DB URIs** | Plaintext credentials, connection strings | 0 leaks detected | **PASS** |
| **Environment Files** | `.env`, `.env.local`, `.env.production` | Untracked; protected by `.gitignore` | **PASS** |
| **Private Personal Data** | Phone numbers, citizen IDs (CCCD), home addresses | 0 violations detected | **PASS** |

**Remediation Required**: None. All checks passed without violations.

---

## 4. Ongoing Preventive Measures

To maintain repository security across future milestones:
1. **Pre-Commit Checks**: Developers should run `git status` and `gitleaks protect --staged` locally before committing.
2. **Secret Incident Procedure**: If any secret is accidentally committed, follow Section 13.2 of the Git Tutorial: immediately revoke and rotate the secret at the provider, remove it from git history, and notify the Tech Lead.
