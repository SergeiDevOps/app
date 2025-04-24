from flask import Flask
import redis
import os

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "fallback-secret-key")
# fallback для отладки
r = redis.Redis(host=os.getenv("REDIS_HOST", "localhost"), decode_responses=True)

@app.route("/health")
def health():
    return {"status": "ok"}

@app.route("/visit")
def visit():
    count = r.incr("visits")
    return f"Страница посещена {count} раз"

@app.route("/")
def index():
    return "Привет! Доступные маршруты: /health и /visit"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

