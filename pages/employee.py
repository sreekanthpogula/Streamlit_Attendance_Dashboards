import streamlit as st
import pandas as pd
from menu import menu_with_redirect

# Redirect to app.py if not logged in, otherwise show the navigation menu
menu_with_redirect()

st.title("Employee Attendance Dashboard")

# Create dummy data
data = {
    "status": ["Work From Home", "Work From Office", "Work From Home", "Work From Office", "Work From Home", "Work From Office", "Work From Office", "Work From Home", "Work From Office", "Work From Home"]
}
df = pd.DataFrame(data)

# Calculate metrics
wfh_count = len(df[df['status'] == "Work From Home"])
wfo_count = len(df[df['status'] == "Work From Office"])

st.metric("Work From Home", wfh_count)
st.metric("Work From Office", wfo_count)

st.bar_chart(df['status'].value_counts())
