def menu_principale():
    print("Menu principale")
    print("=" * 30)
    menus = ["Liste des events", "Creer un event"]

    for i, m in enumerate(menus):
        print(f"{i + 1}. {m}")

    print("\n0. Quitter")

    while True:
        # saisie utilisateur
        choix = input("faire un choix: ")
        if choix == "1":
            print("Affichage liste des events")
        if choix == "2":
            print("Affichage formulaire créer")

        if choix == "0":
            print("Quitter....")
            break


# execution de la fonction
menu_principale()
