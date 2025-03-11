Key Features:
OpenAI Integration for Text Processing

Uses OpenAI’s text-moderation-latest model to analyze and respond to user questions.
Configures temperature=0.5 for a balanced response (neither too random nor too deterministic).
Streamlit-based Web Interface

Provides an interactive UI with a text input field for users to ask questions.
Displays AI-generated responses instantly upon clicking the “Ask the question” button.
Environment Variables for Security

Loads the OpenAI API Key from a .env file to ensure security and prevent hardcoding.
Minimalistic & Efficient Implementation

Uses LangChain’s OpenAI wrapper for easy LLM access and processing.
Implements a clean, single-function design to handle user queries efficiently.
Technologies Used:
Streamlit – For building the interactive web app.
LangChain – For easy interaction with OpenAI models.
OpenAI API – To generate AI responses.
Dotenv – For managing API keys securely.
