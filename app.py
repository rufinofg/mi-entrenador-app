import datetime
import streamlit as st
from garminconnect import Garmin

st.set_page_config(page_title="Mi Entrenador Personal", page_icon="🚴‍♂️")

st.title("🚴‍♂️ Asistente de Entrenamiento Personal")
st.subheader("Planificación & Registro Semanal")

st.markdown("""
¡Bienvenido a tu app de entrenamiento! Aquí iremos registrando tus datos diarios:
- **FCR (Frecuencia Cardíaca en Reposo)**
- **Peso Corporal**
- **Sesiones de Ciclismo y Fuerza**
""")

# --- CONEXIÓN CON GARMIN CONNECT ---
st.header("🔄 Sincronización con Garmin")

try:
    email = st.secrets["GARMIN_EMAIL"]
    password = st.secrets["GARMIN_PASSWORD"]

    api = Garmin(email, password)
    api.login()
    st.success("¡Conectado con éxito a Garmin Connect!")

    if st.button("🔄 Descargar datos de hoy"):
        fecha_hoy = datetime.date.today().isoformat()
        datos_hoy = api.get_stats(fecha_hoy)
        st.write("Datos recuperados de hoy:", datos_hoy)

except Exception as e:
    st.info("Para sincronizar automáticamente con Garmin, configura tus credenciales en los Secrets de Streamlit.")
    st.error(f"Detalle del estado: {e}")

# --- REGISTRO MANUAL EN BARRA LATERAL ---
st.sidebar.header("Métricas de Hoy")
peso = st.sidebar.number_input("Peso (kg):", value=75.5, step=0.1)
fcr = st.sidebar.number_input("FCR (ppm):", value=54, step=1)

if st.sidebar.button("Guardar Registro Manual"):
    st.sidebar.success(f"Guardado: {peso} kg | FCR: {fcr} ppm")