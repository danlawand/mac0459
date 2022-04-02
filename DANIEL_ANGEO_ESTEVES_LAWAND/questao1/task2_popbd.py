from neo4j import GraphDatabase
import pandas as pd
from datetime import datetime

url = "bolt://localhost:7687"

db = GraphDatabase.driver(url, auth=("neo4j", "1234"))

df_ocorrencias = pd.read_csv("ocorrencia.csv", sep=";")
df_ocorrencias_tipo = pd.read_csv("ocorrencia_tipo.csv", sep=";")

df_ocorrencias["year"] = pd.DatetimeIndex(df_ocorrencias["ocorrencia_dia"]).year
df_ocorrencias["month"] = pd.DatetimeIndex(df_ocorrencias["ocorrencia_dia"]).month

create_node = []

for index, row in df_ocorrencias.iterrows():
    comandos = f'CREATE (item: ocorrencia) SET item.year = "{row["year"]}", \
        item.month = "{row["month"]}", item.ocorrencia_uf = "{row["ocorrencia_uf"]}", \
            item.ocorrencia_cidade = "{row["ocorrencia_cidade"]}"'
    create_node.append(comandos)

for index, row in df_ocorrencias_tipo.iterrows():
    comandos = f'CREATE (item: ocorrencia_tipo) SET item.ocorrencia_tipo = "{row["ocorrencia_tipo"]}"'
    create_node.append(comandos)

with db.session() as session:
    print("Adicionando nodes...")
    for cmd in create_node:
        session.run(cmd)
    print("Terminado")
    print("")
db.close()
