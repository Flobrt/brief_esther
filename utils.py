from sqlalchemy import create_engine, text, Table, Column, Integer,Float, String, MetaData
import pandas as pd

# <============================== PARTIE SQLALCHEMY ==============================>

# Connexion à la base de données
def connexion_csv(user, password, host, port, database):
    try:
        engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}:{port}")
        conn = engine.connect()

        conn.execute(text(f"CREATE DATABASE IF NOT EXISTS {database}"))
        print(f"Database {database} created")
        engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}")
        conn = engine.connect()
    
        return conn, engine
    except Exception as e:
        print(e)
        return None, None
    

# création de la table
def infer_sqlalchemy_type(dtype):
    # Map des types de données 
    if "int" in dtype.name:
        return Integer
    elif "float" in dtype.name:
        return Float
    elif "object" in dtype.name:
        return String(255)
    else:
        return String(255)
    

# Create table 
def create_table(df, engine, table_name):
    metadata = MetaData()
    columns = [Column(name, infer_sqlalchemy_type(dtype)) for name, dtype in df.dtypes.items()]
    table = Table(table_name, metadata, *columns)

    table.create(engine)


# Connexion à la base de données
def insert_data(df, engine, table_name):
    # Insertion des données dans la table clients
    try:
        df.to_sql(table_name, con=engine, if_exists='replace', index=False)
        print("Data inserted")
    except Exception as e:
        print(e)
        print("Data not inserted")
        exit()


# Excuter une requête SQL
def requete(engine, rqt):
    try:
        result = engine.execute(text(rqt))
        # Transformer le résultat en liste de dictionnaires (pour pandas)
        data = result.fetchall()
        # Récupérer les noms des colonnes
        columns = result.keys()
        # Créer un DataFrame pandas
        df = pd.DataFrame(data, columns=columns)
        return df
    
    except Exception as e:
        print("Requête non exécutée.")
        print(e)
        return None
    

# <============================== PARTIE MONGODB ==============================>

# Faire une rquete sur la base de données MongoDB
def requete_mongo(collection, rqt):
    try:
        result = collection.find(rqt)
        return list(result)
    except Exception as e:
        print("Requête non exécutée.")
        print(e)
        return None