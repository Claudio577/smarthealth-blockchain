import pandas as pd
import os
import streamlit as st 

def carregar_dados():
    """
    Carrega e trata o dataset do arquivo CSV local (brazil_covid19_sample.csv),
    usando os nomes de colunas corretos (date, state, cases, deaths).
    """
    
    # Caminho ajustado para rodar no Streamlit Cloud
    caminho_csv = os.path.join(os.path.dirname(__file__), '..', 'brazil_covid19_sample.csv') 
    
    try:
        df = pd.read_csv(caminho_csv)
        
        # --- TRATAMENTO DE DADOS CORRIGIDO ---
        # Usamos os nomes de colunas reais: 'cases' e 'deaths'
        
        df_estado = df.groupby(['date', 'state'])[['cases', 'deaths']].sum().reset_index()
        
        df_estado.rename(columns={
            'date': 'data',
            'state': 'estado',
            # Corrigimos o mapeamento de 'cases' para 'novos_casos'
            'cases': 'novos_casos',
            'deaths': 'obitos'
        }, inplace=True)
        
        return df_estado

    except Exception as e:
        # Capturamos qualquer erro que possa surgir e exibimos no Streamlit
        st.error(f"ERRO FATAL no carregamento/tratamento dos dados: {e}. Verifique o caminho e os nomes das colunas.")
        return pd.DataFrame()
