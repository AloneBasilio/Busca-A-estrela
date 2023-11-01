A busca A* (A estrela) é um algoritmo de busca utilizado em computação e inteligência artificial para encontrar o caminho mais curto entre dois pontos em um gráfico ou mapa ponderado.
Foi desenvolvido por Peter Hart, Nils Nilsson e Bertram Raphael em 1968 e é amplamente aplicado em áreas como sistemas de informação geográfica, jogos, robótica, e em muitos outros contextos de otimização de rotas.
O algoritmo A* combina as características da busca em largura (BFS) e da busca em profundidade (DFS) com uma heurística que orienta a busca na direção do objetivo de forma eficiente. Aqui está uma visão geral de como o algoritmo funciona:
Inicialização : Começa com um nó de origem e um nó de destino (ou objetivo). Também inicializa uma estrutura de dados chamada "fronteira" (ou lista de abertos) que contém o nó de origem.

Avaliação de Nós : O algoritmo avalia nós na fronteira. Cada nó está associado a um custo acumulado (geralmente à soma das distâncias percorridas até agora) e a uma heurística que estima o custo restante até o objetivo. O custo total é a soma do custo acumulado e da estimativa heurística.

Seleção do Próximo Nó : O algoritmo escolhe o nó na fronteira com o menor custo total. Isso é feito para minimizar a função de custo que é a soma do custo já percorrido e a estimativa do custo restante.

Expansão de Nós : O nó selecionado é removido da fronteira e seus vizinhos são considerados. Para cada vizinho, o algoritmo calcula o custo total e os acréscimos à fronteira, se ainda não existirem nela.

Repetição : Os passos 3 e 4 são repetidos até que o nó de destino seja atingido ou até que não haja mais nós na fronteira para avaliar. Se o nó de destino for atingido, o algoritmo melhora o caminho mais curto retrocedendo a partir do nó de destino através de nós com menores custos acumulados.

