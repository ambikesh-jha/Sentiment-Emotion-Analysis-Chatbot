# Sentiment & Emotion Analysis Chatbot

An intelligent chatbot that not only responds to queries but also analyzes the emotional content of user messages. Built with Flask and powered by Llama 3.2 via Ollama, this application provides real-time sentiment analysis and emotion classification for every interaction.

## Features
- **Sentiment Analysis**: Classifies messages as positive, negative, or neutral
- **Emotion Detection**: Identifies specific emotions (angry, happy, threatening, etc.)
- **Real-time Streaming**: See responses as they're generated
- **Concurrency Control**: Thread-safe design prevents LLM overload
- **Lightweight**: Minimal dependencies, fast response times
- **Error Handling**: Graceful degradation with user-friendly error messages

## How It Works
1. User sends a message through the web interface
2. System prompt guides the LLM to provide structured analysis
3. Llama 3.2 processes the input with sentiment/emotion instructions
4. Response streams back in real-time
5. Output format: "sentiment (positive/negative/neutral) + emotion (one word)"

## Tech Stack
- **Backend**: Flask (Python)
- **LLM**: Llama 3.2 1B via Ollama
- **Concurrency**: Python threading
- **Frontend**: HTML, JavaScript

## Installation

1. Clone the repository
   git clone https://github.com/yourusername/sentiment-emotion-chatbot.git
   cd sentiment-emotion-chatbot
