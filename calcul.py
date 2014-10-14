from main import arguments

# Calcul le pourcentage total rentré dans l'ensemble des paramètre
def pourcentageTotal():
    sommePourcentage = 0
    for somme in ['genre', 'artiste', 'album', 'titre']:
        if getattr(arguments, somme) is not None:
            for pourcentagePlaylist in getattr(arguments, somme):
                sommePourcentage += pourcentagePlaylist[1]
    return sommePourcentage

# Converti les pourcentages en minutes
def conversionMinutes():
    for conversion in ['genre', 'artiste', 'album', 'titre']:
        if getattr(arguments, conversion) is not None:
            for unArgument in getattr(arguments, conversion):
                unArgument [0][1] = int (arguments.temps*unArgument[0][1]/100)
    