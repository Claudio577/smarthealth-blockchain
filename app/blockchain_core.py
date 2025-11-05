"""
Módulo base do Blockchain PoA adaptado para dados de Transações Financeiras.
"""

import hashlib
import pandas as pd
from datetime import datetime

def gerar_hash(conteudo, hash_anterior):
    """Gera o hash SHA256 do conteúdo, encadeado com o hash anterior."""
    return hashlib.sha256((conteudo + hash_anterior).encode()).hexdigest()

def criar_blockchain_inicial(df_eventos):
    """
    Cria a blockchain a partir de um DataFrame de eventos de transação.
    
    O Conteúdo do Bloco é baseado em: Time, Amount, V1 e Class.
    """
    # Verifica se as colunas necessárias estão presentes
    colunas_necessarias = ['Time', 'Amount', 'V1', 'Class']
    if not all(col in df_eventos.columns for col in colunas_necessarias):
        print(f"Erro: O DataFrame não contém todas as colunas necessárias para o blockchain: {colunas_necessarias}")
        return pd.DataFrame()


    blockchain = []
    hash_anterior = "0" * 64
    for _, linha in df_eventos.iterrows():
        
        # --- CONTEÚDO DO BLOCO ADAPTADO ---
        # Usando os novos dados: Time, Amount, V1, e Class
        conteudo = f"{linha['Time']}-{linha['Amount']}-{linha['V1']}-{linha['Class']}"
        
        hash_atual = gerar_hash(conteudo, hash_anterior)
        
        blockchain.append({
            "Time": linha['Time'],
            "Amount": linha['Amount'],
            "V1_Feature": linha['V1'],  # Renomeado para evitar confusão se for exibido
            "Class_Fraude": linha['Class'], # Renomeado para exibição
            "hash_anterior": hash_anterior,
            "hash_atual": hash_atual
        })
        hash_anterior = hash_atual
        
    return pd.DataFrame(blockchain)
