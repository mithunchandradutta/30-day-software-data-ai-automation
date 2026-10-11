# Day 08 — APIs + Python (Self Learning)

এই folder এ আমি নিজে হাতে টাইপ করে API শিখেছি। প্রতিটা `step` file একটা করে concept শেখায়। পরে revise করার সময় এই README দেখলেই বুঝব কোন file এ কী শিখেছি আর কেন বানিয়েছি।

**Practice API:** `https://jsonplaceholder.typicode.com` (নকল API, শেখার জন্য নিরাপদ, কিছু আসলে save হয় না)

---

## Folder structure

```
Day-08/
└── self-learning/
    ├── README.md
    ├── step2.py
    ├── step3.py
    ├── step4.py
    ├── step5.py
    ├── step6.py
    ├── step7.py
    ├── step8.py
    ├── step9.py
    ├── step10.py
    ├── final.py
    └── users.csv   (final.py চালালে তৈরি হয়)
```

---

## Setup

```bash
pip install requests
```

---

## Step by step: কোন file এ কী শিখেছি

### step2.py — প্রথম API request
- **কী শিখেছি:** `requests.get(url)` দিয়ে Python থেকে API call করা, আর `status_code` দেখা।
- **কেন বানিয়েছি:** সবচেয়ে ছোট কাজ দিয়ে শুরু করতে, যাতে বুঝি Python ও browser এর মতোই server এর সাথে কথা বলতে পারে।
- **মনে রাখব:** `200` মানে সফল।

### step3.py — JSON data হাতে পাওয়া
- **কী শিখেছি:** `response.json()` JSON কে Python dictionary বানায়। `data["name"]`, আর ভেতরের dict এর জন্য `data["address"]["city"]`।
- **কেন বানিয়েছি:** শুধু status code দেখে লাভ নেই, আসল data থেকে দরকারি field বের করা শিখতে।
- **মনে রাখব:** JSON আর Python dict দেখতে প্রায় একই।

### step4.py — অনেকগুলো data (list)
- **কী শিখেছি:** `/users` call করলে list of dictionary আসে। `for` loop দিয়ে একটা একটা করে পড়া যায়।
- **কেন বানিয়েছি:** একজনের data (dict) আর অনেকজনের data (list) এর পার্থক্য বুঝতে।
- **মনে রাখব:** `/users/1` = একজন (dict), `/users` = সবাই (list)।

### step5.py — Query parameters (filter)
- **কী শিখেছি:** `params={"userId": 2}` দিলে URL এ `?userId=2` যোগ হয় আর server filter করে data দেয়।
- **কেন বানিয়েছি:** সব data না এনে শুধু দরকারি data আনা শিখতে।
- **মনে রাখব:** `params=` দিলে Python নিজেই `?` আর `&` বসায়।

### step6.py — Status code দিয়ে সমস্যা ধরা
- **কী শিখেছি:** ঠিক URL এ `200`, ভুল URL (`/users/9999`) এ `404`।
- **কেন বানিয়েছি:** সফল আর ব্যর্থ request এর পার্থক্য নিজের চোখে দেখতে।
- **মনে রাখব:**

| Code | মানে |
|---|---|
| 200 | সব ঠিক |
| 201 | নতুন কিছু তৈরি হয়েছে |
| 400 | আমার পাঠানো data ভুল |
| 401 | token নেই বা ভুল |
| 403 | পরিচয় ঠিক, permission নেই |
| 404 | যা চেয়েছি সেটা নেই |
| 429 | অনেক বেশি request পাঠিয়েছি |
| 500 | server এর সমস্যা |

সহজ নিয়ম: **2xx = ভালো, 4xx = আমার ভুল, 5xx = server এর ভুল**।

### step7.py — Error handling
- **কী শিখেছি:** `try/except`, `raise_for_status()`, `timeout=10`।
- **কেন বানিয়েছি:** Real কাজে internet যায়, URL ভুল হয়, server down হয়। Program যেন crash না করে।
- **মনে রাখব:**
  - সবসময় `timeout` দেব
  - `raise_for_status()` 4xx/5xx হলে error তোলে
  - `HTTPError`, `ConnectionError`, `Timeout` আলাদা করে ধরা যায়

