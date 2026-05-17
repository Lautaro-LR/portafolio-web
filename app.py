import streamlit as st

# Configuración básica de la página (Pestaña del navegador)
st.set_page_config(page_title="Portafolio | Lautaro", page_icon="📊", layout="wide")

# --- BASE DE DATOS DE PROYECTOS (Fácilmente escalable) ---
# Para agregar un proyecto nuevo en el futuro, solo añade un bloque como estos a la lista.
proyectos = [
    {
        "id": "p1",
        "titulo": "Segmentación de Productos",
        "tecnologia": "Power BI / DAX",
        "descripcion_corta": "Dashboard interactivo...",
        "imagen": "imaganes/foto 1.jpg",
        # AGREGA ESTA LÍNEA (Obtén el link en Power BI: Archivo -> Insertar informe -> Sitio web o portal)
        "url_powerbi": "https://app.powerbi.com/view?r=eyJrIjoiNDM1ODIyMWItMWI0ZS00YjdiLWEzMWItNzE3YzM2NzFiYzk1IiwidCI6IjNlZDkxMGEyLTZlYjUtNDBiNy05M2VkLWQ5YTFmMTcxNTgzZiIsImMiOjR9&embedImagePlaceholder=true&pageName=f02ef6238b8c94a9eb3d", 
        "detalle_completo": """
        ### Análisis de Segmentación
        Este informe permite filtrar por categoría y región...
        """
    },
    {
        "id": "p2",
        "titulo": "Automatización de Facturación Hospitalaria",
        "tecnologia": "Excel Avanzado",
        "descripcion_corta": "Sistema diseñado en Excel para optimizar y agilizar los procesos de valoración médica.",
        "imagen": "imaganes/foto 1.jpg",
        "detalle_completo": """
        ### Contexto del Proyecto
        El objetivo principal fue reducir el tiempo de procesamiento en la facturación y minimizar errores manuales mediante automatizaciones...
        
        **Herramientas clave:** Excel, Power Query, Macros.
        """
    },
    {
        "id": "p3",
        "titulo": "Gestor de Tareas Automatizado",
        "tecnologia": "Google Sheets / Apps Script",
        "descripcion_corta": "Sistema de gestión de agenda profesional sincronizado y automatizado.",
        "imagen": "imaganes/foto 1.jpg",
        "detalle_completo": """
        ### Contexto del Proyecto
        Creación de un sistema a medida usando Google Sheets y programación con Apps Script para manejar la carga de trabajo diaria de forma eficiente...
        """
    },
    {
        "id": "p4",
        "titulo": "Gestor de Tareas Automatizado",
        "tecnologia": "Google Sheets / Apps Script",
        "descripcion_corta": "Sistema de gestión de agenda profesional sincronizado y automatizado.",
        "imagen": "imaganes/foto 1.jpg",
        "detalle_completo": """
        ### Contexto del Proyecto
        Creación de un sistema a medida usando Google Sheets y programación con Apps Script para manejar la carga de trabajo diaria de forma eficiente...
        """
    }
]

# --- NAVEGACIÓN LATERAL ---
# Crea un menú limpio a la izquierda
menu = st.sidebar.radio("Navegación", ["Sobre mi", "Proyectos"])

