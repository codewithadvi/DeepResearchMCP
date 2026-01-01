# Cloud Deployment Guide - Groq-Optimized Version

This folder contains a **cloud-optimized version** of the Deep Research MCP that uses **Groq Cloud API exclusively** (no Ollama fallback).

## 🎯 When to Use This Folder

Use this folder if you want to:
- Deploy **only to Streamlit Cloud** (not local development)
- Maximize **startup speed** (skip Ollama connection checks)
- Use **only Groq API** (simpler configuration)
- Have a **minimal, cloud-focused codebase**

## 🚀 Quick Start (5 minutes)

### Step 1: Get Groq API Key

```bash
# Go to https://console.groq.com
# Sign up (FREE, no credit card)
# Copy your API key
```

### Step 2: Get LinkUp API Key

```bash
# Go to https://linkup.so
# Sign up for free
# Copy your API key
```

### Step 3: Set Environment Variables

Create `.env` file:
```
LINKUP_API_KEY=your_linkup_key
GROQ_API_KEY=your_groq_key
```

### Step 4: Run Locally (Optional)

```bash
# Activate virtual environment
.\venv\Scripts\activate

# Run Streamlit
streamlit run app.py
```

Opens at `http://localhost:8501`

### Step 5: Deploy to Streamlit Cloud

1. **Push to GitHub:**
   ```bash
   git init
   git add .
   git commit -m "Deploy Deep Research to cloud"
   git push origin main
   ```

2. **Create Streamlit Cloud App:**
   - Go to https://share.streamlit.io
   - Click "New app"
   - Select your repository
   - Main file: `app.py`

3. **Add Secrets:**
   - In Streamlit Cloud dashboard
   - Settings → Secrets
   - Paste:
     ```
     LINKUP_API_KEY=your_key
     GROQ_API_KEY=your_key
     ```

4. **Done!** Your app is live 🎉

---

## 📁 Files in This Folder

| File | Purpose |
|------|---------|
| `app.py` | Streamlit web interface |
| `agents.py` | CrewAI system (Groq-only) |
| `requirements.txt` | Python dependencies |
| `.env` | Local API keys (not committed) |
| `.gitignore` | Protects secrets |
| `SETUP_CLOUD.md` | This file |

---

## 🔑 Key Differences from Main Folder

### Main Folder (`../`)
```python
# agents.py - Hybrid approach
def get_llm_client():
    # Try Ollama first (local)
    try:
        return LLM(model="ollama/deepseek-r1:7b", ...)
    except:
        pass
    
    # Fall back to Groq (cloud)
    if groq_key:
        return LLM(model="groq/mixtral-8x7b-32768", ...)
```

### This Folder (`groq-cloud-version/`)
```python
# agents.py - Cloud-optimized
def get_llm_client():
    # Direct Groq only
    if groq_key:
        return LLM(model="groq/mixtral-8x7b-32768", ...)
    else:
        raise ValueError("GROQ_API_KEY required")
```

**Benefits of Groq-only version:**
- ✅ Faster startup (no Ollama connection check)
- ✅ Simpler code (fewer conditionals)
- ✅ Optimized for cloud (matches deployment environment)
- ✅ Clear error messages (no confusing fallbacks)

---

## 💰 Cost Breakdown

| Service | Cost | Usage |
|---------|------|-------|
| Streamlit Cloud | FREE | Host forever |
| Groq API | FREE tier (~$0.14/1M tokens) | ~$0-3/month |
| LinkUp API | FREE tier (~100/mo) | Limited searches |
| **Total** | **FREE** | Fully free! |

### Example Query Cost
- 1 research query = ~100K tokens
- 100K tokens on Groq = $0.014 (less than 2 cents!)

---

## 🚀 Performance

### Response Times (Groq Cloud)

| Task | Time |
|------|------|
| Search papers | 15 sec |
| Extract methodology | 25 sec |
| Identify gaps | 35 sec |
| Generate report | 45 sec |
| **Total** | **~2 minutes** |

Much faster than local Ollama on CPU!

---

## 🐛 Troubleshooting

### "GROQ_API_KEY not found"

**Solution:** Add to `.env`:
```
GROQ_API_KEY=your_actual_key_from_console.groq.com
```

### "Streamlit app is slow"

**Cause:** Using Groq free tier (shared resources)

**Solutions:**
1. Use local Ollama for faster iteration (switch to main folder)
2. Upgrade to Groq paid tier (~$0.14 per 1M tokens)
3. Optimize prompts to use fewer tokens

### "LinkUp search returns empty"

**Solutions:**
1. Check your LinkUp API key is valid
2. Try different search keywords
3. Wait a few seconds (rate limiting)
4. Upgrade LinkUp plan if hitting limits

---

## 📚 API Documentation

### Groq API
- **Endpoint:** https://api.groq.com
- **Models:** mixtral-8x7b-32768, llama-3.1-70b
- **Rate:** 120 requests/min free tier
- **Docs:** https://console.groq.com/docs

### LinkUp API
- **Endpoint:** https://api.linkup.so
- **Searches/month:** ~100 free
- **Output:** Academic papers with snippets
- **Docs:** https://docs.linkup.so

---

## 🔄 Switching Back to Main Folder

If you want to:
- Use **local Ollama** for better quality
- Have **fallback to Groq** as backup
- **Develop locally** then deploy to cloud

Use the **main folder** instead:

```bash
cd ..
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

The main folder has automatic fallback from Ollama → Groq!

---

## ✅ Checklist

- [ ] Get Groq API key from https://console.groq.com
- [ ] Get LinkUp API key from https://linkup.so
- [ ] Create `.env` with both keys
- [ ] Test locally with `streamlit run app.py`
- [ ] Push to GitHub
- [ ] Create Streamlit Cloud app
- [ ] Add secrets in Streamlit dashboard
- [ ] Test your live app!
- [ ] Share public URL with others 🎉

---

**Questions?** Check main folder README for detailed documentation.

**Built for cloud** ☁️ using Groq + LinkUp + Streamlit
