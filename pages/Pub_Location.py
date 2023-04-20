import streamlit as st
import pandas as pd
import numpy as np
import os


#Load data
FILE_DIR1 = os.path.dirname(os.path.abspath(__file__))
FILE_DIR = os.path.join(FILE_DIR1,os.pardir)
dir_of_interest = os.path.join(FILE_DIR, "resources")
DATA_PATH1 = os.path.join(dir_of_interest, "clean_open_pubs.csv")
df = pd.read_csv(DATA_PATH1)


#Background Image
img = '''
<style>
.stApp {
background-image: url("https://wallpapercave.com/wp/wp2590324.jpg");
background-size: cover;
background-position: top center;
background-repeat: no-repeat;
background-attachment: local;
background-blur;
}
</style>
'''
st.markdown(img, unsafe_allow_html=True)


# make header
st.header("Location of all Bars in UK")
# enter either postal code or local authority

local_author = st.selectbox('Select Local Authority : ', set(df['local_authority']))
button_1 = st.button("Submit")

if button_1:
    df_new = df.loc[(df['local_authority'] == local_author)]
    st.text("Total Number of Pubs in this location is:")

    st.map(df_new)
    st.dataframe(df_new)
