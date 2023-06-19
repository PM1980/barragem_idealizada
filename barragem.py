import streamlit as st
import matplotlib.pyplot as plt

def calculate_normal_stresses(B, H, g, rho_conc, rho_agua, z):
    gamma_conc = rho_conc * g
    gamma_agua = rho_agua * g

    N = -B * (H - z) * gamma_conc
    p = gamma_agua * (H - z)
    E = p * (H - z) * (1 / 2)
    d = (1 / 3) * (H - z)
    M_agua = E * d

    L = B
    A = B * 1
    I = 1 * (B ** 3) / 12
    sigma_montante = N / A + M_agua * (L / 2) / I
    sigma_jusante = N / A - M_agua * (L / 2) / I

    return sigma_montante, sigma_jusante

def plot_normal_stresses(sigma_montante, sigma_jusante, B):
    x = [0, B]
    y = [sigma_montante / 1000, sigma_jusante / 1000]
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.axhline(0, color='r', linestyle='--')
    ax.set_xlabel('posição medida a partir de montante (m)')
    ax.set_ylabel('tensão normal (kPa)')
    ax.grid(True)
    st.pyplot(fig)

def main():
    st.title("Dam Normal Stresses")

    B = st.number_input("Base da barragem (m)", value=5.0)
    H = st.number_input("Altura da barragem (m)", value=10.0)
    g = st.number_input("Aceleração da gravidade (m/s^2)", value=10.0)
    rho_conc = st.number_input("Massa específica do concreto (kg/m^3)", value=2400.0)
    rho_agua = st.number_input("Massa específica da água (kg/m^3)", value=1000.0)
    z = st.number_input("Elevação de cálculo (m)", value=0.0)

    sigma_montante, sigma_jusante = calculate_normal_stresses(B, H, g, rho_conc, rho_agua, z)
    plot_normal_stresses(sigma_montante, sigma_jusante, B)

    st.write("Tensão normal a montante:", sigma_montante, "Pa")
    st.write("Tensão normal a jusante:", sigma_jusante, "Pa")

if __name__ == "__main__":
    main()
