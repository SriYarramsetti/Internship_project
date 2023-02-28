import streamlit as st
from PIL import Image
import pandas as pd
import plotly.express as px
import os

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "heart attack.jpg")
DATA_PATH = os.path.join(dir_of_interest, "data", "heart.csv")

st.title("Welcome to my project:sunglasses:")
st.header(":red[Heart] Attack Analysis & Prediction")

img = Image.open(IMAGE_PATH)
st.image(img)

df = pd.read_csv(DATA_PATH)
st.dataframe(df)
st.write("Age : Age of the patient")
st.write("Sex : Sex of the patient")
st.write("exang: exercise induced angina (1 = yes; 0 = no)")
st.write("ca: number of major vessels (0-3)")
st.write("cp : Chest Pain type chest pain type ,Value 1: typical angin ,Value 2: atypical angina,Value 3: non-anginal pain,Value 4: asymptomatic")
st.write("trtbps : resting blood pressure (in mm Hg)")
st.write("chol : cholestoral in mg/dl fetched via BMI sensor")
st.write("fbs : (fasting blood sugar > 120 mg/dl) (1 = true; 0 = false)")
st.write("rest_ecg : resting electrocardiographic results,Value 0: normal,Value 1: having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV),Value 2: showing probable or definite left ventricular hypertrophy by Estes")
st.write("thalach : maximum heart rate achieved")
st.write("target : 0= less chance of heart attack 1= more chance of heart attack")


output = st.selectbox(":blue[Select the chance of heart attack:]", df['output'].unique())

fig_1 = px.histogram(df[df['output'] == output], x="sex")
fig2 = px.histogram(df[df['output'] == output], x="age")
fig_3 = px.histogram(df[df['output'] == output], x="fbs")
fig_4 = px.histogram(df[df['output'] == output], x="thalachh")

col1, col2 = st.columns(2)

with col1:
   st.subheader("Gender count who are attacked / not attacked")
   st.plotly_chart(fig_1, use_container_width=True)

with col2:
   st.subheader("Age varying acc to output")
   st.plotly_chart(fig2, use_container_width=True)

col3, col4 = st.columns(2)

with col3:
   st.subheader("Blood sugar>120 or not")
   st.plotly_chart(fig_3, use_container_width=True)


with col4:
   st.subheader("heart beat rate")
   st.plotly_chart(fig_4, use_container_width=True)

select = st.selectbox(":blue[Select chest pain type:]", df['cp'].unique())
fig_5 = px.histogram(df[df['cp'] == select], x="output")

col5, col6 = st.columns(2)

with col5:
   st.subheader("Chances of attack based on chest pain type")
   st.plotly_chart(fig_5, use_container_width=True)

