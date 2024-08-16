from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)
summarizer = pipeline("summarization")

@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.json
    summary = summarizer(data['text'], max_length=130, min_length=30, do_sample=False)
    return jsonify(summary)

if __name__ == '__main__':
    app.run(port=5001)
