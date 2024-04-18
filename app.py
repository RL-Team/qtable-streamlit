import streamlit as st
import numpy as np

# Function to update Q-table based on user inputs
def update_q_table(q_table, state, action, reward, learning_rate=0.1, discount_factor=0.9):
    current_q = q_table[state][action]
    max_future_q = np.max(q_table[state])
    new_q = current_q + learning_rate * (reward + discount_factor * max_future_q - current_q)
    q_table[state][action] = new_q

    return q_table

# Streamlit web app
def main():
    st.title("Q-Table Updation")

    # Example Q-table and environment
    q_table = np.zeros((10, 4))  # Example Q-table with 10 states and 4 actions
    environment = {"states": 10, "actions": 4}

    # User input section
    state = st.number_input("Enter current state (0 - {}):".format(environment["states"] - 1), min_value=0, max_value=environment["states"] - 1, step=1)
    action = st.number_input("Enter action taken (0 - {}):".format(environment["actions"] - 1), min_value=0, max_value=environment["actions"] - 1, step=1)
    reward = st.number_input("Enter reward received:", step=0.01)

    if st.button("Update Q-Table"):
        q_table = update_q_table(q_table, int(state), int(action), reward)
        st.write("Q-Table Updated Successfully!")

    st.write("Updated Q-Table:")
    st.write(q_table)

if __name__ == "__main__":
    main()
