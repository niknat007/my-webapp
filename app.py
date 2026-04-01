from flask import Flask
import redis
import os

app = Flask(__name__)

redis_host = os.environ.get("REDIS_HOST", "redis")
r = redis.Redis(host=redis_host, port=6379, decode_responses=True)

@app.route("/")
def hello():
    try:
        visits = r.incr("counter")
    except Exception as e:
        visits = f"Redis error: {e}"
    return f"Hello from Flask + Redis! Visits: {visits}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
