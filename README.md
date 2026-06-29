# Sudhir Vissa

Machine-learning engineer focused on the parts that actually decide whether ML works in production — evaluation, thresholds, drift, identity/fraud signals, serving, and the tooling around them.

I like small, sharp utilities: one job each, minimal dependencies, tests and CI included.

### Focus
- Production ML platforms & evaluation
- Identity / fraud / biometrics ML
- LLM & agentic systems (MCP, RAG, eval harnesses)
- Real-time serving & streaming

### Utilities I maintain

| Repo | Lang | What it does |
|------|------|--------------|
| [ml-eval-report](https://github.com/shadowmodder/ml-eval-report) | Python | Binary-classifier eval: metrics, ROC/PR + AUC, threshold sweep, calibration |
| [thresholdkit](https://github.com/shadowmodder/thresholdkit) | Python | Pick operating thresholds under precision / FPR / cost constraints |
| [featurecheck](https://github.com/shadowmodder/featurecheck) | Python | Feature drift (PSI/KS) + schema/null/dtype validation |
| [idgraph](https://github.com/shadowmodder/idgraph) | Python | Identity/entity graphs from shared signals; surface synthetic-identity rings |
| [pii-redactor](https://github.com/shadowmodder/pii-redactor) | Python | Detect & redact PII (email, phone, SSN, IP, Luhn-validated cards) |
| [llm-eval-lite](https://github.com/shadowmodder/llm-eval-lite) | Python | Assertion-based eval harness for LLM/agent outputs |
| [capture-qa](https://github.com/shadowmodder/capture-qa) | Python | Image capture-quality gates (sharpness, exposure, resolution) |
| [modelcard-gen](https://github.com/shadowmodder/modelcard-gen) | Python | Generate Model Card markdown from a JSON config |
| [tps-bench](https://github.com/shadowmodder/tps-bench) | Go | HTTP throughput & p50/p90/p99 latency benchmark for serving endpoints |
| [cmsketch](https://github.com/shadowmodder/cmsketch) | Rust | Count-Min Sketch: approximate counts over high-cardinality streams |

### Background
20+ years across devices, cloud, and ML — biometrics & sensing at Motorola/Google/Lenovo, real-time services at Amazon Alexa scale, and ML-platform / data-science work at SpotHero and Apple. ~50 granted patents.

---

Find me on [LinkedIn](https://linkedin.com/in/sudhirvissa).
