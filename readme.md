docker build -t mock-users-api .
docker run -p 5000:5000 mock-users-api



python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
