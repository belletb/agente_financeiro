# Copiloto de Bem-Estar Financeiro com IA Generativa

## Contexto

No setor financeiro, os clientes não buscam apenas **investimentos** ou **alertas de gastos**: eles querem **tranquilidade e equilíbrio** entre consumo, poupança e objetivos de vida.  
Este projeto propõe um agente virtual que atua como um **copiloto de bem-estar financeiro**, capaz de:

- **Diagnosticar hábitos de consumo** com base em transações históricas  
- **Sugerir planos de equilíbrio** entre gastos essenciais, supérfluos e investimentos  
- **Gerar simulações personalizadas** (ex: “se você economizar X por mês, alcança sua meta em Y anos”)  
- **Educar o cliente** com explicações simples e consultivas, evitando jargões técnicos  
- **Garantir confiabilidade** com checagem cruzada em dados e regras anti-alucinação  

> [!TIP]  
> Este agente não substitui um consultor financeiro, mas atua como **parceiro educativo e proativo**.

---

### 1. Documentação do Agente

- **Caso de Uso:** Planejamento de bem-estar financeiro (equilíbrio entre consumo, poupança e metas).  
- **Persona e Tom de Voz:** Amigável, consultivo e educativo, como um “coach financeiro digital”.  
- **Segurança:**  
  - Respostas baseadas em dados mockados  
  - Validação de cálculos antes de sugerir metas  
  - Transparência: sempre indicar a fonte dos números  

---

### 2. Base de Conhecimento

| Arquivo | Formato | Descrição |
|---------|---------|-----------|
| `transacoes.csv` | CSV | Histórico de gastos categorizados (essenciais, supérfluos, investimentos) |
| `metas_financeiras.json` | JSON | Objetivos do cliente (ex: comprar casa, viajar, aposentadoria) |
| `perfil_cliente.json` | JSON | Perfil comportamental e preferências |
| `educacao_financeira.json` | JSON | Conteúdos educativos e dicas |

---

### 3. Prompts do Agente

- **System Prompt:**  
  “Você é um copiloto financeiro que ajuda clientes a equilibrar gastos, poupança e metas. Sempre explique de forma clara e consultiva, sem jargões técnicos.”  

- **Exemplo de Interação:**  
  - Entrada: “Quero viajar em 2 anos, mas gasto muito com restaurantes.”  
  - Saída: “Se você reduzir 20% dos gastos em restaurantes, pode economizar R$ 500/mês. Isso te permite alcançar sua meta de viagem em 24 meses.”  

- **Edge Cases:**  
  - Cliente sem metas → sugerir metas simples (ex: reserva de emergência)  
  - Cliente com dívidas → priorizar plano de quitação antes de sugerir investimentos  

---

### 4. Aplicação Funcional

- Protótipo em **Streamlit** com interface interativa  
- Conexão com base de dados mockada  
- Geração de relatórios em Excel (gráficos de gastos vs metas)  
- Integração com LLM para explicações consultivas  

---

### 5. Avaliação e Métricas

- **Precisão:** Cálculos corretos de simulação financeira  
- **Segurança:** Nenhuma recomendação sem base em dados  
- **Clareza:** Explicações compreensíveis para qualquer perfil de cliente  
- **Engajamento:** Taxa de clientes que definem metas após interação  

---

## Estrutura do Repositório

agente_financeiro/
├── data/                  # Seus arquivos de dados
│   ├── transacoes.csv
│   ├── perfil_cliente.json
│   ├── produtos_financeiros.json
│   └── educacao_financeira.json
├── src/                   # Onde o código mora 
│   ├── agente.py          # Lógica, cálculos e IA
│   └── app.py             # Interface visual (Streamlit)
├── requirements.txt       # Lista de bibliotecas para instalar
└── README.md              # Instruções de como rodar

---
