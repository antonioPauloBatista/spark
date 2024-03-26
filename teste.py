from pyspark.sql import SparkSession

# Substitua 'SEU_IP_AQUI' pelo endereço IP do servidor Spark
# Substitua 'SUA_PORTA_AQUI' pela porta desejada (por exemplo, 7077)
spark = SparkSession.builder \
    .master('spark://127.0.0.1:4041') \
    .appName('test') \
    .getOrCreate()

# Exemplo de leitura de um arquivo CSV
df = spark.read.csv('caminho/do/arquivo.csv', header=True, inferSchema=True)

# Exibindo algumas linhas do DataFrame
df.show()

# Encerrando a sessão Spark
spark.stop()




