from pathlib import Path


PASTA_PROJETO = Path(__file__).resolve().parents[2]

PASTA_DADOS = PASTA_PROJETO / "dados"

# abaixo o caminho para os arquivos de dados do projeto
DADOS_ORIGINAIS = PASTA_DADOS / "employee_attrition.csv"
DADOS_TRATADOS = PASTA_DADOS / "employee_attrition.parquet"

# abaixo o caminho para os arquivos de modelos do projeto
PASTA_MODELOS = PASTA_PROJETO / "modelos"
MODELO_FINAL = PASTA_MODELOS / "logistic_regression_rus.joblib"

# abaixo o caminho para as pastas relatorios e imagens
PASTA_RELATORIOS = PASTA_PROJETO / "relatorios"
PASTA_IMAGENS = PASTA_RELATORIOS / "imagens"