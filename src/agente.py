import pandas as pd
import json
import requests
import os

OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://localhost:55000")

class CopilotoFinanceiro:
    def __init__(self, perfil_path, transacoes_path, produtos_path, educacao_path):
        # Carregar dados mockados
        self.perfil = self._load_json(perfil_path)
        self.transacoes = pd.read_csv(transacoes_path)
        self.produtos = self._load_json(produtos_path)
        self.educacao = self._load_json(educacao_path)

    def _load_json(self, path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    def calcular_gastos_por_categoria(self):
        return self.transacoes.groupby("categoria")["valor"].sum()

    def simular_meta(self, meta):
        saldo_atual = self.perfil["reserva_emergencia_atual"]
        valor_necessario = meta["valor_necessario"]
        falta = valor_necessario - saldo_atual
        return falta

    def recomendar_produtos(self):
        perfil = self.perfil["perfil_financeiro"]
        if perfil == "moderado":
            return [p for p in self.produtos if p["risco"] in ["baixo", "medio"]]
        elif perfil == "conservador":
            return [p for p in self.produtos if p["risco"] == "baixo"]
        else:
            return [p for p in self.produtos if p["risco"] in ["medio", "alto"]]

    def dicas_educativas(self, n=3):
        return self.educacao[:n]

    def chat_with_ollama(self, user_input):
        payload = {
            "model": "gemma:2b",   
            "messages": [
                {"role": "system", "content": "Você é um copiloto financeiro consultivo e educativo."},
                {"role": "user", "content": user_input}
            ]
        }
        response = requests.post(f"{OLLAMA_HOST}/api/chat", json=payload, stream=True)

        content = ""
        for line in response.iter_lines():
            if line:
                try:
                    data = json.loads(line.decode("utf-8"))
                    if "message" in data and "content" in data["message"]:
                        content += data["message"]["content"]
                    elif "error" in data:
                        return f"Erro do Ollama: {data['error']}"
                except Exception:
                    continue

        return content if content else "Não houve resposta do modelo."
