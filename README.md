# Personal Finance Chatbot


## Quickstart (VS Code)


1. Clone repo


git clone <repo-url>
cd personal-finance-chatbot


2. Create virtual environment


python -m venv .venv
source .venv/bin/activate # mac/linux
.\.venv\Scripts\activate # windows


3. Install


pip install -r requirements.txt


4. Paste your IBM Granite pipeline code into `granite_pipeline.py`. Ensure it exposes `get_generator()` which returns an object with `.generate(prompt, **kwargs)`.


5. Run Streamlit


streamlit run app.py




## Docker


Build:


docker build -t personal-finance-chatbot:latest .


Run (example):


docker run -p 8501:8501 --env-file .env personal-finance-chatbot:latest




## Notes
- Keep your Hugging Face credentials or model access tokens in `.env`.
- For GPU usage, ensure `device_map` or `accelerate` is configured in your pipeline code.