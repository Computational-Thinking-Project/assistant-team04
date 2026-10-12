# Which assistant questions need AI?

Issue: [#46](https://github.com/Computational-Thinking-Project/assistant-team04/issues/46).

## Scope

The project helps students locate university offices and their opening hours.
The current backend in `src/assistant/rules.py` handles known greetings, empty
input, full-name office matches, and unknown-question fallback. It has no LLM,
retrieval pipeline, citation output, partial-name matching, or `help` command.

Here, **needs AI** means a proposed language task that would benefit from an
LLM rather than enumerating many wording rules. It is a design classification,
not a claim that the task is impossible without AI or already implemented.
Use supplied public evidence; AI must not invent university facts.

**Does not need AI** means deterministic code or structured data is enough.
Rows marked *Planned deterministic* are not supported by the current backend.

## Ten questions that need AI for the proposed language path

All ten are future capabilities, conditional on suitable public evidence.

| # | Student question | One-line reason |
|---|---|---|
| 1 | Can you summarize the supplied student support guide in two sentences? | Condensing a supplied document requires language understanding while retaining its supported facts. |
| 2 | Can you explain this public office notice in simpler English? | Simplifying varied prose benefits from controlled paraphrasing grounded in the notice. |
| 3 | Can you translate this supplied office notice into Vietnamese? | Translation handles language variation without changing the notice's facts. |
| 4 | The guide is long; which parts mention getting a replacement student card? | Locating relevant passages across varied wording requires semantic relevance over the supplied guide. |
| 5 | Based on these supplied office descriptions, which office should I contact about a lost student card? | Matching an informal need to published descriptions benefits from semantic intent interpretation. |
| 6 | Can you turn this public procedure into a short checklist without adding steps? | Extracting and reformatting prose steps requires preserving meaning and original order. |
| 7 | What is the difference between the responsibilities of these two offices, according to the supplied descriptions? | A grounded comparison synthesizes differently worded descriptions rather than comparing CSV fields. |
| 8 | I do not understand this phrase in the supplied office guide; can you explain it in context? | Context-sensitive explanation benefits from language understanding beyond exact keyword matching. |
| 9 | Do these two supplied public notices contradict each other about the procedure? | Comparing claims across documents requires semantic analysis and citations, with uncertainty retained. |
| 10 | Can you draft a polite message asking the office to clarify this notice? | Drafting a clear inquiry requires language generation without inventing an official answer or sending it. |

Missing or conflicting evidence must produce a cautious fallback or a request
for clarification. Translation and summarization must preserve dates,
conditions, and qualifications. Fees or eligibility calculations remain
deterministic tasks owned by `src/tools/`; a model must not decide them.

## Ten questions that do not need AI

Examples refer to the repository's demo data, not independently verified
university facts. Current lookup replies return the office's room and full
hours string, even when the question asks for just one of those fields.

| # | Student question / input | Status | One-line reason |
|---|---|---|---|
| 1 | hi | Current | A fixed set of greetings maps directly to a constant response. |
| 2 | Where is the Training Office? | Current | The full office name selects its structured CSV row. |
| 3 | What are the opening hours of the Training Office? | Current | The matching CSV row already contains an hours string to return unchanged. |
| 4 | Where is Student Affairs? | Current | Exact full-name matching retrieves its room and hours without inference. |
| 5 | Where is the Library? | Current | The named office can be located directly in the CSV directory. |
| 6 | When is IT Helpdesk open? | Current | Full-name matching retrieves the existing hours field. |
| 7 | An empty or whitespace-only question | Current | Input normalization detects blank text and returns a fixed prompt. |
| 8 | help | Planned deterministic | A static capability list can be implemented with a command rule, as requested in issue #42. |
| 9 | Where is training? | Planned deterministic | Explicit aliases or tested partial-name matching can resolve this query, as requested in issue #41. |
| 10 | Which offices are listed in the directory? | Planned deterministic | Iterating over CSV office names can produce a directory list without generating facts. |

## Choosing the route

Use rules for known commands and exact data queries. Reserve the proposed AI
path for an in-scope language task with supplied evidence; otherwise keep the
existing fallback. Reject unsupported topics rather than routing every
unmatched message to a model.

Validate usefulness with student examples before enabling AI: compare answer
accuracy and usefulness with the rule-based baseline, and record latency and
provider cost. Exact office lookup should remain available offline.

## Complexity of the deterministic baseline

For CSV size `B`, `N` offices, message length `L`, and maximum office-name
length `K`, the existing backend uses O(B + NLK) time and O(B + L) space for a
non-greeting reply that loads its own dataset. Greeting/blank-input handling
uses O(L) time and space for normalization. Listing an already-loaded
directory would take O(N) time plus the total output length; that feature is
proposed, not implemented. No LLM inference bound is claimed for the future
language tasks.
