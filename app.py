from flask import Flask, jsonify, render_template
import json

app = Flask(__name__)

# Load papers metadata
with open('papers.json') as f:
    papers = json.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/papers')
def get_papers():
    return jsonify(papers)

if __name__ == '__main__':
    app.run(debug=True)