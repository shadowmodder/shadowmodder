# Sudhir Vissa

Machine-learning engineer focused on the parts that actually decide whether ML works in production — evaluation, calibration, thresholds, drift, identity/fraud signals, serving, and the tooling around them. Also building production agentic systems: tool loops, MCP servers, streaming parsers, and agent memory.

[Blog](https://shadowmodder.github.io) · [LinkedIn](https://linkedin.com/in/sudhirvissa)

---

### Upstream contributions

Bug fixes shipped to production ML/LLM libraries. Open PRs tracked at [PORTFOLIO.md](https://github.com/shadowmodder/shadowmodder.github.io/blob/master/PORTFOLIO.md). Table below updates automatically each day — merged PRs appear here once landed.

<!-- PR-STATUS-START -->
| PR | Repository | Description | Merged |
|---|---|---|---|
| *(none merged yet — 9 open PRs in review)* | | | |
<!-- PR-STATUS-END -->

---

### Writing

Technical posts on production ML/LLM systems.

| Post | Tags |
|---|---|
| [Your Fraud Model's Scores Are Not Probabilities](https://shadowmodder.github.io/posts/calibration-in-production.html) | calibration · production ML · fraud |
| [RAG Retrieval Isn't a Similarity Problem](https://shadowmodder.github.io/posts/rag-retrieval-isnt-similarity.html) | RAG · IR metrics · NDCG · MRR |
| [Running an LLM Gateway in Production](https://shadowmodder.github.io/posts/llm-gateway-production.html) | LLM · rate limiting · cost · caching |
| [Streaming LLMs in Production: The Edge Cases That Break Your App](https://shadowmodder.github.io/posts/streaming-llms-production.html) | streaming · SSE · LangChain · production |
| [Fine-Tuning vs. Prompting: A Decision Framework That Doesn't Lie to You](https://shadowmodder.github.io/posts/finetuning-vs-prompting.html) | fine-tuning · LoRA · RAG · prompting |

Also on [LinkedIn](https://linkedin.com/in/sudhirvissa).

---

### Agentic & LLM infrastructure

| Repo | What it does |
|------|--------------|
| [tool-loop](https://github.com/shadowmodder/tool-loop) | Correct agentic tool-use loop: parallel dispatch, error isolation, auto-schema from Python functions |
| [mcp-quickserver](https://github.com/shadowmodder/mcp-quickserver) | MCP server template: tools, resources, and prompts with stdio and SSE transports |
| [stream-parse](https://github.com/shadowmodder/stream-parse) | Parse streaming LLM output: incremental JSON, markdown blocks, tool-call deltas, SSE events |
| [agent-scratchpad](https://github.com/shadowmodder/agent-scratchpad) | Persistent vector memory for agents: embed, store, retrieve by cosine similarity |
| [prompt-cache-bench](https://github.com/shadowmodder/prompt-cache-bench) | Benchmark prompt caching: cache hit rate, latency delta, cost savings with real measurements |
| [llm-eval-lite](https://github.com/shadowmodder/llm-eval-lite) | Assertion-based eval harness for LLM/agent outputs; composite checks (AllOf, AnyOf) |
| [rag-eval](https://github.com/shadowmodder/rag-eval) | RAG pipeline evaluation: chunking strategies, retrieval quality, answer faithfulness |
| [llm-gateway](https://github.com/shadowmodder/llm-gateway) | Production Anthropic API proxy: token-bucket rate limiting, retry with backoff, cost tracking |
| [rag-demo](https://github.com/shadowmodder/rag-demo) | End-to-end RAG demo: BM25 + tool-loop agent + faithfulness eval + persistent memory |

### ML evaluation & calibration

| Repo | What it does |
|------|--------------|
| [ml-eval-report](https://github.com/shadowmodder/ml-eval-report) | Binary-classifier eval: metrics, ROC/PR + AUC, threshold sweep, Brier score, ECE |
| [calibrate-ml](https://github.com/shadowmodder/calibrate-ml) | Probability calibration: Platt scaling, isotonic regression, ECE, reliability diagram |
| [thresholdkit](https://github.com/shadowmodder/thresholdkit) | Pick operating thresholds under precision / FPR / cost / expected-value constraints |
| [rankeval](https://github.com/shadowmodder/rankeval) | NDCG, MRR, AP@K, P@K, R@K — ranking metrics for search, recommendation, RAG |

### Production ML & data

| Repo | What it does |
|------|--------------|
| [featurecheck](https://github.com/shadowmodder/featurecheck) | Feature drift (PSI/KS/chi-squared) + schema/null/dtype validation |
| [idgraph](https://github.com/shadowmodder/idgraph) | Identity/entity graphs from shared signals; surface synthetic-identity rings + risk scoring |
| [pii-redactor](https://github.com/shadowmodder/pii-redactor) | Detect & redact PII (email, phone, SSN, IP, Luhn-validated cards); custom patterns |
| [capture-qa](https://github.com/shadowmodder/capture-qa) | Image capture-quality gates (sharpness, exposure, resolution) |
| [modelcard-gen](https://github.com/shadowmodder/modelcard-gen) | Generate Model Card markdown from a JSON config |

### Systems & infrastructure

| Repo | What it does |
|------|--------------|
| [tps-bench](https://github.com/shadowmodder/tps-bench) | HTTP throughput & p50/p90/p99 latency benchmark for serving endpoints; warmup + JSON output |
| [cmsketch](https://github.com/shadowmodder/cmsketch) | Count-Min Sketch: approximate counts over high-cardinality streams; merge + serialization |

---

### Background

20+ years across devices, cloud, and ML — biometrics & sensing at Motorola/Google/Lenovo, real-time services at Amazon Alexa scale, ML-platform work at SpotHero and Apple (feature pipelines, scoring infrastructure, model monitoring, data-science tooling). ~50 granted patents.
