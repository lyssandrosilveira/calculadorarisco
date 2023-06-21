import streamlit as st

def calculate_ruin_risk(drawdown, win_rate, bet_size):
    ruin_risk = (1 - win_rate) / (win_rate * (1 + (drawdown - 1) / bet_size))
    return ruin_risk

def main():
    st.title("Calculadora de Risco de Ruína")

    drawdown = st.number_input("Drawdown:", value=-0.87)
    win_rate = st.number_input("Taxa de Vitória (%):", min_value=0.0, max_value=100.0, value=94.0)
    bet_size = st.number_input("Tamanho da Aposta:", value=10.0)

    if st.button("Calcular Risco de Ruína"):
        ruin_risk = calculate_ruin_risk(drawdown, win_rate / 100, bet_size)
        ruin_risk_percentage = ruin_risk * 100
        st.write("Risco de Ruína: {}%".format(ruin_risk_percentage))

if __name__ == '__main__':
    main()
