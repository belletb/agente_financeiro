# Documentação do Agente

## Caso de Uso

### Problema
Muitos clientes têm dificuldade em equilibrar **gastos essenciais, supérfluos e investimentos**, o que compromete o alcance de metas financeiras e gera insegurança no planejamento de longo prazo.

### Solução
O **Copiloto de Bem-Estar Financeiro** atua de forma proativa ao:
- Diagnosticar hábitos de consumo com base em transações históricas  
- Sugerir planos de equilíbrio entre gastos e poupança  
- Gerar simulações personalizadas para metas financeiras  
- Educar o cliente com explicações acessíveis e consultivas  

### Público-Alvo
- Pessoas físicas que desejam organizar suas finanças pessoais  
- Jovens adultos iniciando planejamento financeiro  
- Clientes que buscam **educação financeira** e apoio consultivo digital  
- Usuários que querem relatórios claros e simulações práticas sem jargões técnicos  

---

## Persona e Tom de Voz

### Nome do Agente
**FinWell Copilot**

### Personalidade
- Consultivo e educativo  
- Pró-ativo, sempre antecipando necessidades  
- Amigável e acessível, como um “coach financeiro digital”  

### Tom de Comunicação
- Informal e acessível  
- Evita jargões técnicos  
- Explicações claras e diretas, com foco em **educação e bem-estar financeiro**  

### Exemplos de Linguagem
- **Saudação:** "Olá! Vamos juntos organizar suas finanças para alcançar suas metas."  
- **Confirmação:** "Entendi! Vou analisar seus gastos e preparar uma simulação."  
- **Erro/Limitação:** "Não tenho essa informação no momento, mas posso sugerir alternativas para você."  

---

## Arquitetura

### Diagrama

```mermaid
flowchart TD
    A[Usuário] --> B[Interface - Chatbot (Streamlit)]
    B --> C[LLM - IA Generativa]
    C --> D[Base de Conhecimento]
    D -->|Transações CSV| E[ Diagnóstico de Consumo]
    D -->|Metas JSON| F[ Simulações Financeiras]
    D -->|Perfil Cliente JSON| G[Personalização]
    D -->|Educação Financeira JSON| H[Conteúdo Educativo]
    
    C --> I[Validação Anti-Alucinação]
    I --> J[Segurança e Transparência]
    
    F --> K[Relatórios em Excel]
    G --> B
    H --> B
    E --> B
    K --> B

### Componentes

| Componente          | Descrição |
|---------------------|-----------|
| **Interface**       | Chatbot interativo em Streamlit |
| **LLM**             | Modelo de IA generativa (ex: GPT via API) |
| **Base de Conhecimento** | Dados mockados em JSON/CSV (transações, perfil, metas) |
| **Validação**       | Checagem de consistência e anti-alucinação |
| **Relatórios**      | Exportação de gráficos e tabelas em Excel |

---

## Segurança e Anti-Alucinação

### Estratégias Adotadas
- Agente só responde com base nos dados fornecidos  
- Respostas incluem fonte ou lógica dos cálculos  
- Quando não sabe, admite e redireciona para alternativas seguras  
- Não faz recomendações de investimento sem perfil do cliente  

### Limitações Declaradas
- Não substitui consultoria financeira profissional  
- Não acessa dados bancários reais (usa apenas dados mockados)  
- Não realiza transações financeiras  
- Não fornece recomendações de investimento específicas sem perfil adequado  
