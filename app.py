import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Recetario TM6", layout="wide")

# Leer archivos .md en la carpeta 'recetas'
recetas_path = Path("recetas")
archivos = list(recetas_path.glob("*.md"))

# Diccionario {nombre bonito: ruta}
recetas = {
    archivo.stem.replace("_", " "): archivo
    for archivo in archivos
}

# Sidebar
st.sidebar.title("🍽️ Recetario TM6")
seleccion = st.sidebar.selectbox("Selecciona una receta", ["Inicio"] + list(recetas.keys()))

# Mostrar contenido
if seleccion == "Inicio":
    st.title("👩‍🍳 Bienvenido al Recetario para Thermomix TM6")
    st.write("Explora recetas fáciles y saludables diseñadas para tu TM6.")
    st.info("Selecciona una receta desde el menú lateral.")
else:
    receta_path = recetas[seleccion]
    # st.title(seleccion)
    
    # Mostrar imagen si existe
    imagen_path = f"imagenes/{receta_path.stem}.jpg"
    if Path(imagen_path).exists():
        st.image(imagen_path, width=400)

    # Mostrar contenido del archivo
    contenido = receta_path.read_text(encoding="utf-8")
    st.markdown(contenido, unsafe_allow_html=True)
