from sqlalchemy import create_engine, text, Table, Column, Integer,Float, String, MetaData
import pandas as pd


username = "root"
password = "password"
host =  "127.0.0.1" 
port = "40000"
database_csv = "brief2_csv"
database_json = "brief2_json"


# connexion à la db mysql
def connexion(user, password, host, port, database):
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
    """ Map pandas dtype to SQLAlchemy's types """
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


############################
# Gestion des fichiers CSV #
############################

try:
    # Connexion à la base de données mariadb et création de la base de données brief2
    conn, engine = connexion(username, password, host, port, database_csv)
    print("Connexion success")
except Exception as e:
    print(e)
    print("Connexion failed")
    exit()

try:
    # Ouverture des fichiers
    df_client = pd.read_csv("data/data-csv/data-csv/clients.csv", sep=";")
    df_client.drop_duplicates(inplace=True)
    df_product = pd.read_csv("data/data-csv/data-csv/produits_sous-categorie.csv", sep=";")
    df_product.drop_duplicates(inplace=True)
    df_vente = pd.read_csv("data/data-csv/data-csv/ventes.csv", sep=";")
    df_vente.drop_duplicates(inplace=True)
    print("Files CSV opened")
except Exception as e:
    print(e)
    print("Files CSV not opened")
    exit()

# Création des listes de dataframes et de noms
df_list = [df_client, df_product, df_vente]
df_name = ["clients", "produits", "ventes"]

# Création des tables
for df, df_name in zip(df_list, df_name):
    # Si la table n'existe pas 
    if not engine.dialect.has_table(conn, df_name):
        create_table(df, engine, df_name)
        print(f"Table {df_name} created")
    else:
        print(f"Table {df_name} already exists")

    # Insertions des données dans les tables
    insert_data(df, engine, df_name)



###############################
# Ouverture des fichiers JSON #
###############################

try:
    # Connexion à la base de données mariadb et création de la base de données brief2
    conn, engine = connexion(username, password, host, port, database_json)
    print("Connexion success")
except Exception as e:
    print(e)
    print("Connexion failed")
    exit()

try:
    # Ouverture des fichiers
    df_client = pd.read_json("data/data-json/data-json/clients.json")
    df_client.drop_duplicates(inplace=True)
    df_product = pd.read_json("data/data-json/data-json/produits_sous-categorie.json")
    df_product.drop_duplicates(inplace=True)
    df_vente = pd.read_json("data/data-json/data-json/ventes.json")
    df_vente.drop_duplicates(inplace=True)
    print("Files JSON opened")
except Exception as e:
    print(e)
    print("Files JSON not opened")
    exit()

# Création des listes de dataframes et de noms
df_list = [df_client, df_product, df_vente]
df_name = ["clients", "produits", "ventes"]

# Création des tables
for df, df_name in zip(df_list, df_name):
    # Si la table n'existe pas 
    if not engine.dialect.has_table(conn, df_name):
        create_table(df, engine, df_name)
        print(f"Table {df_name} created")
    else:
        print(f"Table {df_name} already exists")

    # Insertions des données dans les tables
    insert_data(df, engine, df_name)

# Fermeture de la connexion
conn.close()
print("Done!")