# AI Company Assist – Streamlit Prototype
# Run with: streamlit run ai_company_assist_streamlit_app.py

import streamlit as st
import pandas as pd
import re
from datetime import datetime

# ---------- Page Config ----------
st.set_page_config(
    page_title="AI Company Assist – Prototype",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------- Minimalist Styling (White base, Bold Black text) ----------
CUSTOM_CSS = """
<style>
    html, body, [class^="css"]  {
        background-color: #FFFFFF !important;
        color: #000000 !important;
    }
    /* Make headings and labels bold + black */
    h1, h2, h3, h4, h5, h6, .stMarkdown p strong, .st-emotion-cache-16idsys p, label, .stTextInput label, .stSelectbox label, .stTextArea label {
        color: #000000 !important;
        font-weight: 700 !important;
    }
    /* Cards / containers */
    .card {
        border: 1px solid #EAEAEA;
        border-radius: 16px;
        padding: 20px;
        background: #FFFFFF;
        box-shadow: 0 2px 10px rgba(0,0,0,0.04);
    }
    /* Buttons */
    .stButton>button {
        background: #000000 !important;
        color: #FFFFFF !important;
        border-radius: 10px !important;
        padding: 10px 18px !important;
        border: 1px solid #000000 !important;
        font-weight: 700 !important;
    }
    .stDownloadButton>button {
        background: #000000 !important;
        color: #FFFFFF !important;
        border-radius: 10px !important;
        padding: 10px 18px !important;
        border: 1px solid #000000 !important;
        font-weight: 700 !important;
    }
    /* Inputs */
    .stTextInput input, .stTextArea textarea, .stSelectbox div[data-baseweb="select"] > div {
        border: 1px solid #00000022 !important;
        border-radius: 10px !important;
    }
    .small-muted {
        color: #333 !important;
        font-weight: 600;
        opacity: 0.8;
        font-size: 0.9rem;
    }
    .divider {
        height: 1px;
        background: #EEE;
        margin: 8px 0 16px 0;
    }
</style>
"""
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# ---------- Header ----------
col_logo, col_title, col_cta = st.columns([0.6, 3, 1.4])
with col_logo:
    st.write("")
    st.markdown("### 🤖")
with col_title:
    st.markdown("# *AI Company Assist*")
    st.markdown("*Accelerating Workplace Efficiency with Intelligent Automation*")
with col_cta:
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("*Prototype Build*")
        st.markdown(f'<p class="small-muted">Updated: {datetime.now().strftime("%Y-%m-%d %H:%M")}</p>', unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ---------- Sidebar ----------
with st.sidebar:
    st.markdown("## *Navigation*")
    st.write("Choose a module to explore:")
    st.write("• *Internal Assistant* – Company Q&A, templates, reminders")
    st.write("• *Solution Recommendations* – Proposal generator")
    st.write("• *Contract Risk Detector* – Clause risk analysis")
    st.markdown("---")
    st.markdown("*Settings*")
    light = st.toggle("Light Mode (White Base)", value=True, help="Prototype uses a white base by default.")
    st.markdown("---")
    st.caption("This is a static prototype for demo purposes.\nIntegrate with your data sources (SOPs, projects, product catalog, contracts) for live results.")

# ---------- Tabs ----------
tab1, tab2, tab3 = st.tabs(["🧭 Internal Assistant", "🧩 Solution Recommendations", "⚖ Contract Risk Detector"])

# ---------- Tab 1: Internal Assistant ----------
with tab1:
    st.markdown("## *Internal Assistant*")
    st.markdown("*Ask about SOPs, policies, project status, or fetch templates.*")

    col_a, col_b = st.columns([2, 1])
    with col_a:
        question = st.text_input("*Your Question*", placeholder="Example: What is the reimbursement policy timeline?")
        fetch_template = st.selectbox("*Fetch Template (optional)*", ["None", "SOP Template", "Leave Request Form", "Expense Claim Sheet", "Onboarding Checklist"])
        remind_toggle = st.toggle("*Set Reminder*")
        reminder = None
        if remind_toggle:
            reminder = st.text_input("*Reminder Note*", placeholder="e.g., Follow up with Finance about reimbursement policy")
    with col_b:
        st.markdown("*Quick Filters*")
        dept = st.multiselect("*Department*", ["HR", "Finance", "Operations", "Sales", "Legal", "IT"])
        project = st.text_input("*Project/Team (optional)*", placeholder="e.g., Project A / Client X")

    if st.button("Ask / Fetch"):
        with st.container():
            st.markdown('<div class="card">', unsafe_allow_html=True)
            if question:
                # Mocked result (RAG placeholder)
                mock_answer = (
                    "According to the *Reimbursement Policy v2.1 (HR/SOP/FIN-08)*, claims must be submitted "
                    "within *7 calendar days* after the expense date. Approval flow: *Employee → Manager → Finance*. "
                    "Processing time target is *3–5 business days* upon approval."
                )
                st.markdown("*Answer*")
                st.write(mock_answer)
                with st.expander("Show Sources (mock)"):
                    st.write("- HR Handbook › Reimbursement Policy v2.1")
                    st.write("- Finance SOP › Expense Processing SLAs")

            if fetch_template and fetch_template != "None":
                st.markdown("*Template*")
                st.write(f"Prepared *{fetch_template}* for download.")
                # Provide a minimal CSV/Doc example based on template choice
                if fetch_template == "Expense Claim Sheet":
                    df = pd.DataFrame({
                        "Date": [], "Category": [], "Amount": [], "Currency": [], "Description": []
                    })
                    csv = df.to_csv(index=False).encode("utf-8")
                    st.download_button("Download Expense Claim CSV", csv, file_name="expense_claim_template.csv")
                else:
                    content = f"{fetch_template}\n\n[Insert your standardized content here]"
                    st.download_button("Download Template (.txt)", content, file_name=f"{fetch_template.lower().replace(' ','_')}.txt")

            if reminder:
                st.markdown("*Reminder*")
                st.write(f"Saved reminder (demo): {reminder}")
            st.markdown("</div>", unsafe_allow_html=True)

# ---------- Tab 2: Solution Recommendations ----------
with tab2:
    st.markdown("## *Solution / Product Recommendations*")
    st.markdown("*Generate a tailored proposal based on client requirements.*")

    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        col1, col2, col3 = st.columns(3)
        with col1:
            industry = st.selectbox("*Client Industry*", ["Technology", "Retail", "Finance", "Healthcare", "Manufacturing", "Public Sector"])
            budget = st.selectbox("*Budget Range*", ["<$10K", "$10K–$50K", "$50K–$200K", ">$200K"])
        with col2:
            timeline = st.selectbox("*Desired Timeline*", ["2–4 weeks", "1–2 months", "3–4 months"])
            priority = st.selectbox("*Priority*", ["Speed", "Cost", "Scalability", "Security"])
        with col3:
            needs = st.multiselect("*Key Requirements*", ["RAG Knowledge Base", "OCR Intake", "CRM Integration", "Contract Review", "Analytics Dashboard", "Mobile Access"])
            refs = st.toggle("*Show similar past projects (demo)*", value=True)

        brief = st.text_area("*Client Brief / Prompt*", placeholder="Describe the client’s problem, environment, and constraints…", height=150)

        if st.button("Generate Recommendation"):
            st.markdown("*Proposed Architecture (Demo)*")
            bullets = [
                "RAG-based knowledge retrieval for internal docs (FAISS/Qdrant + LangChain).",
                "LLM-driven recommendation engine with rule-based constraints for product fit.",
                "OCR pipeline for PDF/Word brief ingestion (Textract/Form Recognizer).",
                "Optional Contract Risk Detector for legal pre-checks."
            ]
            if "CRM Integration" in needs:
                bullets.append("Bi-directional CRM sync for opportunities, contacts, and notes.")
            if "Analytics Dashboard" in needs:
                bullets.append("Lightweight metrics dashboard for usage, response time, and satisfaction.")

            for b in bullets:
                st.write(f"• *{b}*")

            data = [
                {"Component": "Knowledge Base", "Option": "FAISS + SentenceTransformer", "Notes": "Fast retrieval; exportable index"},
                {"Component": "Orchestration", "Option": "LangChain / LlamaIndex", "Notes": "Composable tools; mature ecosystem"},
                {"Component": "LLM Layer", "Option": "Open-source or API (GPT-4 class)", "Notes": "Switchable by environment"},
                {"Component": "OCR Intake", "Option": "Textract / Form Recognizer", "Notes": "Structured field extraction"},
                {"Component": "Hosting", "Option": "Container / Serverless", "Notes": "Scalable by workload"}
            ]
            st.markdown("*Bill of Materials (Demo)*")
            st.dataframe(pd.DataFrame(data))

            if refs:
                with st.expander("Similar Past Projects (Demo)"):
                    st.write("- Knowledge portal for Retail – reduced search time by 70%")
                    st.write("- Proposal engine for B2B Tech – response time cut from 3 days to 6 hours")

        st.markdown("</div>", unsafe_allow_html=True)

# ---------- Tab 3: Contract Risk Detector ----------
with tab3:
    st.markdown("## *Contract Risk Detector*")
    st.markdown("*Upload a contract and detect potential risk clauses (demo).*")

    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        uploaded = st.file_uploader("*Upload Contract (TXT/MD preferred for demo)*", type=["txt", "md"])
        risk_keywords = {
            "SLA": r"\bSLA\b|\bservice level\b",
            "Penalty": r"\bpenalt(y|ies)\b|\bliquidated damages\b|\bfine(s)?\b",
            "Liability": r"\bliabilit(y|ies)\b|\bindemnif(y|ication)\b",
            "Termination": r"\btermination\b|\bterminate\b|\bfor cause\b",
            "Payment": r"\bpayment terms\b|\bnet\s+\d+\b|\binvoice\b",
            "Confidentiality": r"\bconfidential(it|y)\b|\bNDA\b",
            "Jurisdiction": r"\bgovern(ing)? law\b|\bjurisdiction\b"
        }

        if uploaded is not None:
            text = uploaded.read().decode("utf-8", errors="ignore")
            findings = []
            for label, pattern in risk_keywords.items():
                for m in re.finditer(pattern, text, flags=re.IGNORECASE):
                    start = max(m.start() - 60, 0)
                    end = min(m.end() + 60, len(text))
                    snippet = text[start:end].replace("\n", " ")
                    findings.append({"Category": label, "Excerpt": f"...{snippet}..."})
            if findings:
                st.markdown("*Detected Risk Highlights (Demo)*")
                st.dataframe(pd.DataFrame(findings))
            else:
                st.success("No predefined risk keywords detected in this demo scan.")

        st.markdown("</div>", unsafe_allow_html=True)

# ---------- Footer ----------
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
st.markdown("*Roadmap (Demo):* MVP (Internal Assistant) → Recommendations → Contract Risk Detector → Integrations")
st.caption("Prototype build. Replace demo logic with your RAG indices, product catalog, and legal NLP models.")