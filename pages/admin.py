import streamlit as st
from menu import menu_with_redirect

# Ensure session state has a 'role' attribute
def check_role():
    if "role" not in st.session_state:
        st.session_state.role = None  # Default to None if not set

# Redirect to app.py if not logged in, otherwise show the navigation menu
menu_with_redirect()

check_role()  # Ensure 'role' exists before accessing it

# Verify the user's role
if st.session_state.role != "admin":
    st.warning("You do not have permission to view this page.")
    st.stop()

st.title("Admin Dashboard")
st.markdown(f"You are currently logged in with the role of **{st.session_state.role}**.")
