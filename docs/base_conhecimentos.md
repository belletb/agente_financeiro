# Base de Conhecimento

## Dados Utilizados

| Arquivo                   | Formato | Utilização no Agente |
|----------------------------|---------|-----------------------|
| `transacoes.csv`           | CSV     | Analisar padrão de gastos do cliente (essenciais, supérfluos, investimentos) |
| `metas_financeiras.json`   | JSON    | Definir e acompanhar objetivos financeiros (ex: viagem, compra de imóvel, aposentadoria) |
| `perfil_cliente.json`      | JSON    | Personalizar recomendações de acordo com perfil comportamental e preferências |
| `educacao_financeira.json` | JSON    | Fornecer conteúdos educativos e dicas de organização financeira |


---

## Adaptações nos Dados

- Expansão do `transacoes.csv` para incluir categorias adicionais (ex: saúde, lazer, transporte).  
- Inclusão de campo **prioridade** em `metas_financeiras.json` para diferenciar metas de curto, médio e longo prazo.  
- Adição de **nível de conhecimento financeiro** em `perfil_cliente.json` para ajustar o tom das explicações (iniciante, intermediário, avançado).  
- Curadoria de conteúdos em `educacao_financeira.json` para incluir dicas práticas de economia e reserva de emergência.  

---

## Estratégia de Integração

### Como os dados são carregados?
- Os arquivos **CSV/JSON** são carregados no início da sessão.  
- São transformados em **dataframes (Python/SQL)** para consultas rápidas.  
- O agente acessa os dados dinamicamente conforme a interação do usuário.  

### Como os dados são usados no prompt?
- Informações relevantes são **injetadas no contexto** do LLM durante a conversa.  
- O agente consulta dinamicamente os dados para responder perguntas específicas.  
- Exemplo: ao calcular uma meta, o agente busca transações recentes e saldo disponível.  

---

## Exemplo de Contexto Montado

```text
Dados do Cliente:
- Nome: João Silva
- Perfil: Moderado
- Saldo disponível: R$ 5.000
- Nível de conhecimento: Iniciante

Últimas transações:
- 01/11: Supermercado - R$ 450
- 03/11: Streaming - R$ 55
- 05/11: Transporte - R$ 120
- 07/11: Restaurante - R$ 200

Metas Financeiras:
- Viagem Internacional (Curto prazo) - R$ 12.000
- Reserva de Emergência (Médio prazo) - R$ 20.000

Sugestões Educativas:
- "Reduza gastos supérfluos em 15% para acelerar sua reserva de emergência."
- "Defina um valor fixo mensal para poupança automática."
