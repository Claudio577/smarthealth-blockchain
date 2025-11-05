import pandas as pd
import os
import streamlit as st # <<<< NOVO: Importamos 'st' para usar st.error()

# Removida a importação e uso da KaggleApi

def carregar_dados():
    """
    Carrega e trata o dataset do arquivo CSV local (brazil_covid19_sample.csv).
    Assume que o CSV está no diretório raiz do projeto (um nível acima da pasta 'app').
    """
    
    # Usando o método mais robusto para definir o caminho
    caminho_csv = os.path.join(os.path.dirname(__file__), '..', 'brazil_covid19_sample.csv') 
    
    try:
        df = pd.read_csv(caminho_csv)
        
        # --- TRATAMENTO DE DADOS (Baseado no seu código original) ---
        # Mantendo as colunas originais para o agrupamento
        
        df_estado = df.groupby(['date', 'state'])[['newCases', 'deaths']].sum().reset_index()
        
        df_estado.rename(columns={
            'date': 'data',
            'state': 'estado',
            'newCases': 'novos_casos',
            'deaths': 'obitos'
        }, inplace=True)
        
        return df_estado

    except FileNotFoundError:
        # Usamos st.error() agora que 'st' está importado!
        st.error(f"ERRO: Arquivo CSV não encontrado em '{os.path.abspath(caminho_csv)}'. Certifique-se de que 'brazil_covid19_sample.csv' está no diretório raiz do projeto.")
        return pd.DataFrame()
    except KeyError as e:
        # Captura de erro para colunas ausentes
        st.error(f"ERRO no tratamento dos dados: Coluna esperada não encontrada no CSV. Coluna faltando: {e}. Verifique se 'brazil_covid19_sample.csv' tem as colunas 'date', 'state', 'newCases' e 'deaths'.")
        return pd.DataFrame()