### step8.py — POST (data পাঠানো)
- **কী শিখেছি:** `requests.post(url, json=data)` দিয়ে নতুন data পাঠানো। সফল হলে `201`।
- **কেন বানিয়েছি:** GET শুধু data আনে, POST দিয়ে data পাঠানো যায়।
- **মনে রাখব:**
  - GET = data আনা, POST = data পাঠানো
  - `json=` দিলে Python নিজে JSON বানিয়ে দেয়
  - JSONPlaceholder নকল server, তাই আসলে কিছু save হয় না

### step9.py — Headers
- **কী শিখেছি:** `headers={...}` দিয়ে request এর সাথে extra তথ্য পাঠানো। `httpbin.org/headers` আমার পাঠানো headers ফেরত দেখায়।
- **কেন বানিয়েছি:** Authentication বোঝার আগে header কী জিনিস সেটা দেখতে।
- **মনে রাখব:** Header = খামের গায়ে লেখা ঠিকানার মতো metadata। সবচেয়ে দরকারি: `Authorization`, `Content-Type`, `User-Agent`।

### step10.py — Authentication
- **কী শিখেছি:** Token ছাড়া `401`, `Authorization: Bearer <token>` header দিলে `200`।
- **কেন বানিয়েছি:** GitHub, OpenAI, Anthropic এর মতো real API এভাবেই কাজ করে।
- **মনে রাখব:**
  - **API Key:** একটা secret লেখা, header বা params এ যায়
  - **Bearer Token:** `Authorization: Bearer <token>`
  - **OAuth:** "Login with Google" এর মতো (এখন শুধু নাম জানা)
  - **নিরাপত্তা:** আসল key code এ লিখব না, GitHub এ push করব না। ব্যবহার করব `os.getenv("MY_TOKEN")`

### final.py — সব মিলিয়ে mini project
- **কী শিখেছি:** API থেকে users এনে দরকারি field বেছে `users.csv` file বানানো (GET + JSON + error handling + CSV)।
- **কেন বানিয়েছি:** শেখা সব concept একসাথে কাজে লাগাতে। API থেকে data এনে file এ রাখা data ও automation এর আসল কাজ।
- **Output:** `users.csv` (Excel এ খোলা যায়)

---

## Quick cheat sheet

```python
import requests

r = requests.get(url, params=..., headers=..., timeout=10)
r = requests.post(url, json=..., headers=..., timeout=10)

r.status_code        # 200, 404 ...
r.json()             # dict / list
r.text               # raw text
r.headers            # response headers
r.raise_for_status() # 4xx/5xx হলে error
```

---

## Day 8 checklist

- [ ] step2: `200` পেয়েছি
- [ ] step3: dict থেকে name, email বের করেছি
- [ ] step4: list loop করেছি
- [ ] step5: `params` দিয়ে filter করেছি
- [ ] step6: `404` দেখেছি
- [ ] step7: error handle করেছি
- [ ] step8: POST করে `201` পেয়েছি
- [ ] step9: headers পাঠিয়েছি
- [ ] step10: `401` আর `200` দুটোই দেখেছি
- [ ] final: `users.csv` বানিয়েছি

## নিজেকে পরীক্ষা (সাহায্য ছাড়া পারলে Day 8 শেষ)

1. কোনো API থেকে GET করে JSON এর একটা field print করা
2. ভুল URL দিয়ে `404` ধরা
3. API থেকে data এনে CSV তে save করা

## এখনো বাকি (পরে শিখব)

- Pagination
- Retry আর rate limit (`429`) handle করা
- OAuth এর আসল implementation
- নিজে API বানানো (Flask / FastAPI)

## আমার নোট

(এখানে নিজের ভাষায় লিখব: কোথায় আটকেছিলাম, কোন error পেয়েছি, কীভাবে ঠিক করেছি)

-