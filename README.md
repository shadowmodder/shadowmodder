# Sudhir Vissa

Machine-learning engineer focused on the parts that actually decide whether ML works in production — evaluation, calibration, thresholds, drift, identity/fraud signals, serving, and the tooling around them. Also building production agentic systems: tool loops, MCP servers, streaming parsers, and agent memory.

[Blog](https://shadowmodder.github.io) · [LinkedIn](https://linkedin.com/in/sudhirvissa)

---

### Upstream contributions

Bug fixes shipped to production ML/LLM libraries. Status syncs automatically each day.

<!-- PR-STATUS-START -->
| PR | Repository | Description | Status |
|---|---|---|---|
| [#3913](https://github.com/EleutherAI/lm-evaluation-harness/pull/3913) | [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) | ECE + RMS calibration metrics | 🟢 Open |
| [#2816](https://github.com/vibrantlabsai/ragas/pull/2816) | [ragas](https://github.com/vibrantlabsai/ragas) | NDCG, MRR, Precision@K, Recall@K retrieval metrics | 🟢 Open |
| [#32198](https://github.com/BerriAI/litellm/pull/32198) | [litellm](https://github.com/BerriAI/litellm) | `stream_chunk_builder` KeyError on missing `choices` | 🟢 Open |
| [#32199](https://github.com/BerriAI/litellm/pull/32199) | [litellm](https://github.com/BerriAI/litellm) | `reasoning_tokens` forced to `0` in Responses API proxy | 🟢 Open |
| [#32200](https://github.com/BerriAI/litellm/pull/32200) | [litellm](https://github.com/BerriAI/litellm) | Async cache streaming drops `reasoning_content` | 🟢 Open |
| [#32205](https://github.com/BerriAI/litellm/pull/32205) | [litellm](https://github.com/BerriAI/litellm) | `previous_response_id` double-encoded in MCP tool loops | 🟢 Open |
| [#38680](https://github.com/langchain-ai/langchain/pull/38680) | [langchain](https://github.com/langchain-ai/langchain) | Streaming tool call fires prematurely with empty args | 🟢 Open |
| [#3391](https://github.com/huggingface/peft/pull/3391) | [peft](https://github.com/huggingface/peft) | `update_and_allocate` unreachable after `inject_adapter_in_model` | 🟢 Open |
| [#6297](https://github.com/huggingface/trl/pull/6297) | [trl](https://github.com/huggingface/trl) | NaN logprobs crash in GRPO trainer with vLLM importance sampling | 🟢 Open |
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
