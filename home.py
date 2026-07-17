import pandas as pd
import streamlit as st

from joblib import load

from notebooks.src.config import DADOS_TRATADOS, MODELO_FINAL

@st.cache_data
def carregar_dados():
    return pd.read_parquet(DADOS_TRATADOS)

@st.cache_resource
def carregar_modelo():
    return load(MODELO_FINAL)

df = carregar_dados()
modelo = carregar_modelo()

# dicionarios atribuidos aos níveis
niveis_educacionais_texto = {
    1: "Below College",
    2: "College",
    3: "Bachelor",
    4: "Master",
    5: "PhD",
}

niveis_satisfacao_texto = {
    1: "Low",
    2: "Medium",
    3: "High",
    4: "Very High",
}

niveis_vida_trabalho_texto = {
    1: "Bad",
    2: "Good",
    3: "Better",
    4: "Best",
}

niveis_envolvimento_trabalho_texto = {
    1: "Low",
    2: "Medium",
    3: "High",
    4: "Very High",
}


# dicionario exibindo ao usuário apenas uma nomeclatura padrão ao widgted viagem_negocios
viagem_negocios_texto_formatado = {
    "Non-Travel": "Non Travel",
    "Travel_Frequently": "Travel Frequently",
    "Travel_Rarely": "Travel Rarely",
}

# variaveis das colunas que dão sentido a texto.
generos = sorted(df["Gender"].unique())
niveis_educacionais = sorted(df["Education"].unique())
area_foramacao = sorted(df["EducationField"].unique())
departamentos = sorted(df["Department"].unique())
viagem_negocios = sorted(df["BusinessTravel"].unique())
hora_extra = sorted(df["OverTime"].unique())
satisfacao_trabalho = sorted(df["JobSatisfaction"].unique())
satisfacao_colegas = sorted(df["RelationshipSatisfaction"].unique())
satisfacao_ambiente = sorted(df["EnvironmentSatisfaction"].unique())
vida_trabalho = sorted(df["WorkLifeBalance"].unique())
opcao_acoes = sorted(df["StockOptionLevel"].unique())
envolvimento_trabalho = sorted(df["JobInvolvement"].unique())
marital_stats = sorted(df["MaritalStatus"].unique())

# colunas que irão utilizar os sliders
colunas_slider = [
    "DistanceFromHome",
    "MonthlyIncome",
    "NumCompaniesWorked",
    "PercentSalaryHike",
    "TotalWorkingYears",
    "TrainingTimesLastYear",
    "YearsAtCompany",
    "YearsInCurrentRole",
    "YearsSinceLastPromotion",
    "YearsWithCurrManager",
    
]

# colunas que terão min e max para os sliders
colunas_slider_min_max = {
    coluna: {"min_value": df[coluna].min(), "max_value": df[coluna].max()}
    for coluna in colunas_slider
}

# colunas a serem ignoradas, que irão ficar apenas em background
colunas_ignoradas = (
    "Age",
    "DailyRate",
    "JobLevel",
    "HourlyRate",
    "MonthlyRate",
    "PerformanceRating",
) 

medianas_colunas_ignoradas = {
    coluna: df[coluna].median() for coluna in colunas_ignoradas
}

st.title("Previsão de Atrito")

# container das informações pessoais
with st.container(border=True):
    st.write("### Informações pessoais")

    widget_marital_status = st.selectbox(
        "Estado civil",
        marital_stats, 
        index=None
    )
    
    widget_genero = st.selectbox(
        "Selecione o gênero", 
        generos, 
        index=None
    )

    widget_nivel_ensino = st.selectbox(
        "Nível educacional", 
        niveis_educacionais, 
        format_func=lambda numero: niveis_educacionais_texto[numero], 
        index=None
    )

    widget_area_formacao = st.selectbox(
        "Área de formação", 
        area_foramacao, 
        index=None
    )
    
    widget_distancia_casa = st.slider(
        "Distância de casa em milhas", 
        **colunas_slider_min_max["DistanceFromHome"]
    )

# container da rotinas da empresa junto com colunas para organizar o conteúdo
with st.container(border=True):
    st.write("### Rotinas na empresa")

    coluna_esquerda, coluna_direita = st.columns(2)

    with coluna_esquerda:
        
        widget_departamento = st.selectbox(
            "Departamento", 
            departamentos, 
            index=None
        )
        
        widget_viagem_negocios = st.selectbox(
            "Viagem a negócios", 
            viagem_negocios, 
            format_func=lambda texto_formatado: viagem_negocios_texto_formatado[texto_formatado], 
            index=None
        )

    with coluna_direita:
        
        widget_cargo = st.selectbox(
            "Cargo", 
            sorted(df[df["Department"] == widget_departamento]["JobRole"].unique()), 
            index=None
        )
        
        widget_hora_extra = st.radio(
            "Possui horas extras?",
            hora_extra, 
            index=None
        ) 
        
    widget_salario = st.slider("Salário mensal", **colunas_slider_min_max["MonthlyIncome"])
    
