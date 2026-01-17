# Copiloto de Bem-Estar Financeiro com IA Generativa

<div align="center">

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

Um agente virtual inteligente que atua como seu parceiro pessoal de educação financeira, ajudando você a equilibrar gastos, poupança e alcançar suas metas de vida.

</div>

## Sobre o Projeto

No setor financeiro moderno, os clientes buscam mais do que simples alertas de gastos ou recomendações de investimentos. Eles precisam de **tranquilidade e equilíbrio** entre consumo, poupança e objetivos de vida.

Este projeto oferece um **copiloto de bem-estar financeiro** baseado em IA Generativa, capaz de:

- **Diagnosticar** hábitos de consumo com base em transações históricas
- **Sugerir** planos personalizados de equilíbrio financeiro
- **Simular** cenários futuros ("Se economizar X, alcança meta Y em Z meses")
- **Educar** com linguagem simples e consultiva
- **Garantir** confiabilidade com validação de dados e anti-alucinação

> **💡 Importante:** Este agente não substitui um consultor financeiro certificado, mas atua como um parceiro educativo e proativo para melhorar sua saúde financeira.

---

## ✨ Principais Funcionalidades

### Diagnóstico Inteligente
- Análise automática de padrões de gastos
- Categorização de despesas (essenciais, supérfluas, investimentos)
- Identificação de oportunidades de economia

### Planejamento Personalizado
- Criação de planos de equilíbrio financeiro
- Simulações de cenários futuros
- Ajuste de metas conforme perfil do usuário

### Educação Financeira
- Explicações claras sem jargões técnicos
- Conteúdos educativos contextualizados
- Dicas práticas baseadas em comportamento

### Visualização de Dados
- Gráficos interativos de gastos vs. metas
- Relatórios em Excel exportáveis
- Dashboard intuitivo no Streamlit

### Segurança e Confiabilidade
- Validação de cálculos antes de recomendações
- Transparência nas fontes de dados
- Proteção contra alucinações da IA

---

## Tecnologias

- **Python 3.9+** - Linguagem principal
- **Streamlit** - Interface web interativa
- **LangChain** - Framework para LLM
- **OpenAI/Anthropic** - Modelos de linguagem
- **Pandas** - Manipulação de dados
- **Plotly** - Visualizações interativas
- **Docker** - Containerização
- **Poetry/pip** - Gerenciamento de dependências

---

## Instalação

### Pré-requisitos

- Python 3.9 ou superior
- Docker (opcional)

### Instalação Local

```bash
# Clone o repositório
git clone https://github.com/belletb/agente_financeiro.git
cd agente_financeiro

# Crie um ambiente virtual
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate

# Instale as dependências
pip install -r requirements.txt

# Configure as variáveis de ambiente
cp .env.example .env
# Edite o arquivo .env com suas credenciais
```

### Instalação com Docker

```bash
# Clone o repositório
git clone https://github.com/belletb/agente_financeiro.git
cd agente_financeiro

# Execute com docker-compose
docker-compose up -d
```

---

## Como Usar

### Iniciando a Aplicação

```bash
# Modo local
streamlit run src/app.py

# Com Docker
docker-compose up
```

Acesse a aplicação em: `http://localhost:8501`

### Configuração Inicial

1. **Configure suas credenciais** no arquivo `.env`
2. **Importe seus dados** (CSV de transações)
3. **Defina suas metas** financeiras
4. **Inicie a conversa** com o agente

---

## Arquitetura

