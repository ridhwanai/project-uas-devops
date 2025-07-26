from flask import Flask, jsonify
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

@app.route('/')
def home():
    return jsonify({"message": "Hello World"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


print("Log testing: Flask app started")
