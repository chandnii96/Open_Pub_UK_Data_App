

import streamlit as st
import numpy as numpy
import pandas as pd
from PIL import Image
from matplotlib import image
import os

st.title(':green[Welcome to Open Pub Application 🍻🍻]')



#Background Image
img = '''
<style>
.stApp {
background-image: url("https://media.istockphoto.com/photos/light-blue-background-with-pattern-picture-id624409380?k=6&m=624409380&s=612x612&w=0&h=XYHFBLtqTp3EMuKDtJMzTW5wTzkFbalhfArb14U6mWI=");
background-size: cover;
background-position: top center;
background-repeat: no-repeat;
background-attachment: local;
background-blur;
}
</style>
'''
st.markdown(img, unsafe_allow_html=True)

#Adding image
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
dir_of_interest = os.path.join(FILE_DIR, "resources")
IMAGE_PATH = os.path.join(dir_of_interest, "images")
IMAGE_PATH1 = os.path.join(IMAGE_PATH, "bartender.jpg")

img = image.imread(IMAGE_PATH1)
st.image(img)

st.subheader('Find the Basic information of the pub dataset')


df = pd.read_csv('clean_open_pubs.csv')

choice = st.selectbox('',('Total pubs in UK','Head','Tail','unique local authority','null_values'))

if choice=='Total pubs in UK':
    st.markdown(f'There  are  **{df.shape[0]}**  Pubs  in  **United Kingdom**')

elif choice=='Head':
    st.dataframe(df.head())

elif choice=='Tail':
    st.dataframe(df.tail())

elif choice=='unique local authority':
    st.text(f'Total no of pub local authority is {len(df.local_authority.unique())} in UK')

elif choice=='null_values':
    st.markdown('**There are no null values in our dataset**')
    st.text(df.isnull().sum())

elif choice=='Statistics information':
     st.dataframe(df.describe())

st.text('')
st.text('')

st.subheader('Find the Statistics information of the pub dataset')

stat = st.button('Describe')
if stat==True:
    st.dataframe(df.describe())
else:
    st.text('')


#subheader
st.write('By: :green[Chandni Kumari]')

btn_click = st.button("Click me")

if btn_click == True:
    st.markdown(":lightblue[Connect with me ]")
    st.write(":blue[LinkedIn]:(https://www.linkedin.com/in/chandniikumari/)")

    st.write(":green[GitHub]:(https://github.com/chandnii96)")

    st.write(":red[Instagram]:(https://www.instagram.com/chand__nii/ )")