import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Recetario TM6", layout="centered")

# Leer archivos .md en la carpeta 'recetas'
recetas_path = Path("recetas")
archivos = list(recetas_path.glob("*.md"))

# Diccionario {nombre bonito: ruta}
recetas = {
    archivo.stem.replace("_", " "): archivo
    for archivo in archivos
}

# Obtener el índice de la opción seleccionada
opciones = ["Inicio"] + list(recetas.keys())
indice_actual = opciones.index(st.session_state["seleccion"])

# Sidebar
st.sidebar.title("🍽️ Recetario TM6")
st.session_state["seleccion"] = st.sidebar.selectbox(
    "Selecciona una receta",
    opciones,
    index=indice_actual
)

seleccion = st.session_state["seleccion"]


# Mostrar contenido
if seleccion == "Inicio":
    st.title("👩‍🍳 Bienvenido al Recetario para Thermomix TM6")
    st.write("Explora recetas fáciles y saludables diseñadas para tu TM6.")
    st.info("En móviles, toca el botón de la esquina superior izquierda (») para ver las recetas.")

    st.markdown("### Accesos rápidos:")

    for nombre_receta in recetas.keys():
        if st.button(f"📄 {nombre_receta}"):
            st.session_state['seleccion'] = nombre_receta
            st.rerun()

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
