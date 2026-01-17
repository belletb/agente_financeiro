import pandas as pd
import json
import requests
import os

class CopilotoFinanceiro:
    def __init__(self, perfil_path, transacoes_path, produtos_path, educacao_path):
        # Carregamento dos seus dados originais
        self.perfil = self._load_json(perfil_path)
        self.transacoes = pd.read_csv(transacoes_path)
        self.produtos = self._load_json(produtos_path)
        self.educacao = self._load_json(educacao_path)
        # Configuração para o Docker falar com o Ollama
        self.ollama_url = os.getenv("OLLAMA_HOST", "http://ollama:11434")

    def _load_json(self, path):
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        return {}

    # --- Sua lógica original de cálculos ---
    def calcular_gastos_por_categoria(self):
        return self.transacoes.groupby("categoria")["valor"].sum()

    def simular_meta(self, meta):
        saldo_atual = self.perfil.get("reserva_emergencia_atual", 0)
        valor_necessario = meta.get("valor_necessario", 0)
        return max(0, valor_necessario - saldo_atual)

    # --- Integração com a IA ---
    def chat_with_ollama(self, user_input):
        gastos = self.calcular_gastos_por_categoria().to_dict()
        contexto = f"Você é o FinWell. Cliente {self.perfil.get('nome')} tem renda de R${self.perfil.get('renda_mensal')}. Gastos: {gastos}. Responda rápido."
        
        payload = {
            "model": "gemma:2b",
            "messages": [
                {"role": "system", "content": contexto},
                {"role": "user", "content": user_input}
            ],
            "stream": False
        }
        try:
            response = requests.post(f"{self.ollama_url}/api/chat", json=payload)
            return response.json()['message']['content']
        except:
            return "A IA ainda está acordando... Tente novamente em instantes!"