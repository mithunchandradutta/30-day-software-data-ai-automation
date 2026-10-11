# Idempotency Checklist (notun endpoint/workflow banano-r shomoy)

- [ ] Eta ki "notun kichu banao / jog koro" dhoroner kaj? Tahole request_id lagbe.
- [ ] Client prottek kaj-e unique request_id pathay? Retry-te SAME id?
- [ ] request_id chhara request reject hoy?
- [ ] "Age-i hoyeche?" check ache, ar hoye thakle ager result dey?
- [ ] Database-e request_id PRIMARY KEY (race condition guard)?
- [ ] Kaj fail hole claim rollback hoy (jate retry kora jay)?
- [ ] 2 bar pathiye test korechi? Bhul data diye test korechi?
- [ ] n8n workflow-te-o ekoi check ache?
- [ ] Error hole silent na - visible?
