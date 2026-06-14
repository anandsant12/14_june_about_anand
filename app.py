
import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="Anand Sant | AI Engineer",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Unified Injection: Combines structural style resets and your custom portfolio theme
st.markdown("""
<style>
    /* Streamlit UI Reset Guardrails */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container { padding: 0 !important; margin: 0 !important; max-width: 100% !important; }
    section[data-testid="stSidebar"] {display: none;}
    .stApp { margin: 0; padding: 0; background: #faf8f4; }

    /* Custom Design Tokens & Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Inter:wght@300;400;500;600&display=swap');

    :root {
      --ivory: #faf8f4;
      --paper: #f2efe8;
      --ink: #1a1714;
      --ink2: #3d3a36;
      --ink3: #7a756e;
      --ink4: #b5b0a8;
      --accent: #c8622a;
      --border: #e8e3da;
      --borderD: #d4cec4;
    }

    /* Element Resets inside Streamlit App container */
    .stApp h1, .stApp h2, .stApp p, .stApp a, .stApp div, .stApp span {
        font-family: 'Inter', sans-serif;
        color: var(--ink);
    }
    
    html { scroll-behavior: smooth; }

    /* NAVIGATION */
    nav {
      position: fixed; top: 0; left: 0; right: 0; z-index: 100;
      display: flex; align-items: center; justify-content: space-between;
      padding: 0 clamp(20px, 5vw, 72px); height: 56px;
      background: rgba(250, 248, 244, 0.92);
      backdrop-filter: blur(16px); -webkit-backdrop-filter: blur(16px);
      border-bottom: 1px solid var(--border);
    }
    .logo { font-size: 14px; font-weight: 600; letter-spacing: -.2px; }
    .logo span { color: var(--accent); }
    .nav-links { display: flex; align-items: center; gap: 32px; }
    .nav-links a {
      text-decoration: none; font-size: 13px; font-weight: 400;
      color: var(--ink3); transition: color .15s; letter-spacing: .1px;
    }
    .nav-links a:hover, .nav-links a.active { color: var(--ink); }
    .nav-contact {
      font-size: 12px; font-weight: 500; color: var(--accent);
      text-decoration: none; letter-spacing: .2px;
      border-bottom: 1px solid var(--accent);
      padding-bottom: 1px; transition: opacity .15s;
    }
    .nav-contact:hover { opacity: .7; }

    .ham { display: none; flex-direction: column; gap: 4px; cursor: pointer; background: none; border: none; padding: 6px; }
    .ham span { display: block; width: 18px; height: 1px; background: var(--ink); transition: .25s; }
    .ham.open span:first-child { transform: translateY(5px) rotate(45deg); }
    .ham.open span:nth-child(2) { opacity: 0; }
    .ham.open span:last-child { transform: translateY(-5px) rotate(-45deg); }

    .drawer {
      display: none; position: fixed; inset: 56px 0 0 0;
      background: var(--ivory); z-index: 99;
      flex-direction: column; padding: 24px clamp(20px, 5vw, 72px);
      border-top: 1px solid var(--border);
    }
    .drawer.open { display: flex; }
    .drawer a {
      text-decoration: none; color: var(--ink); font-size: 22px;
      font-family: 'Instrument Serif', serif !important;
      padding: 18px 0; border-bottom: 1px solid var(--border);
      display: flex; align-items: center; justify-content: space-between;
    }
    .drawer a span { font-family: 'Inter', sans-serif; font-size: 12px; color: var(--ink4); }

    /* HERO */
    .hero {
      min-height: 100vh;
      display: flex; flex-direction: column; justify-content: flex-end;
      padding: 0 clamp(20px, 5vw, 72px) clamp(40px, 6vh, 72px);
      position: relative; overflow: hidden;
      margin-top: 56px;
    }
    .hero-bg { position: absolute; inset: 0; background: var(--ivory); }
    .hero-rule { position: absolute; right: clamp(20px, 5vw, 72px); top: 0; bottom: 0; width: 1px; background: var(--border); }
    .hero-rule2 { position: absolute; left: 0; right: 0; top: 40%; height: 1px; background: var(--border); }
    .hero-tag {
      position: relative; z-index: 1; font-size: 11px; font-weight: 500; color: var(--ink3);
      letter-spacing: 2px; text-transform: uppercase; margin-bottom: 20px; display: flex; align-items: center; gap: 10px;
    }
    .hero-tag::before { content: ''; width: 24px; height: 1px; background: var(--accent); }
    .hero h1 {
      position: relative; z-index: 1; font-family: 'Instrument Serif', serif !important;
      font-size: clamp(52px, 10vw, 120px); font-weight: 400; line-height: .93;
      letter-spacing: -2px; color: var(--ink); margin-bottom: clamp(24px, 4vh, 48px);
    }
    .hero h1 em { font-style: italic; color: var(--accent); display: block; }
    .hero-footer { position: relative; z-index: 1; display: flex; align-items: flex-end; justify-content: space-between; gap: 24px; flex-wrap: wrap; }
    .hero-desc { font-size: clamp(13px, 1.4vw, 15px); color: var(--ink3); line-height: 1.7; max-width: 440px; }
    .hero-desc strong { color: var(--ink); font-weight: 500; }
    .hero-links { display: flex; gap: 20px; align-items: center; flex-shrink: 0; }
    .hero-links a { font-size: 12px; color: var(--ink3); text-decoration: none; letter-spacing: .3px; transition: color .15s; display: flex; align-items: center; gap: 5px; }
    .hero-links a:hover { color: var(--ink); }
    .hero-links a svg { opacity: .5; }

    /* STATS STRIP */
    .strip { display: grid; grid-template-columns: repeat(4, 1fr); border-top: 1px solid var(--border); border-bottom: 1px solid var(--border); background: var(--paper); }
    .strip-item { padding: clamp(20px, 3vh, 32px) clamp(16px, 2.5vw, 32px); border-right: 1px solid var(--border); }
    .strip-item:last-child { border-right: none; }
    .strip-n { font-family: 'Instrument Serif', serif !important; font-size: clamp(28px, 4vw, 44px); color: var(--ink); line-height: 1; margin-bottom: 4px; }
    .strip-l { font-size: 11px; color: var(--ink3); text-transform: uppercase; letter-spacing: 1.2px; }

    /* SECTIONS */
    .section { max-width: 1100px; margin: 0 auto; padding: clamp(60px, 8vh, 100px) clamp(20px, 5vw, 72px); }
    .sec-header { display: flex; align-items: baseline; gap: 16px; margin-bottom: clamp(32px, 5vh, 56px); padding-bottom: 18px; border-bottom: 1px solid var(--border); }
    .sec-num { font-size: 11px; color: var(--ink4); font-weight: 500; letter-spacing: 1px; }
    .sec-title { font-family: 'Instrument Serif', serif !important; font-size: clamp(26px, 4vw, 40px); font-weight: 400; color: var(--ink); letter-spacing: -.5px; }

    /* EXPERIENCE */
    .exp-item { display: grid; grid-template-columns: 200px 1fr; gap: 0 clamp(24px, 4vw, 60px); padding: clamp(24px, 3.5vh, 40px) 0; border-bottom: 1px solid var(--border); }
    .exp-left { padding-top: 2px; }
    .exp-company { font-size: 13px; font-weight: 600; color: var(--ink); margin-bottom: 3px; }
    .exp-period { font-size: 11px; color: var(--ink4); letter-spacing: .3px; }
    .exp-role { font-family: 'Instrument Serif', serif !important; font-size: clamp(18px, 2.2vw, 24px); color: var(--ink); margin-bottom: 12px; line-height: 1.2; letter-spacing: -.3px; }
    .exp-desc { font-size: 13px; color: var(--ink3); line-height: 1.85; margin-bottom: 16px; }
    .exp-tags { display: flex; flex-wrap: wrap; gap: 6px; }
    .exp-tags span { font-size: 11px; color: var(--ink3); background: var(--paper); border: 1px solid var(--borderD); padding: 3px 10px; border-radius: 2px; letter-spacing: .2px; }

    /* SKILLS */
    .skills-table { display: flex; flex-direction: column; }
    .skill-row { display: grid; grid-template-columns: 200px 1fr; gap: 0 clamp(24px, 4vw, 60px); padding: clamp(18px, 2.5vh, 28px) 0; border-bottom: 1px solid var(--border); align-items: start; }
    .skill-row:last-child { border-bottom: none; }
    .skill-cat { font-size: 12px; font-weight: 600; color: var(--ink); letter-spacing: .2px; padding-top: 2px; }
    .skill-items { display: flex; flex-wrap: wrap; gap: 6px; }
    .skill-items span { font-size: 12px; color: var(--ink2); padding: 5px 14px; border-radius: 2px; background: var(--paper); border: 1px solid var(--borderD); letter-spacing: .1px; }

    /* PROJECTS */
    .proj-list { display: flex; flex-direction: column; }
    .proj-item { display: grid; grid-template-columns: 40px 1fr auto; gap: 0 20px; align-items: start; padding: clamp(20px, 3vh, 32px) 0; border-bottom: 1px solid var(--border); }
    .proj-num { font-size: 11px; color: var(--ink4); font-weight: 500; letter-spacing: .5px; padding-top: 3px; }
    .proj-title { font-family: 'Instrument Serif', serif !important; font-size: clamp(17px, 2vw, 22px); color: var(--ink); margin-bottom: 8px; letter-spacing: -.3px; }
    .proj-desc { font-size: 13px; color: var(--ink3); line-height: 1.8; margin-bottom: 10px; }
    .proj-stack { display: flex; flex-wrap: wrap; gap: 5px; }
    .proj-stack span { font-size: 10px; text-transform: uppercase; letter-spacing: .8px; color: var(--ink4); border: 1px solid var(--borderD); padding: 2px 8px; border-radius: 2px; }

    /* CONTACT */
    .contact-section { background: var(--ink); padding: clamp(60px, 8vh, 100px) clamp(20px, 5vw, 72px); }
    .contact-inner { max-width: 1100px; margin: 0 auto; }
    .contact-sub { font-size: 11px; color: rgba(255,255,255,.35); letter-spacing: 2px; text-transform: uppercase; margin-bottom: 16px; }
    .contact-headline { font-family: 'Instrument Serif', serif !important; font-size: clamp(36px, 7vw, 80px); font-weight: 400; color: #fff; line-height: .95; letter-spacing: -2px; margin-bottom: clamp(32px, 5vh, 56px); }
    .contact-headline em { font-style: italic; opacity: .55; }
    .contact-row { display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 24px; padding-top: 32px; border-top: 1px solid rgba(255,255,255,.1); }
    .contact-links { display: flex; flex-direction: column; gap: 14px; }
    .contact-links a { text-decoration: none; font-size: 15px; color: #fff; display: flex; align-items: center; gap: 10px; letter-spacing: .1px; transition: opacity .15s; }
    .contact-links a:hover { opacity: .65; }
    .contact-links a .cl { width: 32px; height: 32px; border-radius: 50%; border: 1px solid rgba(255,255,255,.15); display: flex; align-items: center; justify-content: center; font-size: 14px; flex-shrink: 0; }
    .contact-note { font-size: 12px; color: rgba(255,255,255,.3); line-height: 1.8; max-width: 260px; text-align: right; }

    /* FOOTER */
    .site-footer { background: var(--ink); border-top: 1px solid rgba(255,255,255,.08); padding: 20px clamp(20px, 5vw, 72px); display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 12px; }
    .site-footer span { font-size: 11px; color: rgba(255,255,255,.25); letter-spacing: .3px; }

    /* BACK TO TOP */
    .up { position: fixed; bottom: 20px; right: 20px; z-index: 50; width: 36px; height: 36px; border-radius: 50%; background: var(--ink); color: #fff; border: none; cursor: pointer; font-size: 14px; opacity: 0; transition: opacity .3s; display: flex; align-items: center; justify-content: center; text-decoration: none; }
    .up.show { opacity: 1; }
    .up:hover { background: var(--accent); }

    /* TABLET BREAKPOINTS */
    @media(max-width:900px){
      .exp-item, .skill-row { grid-template-columns: 1fr; }
      .exp-left { display: flex; gap: 12px; align-items: baseline; margin-bottom: 8px; }
      .proj-item { grid-template-columns: 32px 1fr; }
    }

    /* MOBILE BREAKPOINTS */
    @media(max-width:640px) {
      .nav-links, .nav-contact { display: none; }
      .ham { display: flex; }
      .hero-rule, .hero-rule2 { display: none; }
      .hero h1 { letter-spacing: -1px; }
      .hero-footer { flex-direction: column; gap: 20px; align-items: flex-start; }
      .strip { grid-template-columns: 1fr 1fr; }
      .strip-item:nth-child(2) { border-right: none; }
      .strip-item:nth-child(3), .strip-item:nth-child(4) { border-top: 1px solid var(--border); }
      .proj-item { grid-template-columns: 1fr; }
      .proj-num { display: none; }
      .contact-note { text-align: left; max-width: 100%; }
      .site-footer { justify-content: center; }
    }
</style>
""", unsafe_allow_html=True)

