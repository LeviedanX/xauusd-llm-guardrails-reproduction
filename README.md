# Fixed-artifact XAU/USD admission study: reproduction archive

This archive reproduces the primary historical analysis:40 fixed synthetic cases,160 model-call attempts,157 contract-valid responses,3 preserved failures, and identical recorded B2-to-P artifacts. It does not contain new inference or claim market performance, independent financial ground truth, immutable backend weights, or independent researcher validation. The later320 supplementary calls remain a separate evidence set; they are not merged into this primary archive.

Run with a standard-library Python interpreter:

```
python -I -S -B verify_archive.py
```

Verified execution environments for the underlying replay are Windows/Python3.13.5 and network-disabled Linux/Python3.11.2. No API key, provider request, MT5, broker, package install, or network access is required. `replay/manifest.json` is the original177-file manifest; `release_manifest.json` independently inventories this prepared deposit. Original replay artifacts remain byte-identical to the retained author-review archive.

The full historical study commit/environment was not recorded; source hashes are retained in source_snapshot.csv. Failed historical envelopes, exact HTTP send-starts, fixed backend weights/default sampling values, and request-level invoice costs are not reconstructed. The original README and protocol notes inside replay/ describe the historical archive; this README defines the current public deposit.

Public repository: [https://github.com/LeviedanX/xauusd-llm-guardrails-reproduction](https://github.com/LeviedanX/xauusd-llm-guardrails-reproduction). This deposit is a current archival publication, not evidence of a historical study commit. No DOI or independent researcher verification is asserted. No new license, coauthor approval, or third-party rights grant is invented. Only the selected reproduction files are deposited; the surrounding private project is excluded. The original notes inside replay/ retain their historical wording and bytes.
