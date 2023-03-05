# Autocompleter

Autocompleter is a web-based application that uses machine learning techniques to autocomplete user input and provides suggestions for the next phrase or word. The application is built with Flask, a Python web framework, and leverages the OpenAI GPT (Generative Pre-trained Transformer) model for generating the suggestions.

## Features
- Autocomplete user input with AI-generated suggestions
- Web-based interface for easy accessibility
- Lightweight and fast

## Requirements
- Python 3
- Flask 2.0 or later
- OpenAI API key (to use the GPT model)
- Modern web browser with JavaScript enabled

## Installation and Usage
1. Clone the repository to your local machine.
```bash
git clone https://github.com/pneb/autocompleter.git
```

2. Install the required Python packages using pip.
```bash
pip install -r requirements.txt
```

3. Set the OpenAI API key as an environment variable.
```bash
export OPENAI_API_KEY=<your_api_key>
```

4. Start the Flask development server.
```bash
flask run
```

5. Open a modern web browser and navigate to `http://localhost:5000`.

6. Enter some text in the input field and click the "Generate Suggestion" button to see the AI-generated suggestion.

## Contribution
If you'd like to contribute to the project, please follow the steps below:

1. Fork the repository to your GitHub account.

2. Clone the forked repository to your local machine.
```bash
git clone https://github.com/pneb/autocompleter.git
```

3. Create a new branch for your changes and switch to it.
```bash
git checkout -b <your-branch-name>
```

4. Make your changes, add and commit them.
```bash
git commit -am "<your-commit-message>"
```

5. Push your changes to your forked repository.
```bash
git push origin <your-branch-name>
```

6. Create a pull request from your branch to the main branch of the original repository.
