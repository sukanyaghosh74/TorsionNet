from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route('/concepts')
def concepts():
    with open('data/concepts.json') as f:
        data = json.load(f)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
