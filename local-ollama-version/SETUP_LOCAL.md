# 🏠 Local Ollama Version - Complete Setup Guide

This folder contains the **local development version** optimized for running on your computer with Ollama.

## ✨ Features

- 🏠 **Local Development** - Run on your machine with Ollama + DeepSeek-R1 7B
- 🔄 **Cloud Fallback** - Automatically falls back to Groq if Ollama unavailable
- 🚀 **Best Quality** - DeepSeek-R1 7B is the highest quality model
- ⚡ **Faster with GPU** - If you have NVIDIA/AMD GPU, inference is very fast
- 📊 **Full Features** - Export JSON, Markdown, PDF
- 💾 **Session History** - Track all your research

## 📋 Prerequisites

### Required
- Python 3.10+
- 8GB RAM minimum (16GB recommended)
- Virtual environment

### Optional but Recommended
- Ollama installed (https://ollama.ai)
- NVIDIA/AMD GPU (makes it 10x faster)

## ⚡ Quick Start (10 minutes)

### Step 1: Install Ollama (5 min)

```bash
# Download from https://ollama.ai
# Install and run in background

# Verify Ollama is running
curl http://localhost:11434/api/tags
# Should return list of models

# Pull DeepSeek-R1 model (4.7GB, first time only)
ollama pull deepseek-r1:7b
```

### Step 2: Configure Environment (2 min)

Create `.env` file in this folder:

```
LINKUP_API_KEY=your_linkup_key_here
GROQ_API_KEY=your_groq_key_here
```

Get API keys:
- **LinkUp**: https://linkup.so (free)
- **Groq**: https://console.groq.com (free, fallback only)

### Step 3: Install Dependencies (2 min)

```bash
# Create virtual environment
python -m venv venv

# Activate
.\venv\Scripts\activate  # Windows
# source venv/bin/activate  # Mac/Linux

# Install packages
pip install -r requirements.txt
```

### Step 4: Run! (1 min)

```bash
streamlit run app.py
```

Opens at: `http://localhost:8501`

**That's it! You're ready to research!** 🎉

---

## 🎯 How It Works

### LLM Selection (Automatic)

```
When you run the app:
│
├─ Check if Ollama is running locally
│  ├─ YES → Use DeepSeek-R1 7B (best quality!)
│  └─ NO → Next step
│
└─ Check for GROQ_API_KEY
   ├─ YES → Use Groq Mixtral (always available)
   └─ NO → Error (need one of them)
```

**Result:** You always get the best available LLM!

---

## 💻 Performance by Hardware

### With NVIDIA GPU
```
Search + Analysis + Report = ~1.5-2 minutes ⚡
```

### With AMD GPU
```
Search + Analysis + Report = ~2-3 minutes ⚡
```

### CPU Only
```
Search + Analysis + Report = ~5-10 minutes ⏱️
(Still works great, just slower)
```

---

## 🔧 Troubleshooting

### "No LLM available" error

**Solution:**
```bash
# Make sure Ollama is running
ollama serve

# In another terminal, test it
curl http://localhost:11434/api/tags

# If that fails, ensure Ollama is installed
# Download from https://ollama.ai
```

### "Ollama not found" or connection errors

**Solutions:**
1. Restart your computer
2. Run `ollama serve` in a terminal
3. Keep that terminal open while using the app
4. Test with `curl http://localhost:11434/api/tags`

### Model loading is very slow

**Why:** First load downloads model from disk (~4.7GB)

**Solution:** Be patient. It only happens once. Next runs use cached model.

### App is still slow even after model loads

**Cause:** Running on CPU

**Solutions:**
1. Use GPU if available
2. Close other applications
3. Or use Groq (cloud) - it's actually faster!

### "LinkUp API not found" error

**Solution:**
1. Get free key from https://linkup.so
2. Add to `.env`: `LINKUP_API_KEY=your_key`
3. Restart the app

---

## 📚 File Structure

```
local-ollama-version/
├── app.py ..................... Streamlit UI
├── agents.py .................. CrewAI system (Ollama + Groq fallback)
├── requirements.txt ........... Dependencies
├── .env.example ............... Template (copy to .env)
├── .gitignore ................. Protect secrets
└── SETUP_LOCAL.md ............. This file
```

---

## 🔄 agents.py Explained

The `get_llm_client()` function does the magic:

```python
def get_llm_client():
    # 1. Try Ollama (local, best quality)
    try:
        return LLM(model="ollama/deepseek-r1:7b", ...)
    except:
        pass
    
    # 2. Fall back to Groq (cloud, always works)
    if groq_key:
        return LLM(model="groq/mixtral-8x7b-32768", ...)
    
    # 3. If neither works, error
    raise ValueError("Install Ollama or set GROQ_API_KEY")
```

**Benefits:**
- ✅ Always tries best option first
- ✅ Graceful fallback
- ✅ Works offline (with Ollama)
- ✅ Works online (with Groq)

---

## 🚀 Next Steps

### Option 1: Keep Using Locally
- Develop and test locally
- Deploy to Streamlit Cloud later (when ready)
- See main folder README for cloud deployment

### Option 2: Deploy to Cloud
1. When ready, see [main folder README](../README.md)
2. Code already has Groq fallback ready
3. Just needs API key in secrets

### Option 3: Optimize Further
- Add caching to LinkUp searches
- Implement vector DB for paper storage
- Create custom agents for your domain

---

## 💡 Pro Tips

1. **Keep Ollama running** in background while developing
   ```bash
   # Terminal 1: Keep this open
   ollama serve
   
   # Terminal 2: Run the app
   streamlit run app.py
   ```

2. **Test with simple queries first**
   - Good: "machine learning"
   - Better: "attention mechanisms in transformers"

3. **Check GPU usage** (if you have GPU)
   - Windows: Open Task Manager → GPU
   - See if it's being used
   - If not, might be CPU-based run

4. **Export results frequently**
   - Save as JSON (structured)
   - Save as Markdown (readable)
   - Save as PDF (shareable)

---

## 🔗 Useful Links

- **Ollama**: https://ollama.ai
- **LinkUp**: https://linkup.so
- **Groq**: https://console.groq.com
- **Streamlit**: https://streamlit.io
- **CrewAI**: https://docs.crewai.com

---

## ✅ Checklist

Before running:
- [x] Python 3.10+ installed
- [x] Ollama installed (or Groq API key)
- [x] Virtual environment created
- [x] `.env` file with API keys
- [x] Dependencies installed: `pip install -r requirements.txt`

Before deploying to cloud:
- [x] Works locally
- [x] All exports work
- [x] Tested with real queries

---

## 📞 Need Help?

**Check these in order:**
1. Troubleshooting section above
2. Main folder README.md
3. Code comments in agents.py

---

## 🎓 What You're Learning

By using this version, you learn:
- ✅ Multi-agent AI systems (CrewAI)
- ✅ Local LLM deployment (Ollama)
- ✅ Cloud API fallback patterns
- ✅ Error handling & resilience
- ✅ Hybrid architecture design

**This is professional-grade knowledge!**

---

## 🎉 You're All Set!

Your local development environment is ready. Start researching!

```bash
streamlit run app.py
```

Then:
1. Enter a research topic
2. Wait for results
3. Export your findings
4. Keep building! 🚀

---

**Happy researching!** 

🏠 Local Ollama Version | [☁️ Cloud Groq Version](../groq-cloud-version/SETUP_CLOUD.md) | [📚 Main README](../README.md)
