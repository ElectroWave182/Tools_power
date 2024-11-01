from math import floor, log
from sys import stdout
print = stdout.write


def power():
    fire = [198, 25, 0, 0, 0, 0, 25, 15, 10, 0, 0]
    ice = [236, 53, 0, 10, 0, 10, 15, 48, 0, 0, 15]
    lightning = [213, 6, 15, 15, 0, 0, 20, 0, 10, 0, 0]
    global ele, tools
    for anti in range(3):
        ele, tools = ["Fire", "Ice", "Lightning"], [fire, ice, lightning]
        del tools[anti]
        print("- Anti " + ele[anti] + " -\n")
        ele.append(ele[anti])
        del ele[anti]
        print("\n".join(list(moeMoe())) + "\n\n")


def moeMoe():
    nbt, resultat = len(tools[0]), []
    nbChem = 2**nbt
    chemins = [[0] * (nbt - floor(log(rang) / log(2) + 1)) + list(map(int, str(bin(rang).lstrip("0b")))) for rang in range(1, nbChem)]
    chemins.insert(0, [0] * nbt)
    for compo in range(nbChem):
        chemin = [0] * 2
        for numt in range(nbt):
            tool = chemins[compo][numt]
            chemin[tool] += tools[tool][numt]
        chemin[chemin.index(min(chemin))] *= 2
        resultat.append(chemin)
    resultats = list(map(sum, resultat))
    best = chemins[resultats.index(max(resultats))]
    for numt in range(nbt):
        tool = best[numt]
        if tools[tool][numt] == 0:
            yield ele[-1]
        else:
            yield ele[tool]


power()
