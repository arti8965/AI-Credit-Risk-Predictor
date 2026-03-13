import streamlit as st
import plotly.express as px
from model_logic import calculate_risk, get_metrics

# Page Configuration
st.set_page_config(page_title="AI Credit Risk Guard", layout="wide", page_icon="🛡️")

# Professional UI Styling
st.markdown("""
    <style>
    .stApp { background-color: #f8faff; }
    .main-header { color: #1e3a8a; font-size: 36px; font-weight: bold; text-align: center; margin-bottom: 30px; }
    .stButton>button { width: 100%; background-color: #1e3a8a; color: white; border-radius: 8px; height: 45px; }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<div class="main-header">🛡️ AI-Powered Credit Risk Guard</div>', unsafe_allow_html=True)
st.write("### Advanced Financial Risk Assessment Dashboard")
st.markdown("---")

# Sidebar for Applicant Input
st.sidebar.header("👤 Applicant Profile")
age = st.sidebar.number_input("Applicant Age", 18, 90, 28)
income = st.sidebar.number_input("Annual Income ($)", 10000, 1000000, 50000, step=1000)
loan = st.sidebar.number_input("Loan Amount Requested ($)", 1000, 500000, 15000, step=500)
score = st.sidebar.slider("Credit Score (CIBIL/FICO)", 300, 850, 700)
exp = st.sidebar.number_input("Years of Employment", 0, 50, 5)

# Main Application Layout
col1, col2 = st.columns([1, 1])

with col1:
    st.info("💡 **Instructions:** Provide applicant details in the sidebar and trigger the AI model for risk analysis.")
    predict_btn = st.button("EXECUTE RISK ASSESSMENT")

with col2:
    if predict_btn:
        status, conf = calculate_risk(age, income, loan, score, exp)
        
        # Result Notification
        if status == "Low Risk":
            st.success(f"## ASSESSMENT: {status}")
        elif status == "Medium Risk":
            st.warning(f"## ASSESSMENT: {status}")
        else:
            st.error(f"## ASSESSMENT: {status}")
            
        st.write(f"**Model Confidence Level:** {conf}%")
        
        # Risk Visualization Chart
        fig = px.pie(values=[conf, 100-conf], names=['Confidence', 'Margin of Error'], 
                     hole=0.6, title="Prediction Reliability Index")
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.image("https://img.freepik.com/free-vector/data-analysis-concept-illustration_114360-1594.jpg", width=400)

# Technical Metadata Section
st.markdown("---")
st.subheader("📊 System Architecture & Model Metrics")
metrics = get_metrics()
c1, c2, c3, c4 = st.columns(4)
c1.metric("Engine", metrics["Model"])
c2.metric("Accuracy", metrics["Accuracy"])
c3.metric("Precision", metrics["Precision"])
c4.metric("Feature Set", metrics["Features"])
