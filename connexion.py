import sqlalchemy

#Connexion à la base de donnée
connexion = sqlalchemy.create_engine('postgresql://login:mdp@172.16.99.2:5432/radio_libre')

metadata = sqlalchemy.MetaData()
mes_morceaux = sqlalchemy.Table('morceaux', metadata, sqlalchemy.Column('titre', sqlalchemy.String))

selection_morceaux = sqlalchemy.select([mes_morceaux])

resultat = connexion.execute(selection_morceaux)

for i in resultat:
    print(i)