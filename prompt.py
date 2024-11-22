# from LLM_integration import ask_llm


# # question = "what is the capital of india?"
# question = "I am happy"
# print(question)
# ask_llm(question) 
# # 
# print()
# question = "I hate you "
# print(question)
# ask_llm(question) 

from flask import Flask, request, jsonify, render_template
from threading import Lock
from LLM_integration import ask_llm

app = Flask(__name__)

# Create a lock to handle single requests at a time
lock = Lock()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    global lock
    if not lock.acquire(blocking=False):  # Check if lock is already acquired
        return jsonify({"error": "LLM is busy, please wait."}), 429

    try:
        data = request.json
        question = data.get('question')
        if not question:
            return jsonify({"error": "No question provided."}), 400

        # Ask the LLM
        response = ask_llm(question)
        return jsonify({"answer": response})
    finally:
        lock.release()  # Release the lock after processing

if __name__ == '__main__':
    app.run(debug=True)
