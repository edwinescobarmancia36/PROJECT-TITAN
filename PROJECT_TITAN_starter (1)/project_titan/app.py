import streamlit as st
import requests

# URL de tu API desplegada en Railway
API_BASE_URL = "https://project-titan-production-5d461bd9.up.railway.app"

st.title("⚽ Project Titan - Betting Desk")
st.write("Panel de análisis y registro manual de partidos.")

# Probar conexión con la API
if st.button("Verificar estado de la API"):
    try:
        response = requests.get(f"{API_BASE_URL}/api/v1/status")
        if response.status_code == 200:
            st.success("¡Conexión exitosa con la API en Railway!")
            st.json(response.json())
        else:
            st.error(f"Error en la API: {response.status_code}")
    except Exception as e:
        st.error(f"No se pudo conectar al servidor: {e}")