#!/usr/bin/python3

# Import module python
import logging

# Import module personnel
import verificationArgument
import definitionArguments as defArg


logging.basicConfig(filename='fichier_de.log', level=logging.DEBUG)

defArg.argumentObigatoire()
defArg.argumentOptionnel()

arguments = defArg.parser.parse_args()

# On affiche les arguments obligatoire
logging.info(arguments.temps)
logging.info(arguments.nom)
logging.info(arguments.format)

# On affiche les arguments optionnel s'ils sont présent
for monArgument in ['genre','artiste','album','titre']:
    if getattr(arguments, monArgument) is not None:
        logging.info(' Argument --' + monArgument + ' :\t' + getattr(arguments, monArgument)[0] + '  ' + getattr(arguments, monArgument)[1])
# On vérifie que le 2em sous argument de genre est bien un entier naturel
if verificationArgument.verifArguments(arguments.genre) == True:
    print ('ok')
    logging.debug(' *****************************************')
    
#variable de poucentage
#pourcentage = args.temps-(1-args.genre[1]/100)