# --- SECCIÓN 1: INICIO Y CONTACTO ---
if menu == "Sobre mi":
    st.title("Soy Lautaro Rodriguez")
    st.subheader(" Analista de datos | Contador Público")
    
    st.write("---")
    
    # Dividimos la pantalla en dos columnas para el diseño
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ### Sobre mí
        ##### Soy Contador Público, pero desde siempre me considero una persona con una mentalidad curiosa y analítica, que disfruta encontrando formas de hacer el trabajo diario más fácil y eficiente. Mi recorrido me permitió conocer el "detrás de escena" de las empresas: pasé por la liquidación de impuestos, logré agilizar procesos de facturación y hoy aplico esa experiencia en mi rol actual gestionando cuentas corrientes.
                    
        ##### Para llevar ese impacto al siguiente nivel, entendí que la tecnología es la mejor aliada, por lo que me encuentro cursando la Tecnicatura en Ciencia de Datos e Inteligencia Artificial.
        ##### Mi objetivo es ser el puente entre los números del negocio y la programación, combinando mi visión contable con herramientas como Power BI, SQL y Python para dejar atrás las tareas manuales y construir sistemas automatizados que aporten claridad y valor real.
        
        ### Stack Tecnológico
        ##### • **Visualización y BI:** Power BI, DAX
        ##### • **Bases de Datos:** SQL
        ##### • **Lenguajes:** Python
        ##### • **Herramientas de Negocio:** Excel Avanzado (Power Query, Power Pivot, Tablad dinamicas)
        """)
    
    with col2:
        st.markdown("### Contacto")
        st.write("✉️ **Email:** rodriguez98lt@gmail.com")
        st.write("💼 **LinkedIn:** [Lautaro Rodriguez](www.linkedin.com/in/lautaro-rodríguez-47bb12196)")
        
        # Botón para descargar CV (Asegúrate de poner un archivo PDF real en la misma carpeta)
        try:
            with open("CV_Lautaro.pdf", "rb") as file:
                st.download_button(
                    label="📄 Descargar CV",
                    data=file,
                    file_name="CV_Lautaro.pdf",
                    mime="application/pdf"
                )
        except FileNotFoundError:
            st.info("Sube tu archivo 'CV_Lautaro.pdf' a la carpeta para habilitar la descarga.")

# --- SECCIÓN 2: PROYECTOS ---
elif menu == "Proyectos":
    
    # Lógica para alternar entre la "Galería" y el "Detalle del Proyecto"
    # ESTA ES LA LÍNEA QUE FALTABA: Inicializar el estado si no existe
    if 'proyecto_seleccionado' not in st.session_state:
        st.session_state.proyecto_seleccionado = None

    # VISTA 1: GALERÍA DE PROYECTOS (Si no hay ninguno seleccionado)
    if st.session_state.proyecto_seleccionado is None:
        st.title("Mis Proyectos 🚀")
        st.write("Explora mis desarrollos en análisis de datos, BI y automatización.")
        st.write("---")
        
        # Agrupar y mostrar los proyectos en filas reales de 3
        for i in range(0, len(proyectos), 3):
            cols = st.columns(3) # Crea 3 columnas nuevas por cada "fila"
            
            # Llenar las columnas de esta fila
            for j in range(3):
                if i + j < len(proyectos):
                    proj = proyectos[i + j]
                    with cols[j]:
                        st.image(proj["imagen"], use_container_width=True)
                        st.markdown(f"### {proj['titulo']}")
                        st.caption(f"🛠️ **{proj['tecnologia']}**")
                        
                        # Limitar la descripción corta para emparejar el diseño (ej: máximo 100 caracteres)
                        desc = proj["descripcion_corta"]
                        if len(desc) > 100:
                            st.write(desc[:97] + "...")
                        else:
                            st.write(desc)
                        
                        # Al hacer clic, guardamos el ID del proyecto y recargamos la página
                        if st.button("Ver detalles", key=f"btn_{proj['id']}"):
                            st.session_state.proyecto_seleccionado = proj['id']
                            st.rerun() 
            
            # Espacio visual entre filas para que respire el diseño
            st.write("---")

# VISTA 2: DETALLE DEL PROYECTO (Si hay un proyecto seleccionado)
    else:
        # Buscar la información del proyecto seleccionado en la lista
        proyecto_actual = next(p for p in proyectos if p['id'] == st.session_state.proyecto_seleccionado)
        
        # Botón para volver atrás
        if st.button("⬅️ Volver a la galería"):
            st.session_state.proyecto_seleccionado = None
            st.rerun()
            
        st.title(proyecto_actual["titulo"])
        st.caption(f"Tecnología principal: {proyecto_actual['tecnologia']}")

        # --- LÓGICA PARA MOSTRAR POWER BI O IMAGEN ---
        # Verificamos si el proyecto tiene la clave "url_powerbi" y si no está vacía
        if "url_powerbi" in proyecto_actual and proyecto_actual["url_powerbi"]:
            # Esto crea el marco interactivo. Puedes ajustar el 'height' (altura) a tu gusto.
            st.components.v1.iframe(proyecto_actual["url_powerbi"], height=600, scrolling=True)
        else:
            # Si no hay link, mostramos la imagen como antes
            st.image(proyecto_actual["imagen"], use_container_width=True)
        
        # Mostrar todo el detalle extenso
        st.write("---")
        st.markdown(proyecto_actual["detalle_completo"])