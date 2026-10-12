# Future AI service interface

Issue: [#45](https://github.com/Computational-Thinking-Project/assistant-team04/issues/45).

## Status and purpose

This is a proposed contract, not an implemented API. The application currently
uses `assistant.rules.reply` and makes no LLM calls. This document adds no
provider SDK, dependency, credential, or runtime behavior.

The assistant helps students find university offices and their opening hours.
Keep exact lookups deterministic. Consider an LLM only for language tasks such
as paraphrasing or summarizing supplied public documents. Validate that those
tasks improve student usefulness before adding provider cost and latency.

## Existing backend

The current public function in `src/assistant/rules.py` is:

```python
def reply(
    message: str,
    offices: dict[str, dict[str, str]] | None = None,
) -> str:
    ...
```

It normalizes case and whitespace, handles empty input and known greetings,
then finds the first full office name occurring in the message. If `offices`
is omitted, it loads `data/offices.csv`. Each office row contains `name`, `room`,
and `hours`. Unknown questions receive a fixed fallback string.

Partial-name lookup and a `help` command are separate pending issues. The
backend currently returns text only; it provides no citation metadata or
structured indication that a question matched. CSV loading can raise errors.

## Proposed application boundary

Illustrative signatures for a future implementation:

```python
def answer(
    message: str,
    *,
    context: list[Source] | None = None,
    provider: LLMProvider | None = None,
    timeout_seconds: float = 5.0,
) -> Answer:
    ...

class LLMProvider:
    def generate(
        self,
        message: str,
        *,
        context: list[Source],
        timeout_seconds: float,
    ) -> GeneratedAnswer:
        ...
```

`Source`, `Answer`, and `GeneratedAnswer` are proposed record types below;
they do not exist in the repository. The provider owns request cancellation
and must respect the timeout, rather than merely accepting it as an argument.
The default provider is absent, preserving an offline rule-based path.

### Inputs

| Input | Contract |
|---|---|
| `message` | A string; trim surrounding whitespace. Proposed limit: 4,096 characters. Reject a non-string or an over-limit value without calling a provider. |
| `context` | Public source records supplied by a future retrieval component; `None` means no context. Proposed limits: 10 records and 20,000 total excerpt characters. Reject records exceeding these limits. |
| `provider` | Optional object implementing `generate`; `None` disables the AI path. |
| `timeout_seconds` | A positive, finite number; proposed default 5 seconds. Reject invalid configuration before dispatch. |

Each `Source` contains `id: str`, `title: str`, `locator: str`, and `excerpt: str`.
IDs must be unique and the locator must identify the public document or
repository data file. Context is evidence, never an instruction to override
application rules. Demo data must be identified as demo data. Neither the
caller nor the provider may treat unverified rooms or hours as authoritative.

Do not send secrets, private student records, or unnecessary conversation
history. Fees and eligibility rules belong in `src/tools/` per `AGENTS.md`;
do not calculate or define them through prompts or model guesses.

### Outputs

| Record | Fields |
|---|---|
| `GeneratedAnswer` | `text: str`, `source_ids: list[str]` |
| `Answer` | `text: str`, `mode: str`, `sources: list[Source]`, `error: str | None` |

`mode` is exactly one of `rules`, `ai`, `fallback`, or `invalid`.
`sources` contains only supplied records referenced by accepted output;
never manufacture links or IDs. Rule-based responses currently have no
citation metadata, so their source list remains empty until that backend
contract is extended. An empty source list does not assert that an office
fact was independently verified.

An AI response must be nonempty and cite supplied evidence supporting its
factual claims. Merely returning valid source IDs is insufficient: check
support against the excerpts. If support cannot be established, reject the
response and use fallback. Unstructured or unsupported output is not shown
as a successful AI answer.

## Routing and fallback

1. Validate inputs and configuration. Blank input returns the existing
   `reply` message with `mode="invalid"` and `error="invalid_input"`.
2. Use deterministic handling for known greetings and supported full-name
   office lookups. Preserve the existing answer text.
3. For an in-scope language task, use AI only when a provider and suitable
   public evidence are both available. Out-of-scope questions remain on the
   rule-based fallback path even when a provider is configured.
4. Validate provider output and evidence before constructing an AI answer.
5. On provider failure, return the current rule-based reply with
   `mode="fallback"`, an empty source list, and a stable error code. Reuse an
   already-computed reply instead of loading the CSV again.

A future implementation should expose a structured match result from the
deterministic backend while retaining `reply` for CLI compatibility. Do not
route by comparing the backend's human-readable fallback string. That
extension is future implementation work, not a change made by this document.

The proposed first version performs no automatic retry and makes at most one
provider call per request. Fallback does not answer unsupported questions by
inventing office information.

## Error handling

| Condition | Mode / error | Behavior |
|---|---|---|
| Non-string, blank, or oversized input; invalid context/configuration | `invalid` / `invalid_input` | Return a short validation message; make no provider call. |
| No provider configured | `fallback` / `ai_disabled` | Return the existing rule-based reply. |
| In-scope language task lacks evidence | `fallback` / `no_context` | Return the existing rule-based reply. |
| Question outside the supported domain | `fallback` / `unsupported` | Return the existing unknown-question reply. |
| Provider times out | `fallback` / `timeout` | Cancel the request and return the rule-based reply. |
| Provider rejects the request or is unavailable | `fallback` / `provider_unavailable` | Return the rule-based reply; do not expose provider internals. |
| Malformed or unsupported AI output | `fallback` / `invalid_output` | Discard output and return the rule-based reply. |
| Backend/CSV fails and no safe rule response is available | `fallback` / `backend_unavailable` | Return `Office information is temporarily unavailable. Please try again later.` |

Use stable error codes for logs and UI handling. Do not include tokens, full
user messages, or source excerpts in routine logs. Known greetings and empty
input currently do not require loading the CSV; keep that behavior.

## Response examples

Successful deterministic lookup, using the repository's demo dataset:

Input: `Where is the Training Office?`

```json
{
  "text": "Training Office: room I.101, open Mon-Fri 07:30-16:30.",
  "mode": "rules",
  "sources": [],
  "error": null
}
```

Provider timeout during an in-scope summarization task with supplied context:

Input: `Summarize the supplied student support guide in two sentences.`

```json
{
  "text": "I don't know that yet. Try asking about an office, e.g. 'training office'.",
  "mode": "fallback",
  "sources": [],
  "error": "timeout"
}
```

These response envelopes illustrate the future contract. Only their
rule-based `text` values can be obtained from the current backend.

## Verification and complexity

Before implementing AI, cover deterministic compatibility, invalid input,
disabled provider, missing context, timeout/cancellation, provider failure,
unsupported questions, unsupported citations, and CSV failure. Use fake
providers; tests must not require network access or credentials.

For the current backend, let `B` be CSV size, `N` the office count, `L` the
normalized message length, and `K` the longest office name. Loading costs
O(B) time and space; a conservative substring-search bound is O(NLK) time.
A reply that loads data therefore costs O(B + NLK) time and O(B + L) space.

For the proposed adapter, validation costs O(L + C), where `C` is total
context size. Source indexing uses O(S) extra space for `S` source records;
the request payload requires O(L + C) space. Model inference and factual
support checking depend on the future implementation and are not included
in the backend bound. The timeout is a proposed latency limit, not proof of
a model's computational complexity.
