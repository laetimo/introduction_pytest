def inverse(chaine):
    if isinstance(chaine, int):
        raise ValueError("Vous devez passer une chaine de caractères")
    
    for element in chaine:
        if not isinstance(element, str):
            raise ValueError("Vous devez passer une chaine de caractères")
        
    if len(chaine) == 4:
        chaine.pop()

    chaine = "".join(chaine)

    return chaine[::-1]

if __name__ == "__main__":           # si j'exécute directement le fichier dans lequel je suis
    print(inverse(["a", "b", "c", "d"]))
    # print(inverse(["a", "b", 0, "d"]))
    print("hell")