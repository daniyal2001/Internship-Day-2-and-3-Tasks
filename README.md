# Built and deployed by Muhammad Daniyal
# Nova AI Chatbot

A modern AI chatbot built with Python and Flask, using the Groq API for AI-powered responses.

The application supports conversational context, persistent chat history, Markdown-formatted responses, voice input, and text-to-speech output.

## Features

* AI-powered conversational chat
* Conversation history and context
* Persistent chat history using browser local storage
* Automatic conversation titles based on the main topic
* Markdown-formatted AI responses
* Voice input using browser speech recognition
* Voice output using browser speech synthesis
* Loading/typing indicator
* Error handling
* Responsive dark-themed UI
* Secure API key management using environment variables

## Technology Used

### Backend

* Python
* Flask
* OpenAI Python SDK
* python-dotenv

### AI API

* Groq API
* OpenAI-compatible API interface
* Model: `openai/gpt-oss-20b`

### Frontend

* HTML
* CSS
* JavaScript
* Markdown rendering with Marked.js
* Browser Web Speech API

## Project Structure

```text
nova-ai-chatbot/
│
├── app.py
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
│
└── templates/
    └── index.html
```

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/nova-ai-chatbot.git
cd nova-ai-chatbot
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create the `.env` file

Create a file named `.env` in the project root.

Add:

```text
API_KEY=YOUR_GROQ_API_KEY
BASE_URL=https://api.groq.com/openai/v1
MODEL=openai/gpt-oss-20b
```

Replace `YOUR_GROQ_API_KEY` with your own API key.

### 5. Start the application

```bash
python app.py
```

The Flask server will start locally.

Open the local address shown in the terminal, usually:

```text
http://127.0.0.1:5000
```

## API Integration Approach

The chatbot uses Flask as the backend between the web interface and the AI API.

The basic flow is:

```text
User Message
     ↓
JavaScript Frontend
     ↓
Flask /chat Endpoint
     ↓
Conversation History + System Prompt
     ↓
Groq API
     ↓
AI Model
     ↓
AI Response
     ↓
Flask
     ↓
Frontend
     ↓
Displayed to User
```

The frontend sends the user's message along with the existing conversation history to the Flask `/chat` endpoint.

Flask validates the request, adds the system prompt, and sends the conversation to the Groq API using the OpenAI-compatible Python SDK.

The AI response is returned to the frontend as JSON and displayed in the chat interface.

## Conversation History

The chatbot maintains conversation context by sending previous messages with each new request.

For example:

```text
User: My name is Daniyal.
AI: Nice to meet you, Daniyal!

User: What is my name?
AI: Your name is Daniyal.
```

The conversation history is maintained in the browser and sent to the backend with each request.

Chat conversations are also stored in browser `localStorage`, allowing them to remain available after refreshing the page on the same browser.

## Automatic Chat Titles

The application analyzes the conversation topic and generates a short title.

For example:

```text
User: Hi
User: Tell me the basics of IoT
```

The history can be titled:

```text
Basics of IoT
```

Instead of simply using the first message such as "Hi".

## Voice Features

The chatbot uses browser speech APIs to provide:

### Voice Input

The Web Speech API converts spoken input into text.

### Voice Output

The Speech Synthesis API reads AI responses aloud.

These features depend on browser support.

## Security

API credentials are stored in a `.env` file and are not hard-coded into the application.

The `.env` file is excluded from Git using `.gitignore`.

The repository only contains `.env.example` as a template.

**Never commit the actual API key to GitHub.**

## What I Learned

Through this project, I learned how to:

* Build a basic AI-powered web application
* Create a Flask backend and API endpoint
* Integrate an AI API using the OpenAI Python SDK
* Work with an OpenAI-compatible API
* Manage API credentials using environment variables
* Send conversation history to an AI model
* Build an interactive frontend using HTML, CSS, and JavaScript
* Store client-side data using localStorage
* Handle API errors in a web application
* Add voice input and text-to-speech functionality
* Structure a small full-stack AI application

## Future Improvements

Some improvements I would make in future versions include:

* User authentication and cloud-based conversation storage
* Database integration for persistent server-side history
* Streaming AI responses
* File upload and document analysis
* More advanced voice interaction
* Multiple AI model selection
* Better conversation search and organization
* Deployment with a production WSGI server
* Improved security and rate limiting

## Author

**Muhammad Daniyal**

Built & deployed as part of an AI Internship practical task.

---

## License

This project was created for educational and internship purposes.
