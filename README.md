# Built and Deployed by Muhammad Daniyal
# Nova AI — AI Chatbot

Nova AI is a web-based AI chatbot developed using Python, Flask, HTML, CSS, JavaScript, and the Groq API.

The application allows users to interact with an AI assistant, maintain conversation history, and automatically generate short titles for conversations.

## Features

* AI-powered chat responses
* Groq API integration
* Custom system prompt and assistant personality
* Conversation history
* Automatic AI-generated chat titles
* Markdown response rendering
* Loading indicators
* Error handling
* Input validation
* API rate limiting
* Voice input and output
* Clear chat functionality
* Responsive user interface
* Health-check endpoint
* Secure environment variable configuration

## Technologies Used

| Technology        | Purpose                           |
| ----------------- | --------------------------------- |
| Python            | Backend programming               |
| Flask             | Web framework and API routes      |
| Groq API          | AI response generation            |
| HTML              | Application structure             |
| CSS               | User interface styling            |
| JavaScript        | Frontend functionality            |
| OpenAI Python SDK | API communication                 |
| Flask-Limiter     | Request rate limiting             |
| python-dotenv     | Environment configuration         |
| localStorage      | Browser-side conversation history |

## Architecture

User → Frontend → Flask Backend → Groq API → Flask Backend → Frontend

## Installation

1. Clone the repository:

```bash
git clone https://github.com/daniyal2001/nova-ai-chatbot.git
```

2. Navigate to the project:

```bash
cd nova-ai-chatbot
```

3. Create and activate a virtual environment:

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

5. Create a `.env` file using `.env.example` and configure your Groq API credentials.

6. Run the application:

```bash
python app.py
```

7. Open:

```text
http://127.0.0.1:5000
```

## API Endpoints

* `/` — Main chatbot interface
* `/chat` — Processes user messages and returns AI responses
* `/title` — Generates conversation titles
* `/health` — Checks application status

## Security

* API credentials are stored in environment variables.
* `.env` is excluded from Git.
* User input is validated.
* Request size and rate limits are configured.

## What I Learned

* Building a backend using Python and Flask
* Integrating an external AI API
* Handling JSON requests and responses
* Managing conversation context
* Implementing error handling and validation
* Using environment variables
* Developing an interactive frontend
* Debugging API and deployment issues

## Developer

Muhammad Daniyal
BS Artificial Intelligence Student

Built as part of an AI Internship Project.
