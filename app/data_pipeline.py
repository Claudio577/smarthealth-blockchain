# NO ARQUIVO app/data_pipeline.py

import pandas as pd
import streamlit as st
import os 
import numpy as np

# NOVAS IMPORTAÇÕES NECESSÁRIAS:
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split # Esta é opcional se não for usada, mas se estiver lá, precisa ser importada.
import joblib 



# --- TREINAMENTO DO MODELO (NOVO) ---
@st.cache_resource # Use cache_resource para o modelo
def treinar_modelo_fraude(df):
    
    st.info("Treinando o Modelo de Regressão Logística...")
    
    # 1. Separar features (X) e target (y)
    X = df.drop('Class', axis=1)
    y = df['Class']
    
    # 2. Normalizar as features (crucial para Regressão Logística)
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # 3. Treinar o modelo
    # Devido ao desbalanceamento, podemos usar o parâmetro class_weight='balanced'
    model = LogisticRegression(solver='liblinear', class_weight='balanced', random_state=42)
    model.fit(X_scaled, y)
    
    st.success("Modelo de Regressão Logística treinado com sucesso!")
    return model, scaler


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
