import streamlit as st
import random
from pipeline import run_research_pipeline

# ── Page config ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Autonomous Research Intelligence",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Custom CSS ─────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=Space+Mono:ital,wght@0,400;0,700;1,400&display=swap');

*, *::before, *::after { box-sizing: border-box; }

html, body, [data-testid="stAppViewContainer"] {
    background: #0a0a0f !important;
    color: #e8e6e0 !important;
    font-family: 'Space Mono', monospace !important;
}

#MainMenu, footer, header { visibility: hidden; }
[data-testid="stDecoration"] { display: none; }
.block-container { padding: 3rem 4rem 4rem !important; max-width: 1100px !important; }

.hero {
    border-bottom: 1px solid #2a2a3a;
    padding-bottom: 2.5rem;
    margin-bottom: 3rem;
}
.hero-eyebrow {
    font-family: 'Space Mono', monospace;
    font-size: 0.72rem;
    letter-spacing: 0.25em;
    color: #5a5aff;
    text-transform: uppercase;
    margin-bottom: 0.75rem;
}
.hero-title {
    font-family: 'Syne', sans-serif;
    font-size: clamp(2.4rem, 5vw, 4rem);
    font-weight: 800;
    line-height: 1.05;
    color: #f0ede6;
    margin: 0 0 1rem 0;
    letter-spacing: -0.02em;
}
.hero-title span { color: #5a5aff; }
.hero-sub {
    font-size: 0.82rem;
    color: #6b6b80;
    max-width: 520px;
    line-height: 1.8;
}

.input-label {
    font-family: 'Syne', sans-serif;
    font-size: 0.75rem;
    font-weight: 600;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: #5a5aff;
    margin-bottom: 0.75rem;
}

/* Hide Streamlit's native text input, we render our own animated one */
.animated-input-wrapper {
    position: relative;
    width: 100%;
}
#animated-placeholder-box {
    background: #12121c;
    border: 1px solid #2a2a3a;
    border-radius: 4px;
    color: #3a3a50;
    font-family: 'Space Mono', monospace;
    font-size: 0.95rem;
    padding: 0.85rem 1.2rem;
    width: 100%;
    min-height: 52px;
    display: flex;
    align-items: center;
    pointer-events: none;
    overflow: hidden;
    white-space: nowrap;
}
#animated-placeholder-text {
    opacity: 1;
    transition: opacity 0.4s ease;
}
#cursor {
    display: inline-block;
    width: 2px;
    height: 1.1em;
    background: #5a5aff;
    margin-left: 2px;
    vertical-align: middle;
    animation: blink 1s step-end infinite;
}
@keyframes blink {
    0%, 100% { opacity: 1; }
    50% { opacity: 0; }
}

[data-testid="stTextInput"] input {
    background: #12121c !important;
    border: 1px solid #2a2a3a !important;
    border-radius: 4px !important;
    color: #e8e6e0 !important;
    font-family: 'Space Mono', monospace !important;
    font-size: 0.95rem !important;
    padding: 0.85rem 1.2rem !important;
    transition: border-color 0.2s;
}
[data-testid="stTextInput"] input:focus {
    border-color: #5a5aff !important;
    box-shadow: 0 0 0 3px rgba(90,90,255,0.12) !important;
    outline: none !important;
}
[data-testid="stTextInput"] input::placeholder { color: transparent !important; }

[data-testid="stButton"] > button {
    background: #5a5aff !important;
    color: #fff !important;
    border: none !important;
    border-radius: 4px !important;
    font-family: 'Syne', sans-serif !important;
    font-weight: 700 !important;
    font-size: 0.85rem !important;
    letter-spacing: 0.1em !important;
    text-transform: uppercase !important;
    padding: 0.75rem 2.2rem !important;
    cursor: pointer !important;
    transition: background 0.2s, transform 0.1s !important;
}
[data-testid="stButton"] > button:hover {
    background: #7070ff !important;
    transform: translateY(-1px) !important;
}
[data-testid="stButton"] > button:active { transform: translateY(0) !important; }
[data-testid="stButton"] > button:disabled {
    background: #2a2a3a !important;
    color: #4a4a60 !important;
    cursor: not-allowed !important;
}

