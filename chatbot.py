import streamlit as st
from openai import OpenAI

# ---------- CSS: gold background, black text, and force button text white ----------
st.markdown(
    """
    <style>
        /* Gold background for entire app */
        .stApp {
            background-color: gold;
        }

        /* Centered black title */
        .title {
            text-align: center;
            color: black !important;
            font-size: 2.8em;
            font-weight: 800;
            margin-bottom: 0.5em;
        }

        /* Make most labels and paragraphs black */
        label, .stTextInput label, .stTextArea label, .stMarkdown, p, div, span {
            color: black !important;
        }

        /* Textarea: white background + black text for readability */
        textarea, .stTextArea > div > textarea {
            background-color: white !important;
            color: black !important;
        }

        /* Ensure Streamlit markdown paragraphs are black */
        .stMarkdown p {
            color: black !important;
        }

        /* -------- Button styling --------
           Target common Streamlit button selectors and force white text.
           Use multiple selectors and -webkit-text-fill-color to override browser defaults.
        */
        /* Main button container variant */
        div.stButton > button,
        /* Alternative selectors Streamlit may use */
        button[kind="primary"],
        button[data-testid="stButton"],
        .stButton button {
            background-color: black !important;    /* black background */
            color: white !important;                /* white text (important) */
            -webkit-text-fill-color: white !important; /* extra measure for some browsers */
            border: none !important;
            border-radius: 8px !important;
            height: 3em !important;
            width: 100% !important;
            font-size: 1em !important;
            font-weight: 700 !important;
            box-shadow: none !important;
        }

        /* Keep same style on hover / focus / active (no visual change) */
        div.stButton > button:hover,
        div.stButton > button:focus,
        div.stButton > button:active,
        button[data-testid="stButton"]:hover,
        button[data-testid="stButton"]:focus,
        button[data-testid="stButton"]:active {
            background-color: black !important;
            color: white !important;
            -webkit-text-fill-color: white !important;
            box-shadow: none !important;
            transform: none !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Create OpenAI client
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Centered black title
st.markdown('<h1 class="title">💬 Simple AI Chatbot</h1>', unsafe_allow_html=True)

# User input
prompt = st.text_area("Ask me anything:")

# Chat button and response
if st.button("Chat"):
    if prompt:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        # show response as black text (keeps chat text black)
        st.markdown(f"<div style='color:black; white-space: pre-wrap;'>{response.choices[0].message.content}</div>", unsafe_allow_html=True)
