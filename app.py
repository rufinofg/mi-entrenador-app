import streamlit as st

st.set_page_config(page_title="Mi Entrenador Personal", page_icon="🚴‍♂️")

st.title("🚴‍♂️ Asistente de Entrenamiento Personal")
st.subheader("Planificación & Registro Semanal")

st.markdown("""
¡Bienvenido a tu app de entrenamiento! Aquí iremos registrando tus datos diarios:
- **FCR (Frecuencia Cardíaca en Reposo)**
- **Peso Corporal**
- **Sesiones de Ciclismo y Fuerza**
""")

st.sidebar.header("Métricas de Hoy")
peso = st.sidebar.number_input("Peso (kg):", value=76.4, step=0.1)
fcr = st.sidebar.number_input("FCR (ppm):", value=52, step=1)

if st.sidebar.button("Guardar Registro"):
    st.success(f"Registro guardado con éxito: {peso} kg | FCR: {fcr} ppm")