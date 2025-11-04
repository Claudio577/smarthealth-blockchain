"""
Funções auxiliares gerais.
"""

from datetime import datetime

def timestamp_agora():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
