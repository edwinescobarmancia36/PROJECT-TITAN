import streamlit as st
import requests

# Configuración de la página
st.set_page_config(page_title="Project Titan - Dashboard", page_icon="⚡", layout="wide")

# URL oficial de tu backend desplegado en Railway
API_URL = "https://project-titan-production-5d461bd9.up.railway.app/api/v1"

st.title("⚡ Project Titan - Sports Analytics Dashboard")
st.markdown("Plataforma modular de inteligencia deportiva conectada a Railway.")

# Sidebar para navegación
st.sidebar.header("Panel de Control")
opcion = st.sidebar.radio("Selecciona una vista:", ["📊 Explorador de Equipos", "⚙️ Estado del Sistema"])

if opcion == "⚙️ Estado del Sistema":
    st.subheader("Estado de la API en la Nube")
    try:
        response = requests.get(f"{API_URL}/status")
        if response.status_code == 200:
            data = response.json()
            st.success("🟢 Conexión exitosa con el servidor en Railway.")
            st.json(data)
        else:
            st.error("⚠️ El servidor respondió con un error.")
    except Exception as e:
        st.error(f"❌ No se pudo conectar al servidor: {e}")

elif opcion == "📊 Explorador de Equipos":
    st.subheader("Catálogo de Equipos por Deporte")
    
    # Obtener la lista de deportes disponibles desde el backend
    try:
        res_sports = requests.get(f"{API_URL}/sports")
        sports_list = [s["code"] for s in res_sports.json()] if res_sports.status_code == 200 else ["football", "nba"]
    except:
        sports_list = ["football", "nba"]

    # Filtro por deporte
    deporte_seleccionado = st.selectbox("Selecciona un deporte:", sports_list)
    
    # Petición de equipos filtrados
    try:
        res_teams = requests.get(f"{API_URL}/teams", params={"sport": deporte_seleccionado})
        if res_teams.status_code == 200:
            teams = res_teams.json()
            
            if not teams:
                st.warning(f"No hay equipos registrados para el deporte: {deporte_seleccionado}")
            else:
                st.info(f"Se encontraron {len(teams)} equipos en la base de datos.")
                for team in teams:
                    with st.container():
                        col1, col2, col3 = st.columns([3, 2, 2])
                        col1.markdown(f"**⚽ Equipo:** {team.get('name')}")
                        col2.markdown(f"**🌍 País:** {team.get('country', 'N/A')}")
                        col3.markdown(f"**🆔 ID:** {team.get('id')}")
                        st.divider()
        else:
            st.error("Error al obtener los equipos de la API.")
    except Exception as e:
        st.error(f"Error de conexión: {e}")
