import streamlit as st

st.title("Hello, world!")
st.subheader("This is a subheader")
st.text("This is some text.")
st.write("This is a write statement.")
st.markdown("This is **markdown** text.")

xxx = st.selectbox("Select an option", ["Option 1", "Option 2", "Option 3"])
st.write(f"You selected: {xxx}")

st.success("This is a success message.")
st.error("This is an error message.")
st.warning("This is a warning message.")
st.info("This is an info message.")

