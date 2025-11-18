.PHONY: run build docker


run:
python -m streamlit run app.py


build:
pip install -r requirements.txt


docker:
docker build -t personal-finance-chatbot:latest .