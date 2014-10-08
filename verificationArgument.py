import main

# Fonction pour controler si les arguments sont correctement renseigner 
def verifArguments(liste_arg):
    main.logging.info("verifie argument 2")
    try:
        nb = int(liste_arg[1])
        if nb<0:
            nb = abs(nb)
            main.logging.warning('La quantité saisie doit etre positive')
            main.logging.info('Nombre négatif transformé en positif: ' + str(nb))
        elif nb>100:
            nb = None
            main.logging.warning('La quantité saisie est supérieur à 100')
            main.logging.info('Nombre supérieur à 100 transformé en : ' + str(nb))
            
        #setattr(liste_arg,nomArg, [liste_arg[0],nb])
        return True
    except ValueError:
        print ("Impossible de convertir \"" + liste_arg[1] + "\" en nombre entier !")
        main.logging.error('Impossible de convertir ' + liste_arg[1] + ' en nombre entier !')
        main.logging.debug(' *****************************************')
        exit(1)