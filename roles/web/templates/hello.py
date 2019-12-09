from flask import Flask
import socket
import redis

app = Flask(__name__)

redis_host = '{{ redis_db_server }}'
redis_port = 6379
redis_password = ""
r = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)

@app.route("/")
def hello():
    return r.get("msg:hello") + " served by " + socket.gethostname()
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3001)