from pymongo import MongoClient

from utils import *

choix = "0"

while choix != "Q" or choix != "q":
    print("Sur quel type de base de données voulez-vous travailler ?")
    print("1. MySQL")
    print("2. MongoDB")
    print("Q. Quitter")
    choix = input("Votre choix : ")

    if choix != "1" and choix != "2" and choix != "Q" and choix != "q":
        print("Mauvais choix !")


    elif choix == "1":
        while choix != "Q" and choix != "q":
            # Choisissez votre base de données 
            print("Sur quel type de base de données MySQL voulez-vous travailler ?")
            print("1. CSV")
            print("2. JSON")
            print("Q. Quitter")
            choix = input("Votre choix : ")

            username = "root"
            password = "password"
            host = "127.0.0.1"
            port = "40000"

            if choix != "1" and choix != "2" and choix != "Q":
                print("Mauvais choix !")

            elif choix == "1":
                database = "brief2_csv"   

                try:
                    # connexion à la db mysql
                    conn, engine = connexion_csv(username, password, host, port, database)
                
                except Exception as e:
                    print(e)
                    print("Connexion failed")
                    exit()
                
                # Requetes SQL 
                print("Quelle requête SQL voulez-vous exécuter ?")
                rqt = input("Votre requête : ")

                try: 
                    print("============== RESULT ==============")
                    print(requete(engine, rqt))
                    print("===================================")
                except Exception as e:
                    print(e)
                    print("Requête non exécutée")
                    exit()

            elif choix == "2":
                database = "brief2_json"   

                try:
                    # connexion à la db mysql
                    conn, engine = connexion_csv(username, password, host, port, database)
                
                except Exception as e:
                    print(e)
                    print("Connexion failed")
                    exit()
                
                # Requetes SQL 
                print("Quelle requête SQL voulez-vous exécuter ?")
                rqt = input("Votre requête : ")

                try: 
                    print("============== RESULT ==============")
                    print(requete(engine, rqt))
                    print("===================================")
                except Exception as e:
                    print(e)
                    print("Requête non exécutée")
                    exit()

        
    elif choix == "2":
        while choix != "Q" and choix != "q":
            # Choisissez votre base de données 
            print(" Nouvelles requetes ?")
            print("1. Yeaaaaaah")
            print("Q. Quitter")
            choix = input("Votre choix : ")

            if choix != "1" and choix != "Q":
                print("Mauvais choix !")
            
            elif choix == "1":
                client = MongoClient("mongodb://root:password@localhost:27017")
                # Select the database
                db = client['entreprise']

                # Rentrer votre requête
                print("Quelle requête voulez-vous exécuter ?")
                rqt = input("Votre requête : ")

                try: 
                    print("============== RESULT ==============")
                    print(requete_mongo(db, rqt))
                    print("===================================")

                except Exception as e:
                    print(e)
                    print("Requête non exécutée")
                    exit()

try:
    conn.close()
except:
    pass

print("Done!")