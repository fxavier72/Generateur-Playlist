import argparse

parser = argparse.ArgumentParser()
    
# Arguments obligatoire
def argumentObigatoire():
    parser.add_argument("temps", type=int, help="informer la duree en minutes")
    parser.add_argument("nom", help="indiquer le nom du fichier de sortie")
    parser.add_argument("format", choices=['M3U', 'XSPF', 'PLS'], help=("Choisir entre le format M3U et XSPF"))

# Arguments optionnel
def argumentOptionnel():
    parser.add_argument("-g", "--genre", nargs=2, action = 'append', help="indiquer le genre")
    parser.add_argument("-a", "--artiste", nargs=2, help="indiquer l'artiste")
    parser.add_argument("-A", "--album", nargs=2, help="indiquer l'album")
    parser.add_argument("-t", "--titre", help="indiquer le titre")