#!/usr/bin/python3

# Fonction pour controler si les arguments sont correctement renseigner 
def verifArguments(liste_arg):
    logging.info("verifie argument 2")
    try:
        nb = int(liste_arg[1])
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

# Début du main
import argparse
import logging

logging.basicConfig(filename='fichier_de.log', level=logging.DEBUG)

parser = argparse.ArgumentParser()
    
# Arguments obligatoire
parser.add_argument("temps", type=int, help="informer la duree en minutes")
parser.add_argument("nom", help="indiquer le nom du fichier de sortie")
parser.add_argument("format", choices=['M3U', 'XSPF', 'PLS'], help=("Choisir entre le format M3U et XSPF"))

# Arguments optionnel
parser.add_argument("-g", "--genre", nargs=2, help="indiquer le genre")
parser.add_argument("-a", "--artiste", nargs=2, help="indiquer l'artiste")
parser.add_argument("-A", "--album", nargs=2, help="indiquer l'album")
parser.add_argument("-t", "--titre", help="indiquer le titre")

args=parser.parse_args()

# On affiche les arguments obligatoire
logging.info(args.temps)
logging.info(args.nom)
logging.info(args.format)


# On affiche les arguments optionnel s'ils sont présent
for ARG in ['genre','artiste','album','titre']:
    if getattr(args, ARG) is not None:
        logging.info(' Argument --' + ARG + ' :\t' + getattr(args, ARG)[0] + '  ' + getattr(args, ARG)[1])
# On vérifie que le 2em sous argument de genre est bien un entier naturel
if verifArguments(args.genre) == True:
    print ('ok')
    logging.debug(' *****************************************')
    
#variable de poucentage
#pourcentage = args.temps-(1-args.genre[1]/100)