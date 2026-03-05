from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent.parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic2.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Rodrigo Bogado"
PAGE_ICON = ":wave:"
NAME = "Rodrigo Bogado"
DESCRIPTION = """
| Científico de datos | Python | Bioinformático | Ciberseguridad |
"""
EMAIL = "rodribogado50@gmail.com"


SOCIAL_MEDIA = {
    
    "LinkedIn": "https://www.linkedin.com/in/rodrigo-bogado-a64b4925b/",
    "GitHub": "https://github.com/rodrib",
    
}

PROJECTS = {

"🏆 Septem obtuvo el 3er Lugar en Mi Primer Videojuego Publicado (03/2020 - 08/2020)" : "https://adva.vg/mpvp/",

"🏆 Director del trabajo, Estudio de caso: Videojuegos funcionales que promueven el ejercicio físico como estrategia de rehabilitación de un paciente con trastornos depresivos que padece síndrome de sensibilidad central, en la localidad de El Soberbio, Misiones, Argentina.": "https://drive.google.com/file/d/1PusfGk2XwIKBHUqGAnyR0R3568779IQn/view?usp=drive_link",

"🏆 APLICACIÓN DE UN PANEL MULTIGÉNICO PARA LA BÚSQUEDA DE VARIANTES GENÉTICAS DE RIESGO EN CÁNCER DE MAMA/OVARIO HEREDITARIO DESDE EL ÁMBITO DE LA SALUD PÚBLICA (01/2021 - Presente) Obtuvimos financiamiento a través del Instituto Nacional del Cáncer para el desarrollo de este proyecto":" https://www.argentina.gob.ar/sites/default/files/listado_adjudicacion_ip_linea_cancer-origen-nacional.pdf",

"🏆 Conseguí un secuenciador a través de Equipar Ciencia Miseq (06/2022 - Presente)": "https://www.argentina.gob.ar/noticias/el-mincyt-traves-del-programa-federal-equipar-ciencia-con-una-inversion-de-7800-millones-de",

"🏆 Beca de Salud Investiga: PublicVar (10/2023 - Presente) Para el desarrollo de herramientas bioinformáticas para el cáncer de mama-ovario": "https://www.argentina.gob.ar/salud/investiga/convocatorias-becas-de-investigacion-salud-investiga/ganadores-de-las-becas-salud",

"🏆 Crypthopy: una aplicación de criptografía hecha en Python sobre principios fundamentales, mecanismos, algoritmos y mejores prácticas": "https://crypthophy.streamlit.app/",

"🏆 BinDoc RE: Dashboard para Ingeniería Inversa (2025 - Presente) Plataforma full-stack para la gestión de auditorías de firmware; automatiza la documentación de hallazgos de Ghidra y la respuesta ante vulnerabilidades de hardware.": "https://bindoc-navy-ocean.reflex.run/"



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
        label=" 📄 Descargar Cv",
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


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experiencia y calificaciones")
st.write(
    """
- ✔️ 8 años de experiencia en bioinformática y análisis de datos
- ✔️ Fuerte experiencia y conocimiento en Python
- ✔️ Buen conocimiento de los principios estadísticos y sus respectivas aplicaciones.
- ✔️ Trabajo en equipo y muestro un fuerte sentido de iniciativa en las tareas.
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Habilidades duras")
st.write(
    """
- 👩‍💻 Programacion: Python (Scikit-learn, Pandas), SQL, VBA
- 📊 Visualizacion de Datos: PowerBi, MS Excel, Plotly, Streamlit
- 📚 Modelado: Regresion Logistica, Regresion Lineal, Arbol de decisiones
- 🗄️ Base de datos: Postgres, MongoDB, MySQL
- 🎮 Desarrollador de videojuegos: Unity, Godot
- 🔐 Ciberseguridad: Kali Linux, Parrot
"""
)

# --- WORK HISTORY ---
st.write('\n')
st.subheader("Historial de trabajo")
st.write("---")

# --- JOB 1
st.write("💻🧬", "**Bioinformatico | IGeHM**")
st.write("02/2020 - Presente")
st.write(
    """
- ► Me especializo en realizar procesos de Extracción, Transformación y Carga (ETL) en el contexto de registros médicos.
- ► Mi experiencia incluye el análisis e interpretación de resultados de secuenciación de próxima generación (NGS) utilizando diversos programas.
- ► Me destaco en la implementación de modelos de inteligencia artificial enfocados a la investigación del cáncer, contribuyendo al avance y comprensión de esta compleja enfermedad.
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Programador | Caraya Studios**")
st.write("01/2018 - Present")
st.write(
    """
- ► Juego un papel integral en el diseño de historias y la construcción del universo narrativo de los juegos.
- ► Mi participación en el diseño de juegos abarca desde conceptos creativos hasta la implementación práctica, incluido el diseño de niveles, el establecimiento de objetivos y otros aspectos del diseño de juegos.
- ► Como uno de los líderes de programación, contribuyo activamente a transformar ideas en experiencias de juego inmersivas e interactivas.
"""
)




# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Proyectos y logros")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")