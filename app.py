import streamlit as st

def main():
    st.title("Simple ATM Application")

    if 'balance' not in st.session_state:
        st.session_state.balance = 1000  # Initial balance

    st.write(f"Current Balance: ${st.session_state.balance:.2f}")

    st.subheader("Deposit Money")
    deposit_amount = st.number_input("Enter amount to deposit", min_value=0.0, format="%.2f")
    if st.button("Deposit"):
        st.session_state.balance += deposit_amount
        st.success(f"Successfully deposited ${deposit_amount:.2f}. New balance: ${st.session_state.balance:.2f}")

    st.subheader("Withdraw Money")
    withdraw_amount = st.number_input("Enter amount to withdraw", min_value=0.0, format="%.2f")
    if st.button("Withdraw"):
        if withdraw_amount > st.session_state.balance:
            st.error("Insufficient funds!")
        else:
            st.session_state.balance -= withdraw_amount
            st.success(f"Successfully withdrew ${withdraw_amount:.2f}. New balance: ${st.session_state.balance:.2f}")

    st.subheader("Check Balance")
    if st.button("Show Balance"):
        st.info(f"Your current balance is: ${st.session_state.balance:.2f}")

if __name__ == "__main__":
    main()
