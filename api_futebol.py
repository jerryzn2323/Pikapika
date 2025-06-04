
import requests

API_KEY = "live_3eca01da326ba9ed27d76ca3a0f421"

def obter_jogos_serie_b():
    url = "https://api.api-futebol.com.br/v1/campeonatos/2/partidas"
    headers = {"Authorization": f"Bearer {API_KEY}"}
    res = requests.get(url, headers=headers)
    if res.status_code != 200:
        return []
    partidas = res.json().get("partidas", [])
    jogos = []
    for p in partidas:
        if p["status"] == "agendado":
            jogos.append({
                "time_mandante": p["time_mandante"]["nome_popular"],
                "time_visitante": p["time_visitante"]["nome_popular"],
                "data_realizacao": p["data_realizacao"],
                "hora_realizacao": p["hora_realizacao"],
                "estadio_nome": p["estadio"]["nome_popular"]
            })
    return jogos
