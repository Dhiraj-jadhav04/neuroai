import streamlit as st
import streamlit.components.v1 as components
from PIL import Image
import os

# Page Config
st.set_page_config(
    page_title="Dhiraj Jadhav | AI & Data Science Portfolio",
    page_icon="🚀",
    layout="wide",
)

# Custom CSS for "Blazing" Look
st.markdown("""
<style>
    /* Dark Theme Optimization */
    .stApp {
        background-color: #09090b;
        color: #f8fafc;
    }
    
    /* Hide Streamlit Header/Footer */
    header, footer {visibility: hidden;}
    
    /* Text Gradient & Hero */
    .text-gradient {
        background: linear-gradient(to right, #f8fafc, #94a3b8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 900;
        font-style: italic;
    }
    
    /* Glowing Cards */
    .glow-card {
        background: rgba(15, 23, 42, 0.6);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 1.5rem;
        padding: 2rem;
        transition: all 0.3s ease;
        margin-bottom: 2rem;
    }
    .glow-card:hover {
        border: 1px solid rgba(59, 130, 246, 0.5);
        transform: translateY(-5px);
        box-shadow: 0 10px 30px -10px rgba(0, 0, 0, 0.7);
    }
    
    /* Navigation Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #0f172a;
        border-right: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    /* Circular Image */
    .circular-img {
        border-radius: 50%;
        border: 4px solid rgba(255, 255, 255, 0.1);
        width: 100%;
        max-width: 300px;
        box-shadow: 0 0 30px rgba(59, 130, 246, 0.2);
    }
    
</style>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.title("🚀 Navigation")
page = st.sidebar.radio("Go to", ["Home", "Skills & Arsenal", "Portfolio Projects", "Experience"])

# Helper: Load Skill Category
def skill_card(title, skills):
    with st.container():
        st.markdown(f"### {title}")
        cols = st.columns(len(skills))
        for i, skill in enumerate(skills):
            with cols[i]:
                if "logo" in skill:
                    st.image(skill["logo"], width=40)
                st.caption(skill["name"])

# --- PAGE: HOME ---
if page == "Home":
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2 = st.columns([2, 1], gap="large")
    
    with col1:
        st.markdown("<h1 class='text-gradient' style='font-size: 5rem; line-height: 1;'>DHIRAJ JADHAV</h1>", unsafe_allow_html=True)
        st.markdown("### ✨ AI & Data Science Engineer")
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Social Icons
        social_cols = st.columns(3)
        with social_cols[0]:
            st.link_button("LinkedIn", "https://www.linkedin.com/in/dhiraj-jadhav-920b04215", use_container_width=True)
        with social_cols[1]:
            st.link_button("GitHub", "https://github.com/Dhiraj-jadhav04", use_container_width=True)
        with social_cols[2]:
            st.link_button("Email", "mailto:dhirajjadhav873@gmail.com", use_container_width=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.info("💡 Aspiring AI and Data enthusiast with fundamental knowledge of machine learning models, data visualization, and programming languages such as SQL and Python. Experienced in building end-to-end ML pipelines and automated EDA tools.")

    with col2:
        if os.path.exists("public/profile.jpg"):
            st.markdown('<div class="profile-container">', unsafe_allow_html=True)
            st.image("public/profile.jpg", use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)
        else:
            st.warning("Profile photo not found.")
            
    st.divider()
    
    # Education
    st.subheader("🎓 Academic Foundation")
    with st.container():
        st.markdown("""
        <div class='glow-card'>
            <h4 style="color: #3b82f6;">Bachelor of Engineering (AI & Data Science)</h4>
            <p><b>Datta Meghe College of Engineering</b></p>
            <h3 style="margin-top: 1rem;">CGPA: 7.0</h3>
        </div>
        """, unsafe_allow_html=True)

# --- PAGE: SKILLS ---
elif page == "Skills & Arsenal":
    st.markdown("<h1 class='text-gradient' style='font-size: 4rem;'>Technical Arsenal</h1>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("#### 🐍 Programming & Data")
        st.code("Python, SQL, DSA", language="text")
        
        st.write("#### 📊 Frameworks & Libraries")
        st.markdown("""
        - NumPy & Pandas
        - Matplotlib & Seaborn
        - Scikit-Learn
        - Streamlit
        """)
        
    with col2:
        st.write("#### 🤖 ML/DL Specialization")
        st.markdown("""
        - Regression (Linear, Logistic)
        - KNN, Naive Bayes, Decision Trees
        - SVM & Clustering
        - ANN & CNN
        - TensorFlow & Keras
        """)

    st.divider()
    st.subheader("🏆 Achievements")
    st.success("**NEC IIT Bombay Finalist** - Secured Top 50 Rank in National Entrepreneurship Cell.")
    st.link_button("View Certificate", "https://drive.google.com/file/d/12YyTT4eH94hAbVMPo_JGwGZ6JEQWudrX/view?usp=sharing")

# --- PAGE: PROJECTS ---
elif page == "Portfolio Projects":
    st.markdown("<h1 class='text-gradient' style='font-size: 4rem;'>Innovative Works</h1>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class='glow-card'>
            <h3>CreditWise</h3>
            <p>Loan Approval Prediction System leveraging EDA and ML evaluation.</p>
        </div>
        """, unsafe_allow_html=True)
        st.link_button("Launch App", "https://credit-wise---loan-approval-system-cbknewr7sgnz9qohbp7jsk.streamlit.app/")

    with col2:
        st.markdown("""
        <div class='glow-card'>
            <h3>InsightFlow</h3>
            <p>Automated EDA tool to streamline data preparation pipelines.</p>
        </div>
        """, unsafe_allow_html=True)
        st.link_button("Launch App", "https://datascrubpro.streamlit.app/")

    st.markdown("""
    <div class='glow-card' style='width: 100%'>
        <h3>CineMatch</h3>
        <p>AI Movie Advisor using NLP, Cosine Similarity, and TMDB API integration.</p>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("GitHub Source", "https://github.com/Dhiraj-jadhav04/CineMatch-AI-Movie-Advisor")

# --- PAGE: EXPERIENCE ---
elif page == "Experience":
    st.markdown("<h1 class='text-gradient' style='font-size: 4rem;'>Professional Journey</h1>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='glow-card' style='width: 100%'>
        <h2 style='color: #3b82f6;'>Deloitte</h2>
        <p><b>Virtual Data Analysis Intern</b></p>
        <p>Strategic data visualization and insight curation for business workflows.</p>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("View Deloitte Certificate", "https://drive.google.com/file/d/1krr6ktpJYfWeIIDQc6czNQhV3MKbkR5I/view?usp=sharing")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='glow-card' style='width: 100%'>
        <h2 style='color: #3b82f6;'>Prodigy InfoTech</h2>
        <p><b>Machine Learning Intern</b></p>
        <p>Architecture and evaluation of predictive models for real-world datasets.</p>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("View Prodigy Certificate", "https://drive.google.com/file/d/1xldIhMniPBwdYkMOpdUI9mF-vvupNhEo/view?usp=sharing")

# Footer
st.sidebar.divider()
st.sidebar.caption("Portfolio built with ❤️ by Dhiraj Jadhav")
st.sidebar.link_button("View Resume", "https://drive.google.com/file/d/12ZIykNMKUoB9Dh0yEm1A_IabggCxeBbb/view?usp=sharing", use_container_width=True)
