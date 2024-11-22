from flask import Flask, request, jsonify, render_template
import threading
import ollama

# Flask app setup
app = Flask(__name__)

# Lock to manage concurrent requests
lock = threading.Lock()

# LLM interaction function
def ask_llm(question):
    try:
        # Start streaming the response
        response_stream = ollama.chat(
            model="llama3.2:1b",
            messages=[
                {
                    "role": "system",
                    "content": "First provide sentimental analysis as (positive, negative, or neutral), and then provide the type of emotion in one word (e.g., angry, happy, threatening, etc.)."
                },
                {"role": "user", "content": question}
            ],
            stream=True
        )
        
        response_text = ""
        for chunk in response_stream:
            if isinstance(chunk, dict) and 'message' in chunk:
                response_text += chunk['message']['content']
        
        return response_text.strip()  # Return the full response
    except Exception as e:
        print(f"Error with LLM API: {e}")
        return "An error occurred while contacting the external LLM."

# Route for home page
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle chatbot queries
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

        # Get the response from the LLM
        response = ask_llm(question)

        return jsonify({"answer": response})
    finally:
        lock.release()  # Release the lock after processing

if __name__ == '__main__':
    app.run(debug=True)
