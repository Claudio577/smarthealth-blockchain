import pandas as pd
import streamlit as st
import os

# --- CARREGAMENTO DE DADOS ---
@st.cache_data
def carregar_dados():
    """
    Carrega o dataset de fraude de cartão de crédito diretamente da URL.
    O tratamento de dados anterior foi removido, pois este CSV tem colunas diferentes.
    """
    url = "https://storage.googleapis.com/download.tensorflow.org/data/creditcard.csv"
    
    try:
        df = pd.read_csv(url)
        return df
    
    except Exception as e:
        st.error(f"ERRO ao carregar o dataset da URL: {e}")
        return pd.DataFrame()
    

# A função 'carregar_dados' agora retorna o DataFrame original.
# Se você precisar de um DataFrame agrupado para a blockchain, 
# o tratamento deve ser feito no 'dashboard.py' ou em uma nova função.
