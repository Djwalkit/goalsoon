Goal Soon V9 (Vercel-ready)

## Local run
```bash
pip install -r requirements.txt
export API_FOOTBALL_KEY=YOUR_KEY
uvicorn api.index:app --reload
```
Open: http://127.0.0.1:8000/public/index.html

## Vercel deploy (GitHub import)
1) Push this folder to GitHub (repo root must contain: vercel.json, api/, public/, core/).
2) In Vercel → Add New Project → Import repo.
3) Project Settings → Build & Development:
   - Framework Preset: Other
   - Build Command: (empty)
   - Output Directory: (empty)  ✅ important
4) Settings → Environment Variables:
   - API_FOOTBALL_KEY = your key
5) Redeploy.

## Post-deploy test
- https://YOUR-VERCEL-URL/            (UI)
- https://YOUR-VERCEL-URL/api/ranked  (JSON)
