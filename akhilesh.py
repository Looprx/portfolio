import streamlit as st
from PIL import Image

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Akhilesh K S | AI Engineer Portfolio",
    page_icon="🤖",
    layout="wide",
)

# --- CSS STYLING ---
st.markdown("""
<style>
    .main-header {font-size: 3.5rem; font-weight: 700; color: #4F8BF9; margin-bottom: 0;}
    .sub-header {font-size: 1.5rem; color: #808495; margin-top: -15px;}
    .card {background-color: #f9f9f9; padding: 20px; border-radius: 10px; margin-bottom: 20px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);}
    .project-title {font-size: 1.2rem; font-weight: bold; color: #333;}
    .tech-tag {background-color: #e0f7fa; color: #006064; padding: 5px 10px; border-radius: 15px; font-size: 0.8rem; margin-right: 5px;}
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR INFO ---
with st.sidebar:
    # Placeholder for your photo
    # image = Image.open("your-photo.jpg") 
    # st.image(image, width=150)
    
    st.title("Akhilesh K S")
    st.write("📍 Thrissur, Kerala, India")
    st.write("📧 eshakhil6@gmail.com")
    st.write("📱 +91 9995483807")
    
    st.markdown("---")
    st.header("🔗 Socials")
    st.link_button("GitHub Profile", "https://github.com/Looprx")
    st.link_button("LinkedIn", "#") # Update with your link

    st.markdown("---")
    #with open("C:\Users\eshak\Documents\akhilesh.py"", "rb") as file: # Replace 'app.py' with your actual PDF filename if hosting
     #   btn = st.download_button(
      #      label="📄 Download Resume",
       #     data=file,
        #    file_name="Akhilesh_KS_Resume.pdf",
         #   mime="application/pdf"
        #)

# --- HERO SECTION ---
st.markdown('<p class="main-header">Hi, I\'m Akhilesh K S 👋</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Artificial Intelligence Engineer | Full Stack Developer</p>', unsafe_allow_html=True)
st.write("""
🚀 I am a **Computer Science & AI student** at SNMIMT (KTU) passionate about building intelligent systems using Deep Learning and Computer Vision. 
I bridge the gap between complex AI models and user-friendly web applications.
""")

st.markdown("---")

# --- SKILLS SECTION ---
st.header("🛠 Technical Skills")
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Languages")
    st.code("Python, C++, Java, JavaScript, TypeScript")

with col2:
    st.subheader("AI & ML")
    st.code("TensorFlow, PyTorch, OpenCV, Scikit-learn, Pandas")

with col3:
    st.subheader("Web Stack")
    st.code("React.js, Node.js, Streamlit, Tailwind CSS")

st.markdown("---")

# --- PROJECTS SECTION ---
st.header("💻 Featured Projects")

col1, col2 = st.columns(2)

with col1:
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<p class="project-title">💊 MedSafe Pro</p>', unsafe_allow_html=True)
        st.write("An AI-powered drug safety system that detects toxic interactions and predicts patient disease context.")
        st.write("**Key Tech:** Python, Streamlit, NIH APIs, OpenFDA")
        st.markdown("[View Code >](https://github.com/Looprx)") # Add specific link
        st.markdown('</div>', unsafe_allow_html=True)

    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<p class="project-title">🏨 Hotel Management App</p>', unsafe_allow_html=True)
        st.write("A full-stack operations platform for booking management and customer tracking.")
        st.write("**Key Tech:** React, TypeScript, Tailwind CSS")
        st.markdown("[View Code >](https://github.com/Looprx)")
        st.markdown('</div>', unsafe_allow_html=True)

with col2:
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<p class="project-title">🤝 DOXA - Job Matcher</p>', unsafe_allow_html=True)
        st.write("A hiring ecosystem connecting engineers and startups using a custom matching algorithm.")
        st.write("**Key Tech:** JavaScript, HTML5, CSS3, Algorithms")
        st.markdown("[View Code >](https://github.com/Looprx)")
        st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")

# --- HACKATHONS & ACHIEVEMENTS ---
st.header("🏆 Hackathons & Achievements")

tab1, tab2 = st.tabs(["🚀 Hackathons", "📜 Certifications"])

with tab1:
    st.markdown("""
    * **NASA International Space Apps Challenge (2024):** 🌌 Awarded "Galactic Problem Solver".
    * **KETCON 2024 Hackathon:** ⚡ Selected state-level participant (APJAKTU).
    * **Zephyrus 5.0 (2023):** 💻 Competed in 3-day hackathon at Christ College.
    """)

with tab2:
    st.markdown("""
    * **Content Creation Workshop:** IEDC SNMIMT (Aug 2024).
    * **Electrical Workshop Quiz:** Scored 93/100 (Nov 2023).
    * **Web Designing Competition:** Dignito'23 at De Paul Institute.
    """)

st.markdown("---")

# --- EDUCATION ---
st.header("🎓 Education")
st.write("**B.Tech in CSE (Artificial Intelligence)** | SNMIMT, Maliyankara | *2023 – 2027*")
st.write("**Higher Secondary (Computer Science)** | SN Trust HSS Nattika | *2021 – 2023*")

st.markdown("---")

# --- CONTACT FORM ---
st.header("📬 Get In Touch")
contact_form = """
<form action="https://formsubmit.co/eshakhil6@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your Name" required style="width: 100%; padding: 10px; margin-bottom: 10px; border: 1px solid #ccc; border-radius: 5px;">
     <input type="email" name="email" placeholder="Your Email" required style="width: 100%; padding: 10px; margin-bottom: 10px; border: 1px solid #ccc; border-radius: 5px;">
     <textarea name="message" placeholder="Your Message" required style="width: 100%; padding: 10px; margin-bottom: 10px; border: 1px solid #ccc; border-radius: 5px; height: 150px;"></textarea>
     <button type="submit" style="background-color: #4F8BF9; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer;">Send Message</button>
</form>
"""
st.markdown(contact_form, unsafe_allow_html=True)
