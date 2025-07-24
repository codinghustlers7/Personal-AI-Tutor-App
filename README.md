# Personal AI Tutor

A web-based AI-powered personal tutoring application built with Flask, OpenAI's API, and a clean Bootstrap frontend. It lets users start, manage, and interact with tutoring sessions in real time, offering quick prompts and free-form questions.

## Features

* **Session Management**: Create new tutoring sessions, each with its own student and session IDs.
* **AI-Powered Q\&A**: Ask any question and receive AI-generated responses via the OpenAI API.
* **Quick Prompts**: One-click buttons for common tasks like creating study schedules or explaining concepts.
* **Responsive UI**: Bootstrap-based layout with animated gradient background and translucent chat cards.
* **Dockerized**: Ready-to-run Docker image for easy deployment.
## Gif of Project
![2025-07-23 23 38 47](https://github.com/user-attachments/assets/09cc03fd-e49e-4f48-bcac-2abec0561c8b)


### Prerequisites

* Python 3.9+
* An [OpenAI API key](https://platform.openai.com/account/api-keys)
* Docker (optional, for containerized deployment)

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/personal-ai-tutor-app.git
   cd personal-ai-tutor-app
   ```

2. **Create a virtual environment** (recommended):

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Set environment variables**:

   ```bash
   export OPENAI_API_KEY="sk-..."
   export FLASK_SECRET="your_flask_secret"
   ```

5. **Run the app locally**:

   ```bash
   python main.py
   ```

   Navigate to `http://localhost:3000` in your browser.

## Docker Deployment

1. **Build the image**:

   ```bash
   docker build -t tutor-app .
   ```

2. **Run the container**:

   ```bash
   docker run --rm \
     -e OPENAI_API_KEY="sk-..." \
     -p 3000:3000 \
     tutor-app
   ```

3. **Visit**: `http://localhost:3000`

## Heroku Deployment

1. **Create a `Procfile`** (already included):

   ```text
   web: gunicorn main:app
   ```

2. **Login & create app**:

   ```bash
   heroku login
   heroku create your-app-name
   ```

3. **Set config vars**:

   ```bash
   heroku config:set OPENAI_API_KEY="sk-..."
   heroku config:set FLASK_SECRET="your_flask_secret"
   ```

4. **Deploy**:

   ```bash
   git push heroku main
   heroku open
   ```

## Project Structure

```
personal-ai-tutor-app/
├── controllers/            # Flask route handlers
│   └── tutor_controller.py
├── services/               # OpenAI integration
│   └── tutor_service.py
├── templates/
│   └── tutor.html          # Main HTML template
├── static/
│   └── style.css           # Custom styles
├── main.py                 # App entry point
├── requirements.txt        # Python dependencies
├── Dockerfile              # Docker build instructions
└── README.md               # This file
```

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
