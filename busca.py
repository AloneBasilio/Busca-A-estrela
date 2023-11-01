import heapq

# Defina a estrutura de dados para representar as informações de uma via
def criar_via(codigo, localidade1, localidade2, distancia, piso, portagem, velocidade_media):
    return (codigo, localidade1, localidade2, distancia, (piso, portagem, velocidade_media))

# Defina a representação das vias (exemplo simplificado)
vias = [
    criar_via("a4","Beira", "Inhambane", 65, 5, 500, 130),
    criar_via("a1", "Beira", "Quelimane", 70, 5, 500, 130),
    criar_via("n1", "Beira", "Quelimane", 70, 5, 500, 90),
    criar_via("n109", "Beira", "Quelimane", 60, 5, 0, 70),
    criar_via("n10", "Beira", "Tete", 50, 5, 500, 130),
    criar_via("ip1", "Beira", "Xai-Xai", 30, 2, 0, 60),
    criar_via("n6", "Quelimane", "Nampula", 70, 4, 0, 100),
    criar_via("n23", "Tete", "Maputo", 130, 3, 0, 80),
    criar_via("n35", "Tete", "Dondo", 25, 2, 0, 60),
    criar_via("ic1", "Tete", "Songo", 55, 3, 0, 80),
    criar_via("n31", "Xai-Xai", "Tete", 25, 1, 0, 50),
    criar_via("ip1", "Xai-Xai", "Songo", 45, 3, 0, 90),
    criar_via("n6", "Nampula", "Vilanculos", 70, 2, 0, 70),
]

# Função heurística (critério: menor distância percorrida)
def heuristica(cidade, objetivo):
    for via in vias:
        _, localidade1, localidade2, distancia, _ = via
        if (localidade1 == cidade and localidade2 == objetivo) or (localidade2 == cidade and localidade1 == objetivo):
            return distancia
    return float('inf')  # Valor infinito se não houver conexão direta

# Função A* para encontrar o itinerário ótimo
def a_estrela(vias, inicio, objetivo, estado_piso_minimo):
    abertos = [(0, inicio, [])]
    visitados = set()

    while abertos:
        custo, cidade, caminho = heapq.heappop(abertos)

        if cidade == objetivo:
            return caminho + [(cidade, cidade)]

        if cidade in visitados:
            continue

        visitados.add(cidade)

        for via in vias:
            _, localidade1, localidade2, distancia, (piso, portagem, velocidade_media) = via
            if piso >= estado_piso_minimo:
                novo_custo = custo + distancia
                heur = heuristica(localidade2, objetivo)
                if localidade1 == cidade:
                    proxima_cidade = localidade2
                else:
                    proxima_cidade = localidade1
                heapq.heappush(abertos, (novo_custo + heur, proxima_cidade, caminho + [(cidade, proxima_cidade)]))

    return None

# Exemplo de uso
cidade_inicio = "Xai-Xai"
cidade_objetivo = "Nampula"
estado_piso_minimo = 3
itinerario = a_estrela(vias, cidade_inicio, cidade_objetivo, estado_piso_minimo)

if itinerario:
    print("Itinerário ótimo:")
    for cidade1, cidade2 in itinerario:
        print(f"De {cidade1} até {cidade2}")
else:
    print("Não foi possível encontrar um itinerário com as restrições definidas.")

