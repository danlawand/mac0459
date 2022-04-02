from neo4j import GraphDatabase

url = "bolt://localhost:7687"

db = GraphDatabase.driver(url, auth=("neo4j", "1234"))

querieNumber1 = " \
    MATCH (n:ocorrencia) RETURN DISTINCT n.year AS Ano, \
    COUNT(*) AS N_Ocorrencias_Ano \
    ORDER BY N_Ocorrencias_Ano DESC \
    "
querieNumber2 = " \
    MATCH (n:ocorrencia) RETURN DISTINCT n.month AS Mes, \
    COUNT(*) AS N_Ocorrencias_Mes \
    ORDER BY N_Ocorrencias_Mes DESC \
    "
querieNumber3 = " \
    MATCH (n:ocorrencia) RETURN DISTINCT n.ocorrencia_uf AS Estado, \
    COUNT(*) AS N_Ocorrencias_Estado \
    ORDER BY N_Ocorrencias_Estado DESC \
    "

querieNumber4 = " \
    MATCH (n:ocorrencia) RETURN DISTINCT n.ocorrencia_cidade AS Cidade, \
    COUNT(*) AS N_Ocorrencias_Cidade \
    ORDER BY N_Ocorrencias_Cidade DESC \
    "
querieNumber5 = " \
    MATCH (n:ocorrencia_tipo) RETURN DISTINCT n.ocorrencia_tipo AS Tipo, \
    COUNT(*) AS N_Ocorrencias_Tipo \
    ORDER BY N_Ocorrencias_Tipo DESC \
    "

queries = [
    querieNumber1,
    querieNumber2,
    querieNumber3,
    querieNumber4,
    querieNumber5
]

questions = [
    '1.   Qual o ano com maior quantidade de ocorrências?',
    '2.   Qual o mês do ano com maior quantidade de ocorrências?',
    '3.   Qual Unidade Federativa teve o maior número de ocorrências?',
    '4.   Qual município teve o maior núemro de ocorrências?',
    '5.   Qual tipo de ocorrência é a mais frequente?'
]

with db.session() as session:
    print("______Queries______")
    for i in range(5):
        print(questions[i])
        ans = session.run(queries[i])
        for answers in ans:
            print(answers)
        print("")
db.close()
