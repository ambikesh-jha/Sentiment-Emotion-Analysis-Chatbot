import ollama

def ask_llm(question):
    try:
        # Start streaming the response
        response_stream = ollama.chat(
            model="llama3.2:1b",
            messages=[
                {"role": "system", 
                 "content": " first provide sentimental analysis as (positive ,negative or neutral).and then provide type emotion in one word .e.g (angry ,happy , threatning,etc)"},
                {"role": "user", "content": question}
            ],
            stream=True  # Enable streaming if supported
        )
        
        print("Response: ", end="")  # Start printing without a newline
        for chunk in response_stream:
            if isinstance(chunk, dict) and 'message' in chunk:
                # Print the content directly without adding extra spaces
                print(chunk['message']['content'], end="", flush=True)
        print()  # End with a newline after the full response is printed
        
    except Exception as e:
        print(f"Error with LLM API: {e}")
        return "An error occurred while contacting the external LLM."


