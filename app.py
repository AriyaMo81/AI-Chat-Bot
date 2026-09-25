import streamlit as st
from chat_bot import bot

# ---------- Page config ----------
st.set_page_config(
    page_title="Ariya Chat Bot",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------- Custom CSS ----------
st.markdown(
    """
    <style>
    .stApp {
        background: radial-gradient(circle at 20% 20%, #1a1030 0%, #0d0a17 55%, #05050a 100%);
    }
    header {visibility: hidden;}
    footer {visibility: hidden;}

    .main-title {
        font-family: 'Segoe UI', sans-serif;
        font-weight: 900;
        font-size: 2.6rem;
        letter-spacing: 1px;
        background: linear-gradient(90deg,#7dd3fc,#a855f7,#f472b6,#fb923c);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 0;
        animation: glow 4s ease-in-out infinite alternate;
    }
    @keyframes glow {
        from { filter: drop-shadow(0 0 6px rgba(168,85,247,0.4)); }
        to   { filter: drop-shadow(0 0 18px rgba(244,114,182,0.7)); }
    }
    .subtitle {
        text-align: center;
        color: #c4b5fd;
        font-size: 1rem;
        margin-top: 0.3rem;
        margin-bottom: 1.8rem;
        font-style: italic;
    }
    [data-testid="stChatMessage"] {
        background: rgba(255,255,255,0.045);
        border: 1px solid rgba(168,85,247,0.18);
        border-radius: 16px;
        padding: 12px 16px;
        margin-bottom: 10px;
        backdrop-filter: blur(10px);
        box-shadow: 0 4px 20px rgba(0,0,0,0.25);
    }
    [data-testid="stChatInput"] {
        border-radius: 14px;
        background: rgba(255,255,255,0.05);
        border: 1px solid rgba(168,85,247,0.35);
    }
    section[data-testid="stSidebar"] {
        background: rgba(15,10,25,0.96);
        border-right: 1px solid rgba(168,85,247,0.18);
    }
    .stButton > button {
        width: 100%;
        border-radius: 12px;
        border: 1px solid rgba(255,255,255,0.15);
        background: linear-gradient(135deg,#7c3aed,#db2777);
        color: white;
        font-weight: 600;
        transition: all 0.25s ease;
    }
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 25px rgba(219,39,119,0.45);
    }
    .brand-badge {
        display: inline-block;
        padding: 4px 12px;
        border-radius: 999px;
        font-size: 0.75rem;
        font-weight: 700;
        color: #fde68a;
        background: rgba(251,191,36,0.08);
        border: 1px solid rgba(251,191,36,0.35);
        margin-bottom: 6px;
        letter-spacing: 2px;
    }
    .section-title {
        font-weight: 700;
        font-size: 1.05rem;
        color: #e9d5ff;
        margin-bottom: 0.4rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------- Sidebar ----------
with st.sidebar:
    st.markdown('<div class="brand-badge">✦ ARiYA AI</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">⚙️ تنظیمات Ariya</div>', unsafe_allow_html=True)
    st.write("")

    system_prompt = st.text_area(
        "📝 System Prompt",
        value="تو Ariya هستی، یک دستیار هوشمند، دقیق، مودب و مفید. همیشه به زبان کاربر پاسخ بده.",
        height=120,
    )

    st.divider()
    if st.button("🧹 پاک کردن گفتگو"):
        st.session_state.messages = [
            {"role": "system", "content": system_prompt}
        ]
        st.rerun()

    st.caption("Ariya Chat Bot © ساخته‌شده با ❤️ | Streamlit + Groq")

# ---------- Session state ----------
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": system_prompt}
    ]

if st.session_state.messages and st.session_state.messages[0]["role"] == "system":
    st.session_state.messages[0]["content"] = system_prompt

# ---------- Header ----------
st.markdown('<div class="main-title">✨ Ariya Chat Bot</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">دستیار هوشمند فوق‌سریع Ariya — متصل به Groq API</div>',
    unsafe_allow_html=True,
)

# ---------- Render history ----------
for msg in st.session_state.messages:
    if msg["role"] == "system":
        continue
    avatar = "👤" if msg["role"] == "user" else "✨"
    with st.chat_message(msg["role"], avatar=avatar):
        st.markdown(msg["content"])

# ---------- Chat input ----------
prompt = st.chat_input("✨ با Ariya حرف بزن...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar="👤"):
        st.markdown(prompt)

    with st.chat_message("assistant", avatar="✨"):
        with st.spinner("Ariya در حال فکر کردن است..."):
            try:
                answer = bot(st.session_state.messages)
            except Exception as e:
                answer = f"⚠️ خطا در ارتباط با Groq: `{e}`"

        st.markdown(answer)

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )