cadeiras = [
    (9.2, 96, 1),
    (9.3, 64, 1),
    (9.7, 32, 1),
    (10, 64, 1),
    (9.7, 32, 1),
    (8.1, 96, 1),
    (9.5, 64, 2),
    (9, 64, 2),
    (7.7, 64, 2),
    (10, 64, 2),
    (9.6, 64, 2),
    (10, 64, 2),
    (9.7, 64, 3),
    (9.7, 64, 3),
    (6.3, 64, 3),
    (10, 64, 3),
    (10, 64, 3),
    (10, 64, 3),
    (10, 48, 3),
    (9.3, 64, 4),
    (6.9, 64, 4),
    (8.1, 64, 4),
    (7.7, 64, 4),
    (10, 64, 4),
    (10, 48, 4),
    (2, 64, 4)
]


# Discipina a ser trancada ()
trancada = 0


#iraIndividual = ((p*cargadisciplina*notafinal)/(p*cargadisciplina))*1000

#(1-((0.5*trancada)/Totalcursada))* iraIndividual

def calculaIra():
    somatorio1 = 0
    somatorio2 = 0
    totalcursada = 0

    x = len(cadeiras)

    for n in range(x):

        somatorio1 += ((cadeiras[n][2]*cadeiras[n][1]*cadeiras[n][0]))
        somatorio2 += (cadeiras[n][2]*cadeiras[n][1])
        totalcursada += cadeiras[n][1]

        #print(somatorio)

    totalcursada = totalcursada + trancada

    somatorios = somatorio1/somatorio2

    return ( 1-((0.5*trancada)/totalcursada))*somatorios*1000



print(calculaIra())
