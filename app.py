import streamlit as st
from PIL import Image


# Configuración básica de la página (Pestaña del navegador)
st.set_page_config(page_title="Portafolio | Lautaro", page_icon="📊", layout="wide")

# --- BASE DE DATOS DE PROYECTOS (Fácilmente escalable) ---
# Para agregar un proyecto nuevo en el futuro, solo añade un bloque como estos a la lista.
proyectos = [
    {
        "id": "p1",
        "titulo": "Segmentación de Productos",
        "tecnologia": "Power BI / DAX",
        "descripcion_corta": "Dashboard interactivo en POWER BI sobre segmentación de productos y cartera de clientes.",
        "imagen": "imagenes/Segmentación de Productos_imagen_portada.jpg",
        # AGREGA ESTA LÍNEA (Obtén el link en Power BI: Archivo -> Insertar informe -> Sitio web o portal)
        "url_powerbi": "https://app.powerbi.com/view?r=eyJrIjoiNDM1ODIyMWItMWI0ZS00YjdiLWEzMWItNzE3YzM2NzFiYzk1IiwidCI6IjNlZDkxMGEyLTZlYjUtNDBiNy05M2VkLWQ5YTFmMTcxNTgzZiIsImMiOjR9&embedImagePlaceholder=true&pageName=f02ef6238b8c94a9eb3d", 
        "detalle_completo": """
        ### Análisis de Segmentación
        Descripción por hoja:
        
        Resumen Ejecutivo: Exhibe los KPIs globales (saldo neto, volumen y cantidad de transacciones), la proporción de clientes según su estado (activos, inactivos, suspendidos) y la tendencia histórica de los movimientos entre 2020 y 2025.
        
        Cartera de Clientes: Profundiza en el detalle de los usuarios con una tabla transaccional, analiza la tasa de abandono (churn), identifica el "Top 10" de clientes con mayor saldo neto y desglosa la distribución de las cuentas por tipo y género.
        
        Segmentación de Productos: Evalúa distintas categorías (A, B, C) mediante una tabla de rendimiento, muestra su evolución anual y utiliza un mapa de árbol (treemap) para ilustrar el uso de productos segmentado por canales (Mobile, Web, ATM).
        
        Análisis de Crecimiento: Mide las variaciones porcentuales anuales de las transacciones y clasifica el rendimiento estratégico de las subcategorías de productos utilizando una gráfica de dispersión configurada como Matriz BCG.
        
        ### Arquitectura de Datos: Modelo en Copo de Nieve
        """,

        "imagen_modelo": "imagenes/Segmentacion_de_Productos_imagen_modelo_relacional.jpg",

        "detalle_parte2": """
        

        El análisis se sustenta en un modelo relacional estructurado bajo un esquema en Copo de Nieve (Snowflake). Este diseño centraliza las métricas del negocio y normaliza las tablas de contexto para asegurar la calidad de la información.

        Núcleo Transaccional: El modelo gira en torno a una tabla de hechos principal (Transacciones), la cual registra cada movimiento e interactúa con el resto del ecosistema.
        Jerarquías Normalizadas: Para evitar la redundancia de datos, las dimensiones complejas se desglosaron en sub-tablas lógicas. Esto se refleja claramente en la dependencia entre Clientes y sus Cuentas, así como en la estructuración del catálogo comercial (Categoría > Subcategoría > Producto).
        Eficiencia: Esta arquitectura garantiza la integridad de los datos, optimiza el almacenamiento y asegura un rendimiento fluido al procesar las distintas medidas y cálculos analíticos en el dashboard.
        
        Origen de datos: https://www.kaggle.com/datasets/saidaminsaidaxmadov/financial-transactions?select=DimAccount.csv

        """
    },
    {
        "id": "p2",
        "titulo": "Análisis pruebas PISA",
        "tecnologia": "Power BI / DAX",
        "descripcion_corta": "Dashboard interactivo en POWER BI sobre análisis de resultados pruebas PISA vs Inversión de países en educación.",
        "imagen": "imagenes/Analisis_pruebas_PISA_foto portada.jpg",
        # AGREGA ESTA LÍNEA (Obtén el link en Power BI: Archivo -> Insertar informe -> Sitio web o portal)
        "url_powerbi": "https://app.powerbi.com/view?r=eyJrIjoiMTI4ZjMwN2MtMjg0Ni00MjMzLTkwZTYtMzljMDkxYjU3ZjEzIiwidCI6IjNlZDkxMGEyLTZlYjUtNDBiNy05M2VkLWQ5YTFmMTcxNTgzZiIsImMiOjR9&pageName=3f65cc8b5a2d1e51e958", 
        "detalle_completo": """
        ### Contexto del Proyecto
        Este proyecto fue desarrollado como trabajo final grupal para la materia Laboratorio de Integración. El objetivo principal consistió en cruzar y analizar los resultados de las Pruebas PISA con variables macroeconómicas clave, como el PBI invertido en educación y el Índice de Libertad Económica. 

        
        ### Desarrollo y Análisis
        El resultado final es un dashboard interactivo desarrollado en Power BI, estructurado en tres ejes principales:

        **Panorama Regional:** Análisis de situación y posicionamiento comparativo de los países de Latinoamérica.

        **Correlación Histórica:** Evaluación de la tendencia histórica entre la inversión realizada y los puntajes obtenidos.

        **Rendimiento de la Inversión:** Identificación de eficiencia, destacando qué países logran obtener más puntos por cada dólar invertido.

        ### Desafíos Técnicos
        Más allá del diseño visual y la experiencia de usuario, el núcleo del proyecto requirió un trabajo profundo de estructuración y procesamiento:

        **Integración de Fuentes:** Recopilación, limpieza y consolidación de datos provenientes de entidades totalmente distintas (PISA, Banco Mundial).

        **Arquitectura de Datos:** Diseño e implementación de un modelo relacional sólido para conectar las variables.

        **Lógica DAX:** Automatización de indicadores y creación de formatos condicionales complejos para facilitar la lectura inmediata del rendimiento por categoría.

        """
    },
    {
        "id": "p3",
        "titulo": "Análisis mercado IT Canadá",
        "tecnologia": "Power BI / DAX",
        "descripcion_corta": "Dashboard interactivo en POWER BI sobre mercado laboral IT en Canadá.",
        "imagen": "imagenes/Analisis_TrabajoIT_fotoportada.jpg",
        # AGREGA ESTA LÍNEA (Obtén el link en Power BI: Archivo -> Insertar informe -> Sitio web o portal)
        "url_powerbi": "https://app.powerbi.com/view?r=eyJrIjoiNGMzYzIyOWYtYWYxZi00MWViLWJiMWUtMDEyNTFmNmYzMjcyIiwidCI6IjNlZDkxMGEyLTZlYjUtNDBiNy05M2VkLWQ5YTFmMTcxNTgzZiIsImMiOjR9&pageName=681113709c393d13071f", 
        "detalle_completo": """
        ### Contexto del Proyecto
        Con tanto ruido sobre la supuesta saturación del mercado y el discurso de que "ya no sirve" estudiar programación, decidí ir a las fuentes oficiales para ver la realidad. Para esto construí un tablero utilizando los datos oficiales de Canadá. 

        Podemos ver en los dos primeros indicadores cómo avanzó el porcentaje que ocupa la programación sobre todo el total de trabajadores desde 1,08% hasta en 2024 un 2,17%, y cómo pasó de existir +156.000 programadores a +379.000. Evaluando entonces el peso relativo de la actividad y en términos absolutos la evolución de la misma. 

        Para los 3 indicadores siguientes, me pareció interesante evaluar la profesión en cuestión con otras 3 que tengo tradicionales, demandadas y que también son de prestación de servicios. Podemos tomar como ejemplo la comparación con contadores, se observa que en el 2010 hay 1,64 programadores por cada contador, mientras que en el 2024 hay 2,71 programadores por cada contador, en poco más de una década el ratio aumentó un 65%.
        Abajo de cada ratio se puede visualizar esta relación desde 2001 hasta 2024.

        Por último, 2 gráficos de líneas que muestran el porcentaje de programadores sobre el total de trabajadores, y la cantidad total de los mencionados. Para ambos casos los puntos más altos son 2023, 2024 y 2022, respectivamente. 

        Mis conclusiones: 
        Si bien vemos un corte en el crecimiento que se veía desde 2019-2020 a 2023, e incluso un decrecimiento de 2023 a 2024, este ajuste parece ser una estabilización lógica tras el crecimiento acelerado de los últimos años. Sin embargo, el volumen total de profesionales sigue siendo más del doble que hace una década.
        Estamos ante una industria que ya es un pilar estructural del mercado laboral moderno, puede haber más competencia, un poco menos de demanda y un crecimiento no tan acelerado como hace algunos años, pero los números no mienten: la base estructural de empleo en tecnología es hoy inmensa.

        Este proyecto surge de mi propia evolución. Al ser Contador Público y estudiar Ciencia de Datos e IA, sentí la necesidad de verificar si mi apuesta por la tecnología tiene un respaldo sólido en el mercado actual.

        Origen de datos: Fuente: Statistics Canada (StatCan) - Table 14-10-0202-01.
        """
    },
    {
        "id": "p4",
        "titulo": "Control de stock",
        "tecnologia": "Excel Avanzado",
        "descripcion_corta": "Control de movimientos de stock en EXCEL.",
        "imagen": "imagenes/ControlStock_portada.jpg",
        "video": "imagenes/Video_Control_stock_excel.mp4", # Asegúrate de crear la carpeta y poner la ruta correcta
        "detalle_completo": """
        ### Contexto del Proyecto
        Si bien el registro de las facturas siempre requiere una carga inicial de datos, el verdadero problema de muchas empresas es usar planillas estáticas donde el cálculo del stock y los saldos también debe actualizarse a mano. Esa falta de automatización es la que termina generando errores, quiebres de inventario o inmovilización de capital en productos que no rotan.

        Para solucionar esto de manera accesible, diseñé este Dashboard Automatizado de Control de Stock y Movimientos. 📊

        ¿Qué permite hacer esta herramienta? 

        Control de Estado en Tiempo Real: Alertas automáticas de "REPONER" o "OK" cruzando el stock actual contra el mínimo definido, todo actualizado al instante tras cargar un comprobante. 
        
        Trazabilidad Total: Registro detallado de entradas y salidas con sus respectivas facturas. 
        
        Filtros Dinámicos: Segmentación rápida por categoría o código para analizar la rotación al instante.

        A nivel técnico, el desarrollo incluye: 
        Validación de datos para estandarizar el ingreso manual de información.-
        Tablas dinámicas para la consolidación de movimientos masivos.-
        Funciones lógicas anidadas para la automatización de los estados de inventario.-

        Sé que Excel no es el motor de base de datos ideal. Sin embargo, entiendo perfectamente la realidad de las pymes: muchas veces implementar sistemas complejos o migrar a bases de datos relacionales resulta muy costoso, o la curva de aprendizaje es demasiado alta.

        Estructurar la información de manera sólida en Excel es el paso pragmático y fundamental para "ordenar la casa", antes de escalar hacia herramientas más robustas de Business Intelligence.

        Se utiliza una conexión en Power Pivot para conectar los movimientos de stock con el stock total
        """,

        "imagen_modelo": "imagenes/Control_stock_excel_Diagrama.jpg",
        
        "detalle_parte2": """
        **Herramientas clave:** Excel (Tablas dinámicas, Power Pivot, validación de datos)

        """
    },
        {
        "id": "p5",
        "titulo": "Facturación Hospitalaria",
        "tecnologia": "Excel Avanzado",
        "descripcion_corta": "Sistema diseñado en EXCEL para optimizar y agilizar los procesos de valoración médica.",
        "imagen": "imagenes/Facturacion_hospital_imagen_portada.jpg",
        "video": "imagenes/Video_Facturacion_hospital.mp4", # Asegúrate de crear la carpeta y poner la ruta correcta
        "detalle_completo": """
        ### Contexto del Proyecto
        El objetivo central de este proyecto fue transformar y automatizar el proceso de facturación hospitalaria, reduciendo drásticamente los tiempos de procesamiento y minimizando el margen de error manual en el cálculo de aranceles.

        El principal desafío técnico radicó en la parametrización de un sistema de cobros complejo: cada práctica médica involucra diferentes tipos de gastos (OG, GB, GQ, entre otros) y unidades de medida. La solución implementada logra calcular el precio final de manera automática, multiplicando las unidades de la prestación por el valor de gasto correspondiente, adaptándose de forma dinámica a los tabuladores específicos y cambiantes de cada obra social o empresa de medicina prepaga.
        
        **Herramientas clave:** Excel (BUSCARH, COINCIDIR, SUMAR.SI.CONJUNTO, validación de datos, entre otras) 
        """
    }
]