# container da experiencia profissional
with st.container(border=True):
    st.write("### Experiência profissional")

    coluna_esquerda_prof, coluna_direita_prof = st.columns(2)

    with coluna_esquerda_prof:
        
        widget_empresas_trabalhadas = st.slider(
            "Empresas trabalhadas", 
            **colunas_slider_min_max["NumCompaniesWorked"]
        )
        
        widget_anos_trabalhados = st.slider(
            "Total de anos trabalhados", 
            **colunas_slider_min_max["TotalWorkingYears"]
        )
        
        widget_anos_trabalhados_empresa_atual = st.slider(
            "Total de anos trabalhados na empresa atual", 
            **colunas_slider_min_max["YearsAtCompany"]
        )

    with coluna_direita_prof:
        
        widget_anos_cargo_atual = st.slider(
            "Anos no cargo atual", 
            **colunas_slider_min_max["YearsInCurrentRole"]
        )
        
        widget_anos_mesmo_gerente = st.slider(
            "Anos com o mesmo gerente", 
            **colunas_slider_min_max["YearsWithCurrManager"]
        )
        
        widget_anos_ultima_promocao = st.slider(
            "Anos desde a última promoção", 
            **colunas_slider_min_max["YearsSinceLastPromotion"]
        )
        
# cotainer de incentivos e métricas
with st.container(border=True):
    st.write("### Incentivos e métricas")
    
    coluna_esquerda_metricas, coluna_direita_metricas = st.columns(2)

    with coluna_esquerda_metricas:
        
        widget_satisfacao_trabalho = st.selectbox(
            "Satisfação no trabalho", 
            satisfacao_trabalho, 
            format_func=lambda numero: niveis_satisfacao_texto[numero], 
            index=None
        )
        
        widget_satisfacao_colegas = st.selectbox(
            "Satisfação com colegas", 
            satisfacao_colegas, 
            format_func=lambda numero: niveis_satisfacao_texto[numero], 
            index=None
        )
        
        widget_envolvimento_trabalho = st.selectbox(
            "Envolvimento no trabalho", 
            envolvimento_trabalho, 
            format_func=lambda numero: niveis_envolvimento_trabalho_texto[numero], 
            index=None
        )
        
    with coluna_direita_metricas:
        
        widget_satisfacao_ambiente = st.selectbox(
            "Satisfação com o ambiente", 
            satisfacao_ambiente, 
            format_func=lambda numero: niveis_satisfacao_texto[numero], 
            index=None
        )
        
        widget_balanco_vida_trabalho = st.selectbox(
            "Balanço vida-trabalho", 
            vida_trabalho, 
            format_func=lambda numero: niveis_vida_trabalho_texto[numero], 
            index=None
        )
        
        widget_opcao_acoes = st.radio(
            "Opção de ações", 
            opcao_acoes, 
            index=None
        )

    widget_aumento_salarial = st.slider(
        "Aumento salarial (%)",
        **colunas_slider_min_max["PercentSalaryHike"]
    )

    widget_treinamentos_ano = st.slider(
        "Treinamentos no último ano",
        **colunas_slider_min_max["TrainingTimesLastYear"]
    )

# entradas do modelo
entrada_modelo = {
    "Age": medianas_colunas_ignoradas["Age"],
    "BusinessTravel": widget_viagem_negocios,
    "DailyRate": medianas_colunas_ignoradas["DailyRate"],
    "Department": widget_departamento, 
    "DistanceFromHome": widget_distancia_casa,
    "Education": widget_nivel_ensino,
    "EducationField": widget_area_formacao,
    "EnvironmentSatisfaction": widget_satisfacao_trabalho,
    "Gender": widget_genero,
    "HourlyRate": medianas_colunas_ignoradas["HourlyRate"],
    "JobInvolvement": widget_envolvimento_trabalho, 
    "JobLevel": medianas_colunas_ignoradas["JobLevel"],
    "JobRole": widget_cargo,
    "JobSatisfaction": widget_satisfacao_trabalho,
    "MaritalStatus": widget_marital_status,
    "MonthlyIncome": widget_salario,
    "MonthlyRate": medianas_colunas_ignoradas["MonthlyRate"],
    "NumCompaniesWorked": widget_empresas_trabalhadas,
    "OverTime": widget_hora_extra,
    "PercentSalaryHike": widget_aumento_salarial,
    "PerformanceRating": medianas_colunas_ignoradas["PerformanceRating"],
    "RelationshipSatisfaction": widget_satisfacao_colegas,
    "StockOptionLevel": widget_opcao_acoes,
    "TotalWorkingYears": widget_anos_trabalhados,
    "TrainingTimesLastYear": widget_treinamentos_ano,
    "WorkLifeBalance": widget_balanco_vida_trabalho,
    "YearsAtCompany": widget_anos_trabalhados_empresa_atual,
    "YearsInCurrentRole": widget_anos_trabalhados_empresa_atual,
    "YearsSinceLastPromotion": widget_anos_ultima_promocao,
    "YearsWithCurrManager": widget_anos_mesmo_gerente,    
}

df_entrada_modelo = pd.DataFrame([entrada_modelo])

# btn de enviar as informações
btn_previsao = st.button("Prever Atrito")

if btn_previsao:
    previsao = modelo.predict(df_entrada_modelo)[0]
    probabilidade_atrito = modelo.predict_proba(df_entrada_modelo)[0][1]

    cor = ":red" if previsao == 1 else ":green"

    texto_probabilidade = (
        f"#### Probabilidade de Atrito {cor}[{probabilidade_atrito:.0%}]"
    )

    texto_atrito = f"#### Atrito: {cor}[{'Sim' if previsao == 1 else "Não"}]"

    st.markdown(texto_atrito)
    st.markdown(texto_probabilidade)