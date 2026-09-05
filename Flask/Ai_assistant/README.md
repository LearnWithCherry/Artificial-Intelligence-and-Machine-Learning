# AI Personal Assistant

A simple AI Personal Assistant built using **Flask, JavaScript, HTML, CSS, and the Groq API**.

## 🚀 Features

* Ask questions to the AI assistant
* Get AI-generated responses
* Simple and clean web interface
* Flask backend
* JavaScript frontend
* AI API integration
* Secure API key management using environment variables

## 🛠️ Technologies Used

* Python
* Flask
* HTML
* CSS
* JavaScript
* OpenAI Python SDK
* Groq API

## 📁 Project Structure

```text
Ai_assistant/
│
├── static/
│   └── style.css
│
├── templates/
│   └── index.html
│
├── main.py
├── .env
├── .gitignore
└── README.md
```

> **Note:** `.env` should not be uploaded to GitHub. It is shown above only to describe the local project structure.

## ⚙️ How to Run

### 1. Clone the repository

```bash
git clone YOUR_REPOSITORY_URL
cd Ai_assistant
```

### 2. Install dependencies

```bash
pip install flask python-dotenv openai
```

### 3. Create `.env`

Create a `.env` file in the project root directory:

```env
GROQ_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your actual Groq API key.

### 4. Run Flask

```bash
flask --app main run --debug
```

Then open the application in your browser:

```text
http://127.0.0.1:5000
```

## 🔐 Environment Variables

The project uses a `.env` file to store the API key securely.

Make sure `.env` is included in your `.gitignore` file:

```gitignore
.env
```

**Never commit your API key to GitHub or share it publicly.**

## 📚 What I Learned

This project helped me learn:

* Flask routes
* HTML templates
* Static files
* JavaScript `fetch()`
* POST requests
* FormData
* JSON responses
* Environment variables
* API integration
* Connecting a frontend to a Flask backend

## 🔮 Future Improvements

* Add conversation history
* Add Markdown rendering
* Add loading animation
* Add voice input
* Add AI conversation memory
* Add summarization feature
* Improve the user interface
* Add error handling and API status messages

## 👨‍💻 Author

**Rajat Bhardwaj**

````

### Recommended `.gitignore`

Create a file named `.gitignore` in your project root and add:

```gitignore
.env
__pycache__/
*.pyc
.venv/
venv/
````
