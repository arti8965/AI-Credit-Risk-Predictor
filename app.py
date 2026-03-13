import streamlit as st
import plotly.express as px
from model_logic import calculate_risk, get_metrics

# Page Setup
st.set_page_config(page_title="AI Credit Guard", layout="wide", page_icon="🛡️")

# Custom CSS for a professional Banking UI
st.markdown("""
    <style>
    .stApp { background-color: #fcfcfc; }
    .main-header { color: #1e3a8a; font-size: 40px; font-weight: bold; text-align: center; margin-bottom: 20px; }
    .stButton>button { width: 100%; background-color: #1e3a8a; color: white; border-radius: 8px; height: 50px; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<div class="main-header">🛡️ AI-Powered Credit Risk Guard</div>', unsafe_allow_html=True)
st.write("### Enterprise-grade Risk Assessment Dashboard")
st.markdown("---")

# Layout: Sidebar for Inputs
st.sidebar.header("👤 Applicant Profile")
age = st.sidebar.number_input("Applicant's Age", 18, 90, 28)
income = st.sidebar.number_input("Annual Income ($)", 10000, 1000000, 45000, step=1000)
loan = st.sidebar.number_input("Loan Amount Requested ($)", 1000, 500000, 12000, step=500)
score = st.sidebar.slider("Credit Score (CIBIL/FICO)", 300, 850, 680)
exp = st.sidebar.number_input("Employment Years", 0, 50, 4)

# Main Section
col1, col2 = st.columns([1, 1])

with col1:
    st.info("💡 **Instructions:** Adjust the parameters on the left and click the button to run the AI engine.")
    predict_btn = st.button("RUN RISK ASSESSMENT")

with col2:
    if predict_btn:
        status, conf = calculate_risk(age, income, loan, score, exp)
        
        # Display Result Card
        if status == "Low Risk":
            st.balloons()
            st.success(f"## ✅ ASSESSMENT: {status}")
        elif status == "Medium Risk":
            st.warning(f"## ⚠️ ASSESSMENT: {status}")
        else:
            st.error(f"## ❌ ASSESSMENT: {status}")
            
        # Analytics
        st.write(f"**AI Model Confidence:** {conf}%")
        
        # Risk Visualization
        fig = px.pie(values=[conf, 100-conf], names=['Certainty', 'Uncertainty'], 
                     hole=0.6, title="Prediction Reliability")
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.image("https://img.freepik.com/free-vector/digital-data-security-technology-background_1017-25114.jpg", use_column_width=True)

# Footer for Interviewers
st.markdown("---")
st.subheader("📊 System Architecture & ML Metrics")
metrics = get_metrics()
c1, c2, c3, c4 = st.columns(4)
c1.metric("Selected Model", metrics["Model Type"])
c2.metric("Test Accuracy", metrics["Accuracy"])
c3.metric("Precision", metrics["Precision"])
c4.metric("Input Features", metrics["Features"])