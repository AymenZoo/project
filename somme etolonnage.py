f = open("document.txt", "r")
lignes = f.readlines()
somme = 0

for i in lignes:
    chiffres = []  
    for c in i:
        if c.isdigit():
            chiffres.append(c)  
    if chiffres:  
        premier = chiffres[0]
        dernier = chiffres[-1]
        valeur_etalon = int(premier + dernier)
        somme += valeur_etalon

f.close() 
print(f"La somme des valeurs d'étalonnage est : {somme}")
