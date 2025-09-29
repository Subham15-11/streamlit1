import streamlit as st
import requests
from PIL import Image
from io import BytesIO

st.title("Welcome to the Layout Page")

col1,col2 = st.columns(2)

with col1:
    st.subheader("Column 1")
    
    url1 = "https://cdn11.bigcommerce.com/s-x49po/images/stencil/1280x1280/products/34989/48129/1538404157379_2018-01-10--19-49-53__74205.1539147081.png?c=2"
    response = requests.get(url1)
    img1 = Image.open(BytesIO(response.content))
    img1 = img1.resize((200, 200))  # Resize image to 200x200
    
    st.image(image= img1,caption="Krishna") 
    vote1 = st.button("Button 1")

with col2:
    st.subheader("Column 2")
    
    # st.image("https://i.etsystatic.com/18961489/r/il/c03a47/3473381785/il_1588xN.3473381785_b8a8.jpg", caption="Shiva",width=200,height=200) # streamlit dont support height and width in image function, so we can use PIL to resize the image.
    
    url2 = "https://i.etsystatic.com/18961489/r/il/c03a47/3473381785/il_1588xN.3473381785_b8a8.jpg"
    response = requests.get(url2)  
    img2 = Image.open(BytesIO(response.content))
    img2 = img2.resize((200, 200))  # Resize image to 
    st.image(image= img2,caption="Shiva")  
    
    vote2 = st.button("Button 2")
    
if vote1:
    st.success("You clicked Button 1")
    st.balloons()
if vote2:
    st.success("You clicked Button 2")
    st.balloons()
    
# sidebar

st.sidebar.title("Sidebar Title")
st.sidebar.subheader("Sidebar Subheader")
name = st.sidebar.text_input("Enter your name")
sel = st.sidebar.selectbox("Select your favorite deity", ["Krishna", "Shiva", "Vishnu", "Ganesha"])

st.write(f"Hello, {name}. Your favorite deity is {sel}.")


with st.expander("See explanation"):
    st.write("""
       This is an example of using columns and sidebar in Streamlit.\n
        You can click the buttons to see the effects.\n
        You can also enter your name and select your favorite deity from the sidebar.
    """)
    
st.markdown("---")
st.markdown("# Thank you for visiting!")
st.markdown("> Have a great day!")