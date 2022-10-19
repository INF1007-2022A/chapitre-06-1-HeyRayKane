#!/usr/bin/env python
# -*- coding: utf-8 -*-


def order(values: list = None) -> list:
    if values is None:
        # TODO: demander les valeurs ici
        values=[]
        for i in range(10):
            a = input("Entrez entier, un nombre décimal ou une chaîne de caractères:")
            values.append(a)
    #print(values)
    num_values=[]
    str_values=[]
    for j in values:
        if j.isdigit():
            num_values.append(float(j))
        elif not j.isdigit():
            str_values.append(j)
    """
    num_values = [float(value) for value in values if value.isdigit()]
    str_values = [value for value in values if not value.isdigit()]"""
    return sorted(num_values)+sorted(str_values)


def anagrams(words: list = None) -> bool:
    if words is None:
        # TODO: demander les mots ici
        words=[input("Écrivez le premier mot:"),input("Écrivez le deuxième mot:")]
    return sorted(words[0])==sorted(words[1])

def contains_doubles(items: list) -> bool:
    items=sorted(items)
    no_double =[]
    for i in range(1,len(items)):
        if items[i-1]!=items[i]:
            no_double.append(items[i-1])
    no_double.append(items[i])
    return not(no_double == items)

def best_grades(student_grades: dict) -> dict:
    # TODO: Retourner un dictionnaire contenant le nom de l'étudiant ayant la meilleure moyenne ainsi que sa moyenne
    dict={}
    def average(list):
        average=sum(list)/len(list)
        return average
    for i in student_grades:
        dict[average(student_grades[i])]=i
    return {dict[max(dict)]:max(dict)}


def frequence(sentence: str) -> dict:
    # TODO: Afficher les lettres les plus fréquentes
    new_sentence=""
    for j in sentence:
        if j.isalnum() or j==" ":
            new_sentence+=j
    a=sorted(new_sentence)
    print(a)
    caracteres_frequents = dict()
    lettres_frequentes = dict()
    lettres_organisees= dict()
    b=1
    for i in range(1,len(a)):
        if a[i-1]==a[i]:
            b+=1
        else:
            lettres_frequentes[a[i-1]]=b
            b=1
    lettres_frequentes[a[i-1]]=b
    for k in lettres_frequentes:
        if lettres_frequentes[k]>5:
            lettres_organisees[lettres_frequentes[k]] = k
    lettres_5ouplus = sorted(lettres_organisees)
    tableau_de_lettres = dict()
    for l in lettres_5ouplus[::-1]:
        tableau_de_lettres[lettres_organisees[l]]=l
    #       Retourner le tableau de lettres
    return tableau_de_lettres


def get_recipes():
    # TODO: Demander le nom d'une recette, puis ses ingredients et enregistrer dans une structure de données
    recettes=dict()
    nom_recette = True
    while nom_recette != "2":
        nom_recette = input("Entrez le nom d'une recette, ou entrez le chiffre 2 pour terminer:\n").capitalize()
        if nom_recette != "2":
            recettes[nom_recette] = ()
            recette = dict()
            ingredient = True
            n = 0
            while ingredient != "2":
                ingredient = input("Entrez le nom d'un ingrédient, ou entrez le chiffre 2 pour terminer:\n")
                if ingredient != "2":
                    recette[n] = ingredient.capitalize()
                n += 1
            recette_finale = []
            for a in recette:
                recette_finale.append(recette[a])
            recettes[nom_recette] = recette_finale
    print(recettes)
    return recettes


def print_recipe(ingredients) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    c=ingredients
    demande=input("Nom de la recette que vous souhaitez consulter:")
    if demande.capitalize() in c:
        print(demande.capitalize(), c[demande.capitalize()])
    else:
        print("Cette recette n'existe pas.")


def main() -> None:
    print(f"On essaie d'ordonner les valeurs...")
    print(order())

    print(f"On vérifie les anagrammes...")
    print(anagrams())

    my_list = [3, 3, 5, 6, 1, 1]
    print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")

    grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    best_student = best_grades(grades)
    print(f"{list(best_student.keys())[0]} a la meilleure moyenne: {list(best_student.values())[0]}")

    sentence = "bonjour, je suis une phrase. je suis compose de beaucoup de lettre. oui oui"
    print(frequence(sentence))

    print("On enregistre les recettes...")
    recipes = get_recipes()

    print("On affiche une recette au choix...")
    print_recipe(recipes)


if __name__ == '__main__':
    main()
