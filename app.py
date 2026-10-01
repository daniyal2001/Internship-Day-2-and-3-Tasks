import os
from flask import Flask, request, jsonify, render_template
from openai import OpenAI
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

app = Flask(__name__)


# ==========================================
# GROQ API CONNECTION
# ==========================================

client = OpenAI(
    api_key=os.getenv("API_KEY"),
    base_url=os.getenv(
        "BASE_URL",
        "https://api.groq.com/openai/v1"
    )
)


MODEL = os.getenv(
    "MODEL",
    "openai/gpt-oss-20b"
)


# ==========================================
# SYSTEM PROMPT
# ==========================================

SYSTEM_PROMPT = """
You are a helpful AI assistant.

You have access to the conversation history provided
in the messages.

Use previous messages to understand context and
remember information the user has already provided.

Answer clearly and concisely.

If the user asks something about a previous message,
use the conversation history to answer it directly.

If you are not sure about something, say so.
"""


# ==========================================
# HOME PAGE
# ==========================================

@app.route("/")
def index():

    return render_template("index.html")


# ==========================================
# CHAT API
# ==========================================

@app.route("/chat", methods=["POST"])
def chat():

    # Get JSON data
    data = request.get_json(silent=True) or {}

    # Get conversation history
    history = data.get("messages", [])


    # Make sure history exists
    if not history:

        return jsonify(
            error="No message provided."
        ), 400


    # ======================================
    # VALIDATE HISTORY
    # ======================================

    valid_history = []

    for message in history:

        role = message.get("role")
        content = message.get("content")


        # Only allow user and assistant messages
        if role not in ["user", "assistant"]:

            continue


        # Ignore empty messages
        if not content:

            continue


        valid_history.append({

            "role": role,

            "content": str(content)

        })


    if not valid_history:

        return jsonify(
            error="Invalid conversation history."
        ), 400


    # ======================================
    # BUILD COMPLETE MESSAGE LIST
    # ======================================

    messages = [

        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }

    ] + valid_history


    try:

        # Send complete conversation to Groq
        response = client.chat.completions.create(

            model=MODEL,

            messages=messages

        )


        # Get AI response
        reply = response.choices[0].message.content


        return jsonify(

            reply=reply

        )


    except Exception as e:

        print("AI request error:", e)


        return jsonify(

            error=f"AI request failed: {e}"

        ), 500


# ==========================================
# START SERVER
# ==========================================

if __name__ == "__main__":

    if not os.getenv("API_KEY"):

        raise SystemExit(
            "Missing API_KEY. "
            "Add your Groq API key to the .env file."
        )


    app.run(debug=True)
