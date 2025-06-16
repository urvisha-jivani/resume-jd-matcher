# 📄 Resume-JD Matcher

A simple and useful tool to quickly check how well a resume aligns with a job description — all through a clean Streamlit interface.

## 🔍 What it does

This app takes a resume and a job description (JD) as input and gives you a match score out of 100. Instead of just looking at matching keywords, it uses a BERT model to understand the actual meaning of the text. So even if your wording doesn’t exactly match the JD, it still picks up the similarities.

## ✅ Key Features

- Paste your resume and JD right into the app
- Instant score based on semantic similarity (not just keyword match)
- Built with Streamlit for a quick and clean UI
- No need to upload files — just copy and paste

## ⚙️ Tech Used

- Python
- Streamlit
- sentence-transformers (BERT-based model)
- PyTorch (powers the BERT model internally)

### Install the dependencies
```bash
pip install -r requirements.txt
```

## Run the app
```bash
streamlit run app.py
```


