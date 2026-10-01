# AI Chatbot

## What I built
A simple web chatbot. The user types a message, the Flask backend sends it to an AI model, and the reply is shown in the chat window.

Features: conversation history, system prompt, loading state, error handling, basic UI.

## Technology used
- Python 3, Flask (backend)
- OpenAI Python SDK (works with any OpenAI-compatible API)
- HTML, CSS and vanilla JavaScript (frontend)
- python-dotenv for keeping the API key out of the code

## How to run
```bash
git clone <your-repo-url>
cd ai-chatbot
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env            # Windows: copy .env.example .env
# open .env and paste your API key
python app.py
```
Open http://127.0.0.1:5000 in your browser.

## API integration approach
1. The browser sends the whole conversation (`messages`) to `POST /chat`.
2. The server adds a system prompt at the start and calls `client.chat.completions.create(...)`.
3. The model's reply is returned as JSON and displayed in the page.
4. The server keeps no state. The browser holds the history and resends it each turn, which is how the model "remembers" the conversation.
5. The API key is read from `.env` and `.env` is listed in `.gitignore`, so it is never committed.
6. Errors (bad key, rate limit, network) are caught and shown in the chat.

## What I learned
- [Write 2-3 points in your own words, e.g. how chat APIs are stateless and need the history each time]

## What I would improve next
- Stream the response token by token
- Render Markdown in replies
- Save conversations in a database
- Add voice input and output

## Demo
[Add screenshot here]