```
agente_financeiro/
├── src/
│   ├── app.py                 # Aplicação Streamlit principal
│   ├── agent/
│   │   ├── __init__.py
│   │   ├── prompt.py          # System prompts e templates
│   │   ├── llm_client.py      # Cliente LLM
│   │   └── validator.py       # Validações e anti-alucinação
│   ├── data/
│   │   ├── loader.py          # Carregamento de dados
│   │   └── processor.py       # Processamento de transações
│   └── utils/
│       ├── calculations.py    # Cálculos financeiros
│       └── visualizations.py  # Gráficos e relatórios
├── docs/
│   ├── architecture.md        # Documentação da arquitetura
│   └── prompts.md            # Documentação de prompts
├── assets/
│   └── data/
│       ├── transacoes.csv    # Dados mockados de transações
│       ├── metas_financeiras.json
│       ├── perfil_cliente.json
│       └── educacao_financeira.json
├── tests/
│   ├── test_agent.py
│   └── test_calculations.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## 📚 Documentação

### Base de Conhecimento

| Arquivo | Formato | Descrição |
|---------|---------|-----------|
| `transacoes.csv` | CSV | Histórico de gastos categorizados |
| `metas_financeiras.json` | JSON | Objetivos do cliente |
| `perfil_cliente.json` | JSON | Perfil comportamental |
| `educacao_financeira.json` | JSON | Conteúdos educativos |

### Prompts do Agente

**System Prompt:**
```
Você é um copiloto financeiro que ajuda clientes a equilibrar gastos, 
poupança e metas. Sempre explique de forma clara e consultiva, sem 
jargões técnicos. Base suas respostas em dados validados e seja 
transparente sobre as fontes.
```

### Edge Cases Tratados

- ✅ Cliente sem metas definidas → Sugestão de metas básicas
- ✅ Cliente com dívidas → Priorização de quitação
- ✅ Dados incompletos → Solicitação educativa de informações
- ✅ Metas irrealistas → Ajuste consultivo com simulações

---

## 💬 Exemplos de Uso

### Exemplo 1: Planejamento de Viagem

**Usuário:** "Quero viajar para a Europa em 2 anos, mas gasto muito com delivery."

**Agente:**
```
Analisando seus gastos dos últimos 6 meses, identifiquei:
- Gasto médio mensal com delivery: R$ 850
- Reduzindo 30% (R$ 255/mês), você economiza R$ 6.120 em 24 meses

Para sua viagem à Europa (estimativa: R$ 15.000):
✓ Com essa economia: 40% do valor
✓ Investindo em CDB (8% a.a.): ~R$ 6.500 em 2 anos
✓ Faltaria economizar: R$ 350/mês adicionais

💡 Sugestão: Que tal cozinhar em casa 2x por semana? Isso pode 
gerar a economia necessária sem comprometer seu lazer!
```

### Exemplo 2: Reserva de Emergência

**Usuário:** "Não tenho reserva de emergência. Por onde começar?"

**Agente:**
```
Ótimo que você está pensando nisso! Vamos começar simples:

Seu perfil:
- Renda mensal: R$ 5.000
- Gastos essenciais: R$ 3.500
- Meta recomendada: 6 meses de despesas = R$ 21.000

Plano de ação:
1. Mês 1-3: Economize R$ 300/mês (ajustes pequenos)
2. Mês 4-6: Aumente para R$ 500/mês (com o hábito criado)
3. Depois: R$ 700/mês até completar a reserva

Em 30 meses você terá sua reserva completa. E o melhor: 
investindo em Tesouro Selic, pode chegar em ~24 meses!

Quer que eu sugira onde reduzir esses R$ 300 iniciais?
```

---

## 📊 Avaliação e Métricas

### Métricas de Qualidade

- **Precisão de Cálculos:** 100% (validação automática)
- **Segurança:** 0 recomendações sem base em dados
- **Clareza:** Linguagem acessível (Flesch-Kincaid Grade ≤ 8)
- **Engajamento:** Taxa de definição de metas pós-interação

### KPIs do Agente

- Taxa de conclusão de onboarding
- Número médio de interações por sessão
- Satisfação do usuário (NPS)
- Taxa de adoção de sugestões

---

## Contribuindo

Contribuições são muito bem-vindas! Para contribuir:

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/MinhaFeature`)
3. Commit suas mudanças (`git commit -m 'Adiciona MinhaFeature'`)
4. Push para a branch (`git push origin feature/MinhaFeature`)
5. Abra um Pull Request

### Diretrizes

- Siga o PEP 8 para código Python
- Adicione testes para novas funcionalidades
- Atualize a documentação quando necessário
- Mantenha commits claros e descritivos

---

<div align="center">

</div>
