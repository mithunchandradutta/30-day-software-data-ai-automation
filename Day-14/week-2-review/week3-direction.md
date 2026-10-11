# Week 3 Direction - AI Engineering

```
Reliable, Automated Data System (Week 1-2)
              |
        LLM Fundamentals
              |
        LLM API Integration
              |
   AI layered on top of deterministic data
              |
 (RAG -> tool calling -> agentic workflow -> AI Financial Analyst prototype)
```

## Week 3-er age ja thaka dorkar
- [ ] `python -m unittest` / `verify_week2.py` shob green
- [ ] Day 8 API fetcher-er validation concept mone ache (LLM output-o validate korte hobe!)
- [ ] Day 12 idempotency: LLM API call retry hole duplicate cost/side-effect hote pare - same principle
- [ ] Anthropic/OpenAI API key (environment variable-e, code-e na) + `.env` `.gitignore`-e
- [ ] Kono LLM call-er output **never** direct DB-te likhbe na - age validate (Week 2-er shikha)

## Key idea
AI = probabilistic. Tomar Week 1-2 system = deterministic. Duita-r majhkhane **validation + idempotency** boshao.