# --- NAVEGACIÓN LATERAL ---
# Crea un menú limpio a la izquierda
menu = st.sidebar.radio("Navegación", ["Sobre mí", "Proyectos"])

# --- SECCIÓN 1: INICIO Y CONTACTO ---
if menu == "Sobre mí":
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
        ##### • **Herramientas de Negocio:** Excel Avanzado (Power Query, Power Pivot, Tablas dinámicas)
        """)
    
    with col2:
        st.markdown("### Contacto")
        st.write("✉️ **Email:** rodriguez98lt@gmail.com")
        st.write("💼 **LinkedIn:** [Lautaro Rodriguez](https://www.linkedin.com/in/lautaro-rodríguez-47bb12196)")
        
        
        # Botón para descargar CV (Asegúrate de poner un archivo PDF real en la misma carpeta)
        #try:
        #    with open("CV_Lautaro.pdf", "rb") as file:
        #        st.download_button(
        #            label="📄 Descargar CV",
        #            data=file,
        #            file_name="CV_Lautaro.pdf",
        #            mime="application/pdf"
        #        )
        #except FileNotFoundError:
        #    st.info("Sube tu archivo 'CV_Lautaro.pdf' a la carpeta para habilitar la descarga.")
        
# --- SECCIÓN 2: PROYECTOS ---
elif menu == "Proyectos":
    
    # Lógica para alternar entre la "Galería" y el "Detalle del Proyecto"
    # ESTA ES LA LÍNEA QUE FALTABA: Inicializar el estado si no existe
    if 'proyecto_seleccionado' not in st.session_state:
        st.session_state.proyecto_seleccionado = None

    # VISTA 1: GALERÍA DE PROYECTOS (Si no hay ninguno seleccionado)
    if st.session_state.proyecto_seleccionado is None:
        st.title("Mis Proyectos")
        st.write("---")
        
        # Agrupar y mostrar los proyectos en filas reales de 3
        for i in range(0, len(proyectos), 3):
            cols = st.columns(3) # Crea 3 columnas nuevas por cada "fila"
            
            # Llenar las columnas de esta fila
            for j in range(3):
                if i + j < len(proyectos):
                    proj = proyectos[i + j]
                    with cols[j]:
                        # Cargar la imagen y forzar un tamaño fijo (Ancho, Alto)
                        img_portada = Image.open(proj["imagen"])
                        img_portada = img_portada.resize((800, 500)) 
                        
                        st.image(img_portada, use_container_width=True)
                        st.markdown(f"### {proj['titulo']}")
                        
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

# --- LÓGICA PARA MOSTRAR POWER BI, VIDEO O IMAGEN ---
        col_izq, col_centro, col_der = st.columns([1, 4, 1])
        
        with col_centro:
            if "url_powerbi" in proyecto_actual and proyecto_actual["url_powerbi"]:
                st.components.v1.iframe(proyecto_actual["url_powerbi"], height=600, scrolling=True)
            elif "video" in proyecto_actual:
                st.video(proyecto_actual["video"]) # Reproductor nativo de Streamlit para MP4
            else:
                st.image(proyecto_actual["imagen"], use_container_width=True)
        
        # Mostrar todo el detalle extenso
        st.write("---")
        
        # 1. Imprime la primera parte del texto (que dejaste con el nombre "detalle_completo")
        st.markdown(proyecto_actual.get("detalle_completo", ""))
        
        # 2. Si el proyecto tiene la clave "imagen_modelo", muestra la imagen
        if "imagen_modelo" in proyecto_actual:
            st.image(proyecto_actual["imagen_modelo"], width=900) # Ve cambiando el 500 hasta que te guste el tamaño
            
        # 3. Si el proyecto tiene una segunda parte de texto, la muestra debajo
        if "detalle_parte2" in proyecto_actual:
            st.markdown(proyecto_actual["detalle_parte2"])