import streamlit as st
from streamlit_gsheets import GSheetsConnection
import streamlit.components.v1 as components
import pandas as pd
import time
from datetime import datetime

# 1. SETUP & BRANDING
st.set_page_config(page_title="The Myospot | Practice Performance Analysis", page_icon="🦷", layout="centered")

# Establish Google Sheets Connection
conn = st.connection("gsheets", type=GSheetsConnection)

# Custom Theming (Deep Slate Blue & Teal/Orange Accents)
st.markdown("""
    <style>
    .stApp { background-color: #0b1a29; color: #ffffff; }
    .stNumberInput label, .stTextInput label { color: #ffffff !important; font-weight: 600; }
    
    div.stButton > button:first-child {
        background: linear-gradient(90deg, #00b4db 0%, #0083b0 100%);
        color: white; border: none; padding: 18px 30px; border-radius: 8px;
        font-weight: 800; width: 100%; transition: 0.3s;
        text-transform: uppercase; letter-spacing: 1px;
    }
    div.stButton > button:first-child:hover {
        background: linear-gradient(90deg, #ff8c00 0%, #ff4500 100%);
    }
    
    .report-card { background: rgba(255, 255, 255, 0.04); padding: 35px; border-radius: 15px; border: 2px solid #00b4db; text-align: center; margin-bottom: 30px; }
    .status-container { display: grid; grid-template-columns: repeat(2, 1fr); gap: 10px; margin-bottom: 20px; }
    .status-box { padding: 15px; border-radius: 8px; font-weight: bold; text-align: center; font-size: 0.8rem; border: 2px solid transparent; text-transform: uppercase; }
    .status-green { border-color: #28a745; background: rgba(40, 167, 69, 0.1); color: #28a745; }
    .status-red { border-color: #dc3545; background: rgba(220, 53, 69, 0.1); color: #dc3545; }
    .disclaimer-box { background: rgba(255, 255, 255, 0.05); padding: 20px; border-radius: 8px; border-left: 4px solid #00b4db; margin-top: 20px; font-style: italic; font-size: 0.9rem; }
    
    .custom-warning-box {
        background-color: rgba(255, 140, 0, 0.1) !important;
        border: 1px solid rgba(255, 140, 0, 0.4) !important;
        border-left: 5px solid #ff8c00 !important;
        padding: 15px 20px !important;
        border-radius: 6px !important;
        margin-bottom: 25px !important;
    }
    .custom-warning-box p {
        color: #ffffff !important;
        margin: 0 !important;
        font-size: 0.95rem !important;
        line-height: 1.5 !important;
    }
    
    #MainMenu, footer, header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# App Title & Branding Header
st.image("https://assets.cdn.filesafe.space/MCcnQ0ytnakrb0FwnYIM/media/69ea1f539fe87a999456bbe3.png", width=220)
st.title("The Myospot Analysis Engine™")
st.subheader("Identify Clinical Gaps & Operational Revenue Leaks")

# 2. INPUT SECTION
with st.container():
    practice_name = st.text_input("Practice / Entity Name", placeholder="Enter your name or business name...")
    
    col1, col2 = st.columns(2)
    inputs = {}
    with col1:
        inputs['compliance'] = st.number_input("Patient Compliance Rate %", min_value=0, max_value=100, value=None, step=1, help="Percentage of patients fully adhering to recommended clinical protocols.")
        inputs['screening'] = st.number_input("Screening Rate %", min_value=0, max_value=100, value=None, step=1, help="Percentage of patients screened for systemic health markers.")
        inputs['recall'] = st.number_input("Patient Recall Interval (Months)", min_value=0, value=None, step=1)
    with col2:
        inputs['conversion'] = st.number_input("Case Acceptance / Conversion %", min_value=0, max_value=100, value=None, step=1)
        inputs['product_adoption'] = st.number_input("Home-Care Product Adoption %", min_value=0, max_value=100, value=None, step=1, help="Percentage of base buying premium home-care health assets.")
        inputs['revenue_base'] = st.number_input("Annual Gross Production ($)", min_value=0, value=1200000, step=50000)

    if st.button("Generate Performance Analysis"):
        
        with st.status("Calculating Myospot Benchmarks...", expanded=True) as status:
            time.sleep(1.5)
            st.write("Analyzing protocol alignment...")
            time.sleep(1.5)
            st.write("Isolating compliance and retail product leaks...")
            time.sleep(1)
            status.update(label="Analysis Complete!", state="complete", expanded=False)

        # Warning container if variables are skipped
        if any(v is None for v in [inputs['compliance'], inputs['screening'], inputs['recall'], inputs['conversion'], inputs['product_adoption']]):
            st.markdown("""
                <div class="custom-warning-box">
                    <p>⚠️ Missing values detected. Skipping key indicators can obscure clinical and operational blind spots. The Myospot optimization program relies on comprehensive data points to build full automation ecosystems.</p>
                </div>
            """, unsafe_allow_html=True)

        # 3. THE CALCULATOR ENGINE (THE SILO ENGINE)
        # Change these benchmark metrics below to reflect your specific mathematical sheets.
        FINAL_RESULTS = {}
        REV_BASE = inputs['revenue_base']

        # Benchmark 1: Compliance (e.g., target 85%)
        if inputs['compliance'] is not None:
            target_compliance = 85
            loss = ((target_compliance - inputs['compliance']) / 100 * REV_BASE) if inputs['compliance'] < target_compliance else 0
            FINAL_RESULTS['Patient Compliance'] = {'loss': max(0.0, loss), 'status': "red" if inputs['compliance'] < target_compliance else "green"}

        # Benchmark 2: Screening Rate (e.g., target 70%)
        if inputs['screening'] is not None:
            target_screening = 70
            loss = ((target_screening - inputs['screening']) / 100 * (REV_BASE * 0.25)) if inputs['screening'] < target_screening else 0
            FINAL_RESULTS['Systemic Screening'] = {'loss': max(0.0, loss), 'status': "red" if inputs['screening'] < target_screening else "green"}

        # Benchmark 3: Recall Intervals (e.g., target <= 4 months)
        if inputs['recall'] is not None:
            target_recall = 4
            loss = ((inputs['recall'] - target_recall) * 15000) if inputs['recall'] > target_recall else 0
            FINAL_RESULTS['Recall Optimization'] = {'loss': max(0.0, loss), 'status': "red" if inputs['recall'] > target_recall else "green"}

        # Benchmark 4: Case Conversion (e.g., target 80%)
        if inputs['conversion'] is not None:
            target_conv = 80
            loss = ((target_conv - inputs['conversion']) / 100 * (REV_BASE * 0.40)) if inputs['conversion'] < target_conv else 0
            FINAL_RESULTS['Case Conversion'] = {'loss': max(0.0, loss), 'status': "red" if inputs['conversion'] < target_conv else "green"}

        # Benchmark 5: Home-care Product & Asset Retail Adoption (e.g., target 45%)
        if inputs['product_adoption'] is not None:
            target_adopt = 45
            loss = ((target_adopt - inputs['product_adoption']) / 100 * 50000) if inputs['product_adoption'] < target_adopt else 0
            FINAL_RESULTS['Product Adoption'] = {'loss': max(0.0, loss), 'status': "red" if inputs['product_adoption'] < target_adopt else "green"}

        # Calculate highest priority leak
        if FINAL_RESULTS:
            failing = {k: v for k, v in FINAL_RESULTS.items() if v['status'] == "red"}
            if failing:
                winner_key = max(failing, key=lambda k: failing[k]['loss'])
                winner_loss = failing[winner_key]['loss']
            else:
                winner_key = "System Integration"
                winner_loss = 0

            # --- 4. GOOGLE SHEETS DATA LOGGING ---
            new_data = pd.DataFrame([{
                "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "Entity Name": practice_name if practice_name else "N/A",
                "Primary Gap Category": winner_key,
                "Estimated Loss Impact": winner_loss,
                "Compliance": inputs['compliance'],
                "Screening": inputs['screening'],
                "Recall Interval": inputs['recall'],
                "Conversion Rate": inputs['conversion'],
                "Product Adoption": inputs['product_adoption'],
                "Revenue Base": REV_BASE
            }])

            try:
                existing_df = conn.read(ttl=0)
                existing_df = existing_df.dropna(how='all')
                updated_df = pd.concat([existing_df, new_data], ignore_index=True)
                conn.update(data=updated_df)
            except Exception as e:
                st.error(f"Google Sheets update failed: {e}")

            # --- 5. THE VERDICT UI ---
            st.markdown(f"""
            <div class="report-card">
                <h1 style="color: #ffffff; margin-top:0; font-size: 2.2rem;">The Verdict</h1>
                <p style="font-size: 1.3rem; margin-bottom: 20px;">The Myospot Engine determined that <b>{practice_name if practice_name else 'your organization'}'s</b> primary point of leverage is in <b>"{winner_key}"</b></p>
                <p style="font-size: 1.2rem; color: #00b4db; font-weight: bold; margin-bottom: 25px;">
                    Based on your production scaling parameters, you are leaving an estimated <span style="color: #ff4500;">${winner_loss:,.0f}</span> on the table annually.
                </p>
                <p style="font-size: 1rem; line-height: 1.6; color: #cccccc;">
                    To unlock a comprehensive breakdown of your programmatic health targets and custom clinical architecture, submit the implementation form below. We will break down your exact performance parameters.
                </p>
            </div>
            """, unsafe_allow_html=True)

            # Display Status Matrix Block
            st.markdown('<div class="status-container">', unsafe_allow_html=True)
            for label, data in FINAL_RESULTS.items():
                st.markdown(f'<div class="status-box status-{data["status"]}">{label}</div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

            st.markdown(f"""
            <div style="text-align: center; margin-top: 40px; margin-bottom: 20px;">
                <h2 style="color: #00b4db;">This is just a glimpse of the model.</h2>
                <p style="font-size: 1.2rem; font-weight: bold;">Let’s optimize the entire system pipeline.</p>
                <p style="font-size: 1.1rem; line-height: 1.5;">
                    Fill out your engineering information below to request a fully synchronized audit—isolating systemic bottlenecks across your operations ecosystem.<br><br>
                    <b>If this much visibility opens up from minor inputs…</b><br>
                    imagine the data accuracy when tracking automated pipeline workflows in real time.
                </p>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("""
            <div class="disclaimer-box">
                <b>Systems Disclaimer:</b> These predictive evaluations utilize standard comparative baseline metrics to clarify underlying structural parameters. For exact multi-channel operational insights, continuous structural API tracking and direct data integrations are required.
            </div>
            """, unsafe_allow_html=True)

            # 6. CRM LEAD CAPTURE FORM (GHL EMBED)
            # Replace the link below with your specific Myospot LeadConnector/GHL form ID
            components.html("""
                <iframe src="https://api.leadconnectorhq.com/widget/form/iVFg0wteKeXMSEXviPvh" style="width:100%;height:600px;border:none;border-radius:8px"></iframe>
                <script src="https://link.msgsndr.com/js/form_embed.js"></script>
            """, height=650)
