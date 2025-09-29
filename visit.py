import streamlit as st
import datetime as dt

st.title("Subham's Streamlit App")

if st.button("Click Me"):
    st.write("Button clicked!")
    st.success("You clicked the button!")

check = st.checkbox("Check Me")
if check:
    st.write("Checkbox is checked!")


radio = st.radio("select :", ["1", "2", "3"])
st.markdown(f"You selected: **{radio}**")

selection = st.selectbox("Choose an option", ["A", "B", "C"])
st.write(f"You selected: {selection}")

slider = st.slider("Select a value", 0, 10, 5)

numberInput = st.number_input("Enter a number", min_value=0, max_value=10, step=1)
st.write(f"You selected: {numberInput}")

name = st.text_input("Enter your name")
if name:
    st.subheader(f"Welcome {name}")

toDay = dt.date.today()

dob = st.date_input(
    "Select your date of birth",
    value=toDay,
    min_value=toDay - dt.timedelta(days=365 * 50),
    max_value=toDay + dt.timedelta(days=365 * 50),
)

st.write(f"Your date of birth is: {dob}")

# year = toDay.year - dob.year - ((toDay.month, toDay.day) < (dob.month, dob.day))
# month = toDay.month - dob.month - (toDay.day < dob.day)
# if month < 0:
#     month += 12
#     years = year-1

# day = toDay.day - dob.day
# if day < 0:
#     if month == 0:
#         month = 11
#         years -= 1
#     else:
#         month -= 1
#     day += (dt.date(toDay.year, toDay.month, 1) - dt.date(toDay.year if toDay.month > 1 else toDay.year - 1, toDay.month - 1 if toDay.month > 1 else 12, 1)).days

age = dt.date(toDay.year, toDay.month, toDay.day) - dt.date(
    dob.year, dob.month, dob.day
)
year = age.days // 365
month = (age.days % 365) // 30
day = (age.days % 365) % 30
st.write(f"You are {year} years, {month} months and {day} days old.")
st.write(f"age = {age}")
