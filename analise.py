
def gerar_sugestao_aposta(jogo):
    mandante = jogo["time_mandante"].lower()
    visitante = jogo["time_visitante"].lower()

    favoritos = ["santos", "america-mg", "goias", "chapecoense", "sport"]
    fracos = ["ituano", "avai", "mirassol", "botafogo-sp"]

    if any(fav in mandante for fav in favoritos):
        return "Vitória do mandante (favorito)"
    elif any(fav in visitante for fav in favoritos):
        return "Vitória do visitante (favorito)"
    elif any(f in mandante for f in fracos) and any(f in visitante for f in fracos):
        return "Evitar aposta - Jogo equilibrado entre equipes fracas"
    else:
        return "Dupla chance ou under 2.5 gols"
