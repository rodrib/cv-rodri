from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic2.png"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Rodrigo Bogado"
PAGE_ICON = ":wave:"
NAME = "Rodrigo Bogado"
DESCRIPTION = """
| Data Scientist | Python | Bioinformatician | Cybersecurity |
"""
EMAIL = "rodribogado50@email.com"


SOCIAL_MEDIA = {
    
    "LinkedIn": "https://www.linkedin.com/in/rodrigo-bogado-a64b4925b/",
    "GitHub": "https://github.com/rodrib",
    
}

PROJECTS = {
    "🏆 Sales Dashboard - Comparing sales across three stores": "https://youtu.be/Sb0A9i6d320",
    "🏆 Income and Expense Tracker - Web app with NoSQL database": "https://youtu.be/3egaMfE9388",
    "🏆 Desktop Application - Excel2CSV converter with user settings & menubar": "https://youtu.be/LzCfNanQ_9c",
    "🏆 MyToolBelt - Custom MS Excel add-in to combine Python & Excel": "https://pythonandvba.com/mytoolbelt/",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

#--- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write(f"📫 {EMAIL}")


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")



####### agregue
# # --- SOCIAL LINKS ---
# st.write('\n')
# cols = st.columns(len(SOCIAL_MEDIA))

# # Diccionario de íconos
# social_icons = {
#     "LinkedIn": "https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png",
#     "GitHub": "https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png"
# }

# for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
#     cols[index].markdown(f'<a href="{link}"><img src="{social_icons[platform]}" width="30"></a>', unsafe_allow_html=True)





# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qualifications")
st.write(
    """
- ✔️ 8 years of experience in bioinformatics and data analysis
- ✔️ Strong hands on experience and knowledge in Python
- ✔️ Good understanding of statistical principles and their respective applications
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas), SQL, VBA
- 📊 Data Visulization: PowerBi, MS Excel, Plotly
- 📚 Modeling: Logistic regression, linear regression, decition trees
- 🗄️ Databases: Postgres, MongoDB, MySQL
- 🎮 GameDeveloper: Unity, Godot
- 🔐 Cybersecurity: Kali Linux, Parrot
"""
)

# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("💻🧬", "**Bioinformatician | IGeHM**")
st.write("02/2020 - Present")
st.write(
    """
- ► I specialize in performing Extraction, Transformation, and Loading (ETL) processes in the context of medical records.
- ► My experience includes the analysis and interpretation of next-generation sequencing (NGS) results using various programs.
- ► I excel in implementing artificial intelligence models focused on cancer research, contributing to the advancement and understanding of this complex disease.
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Computer programmer | Caraya Studios**")
st.write("01/2018 - Present")
st.write(
    """
- ► I play an integral role in the story design and narrative universe construction of games.
- ► My involvement in game design spans from creative concepts to practical implementation, including level design, objective setting, and other Game Design aspects.
- ► As one of the programming leads, I actively contribute to transforming ideas into immersive and interactive gaming experiences.
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**Data Analyst | Chegg**")
st.write("04/2015 - 01/2018")
st.write(
    """
- ► Devised KPIs using SQL across company website in collaboration with cross-functional teams to achieve a 120% jump in organic traﬃc
- ► Analyzed, documented, and reported user survey results to improve customer communication processes by 18%
- ► Collaborated with analyst team to oversee end-to-end process surrounding customers' return data
"""
)


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")