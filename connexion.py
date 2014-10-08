import sqlalchemy
import loginMdpBdd as logBDD

# Connexion à la BDD
connexion = sqlalchemy.create_engine('postgresql://'+logBDD.loginBdd+':'+logBDD.mdpBdd+'@172.16.99.2:5432/radio_libre')


metadata = sqlalchemy.MetaData()

# Redéfinition de la table morceux
mes_morceaux = sqlalchemy.Table('morceaux', metadata, sqlalchemy.Column('titre', sqlalchemy.String))

# Requête de selection en BDD
selection_morceaux = sqlalchemy.select([mes_morceaux])

# On stock le resultat de la requête dans une variable
resultat = connexion.execute(selection_morceaux)

# On affiche les résultats de la requête
for i in resultat:
    print(i)