.steps-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 1px;
    background: #2a2a3a;
    border: 1px solid #2a2a3a;
    border-radius: 6px;
    overflow: hidden;
    margin: 2rem 0;
}
.step-card {
    background: #0e0e18;
    padding: 1.25rem 1.1rem;
    position: relative;
}
.step-num {
    font-family: 'Syne', sans-serif;
    font-size: 1.6rem;
    font-weight: 800;
    color: #1e1e2e;
    line-height: 1;
    margin-bottom: 0.4rem;
}
.step-label {
    font-size: 0.72rem;
    font-weight: 700;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: #4a4a60;
    margin-bottom: 0.2rem;
}
.step-desc { font-size: 0.73rem; color: #3a3a50; line-height: 1.5; }

.step-card.active .step-num { color: #5a5aff; }
.step-card.active .step-label { color: #9090ff; }
.step-card.active .step-desc { color: #6b6b80; }
.step-card.active::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 2px;
    background: #5a5aff;
}
.step-card.done .step-num { color: #3a3a50; }
.step-card.done .step-label { color: #3a3a50; }
.step-card.done::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 2px;
    background: #2a2a3a;
}
.step-card.done::after {
    content: '✓';
    position: absolute;
    top: 0.9rem; right: 0.9rem;
    font-size: 0.75rem;
    color: #4a8a4a;
}

.result-panel {
    background: #0e0e18;
    border: 1px solid #2a2a3a;
    border-radius: 6px;
    margin-bottom: 1.25rem;
    overflow: hidden;
}
.result-panel-header {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    padding: 0.85rem 1.25rem;
    border-bottom: 1px solid #2a2a3a;
    background: #0a0a14;
}
.result-panel-tag {
    font-size: 0.65rem;
    font-weight: 700;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    background: #1e1e30;
    color: #5a5aff;
    padding: 0.2rem 0.55rem;
    border-radius: 3px;
}
.result-panel-title {
    font-family: 'Syne', sans-serif;
    font-size: 0.82rem;
    font-weight: 700;
    color: #c0bdb6;
    letter-spacing: 0.05em;
}
.result-panel-body {
    padding: 1.25rem;
    font-size: 0.82rem;
    line-height: 1.9;
    color: #9090a0;
    white-space: pre-wrap;
    word-break: break-word;
    max-height: 340px;
    overflow-y: auto;
}
.result-panel-body::-webkit-scrollbar { width: 4px; }
.result-panel-body::-webkit-scrollbar-thumb { background: #2a2a3a; border-radius: 2px; }

.result-panel.report .result-panel-body {
    max-height: 600px;
    color: #c8c5be;
    font-size: 0.85rem;
}
.result-panel.report .result-panel-tag { color: #ffd166; background: #2a1e06; }
.result-panel.feedback .result-panel-tag { color: #06d6a0; background: #062a1e; }

[data-testid="stProgress"] > div > div {
    background: #5a5aff !important;
    border-radius: 2px !important;
}
[data-testid="stProgress"] > div {
    background: #1e1e2e !important;
    border-radius: 2px !important;
    height: 3px !important;
}

.status-line {
    font-size: 0.75rem;
    color: #5a5aff;
    letter-spacing: 0.08em;
    margin: 0.4rem 0 1.2rem;
    font-family: 'Space Mono', monospace;
}
.status-line::before { content: '▶  '; }

hr { border-color: #1e1e2e !important; margin: 2.5rem 0 !important; }

[data-testid="stAlert"] {
    background: #1e0a0a !important;
    border: 1px solid #5a2020 !important;
    border-radius: 4px !important;
    color: #e06060 !important;
    font-size: 0.82rem !important;
}
</style>
""", unsafe_allow_html=True)

# ── Animated placeholder JS ────────────────────────────────────────────────────
st.markdown("""
<script>
(function() {
  const topics = [
    "Impact of AI on global job markets",
    "Latest breakthroughs in cancer immunotherapy",
    "The rise of autonomous vehicles in 2025",
    "Climate change adaptation strategies",
    "Geopolitics of semiconductor supply chains",
    "Generative AI in creative industries",
    "Future of nuclear fusion energy",
    "Mental health crisis among Gen Z",
    "Decentralised finance and Web3 trends",
    "Quantum error correction in 2025",
    "GLP-1 drugs and the future of obesity treatment",
    "Solid-state batteries and the EV revolution",
    "AI regulation landscape in Europe",
    "CRISPR gene editing — where are we now?",
    "Rise of multimodal AI models",
    "Microplastics in the human body",
    "The future of remote work post-2024",
    "Central bank digital currencies explained",
  ];

  let topicIdx = 0;
  let charIdx = 0;
  let deleting = false;
  let paused = false;

  function getEl() {
    return document.getElementById('animated-placeholder-text');
  }

  function tick() {
    const el = getEl();
    if (!el) { setTimeout(tick, 300); return; }

    const full = topics[topicIdx];

    if (paused) {
      paused = false;
      deleting = true;
      setTimeout(tick, 1200);
      return;
    }

    if (!deleting) {
      charIdx++;
      el.textContent = full.slice(0, charIdx);
      if (charIdx === full.length) {
        paused = true;
        setTimeout(tick, 50);
      } else {
        setTimeout(tick, 55);
      }
    } else {
      charIdx--;
      el.textContent = full.slice(0, charIdx);
      if (charIdx === 0) {
        deleting = false;
        topicIdx = (topicIdx + 1) % topics.length;
        setTimeout(tick, 400);
      } else {
        setTimeout(tick, 28);
      }
    }
  }

  // Wait for DOM
  function init() {
    if (document.getElementById('animated-placeholder-text')) {
      tick();
    } else {
      setTimeout(init, 200);
    }
  }
  init();
})();
</script>
""", unsafe_allow_html=True)

# ── Session state ──────────────────────────────────────────────────────────────
for k, v in {
    "running": False,
    "results": None,
    "current_step": 0,
    "error": None,
}.items():
    if k not in st.session_state:
        st.session_state[k] = v

# ── Hero ───────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
  <div class="hero-eyebrow">Multi-Agent Research System</div>
  <h1 class="hero-title">Autonomous<span>Research</span><br>Intelligence</h1>
  <p class="hero-sub">Four autonomous agents — search, scrape, write, critique — working in sequence to produce a structured research report on any topic.</p>
</div>
""", unsafe_allow_html=True)

# ── Input row ──────────────────────────────────────────────────────────────────
st.markdown('<div class="input-label">Research Topic</div>', unsafe_allow_html=True)

# Animated typewriter placeholder sits visually above the real input
st.markdown("""
<div id="animated-placeholder-box">
  <span id="animated-placeholder-text"></span><span id="cursor"></span>
</div>
<style>
/* Overlap: hide native input visually, keep it functional */
div[data-testid="stTextInput"] {
    margin-top: -56px !important;
    opacity: 0 !important;
    position: relative !important;
    z-index: 10 !important;
}
div[data-testid="stTextInput"]:focus-within {
    opacity: 1 !important;
}
div[data-testid="stTextInput"]:focus-within ~ #animated-placeholder-box,
div[data-testid="stTextInput"]:focus-within + #animated-placeholder-box {
    display: none;
}
</style>
""", unsafe_allow_html=True)

col_input, col_btn = st.columns([5, 1], gap="small")

with col_input:
    topic = st.text_input(
        label="topic",
        placeholder="",
        label_visibility="collapsed",
        disabled=st.session_state.running,
    )

with col_btn:
    run_btn = st.button(
        "Run →",
        disabled=st.session_state.running or not topic.strip(),
        use_container_width=True,
    )

# ── Step tracker ──────────────────────────────────────────────────────────────
STEPS = [
    ("01", "Search Agent", "Retrieves recent, reliable sources"),
    ("02", "Reader Agent", "Scrapes top URL for deep content"),
    ("03", "Writer Chain", "Drafts a structured report"),
    ("04", "Critic Chain", "Reviews and scores the report"),
]

def render_steps(active: int, done_up_to: int):
    cards = ""
    for i, (num, label, desc) in enumerate(STEPS):
        cls = ""
        if i < done_up_to:
            cls = "done"
        elif i == active:
            cls = "active"
        cards += f'<div class="step-card {cls}"><div class="step-num">{num}</div><div class="step-label">{label}</div><div class="step-desc">{desc}</div></div>'
    return f'<div class="steps-grid">{cards}</div>'

steps_placeholder = st.empty()
steps_placeholder.markdown(render_steps(-1, 0), unsafe_allow_html=True)

# ── Pipeline execution ─────────────────────────────────────────────────────────
status_ph = st.empty()
progress_ph = st.empty()

STEP_LABELS = [
    "Search agent retrieving sources…",
    "Reader agent scraping content…",
    "Writer drafting report…",
    "Critic reviewing report…",
]

if run_btn and topic.strip():
    st.session_state.running = True
    st.session_state.results = None
    st.session_state.error = None
    st.session_state.current_step = 0

    try:
        import builtins
        original_print = builtins.print

        step_markers = [
            "Step 1 - Search agent",
            "Step 2 -  Reader agent",
            "Step 3 - Writer",
            "Step 4 - Critic",
        ]

        def patched_print(*args, **kwargs):
            text = " ".join(str(a) for a in args)
            for i, marker in enumerate(step_markers):
                if marker in text:
                    steps_placeholder.markdown(render_steps(i, i), unsafe_allow_html=True)
                    status_ph.markdown(f'<div class="status-line">{STEP_LABELS[i]}</div>', unsafe_allow_html=True)
                    progress_ph.progress((i + 1) / 4)
                    break

        builtins.print = patched_print

        try:
            state = run_research_pipeline(topic.strip())
        finally:
            builtins.print = original_print

        st.session_state.results = state
        steps_placeholder.markdown(render_steps(-1, 4), unsafe_allow_html=True)
        status_ph.markdown('<div class="status-line">Pipeline complete.</div>', unsafe_allow_html=True)
        progress_ph.progress(1.0)

    except Exception as e:
        st.session_state.error = str(e)
        builtins.print = original_print

    st.session_state.running = False
    st.rerun()

# ── Results display ────────────────────────────────────────────────────────────
if st.session_state.error:
    st.error(f"Pipeline error: {st.session_state.error}")

if st.session_state.results:
    r = st.session_state.results
    st.markdown("<hr>", unsafe_allow_html=True)

    if r.get("search_results"):
        st.markdown(f"""
        <div class="result-panel">
          <div class="result-panel-header">
            <span class="result-panel-tag">Agent 01</span>
            <span class="result-panel-title">Search Results</span>
          </div>
          <div class="result-panel-body">{r["search_results"]}</div>
        </div>
        """, unsafe_allow_html=True)

    if r.get("scraped_content"):
        st.markdown(f"""
        <div class="result-panel">
          <div class="result-panel-header">
            <span class="result-panel-tag">Agent 02</span>
            <span class="result-panel-title">Scraped Content</span>
          </div>
          <div class="result-panel-body">{r["scraped_content"]}</div>
        </div>
        """, unsafe_allow_html=True)

    if r.get("report"):
        report_text = r["report"]
        if hasattr(report_text, "content"):
            report_text = report_text.content
        st.markdown(f"""
        <div class="result-panel report">
          <div class="result-panel-header">
            <span class="result-panel-tag">Writer</span>
            <span class="result-panel-title">Generated Report</span>
          </div>
          <div class="result-panel-body">{report_text}</div>
        </div>
        """, unsafe_allow_html=True)

    if r.get("feedback"):
        feedback_text = r["feedback"]
        if hasattr(feedback_text, "content"):
            feedback_text = feedback_text.content
        st.markdown(f"""
        <div class="result-panel feedback">
          <div class="result-panel-header">
            <span class="result-panel-tag">Critic</span>
            <span class="result-panel-title">Review &amp; Feedback</span>
          </div>
          <div class="result-panel-body">{feedback_text}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    full_output = f"""AUTONOMOUS RESEARCH INTELLIGENCE — {topic}
{'='*60}

SEARCH RESULTS
{'-'*60}
{r.get('search_results','')}

SCRAPED CONTENT
{'-'*60}
{r.get('scraped_content','')}

REPORT
{'-'*60}
{r.get('report','')}

CRITIC FEEDBACK
{'-'*60}
{r.get('feedback','')}
"""
    st.download_button(
        label="↓  Download Full Report",
        data=full_output,
        file_name=f"research_{topic[:40].replace(' ','_')}.txt",
        mime="text/plain",
    )