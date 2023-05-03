import streamlit as st
import pickle
import pandas as pd
import numpy as np
import math


pipe = pickle.load(open('pipe.pkl', 'rb'))
lap = pickle.load(open('lap.pkl', 'rb'))
st.title("Laptop Price Predictor")
company = st.selectbox('Brand', lap['Company'].unique())
type = st.selectbox('Type', lap['TypeName'].unique())
ram = int(st.selectbox('RAM(in GB)', [2, 4, 6, 8, 12, 16, 24, 32, 64]))
touch = st.selectbox('TouchScreen', ['NO', 'YES'])
ips = st.selectbox('IPS', ['NO', 'YES'])
s_size = float(st.number_input('ScreenSize'))
resolution = st.selectbox('Screen Resolution',
                          ['1928x1088', '1366x768', '1600x900', '3840x2160', '3200x1800', '2880x1800', '2560x1600',
                           '2560x1440', '2304x1440'])
cpu=st.selectbox('CPU',lap['CPU Brand'].unique())
hdd=st.selectbox('HDD(in GB)',[0,128,256,512,1024,2048])
sdd=st.selectbox('SSD(in GB)',[0,8,128,256,512,1024])
gpu=st.selectbox('GPU',lap["GPU Brand"].unique())
clock=st.selectbox('Clock Speed',lap['Clock_Speed'].unique())
os=st.selectbox('OS',lap['OpSys'].unique())
if st.button('Predict Price'):
    if touch=='YES':
        touch=1
    else:
        touch=0
    if ips=='YES':
        ips=1
    else:
        ips=0
    x_res=int(resolution.split('x')[0])
    y_res=int(resolution.split('x')[1])
    ppi=(((x_res**2)+(y_res**2))**0.5)/float(s_size)
    query=pd.Series([company,type,int(ram),os,touch,ips,ppi,clock,cpu,hdd,sdd,gpu])
    query=query.values
    query=query.reshape((1,12))

    st.title(np.exp(pipe.predict(query)))