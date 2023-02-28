import streamlit as st
from PIL import Image
import os

st.title("Hello everyone:sunglasses:")
st.header(":blue[This is Srikanya]")
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "emoji.jpg")
img = Image.open(IMAGE_PATH)
st.image(img)
st.subheader("Data Science Aspirant")
st.caption("Completed Data Science Course from   :red[Innomatics Research labs]")
st.balloons()


btn_click = st.button("Click Me!")

if btn_click == True:
    st.subheader("You got me :sunglasses:")
    st.write("check out this github [link](https://github.com/SriYarramsetti)")
    st.write("check out this linkedIn [link](https://www.linkedin.com/in/srikanya10/)")
    st.snow()