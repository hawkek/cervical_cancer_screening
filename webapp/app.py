from sklearn.preprocessing import RobustScaler
import streamlit as st
import pandas as pd
import numpy as np
import pickle

#----Prediction-----
def predict_risk(model, df):
    X_test = clean_data(df)
    prediction = model.predict(X_test)
    
    return prediction

#-----Cleaning-----
def clean_data(df):
    return RobustScaler().fit_transform(df)

st.title('Cervical Cancer Screener')
st.subheader('Check to see if you might be at risk & recommendations to reduce your risk')
st.info('*Disclaimer* This is based of an analysis of *data* and should NOT be taken as medical advice. No input responses are saved.')

#------Sidebar Input-----
st.sidebar.title('Fill out your details')
st.sidebar.checkbox('I agree to the disclaimer')
age = st.sidebar.number_input('Age', 0, 100)
num_partners = st.sidebar.number_input('Number of sexual partners', 0, 500)
sex_age = st.sidebar.number_input('First sexual intercourse (age)', 0, 100)
num_preg = st.sidebar.number_input('Number of pregnancies?', 0, 30)
smoke_packs = st.sidebar.number_input('Amount you smoke (packs/year)?', 0, 1000)
contr_years = st.sidebar.number_input('Amount of time used hormonal contraceptives (years)?', 0, 1000)
iud_num = st.sidebar.number_input('Number of years having an IUD?', 0, 50)
std_num = st.sidebar.number_input('Number of STDs you have had?', 0, 50)

#----Model Loading-----
model = pickle.load(open('cervical_cancer_risk_model.sav', 'rb'))

#----Map features-------
features = {'Age' : age,
        'Number of sexual partners': num_partners,
        'First sexual intercourse (age)': sex_age,
        'Num of pregnancies': num_preg,
        'Smokes (packs/year)': smoke_packs,
        'Hormonal Contraceptives (years)': contr_years,
        'IUD (years)': iud_num,
        'STDs (number)': std_num
}

#-----Convert to dataframe----
features_df  = pd.DataFrame([features])

if st.sidebar.button('Submit'):
    
    prediction = predict_risk(model, features_df)
    if prediction<0.5:
        risk = 'low'
        st.success('Based on your answers, your risk level may be low. Learn more below about how to continue to reduce your risk level')
        st.subheader("Ways to Reduce your Risk")
        st.write(
        """    
        - Get vaccinated for HPV
        - Regularly get screened (pap test & HPV)
        - Do not smoke
        - Practice safe sex
        - Work to keep your weight healthy
        - Eat a healthy diet with lots of fruits and vegetables
        - If possible, try not use birth control pills for an extended time

        """
        )
        st.write("More information: [CDC](https://www.cdc.gov/cancer/cervical/basic_info/prevention.htm)")


    else:
        risk = 'high'
        st.warning('Based on your answers, your risk may be high! Learn more below about how to reduce your risk level')
        st.subheader("Ways to Reduce your Risk")
        st.write(
        """    
        - Get vaccinated for HPV
        - Regularly get screened (pap test & HPV)
        - Do not smoke
        - Practice safe sex
        - Work to keep your weight healthy
        - Eat a healthy diet with lots of fruits and vegetables
        - If possible, try not use birth control pills for an extended time

        """
        )
        st.write("More information: [CDC](https://www.cdc.gov/cancer/cervical/basic_info/prevention.htm)")

