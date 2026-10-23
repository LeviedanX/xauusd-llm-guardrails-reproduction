# XAU/USD LLM Validation with Deterministic Guardrails

Reproduce the primary **fixed-artifact admission experiment** from
*Multi-Agent LLM Validation With Deterministic Risk Guardrails for XAU/USD
Trading Signals*. The archive evaluates whether recorded judgments satisfy
explicit input rules and mandatory evidence requirements. It does not evaluate
market forecasting, trading profit or live execution.

## Reproduce offline

Python 3.10+ and the standard library are sufficient:

```console
python -I -S -B verify_archive.py
```

No model call, API key, MT5 installation, broker connection, package install or
network access is required for replay. Previously verified environments include
Windows/Python 3.13.5 and network-disabled Linux/Python 3.11.2. Replay checks
stored computations; it does not reproduce future provider responses.

## Primary study at a glance

| Evidence | Recorded value |
| --- | --- |
| Fixed synthetic cohort | 40 cases selected from 400 generated records |
| Input-rule labels | 12 RULE_COMPLIANT, 22 VIOLATION, 6 UNKNOWN |
| Historical model-call attempts | 160: 40 separate B1 calls and 120 B2 role calls |
| Response status | 157 contract-valid responses and 3 preserved FAILED attempts |
| Known receipt usage | 83,450 tokens; usage unavailable for 3 attempts |
| Protected condition P | Same ordered B2 response artifacts; no additional inference |

| Condition | ACCEPT | REJECT | ABSTAIN |
| --- | ---: | ---: | ---: |
| B0: unconditional acceptance | 40 | 0 | 0 |
| B1: separate technical role | 19 | 19 | 2 |
| B2: three-role majority | 21 | 18 | 1 |
| P: deterministic enforcement | 10 | 22 | 8 |
| Retrospective rule-only comparator | 12 | 22 | 6 |

B2 accepted four inputs labeled VIOLATION and two input-rule-compliant cases
with incomplete mandatory-role evidence: six identified composite invalid
acceptances. Five further B2 acceptances had UNKNOWN input-rule labels and
complete role evidence, and remain unresolved. These categories are distinct;
UNKNOWN input labels are also distinct from unavailable token usage.

## Archive contents

| Path | Purpose |
| --- | --- |
| [verify_archive.py](verify_archive.py) | Release-integrity verification and offline replay entry point |
| [release_manifest.json](release_manifest.json) | SHA-256 inventory of this public wrapper and its files |
| [replay/](replay/) | Original historical replay artifacts, retained byte for byte |
| [replay/manifest.json](replay/manifest.json) | Original 177-entry historical artifact manifest |
| [deposit_metadata.json](deposit_metadata.json) | Study scope and publication metadata |
| [source_snapshot.csv](source_snapshot.csv) | Source hashes; not proof of a historical Git commit |
| [SECURITY.md](SECURITY.md) | Confidential reporting and publication boundary |

The later 320 supplementary calls are a separate evidence set and are not
merged into this primary deposit. The [maestro framework](https://github.com/LeviedanX/maestro)
is a separate trade-log analysis project, not the source of these synthetic
admission outcomes.

## Evidence boundaries

- The guard and test oracle share a rule specification. Zero identified invalid
  acceptances under P demonstrates policy consistency on these artifacts, not
  independent financial-risk detection or incremental benefit over rule-only.
- FAILED is an absent contract-valid response; ABSTAIN is an explicit verdict
  or policy decision. Missing token usage is unknown, not zero.
- The historical full environment/source commit, detailed rejection envelopes,
  exact HTTP send-starts, immutable backend weights/default sampling, and
  invoice-level request costs are not reconstructed.
- Same-agent anonymous retrieval and offline replay are not verification by an
  independent research group. No DOI or new license is asserted.

## Version identity

Repository: https://github.com/LeviedanX/xauusd-llm-guardrails-reproduction.
For citations, use a specific commit rather than the mutable default branch.
The original public deposit is commit
`28b94739c54083a7413b686cadccbd29766a124c`; later documentation updates do not
change the historical replay artifacts. The commit identifies the present
archive publication, not the source-code version used during the experiment.

Historical notes inside `replay/` keep their original wording and bytes,
including their pre-publication status. This top-level README describes the
current public repository. No author, coauthor approval or third-party rights
grant is inferred by this documentation update.
