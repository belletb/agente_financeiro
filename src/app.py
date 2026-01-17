import streamlit as st
from agente import CopilotoFinanceiro

st.set_page_config(page_title="FinWell", layout="wide")

@st.cache_resource
def init():
    return CopilotoFinanceiro(
        "data/perfil_cliente.json", "data/transacoes.csv",
        "data/produtos_financeiros.json", "data/educacao_financeira.json"
    )

agente = init()

st.title("FinWell Copilot")

st.subheader("📊 Diagnóstico Financeiro")
col1, col2 = st.columns(2)
col1.metric("Renda Mensal", f"R$ {agente.perfil.get('renda_mensal', 0)}")
col2.bar_chart(agente.calcular_gastos_por_categoria())

st.divider()

if "messages" not in st.session_state:
    st.session_state.messages = []

for m in st.session_state.messages:
    with st.chat_message(m["role"]): st.markdown(m["content"])

if p := st.chat_input("Dúvida?"):
    st.session_state.messages.append({"role": "user", "content": p})
    with st.chat_message("user"): st.markdown(p)
    with st.chat_message("assistant"):
        r = agente.chat_with_ollama(p)
        st.markdown(r)
        st.session_state.messages.append({"role": "assistant", "content": r})