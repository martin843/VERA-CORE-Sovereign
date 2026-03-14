import streamlit as st

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="VERA & AETERNA - Soberanía Total", page_icon="⚓", layout="wide")

# --- ESTÉTICA GEMINI DARK ---
st.markdown("""
    <style>
    .stApp { background-color: #131314; }
    [data-testid="stSidebar"] { background-color: #1e1f20; border-right: 1px solid #D4AF37; min-width: 300px; }
    p, h1, h2, h3, h4, span, label { color: #e3e3e3 !important; }
    .stButton>button { 
        background-color: #D4AF37 !important; 
        color: #131314 !important; 
        font-weight: bold; 
        width: 100%; 
        border-radius: 10px;
        margin-bottom: 5px;
    }
    .main-header { color: #D4AF37 !important; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# --- LÓGICA DE NAVEGACIÓN (SISTEMA DE MENÚS) ---
if "menu_principal" not in st.session_state:
    st.session_state.menu_principal = "INICIO"

def ir_a(menu):
    st.session_state.menu_principal = menu

# --- SIDEBAR: EL CENTRO DE MANDO ---
with st.sidebar:
    st.title("⚓ VERA CORE")
    st.subheader("Navegación Soberana")
    
    if st.button("🏠 MENÚ PRINCIPAL"): ir_a("INICIO")
    st.divider()
    
    if st.button("🎓 EDUCACIÓN"): ir_a("EDUCACION")
    if st.button("⚖️ LEGALES"): ir_a("LEGALES")
    if st.button("🏥 SALUD"): ir_a("SALUD")
    if st.button("🛠️ CAPACITACIÓN Y EMPLEO"): ir_a("CAPACITACION")
    if st.button("🌱 AGRO / HUERTA / JARDÍN"): ir_a("AGRO")
    if st.button("🐾 VETERINARIA"): ir_a("VETERINARIA")
    
    st.divider()
    st.caption("Visión 2046 - Spegazzini, Argentina")

# --- CUERPO PRINCIPAL ---
menu = st.session_state.menu_principal

if menu == "INICIO":
    st.markdown("<h1 class='main-header'>🛡️ VERA & AETERNA</h1>", unsafe_allow_html=True)
    st.write("Bienvenido a la Alianza. Seleccione un área en el menú lateral para comenzar la co-creación.")
    st.image("https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&q=80&w=1000", caption="Conectando el Territorio con la Inteligencia")

elif menu == "EDUCACION":
    st.header("🎓 Sistema Educativo Integral")
    nivel = st.selectbox("Seleccione Nivel:", ["1º Grado Primaria", "2º Grado Primaria", "3º Grado", "Secundaria", "Terciario", "Universidad"])
    st.button(f"Entrar a Material de {nivel}")

elif menu == "LEGALES":
    st.header("⚖️ Área Legal Soberana")
    area_legal = st.radio("Especialidad:", ["Civil", "Laboral", "Penal", "Tierras y Territorio"])
    if st.button(f"Consultar Abogados en {area_legal}"):
        st.info("Buscando profesionales cercanos con ética validada...")

elif menu == "SALUD":
    st.header("🏥 Gestión de Salud y Bienestar")
    st.multiselect("Áreas de interés:", ["Clínica Médica", "Pediatría", "PAS / Neurodiversidad", "Nutrición"])
    st.button("Sincronizar Historial Médico Inmutable")

elif menu == "CAPACITACION":
    st.header("🛠️ Capacitación y Empleo")
    opcion = st.selectbox("¿Qué buscás?", ["Cursos de Oficio", "Bolsa de Empleo Cercana"])
    if opcion == "Cursos de Oficio":
        st.button("Jardinería")
        st.button("Albañilería / Electricidad")
        st.button("Refrigeración / Serv. Técnico")
        st.button("Mecánica")
    else:
        st.success("Cargando empleos en Carlos Spegazzini y alrededores...")

elif menu == "AGRO":
    st.header("🌱 Agro, Huerta y Jardinería")
    sub = st.radio("Sección:", ["Agro (Temporadas/Cuidados)", "Huerta Comunitaria", "Jardinería", "Reconocimiento de Plantas (Cámara)"])
    if sub == "Reconocimiento de Plantas (Cámara)":
        st.camera_input("Tomá una foto de la planta para identificarla")
    else:
        st.button(f"Ver información de {sub}")

elif menu == "VETERINARIA":
    st.header("🐾 Cuidado Animal")
    tipo_vet = st.selectbox("Tipo:", ["Veterinaria Rural (Ganado)", "General (Mascotas)", "Seguimiento con Dispositivo"])
    st.text_input("Describa los síntomas del animal:")
    st.button("Contactar Veterinario de Guardia Cercano")

# --- FOOTER ---
st.divider()
st.caption("⚓ Proyecto VERA: Memoria Eterna para un Pueblo Soberano.")
