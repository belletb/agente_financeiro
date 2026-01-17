import streamlit as st
from agente import CopilotoFinanceiro

agente = CopilotoFinanceiro(
    perfil_path="data/perfil_cliente.json",
    transacoes_path="data/transacoes.csv",
    produtos_path="data/produtos_financeiros.json",
    educacao_path="data/educacao_financeira.json"
)

# -------------------------------
# Interface Streamlit
# -------------------------------
st.title("Copiloto de Bem-Estar Financeiro")

st.sidebar.header("Perfil do Cliente")
st.sidebar.write(f"Nome: {agente.perfil['nome']}")
st.sidebar.write(f"Idade: {agente.perfil['idade']}")
st.sidebar.write(f"Profissão: {agente.perfil['profissao']}")
st.sidebar.write(f"Renda Mensal: R$ {agente.perfil['renda_mensal']:.2f}")
st.sidebar.write(f"Perfil Financeiro: {agente.perfil['perfil_financeiro']}")

st.subheader("Gastos por Categoria")
gastos = agente.calcular_gastos_por_categoria()
st.bar_chart(gastos)

st.subheader("Metas Financeiras")
for meta in agente.perfil["metas"]:
    falta = agente.simular_meta(meta)
    st.write(f"**Meta:** {meta['meta']}")
    st.write(f"Valor necessário: R$ {meta['valor_necessario']:.2f}")
    st.write(f"Prazo: {meta['prazo']}")
    st.write(f"Falta: R$ {falta:.2f}")
    st.markdown("---")

st.subheader("Produtos Financeiros Recomendados")
for p in agente.recomendar_produtos():
    st.write(f"- **{p['nome']}** ({p['categoria']})")
    st.write(f"  - Risco: {p['risco']}")
    st.write(f"  - Rentabilidade: {p['rentabilidade']}")
    st.write(f"  - Aporte mínimo: R$ {p['aporte_minimo']:.2f}")
    st.write(f"  - Indicado para: {p['indicado_para']}")
    st.markdown("---")

st.subheader("Dicas de Educação Financeira")
for dica in agente.dicas_educativas():
    st.write(f"- **{dica['tema']}**: {dica['conteudo']}")

# -------------------------------
# Chat com Ollama
# -------------------------------
st.subheader("Chat com o Copiloto Financeiro")

with st.form("chat_form"):
    user_input = st.text_input("Digite sua pergunta sobre finanças:")
    submitted = st.form_submit_button("Enviar")

if submitted and user_input:
    resposta = agente.chat_with_ollama(user_input)
    st.markdown("**Resposta do agente:**")
    st.write(resposta)
