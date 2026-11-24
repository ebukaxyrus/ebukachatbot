# Ebuka Chatbot

A compact Streamlit chatbot using OpenAI chat completions.

## Technology stack
- Python
- Streamlit
- OpenAI Python SDK

## Verified implementation
- Accepts a text prompt
- calls an OpenAI chat-completion model
- shows the response in the interface.

## Getting started

```bash
git clone https://github.com/ebukaxyrus/ebukachatbot.git
cd ebukachatbot
python -m venv .venv
source .venv/bin/activate  # Windows PowerShell: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
streamlit run chatbot.py
```

Review the source for required API credentials, data files, local environment settings, and device permissions before running. Never commit real API keys or passwords.

## Important limitations

Requires a configured OPENAI_API_KEY in Streamlit secrets and a supported available model; API usage may incur costs.

## Project structure

- `chatbot.py`: primary application entry point.
- `requirements.txt`: Python package requirements.

## Suggested next improvements

- [ ] Test installation from scratch and pin versions.
- [ ] Include real screenshots, verified live URL and a demo walkthrough.
- [ ] Add automated tests and document tested configuration.
- [ ] Verify source/data rights and operational security.

## Maintainer

**Dimakunne Chukwuebuka Francis**  
[GitHub](https://github.com/ebukaxyrus) · [Portfolio](https://xyrusportfolio.netlify.app/) · [XY AI Solution](https://xyaisolution.online/)

*Documentation is grounded in source review; the application was not independently deployed or benchmarked for this update.*
