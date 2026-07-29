# LendIQ — Deployment Guide (Streamlit Community Cloud)

This app is deployed for free on Streamlit Community Cloud, which runs it straight from a public GitHub repo.

> **Note on the rename:** the project was rebranded from "Customer Loan Risk Prediction System" to **LendIQ**, and the GitHub repo was renamed to `LendIQ`. Renaming a repo does NOT rename an already-deployed Streamlit app — to get a `lendiq-*.streamlit.app` URL you must delete the old app on share.streamlit.io and redeploy using Step 2 below.

## Prerequisites (one-time)
- A GitHub account (username: PavanTeja-hash)
- A free account at https://share.streamlit.io (sign in with GitHub)

## Step 1 — Push the project to GitHub
Run these in the project folder. The repo `LendIQ` already exists on GitHub.

```bash
cd "C:\Users\maddi\OneDrive\Desktop\LendIQ"

git add .
git commit -m "Rebrand project to LendIQ"
git push origin main
```

If `git push` complains the remote has commits you don't have locally, run `git pull --rebase origin main` first, then push again.

## Step 2 — Deploy on Streamlit Cloud
1. Go to https://share.streamlit.io and sign in with GitHub.
2. Click **"Create app"** → **"Deploy a public app from GitHub"**.
3. Fill in:
   - **Repository:** `PavanTeja-hash/LendIQ`
   - **Branch:** `main`
   - **Main file path:** `app.py`
4. Click **Deploy**. First build takes a few minutes (it installs everything in `requirements.txt`).
5. You'll get a public URL like `https://lendiq.streamlit.app` — put this on your resume.

## How it works (for your understanding)
- Streamlit Cloud reads `requirements.txt`, installs those exact pinned versions, then runs `app.py`.
- `app.py` loads `models/best_model.joblib` (the tuned XGBoost pipeline, committed to the repo, ~1.8MB).
- Versions are pinned in `requirements.txt` so the saved model loads without version-mismatch errors.

## If you retrain the model
If you change the model and regenerate `models/best_model.joblib` (via `python src/train_final_model.py`), commit and push it again — Streamlit Cloud auto-redeploys on every push to `main`.

## Updating the app later
Any `git push` to `main` triggers an automatic redeploy. No extra steps.
```