# 3. Main HTML Architecture Structure Block
portfolio_html = """
<nav>
  <div class="logo">Anand<span>.</span></div>
  <div class="nav-links">
    <a href="#experience">Experience</a>
    <a href="#skills">Skills</a>
    <a href="#projects">Projects</a>
  </div>
  <a class="nav-contact" href="mailto:anandsant1212@gmail.com">anandsant1212@gmail.com</a>
  <button class="ham" id="ham" onclick="toggleDrawer()" aria-label="Menu">
    <span></span><span></span><span></span>
  </button>
</nav>

<div class="drawer" id="drawer">
  <a href="#experience" onclick="closeDrawer()">Experience <span>→</span></a>
  <a href="#skills"     onclick="closeDrawer()">Skills <span>→</span></a>
  <a href="#projects"   onclick="closeDrawer()">Projects <span>→</span></a>
  <a href="#contact"    onclick="closeDrawer()">Contact <span>→</span></a>
</div>

<!-- HERO SECTION -->
<section class="hero">
  <div class="hero-bg"></div>
  <div class="hero-rule"></div>
  <div class="hero-rule2"></div>

  <div class="hero-tag">AI Engineer · Mumbai</div>

  <h1>
    Anand
    <em>Sant</em>
  </h1>

  <div class="hero-footer">
    <p class="hero-desc">
      Full-stack <strong>AI Engineer</strong> building production-grade LLM systems,
      RAG pipelines, and intelligent web applications. Currently at Telemerge IT
      Services, previously at LearningMate Solutions.
    </p>
    <div class="hero-links">
      <a href="https://linkedin.com/in/anandsant1212" target="_blank">
        LinkedIn
        <svg width="10" height="10" viewBox="0 0 10 10" fill="none"><path d="M2 8L8 2M8 2H4M8 2V6" stroke="currentColor" stroke-width="1.2"/></svg>
      </a>
      <a href="https://github.com/anandsant12" target="_blank">
        GitHub
        <svg width="10" height="10" viewBox="0 0 10 10" fill="none"><path d="M2 8L8 2M8 2H4M8 2V6" stroke="currentColor" stroke-width="1.2"/></svg>
      </a>
      <a href="mailto:anandsant1212@gmail.com">
        Email
        <svg width="10" height="10" viewBox="0 0 10 10" fill="none"><path d="M2 8L8 2M8 2H4M8 2V6" stroke="currentColor" stroke-width="1.2"/></svg>
      </a>
    </div>
  </div>
</section>

<!-- METRICS STRIP -->
<div class="strip">
  <div class="strip-item">
    <div class="strip-n">2.5+</div>
    <div class="strip-l">Years Experience</div>
  </div>
  <div class="strip-item">
    <div class="strip-n">90%</div>
    <div class="strip-l">Manual Effort Saved</div>
  </div>
  <div class="strip-item">
    <div class="strip-n">75%</div>
    <div class="strip-l">Faster Processing</div>
  </div>
  <div class="strip-item">
    <div class="strip-n">⚡</div>
    <div class="strip-l">SPOT Award Winner</div>
  </div>
</div>

<!-- EXPERIENCE SECTION -->
<div class="section" id="experience">
  <div class="sec-header">
    <span class="sec-num">01</span>
    <h2 class="sec-title">Experience</h2>
  </div>

  <div class="exp-item">
    <div class="exp-left">
      <div class="exp-company">Telemerge IT Services</div>
      <div class="exp-period">Oct 2025 — Present</div>
    </div>
    <div class="exp-right">
      <div class="exp-role">Software Engineer</div>
      <div class="exp-desc">
        Building QA Pariksha — an AI-powered test case generation platform for State Bank of India. Architected dual-database RAG pipelines using LangChain, PostgreSQL (pgvector) and ChromaDB for high-accuracy contextual retrieval from BRD and solution documents. Implemented Role-Based Access Control with JWT authentication and built full-stack document processing in FastAPI and React TypeScript, transforming PDF and DOCX files into selective multimodal inputs for GPT-4.1.
      </div>
      <div class="exp-tags">
        <span>GPT-4.1</span><span>RAG</span><span>LangChain</span><span>FastAPI</span>
        <span>React TS</span><span>pgvector</span><span>ChromaDB</span><span>JWT / RBAC</span>
      </div>
    </div>
  </div>

  <div class="exp-item">
    <div class="exp-left">
      <div class="exp-company">LearningMate Solutions</div>
      <div class="exp-period">Dec 2023 — Sep 2025</div>
    </div>
    <div class="exp-right">
      <div class="exp-role">Associate Software Developer</div>
      <div class="exp-desc">
        Delivered production AI systems for education and accessibility. Automated LCAP document analysis for California CCEE, cutting processing time by 75%. Built an AI-powered alt text generation platform using GPT-4o and Gemini 1.5, reducing manual effort by 90% and fraudulent charges by 50%. Streamlined enterprise data delivery via AWS S3 to Snowflake and architected scalable React microfrontend frameworks. Recognised with a SPOT Award for cross-functional ownership and impactful delivery.
      </div>
      <div class="exp-tags">
        <span>Azure OpenAI</span><span>GPT-4o</span><span>Gemini 1.5</span><span>React MUI</span>
        <span>FastAPI</span><span>AWS S3</span><span>Kubernetes</span><span>MongoDB</span><span>Snowflake</span>
      </div>
    </div>
  </div>

  <div class="exp-item">
    <div class="exp-left">
      <div class="exp-company">CDAC</div>
      <div class="exp-period">Mar 2023 — Nov 2023</div>
    </div>
    <div class="exp-right">
      <div class="exp-role">PG Diploma — Big Data Analytics</div>
      <div class="exp-desc">Rigorous post-graduate programme covering distributed systems, data pipelines, analytics frameworks, and large-scale data engineering fundamentals.</div>
    </div>
  </div>

  <div class="exp-item">
    <div class="exp-left">
      <div class="exp-company">K. K. Wagh Institute</div>
      <div class="exp-period">Jun 2018 — Jun 2022</div>
    </div>
    <div class="exp-right">
      <div class="exp-role">B.E. — Computer Engineering</div>
      <div class="exp-desc">Bachelor's in Computer Engineering covering algorithms, software architecture, operating systems, and computer networks.</div>
    </div>
  </div>
</div>

<!-- SKILLS SECTION -->
<div style="background:var(--paper); border-top:1px solid var(--border); border-bottom:1px solid var(--border);">
  <div class="section" id="skills" style="padding-top:clamp(48px,6vh,80px); padding-bottom:clamp(48px,6vh,80px);">
    <div class="sec-header">
      <span class="sec-num">02</span>
      <h2 class="sec-title">Skills</h2>
    </div>
    <div class="skills-table">
      <div class="skill-row">
        <div class="skill-cat">Generative AI</div>
        <div class="skill-items"><span>LLMs</span><span>RAG</span><span>LangChain</span><span>GPT-4o</span><span>Gemini 1.5</span><span>Azure OpenAI</span><span>Prompt Engineering</span></div>
      </div>
      <div class="skill-row">
        <div class="skill-cat">AI Infrastructure</div>
        <div class="skill-items"><span>ChromaDB</span><span>pgvector</span><span>Embeddings</span><span>Vector Search</span><span>OCR</span><span>Multimodal</span></div>
      </div>
      <div class="skill-row">
        <div class="skill-cat">Backend</div>
        <div class="skill-items"><span>Python</span><span>FastAPI</span><span>REST API</span><span>JWT</span><span>RBAC</span><span>Redis</span><span>System Design</span></div>
      </div>
      <div class="skill-row">
        <div class="skill-cat">Frontend</div>
        <div class="skill-items"><span>React JS</span><span>TypeScript</span><span>React MUI</span><span>Streamlit</span><span>Microfrontend</span></div>
      </div>
      <div class="skill-row">
        <div class="skill-cat">Cloud & DevOps</div>
        <div class="skill-items"><span>AWS S3</span><span>Lambda</span><span>Docker</span><span>Kubernetes</span><span>CI/CD</span><span>GitHub Actions</span></div>
      </div>
      <div class="skill-row">
        <div class="skill-cat">Databases</div>
        <div class="skill-items"><span>PostgreSQL</span><span>MongoDB</span><span>SQLite</span><span>MySQL</span><span>Snowflake</span></div>
      </div>
    </div>
  </div>
</div>

<!-- PROJECTS SECTION -->
<div class="section" id="projects">
  <div class="sec-header">
    <span class="sec-num">03</span>
    <h2 class="sec-title">Projects</h2>
  </div>
  <div class="proj-list">
    <div class="proj-item">
      <div class="proj-num">01</div>
      <div class="proj-body">
        <div class="proj-title">QA Pariksha — SBI Test Case Generator</div>
        <div class="proj-desc">AI-powered SIT/UAT test case generation for State Bank of India. Dual vector DB RAG using pgvector and ChromaDB, environment-specific prompting logic, RBAC with JWT, and multimodal document ingestion via GPT-4.1.</div>
        <div class="proj-stack"><span>GPT-4.1</span><span>RAG</span><span>LangChain</span><span>FastAPI</span><span>React TS</span></div>
      </div>
    </div>

    <div class="proj-item">
      <div class="proj-num">02</div>
      <div class="proj-body">
        <div class="proj-title">LCAP Data Extraction Platform</div>
        <div class="proj-desc">Automated KPI extraction from California CCEE education documents. Full pipeline from ingestion to Snowflake delivery, human-in-the-loop validation, 75% faster processing.</div>
        <div class="proj-stack"><span>Azure OpenAI</span><span>RAG</span><span>MongoDB Atlas</span><span>Kubernetes</span><span>AWS S3</span></div>
      </div>
    </div>

    <div class="proj-item">
      <div class="proj-num">03</div>
      <div class="proj-body">
        <div class="proj-title">AI Alt Text Generation Platform</div>
        <div class="proj-desc">Multimodal accessibility platform with microservice architecture. Supports file uploads, URLs, and S3 inputs. OCR, image classification, keyword extraction — 90% manual effort reduction.</div>
        <div class="proj-stack"><span>GPT-4o</span><span>Gemini 1.5</span><span>Ollama</span><span>FastAPI</span><span>React MUI</span></div>
      </div>
    </div>

    <div class="proj-item">
      <div class="proj-num">04</div>
      <div class="proj-body">
        <div class="proj-title">Real-time Facial Analysis System</div>
        <div class="proj-desc">Computer vision app for real-time emotion recognition, attention monitoring, drowsiness detection via Eye Aspect Ratio, and 3D head pose estimation using solvePnP — visualised on a live analytics dashboard.</div>
        <div class="proj-stack"><span>Python</span><span>OpenCV</span><span>MediaPipe</span><span>Computer Vision</span></div>
      </div>
    </div>

    <div class="proj-item">
      <div class="proj-num">05</div>
      <div class="proj-body">
        <div class="proj-title">AI Innovation POCs</div>
        <div class="proj-desc">Suite of GenAI experiments: multimodal summarisation across text, audio, and video using Gemini 1.5 and GPT-4o, AI evaluation for student responses, image metadata generation, and DALL-E text-to-image.</div>
        <div class="proj-stack"><span>GPT-4o</span><span>Gemini 1.5</span><span>DALL-E</span><span>GPT-3.5</span></div>
      </div>
    </div>
  </div>
</div>

<!-- CONTACT SECTION -->
<div class="contact-section" id="contact">
  <div class="contact-inner">
    <div class="contact-sub">Get in touch</div>
    <h2 class="contact-headline">
      Let's build<br>something
      <em>great.</em>
    </h2>
    <div class="contact-row">
      <div class="contact-links">
        <a href="mailto:anandsant1212@gmail.com">
          <span class="cl">✉</span>
          anandsant1212@gmail.com
        </a>
        <a href="https://linkedin.com/in/anandsant1212" target="_blank">
          <span class="cl">in</span>
          linkedin.com/in/anandsant1212
        </a>
        <a href="https://github.com/anandsant12" target="_blank">
          <span class="cl">gh</span>
          github.com/anandsant12
        </a>
      </div>
      <div class="contact-note">
        Open to AI Engineering roles<br>
        and freelance projects.<br>
        Based in Mumbai, India.
      </div>
    </div>
  </div>
</div>

<footer class="site-footer">
  <span>© 2026 Anand Sant</span>
  <span>Mumbai, India</span>
</footer>

<a class="up" id="upBtn" href="#">↑</a>

<script>
function toggleDrawer(){
  document.getElementById('ham').classList.toggle('open');
  document.getElementById('drawer').classList.toggle('open');
}
function closeDrawer(){
  document.getElementById('ham').classList.remove('open');
  document.getElementById('drawer').classList.remove('open');
}

// Fixed Scroll Listeners targeted at the top window frame
window.parent.addEventListener('scroll', () => {
  const scrollY = window.parent.scrollY;
  document.getElementById('upBtn').classList.toggle('show', scrollY > 500);
  
  const ids = ['experience', 'skills', 'projects', 'contact'];
  const links = document.querySelectorAll('.nav-links a');
  let cur = '';
  
  ids.forEach(id => {
    const el = document.getElementById(id);
    if(el && scrollY >= (el.getBoundingClientRect().top + scrollY - 120)) {
      cur = id;
    }
  });
  links.forEach(a => a.classList.toggle('active', a.getAttribute('href') === '#' + cur));
});

document.addEventListener('click', e => {
  const d = document.getElementById('drawer');
  const h = document.getElementById('ham');
  if(d.classList.contains('open') && !d.contains(e.target) && !h.contains(e.target)) closeDrawer();
});
</script>
"""

# Render application natively
st.markdown(portfolio_html, unsafe_allow_html=True)
