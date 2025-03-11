import streamlit as st


def authenticated_menu():
    # Show a navigation menu for authenticated users
    st.sidebar.page_link("app.py", label="Choose Your Role")
    st.sidebar.page_link("pages/employee.py", label="Your Profile")

    if st.session_state.get("role") in ["manager"]:
        st.sidebar.page_link(
            "pages/employee.py",
            label="Manage Employees",
            disabled=st.session_state.get("role") != "admin",
        )

    if st.session_state.get("role") in ["admin"]:
        st.sidebar.page_link("pages/admin.py", label="Manage Managers")
        st.sidebar.page_link(
            "pages/manager.py",
            label="Manage Employees",
            disabled=st.session_state.get("role") != "admin",
        )


def unauthenticated_menu():
    # Show a navigation menu for unauthenticated users
    st.sidebar.title("Menu")
    st.sidebar.page_link("app.py", label="Log in")


def menu():
    # Determine if a user is logged in or not, then show the correct
    # navigation menu
    if "role" not in st.session_state or st.session_state.role is None:
        unauthenticated_menu()
        return
    authenticated_menu()


def menu_with_redirect():
    # Redirect users to the main page if not logged in, otherwise continue to
    # render the navigation menu
    if "role" not in st.session_state or st.session_state.role is None:
        st.switch_page("app.py")
    menu()