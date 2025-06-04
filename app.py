
import streamlit as st
from api_futebol import obter_jogos_serie_b
from analise import gerar_sugestao_aposta

st.set_page_config(page_title="Análise Série B - Apostas", layout="wide")
st.title("📊 Painel de Apostas - Série B (API-Futebol)")

jogos = obter_jogos_serie_b()

if not jogos:
    st.warning("Nenhum jogo disponível no momento.")
else:
    for jogo in jogos:
        st.subheader(f"{jogo['time_mandante']} x {jogo['time_visitante']}")
        st.write(f"Data: {jogo['data_realizacao']} - Horário: {jogo['hora_realizacao']}")
        st.write(f"Estádio: {jogo['estadio_nome']}")
        sugestao = gerar_sugestao_aposta(jogo)
        st.success(f"💡 Sugestão: {sugestao}")
        st.markdown("---")
