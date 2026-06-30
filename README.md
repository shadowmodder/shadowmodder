# Sudhir Vissa

Machine-learning engineer focused on the parts that actually decide whether ML works in production — evaluation, calibration, thresholds, drift, identity/fraud signals, serving, and the tooling around them.

Small, sharp utilities: one job each, minimal dependencies, tests and CI on every repo.

### Focus
- Production ML platforms — feature pipelines, scoring services, A/B infrastructure, model monitoring
- Identity / fraud / biometrics ML
- LLM & agentic systems (MCP, RAG, eval harnesses, ranking quality)
- Real-time serving & streaming

### Current exploration
- Calibration gaps in production risk models: most deployed fraud scores are uncalibrated, which quietly breaks threshold stability across cohorts
- Ranking quality for RAG retrieval: NDCG/MRR applied to document retrieval surfaces degradations that latency metrics miss entirely

### Utilities I maintain

| Repo | Lang | What it does |
|------|------|--------------|
| [ml-eval-report](https://github.com/shadowmodder/ml-eval-report) | Python | Binary-classifier eval: metrics, ROC/PR + AUC, threshold sweep, Brier score, ECE |
| [calibrate-ml](https://github.com/shadowmodder/calibrate-ml) | Python | Probability calibration: Platt scaling, isotonic regression, ECE, reliability diagram |
| [thresholdkit](https://github.com/shadowmodder/thresholdkit) | Python | Pick operating thresholds under precision / FPR / cost / expected-value constraints |
| [rankeval](https://github.com/shadowmodder/rankeval) | Python | NDCG, MRR, AP@K, P@K, R@K — ranking metrics for search, recommendation, RAG |
| [featurecheck](https://github.com/shadowmodder/featurecheck) | Python | Feature drift (PSI/KS/chi-squared) + schema/null/dtype validation |
| [idgraph](https://github.com/shadowmodder/idgraph) | Python | Identity/entity graphs from shared signals; surface synthetic-identity rings + risk scoring |
| [pii-redactor](https://github.com/shadowmodder/pii-redactor) | Python | Detect & redact PII (email, phone, SSN, IP, Luhn-validated cards); custom patterns |
| [llm-eval-lite](https://github.com/shadowmodder/llm-eval-lite) | Python | Assertion-based eval harness for LLM/agent outputs; composite checks |
| [capture-qa](https://github.com/shadowmodder/capture-qa) | Python | Image capture-quality gates (sharpness, exposure, resolution) |
| [modelcard-gen](https://github.com/shadowmodder/modelcard-gen) | Python | Generate Model Card markdown from a JSON config |
| [tps-bench](https://github.com/shadowmodder/tps-bench) | Go | HTTP throughput & p50/p90/p99 latency benchmark for serving endpoints; warmup + JSON output |
| [cmsketch](https://github.com/shadowmodder/cmsketch) | Rust | Count-Min Sketch: approximate counts over high-cardinality streams; merge + serialization |

### Background
20+ years across devices, cloud, and ML — biometrics & sensing at Motorola/Google/Lenovo, real-time services at Amazon Alexa scale, and ML-platform work at SpotHero and Apple (feature pipelines, scoring infrastructure, model monitoring, data-science tooling). ~50 granted patents.

---

Find me on [LinkedIn](https://linkedin.com/in/sudhirvissa).
