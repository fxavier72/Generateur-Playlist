import logging

# Fonction pour controler si les arguments sont correctement renseigner 
def verifArguments(liste_arg):
    logging.info("verifie argument 2")
    try:
        nb = int(liste_arg[0][1])
        if nb<0:
            nb = abs(nb)
            logging.warning('La quantité saisie doit etre positive')
            logging.info('Nombre négatif transformé en positif: ' + str(nb))
        elif nb>100:
            nb = None
            logging.warning('La quantité saisie est supérieur à 100')
            logging.info('Nombre supérieur à 100 transformé en : ' + str(nb))
            
        #setattr(liste_arg,nomArg, [liste_arg[0],nb])
        return True
    except ValueError:
        print ("Impossible de convertir \"" + liste_arg[1] + "\" en nombre entier !")
        logging.error('Impossible de convertir ' + liste_arg[1] + ' en nombre entier !')
        logging.debug(' *****************************************')
        exit(1)