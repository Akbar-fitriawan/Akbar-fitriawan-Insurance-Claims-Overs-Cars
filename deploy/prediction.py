import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load Model
with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)


def run():
    st.title('Car Insurance Prediction :car::clipboard:')
    st.write('Welcome to the car insurance claim or not claim prediction application. predict whether customers will claim insurance or not in the future based on existing information')
    st.divider()

    st.markdown('## 📝 Input Data')
    with st.form('my_form'):
        # input age
        age = st.selectbox('Age 🧒🏻', ['young', 'middle age', 'old','very old']),
        # input gender
        gender = st.selectbox('Gender 🚻', ['male', 'female']),
        # input race
        race = st.selectbox('RACE 🫱🏼‍🫲🏻', ['majority', 'minority']),
        # input drive
        drive_exp = st.selectbox('Driving Experience 🛣️🚘', ['newbie', 'amateure', 'advanced', 'expert']),
        # input education
        education = st.selectbox('Education 🎓', ['high school','none', 'university']),
        #input income
        income = st.selectbox('Income 💰', ['poverty', 'working class', 'middle class','upper class']),
        # input credit score
        credit_score = st.number_input('Credit score :credit_card:', 0.0, 1.0, step=0.1)
        # input vehicle ownership
        vehicle_ownership = st.radio('Vehicle Ownership 🔑', ('No', 'Yes')),
        vehicle_ownership_value = 0 if vehicle_ownership == 'No' else 1

        # input vehicle year
        vehicle_year = st.selectbox('Vehicle Year 📅', ['before 2015', 'after 2015']),
        # input married
        married = st.radio('Married :man_and_woman_holding_hands::ring:', ('No', 'Yes')),
        married_value = 0 if married == 'No' else 1

        # input children
        children = st.radio('Children 👶', ('No', 'Yes')),
        children_value = 0 if children == 'No' else 1

        # input annual mileage
        annual_mileage = st.slider('Annual Mileage ⏲', 1000, 25000, step=100),
        # input vehicle type
        vehicle_type = st.selectbox('Vehicle Type 🚙', ['sedan', 'sport car']),
        # input speed violations
        speeding_violations = st.slider('Speeding Violations ⚡', 0,15, step=1),
        # input DUIS
        duis = st.slider('DUIS 🥴💊', 0,15, step=1),
        # input past accidents 
        past_accidents = st.slider('Past Accidents 💥', 0,15, step=1),
        # Input city
        city = st.selectbox('City 🏢', ['baltimore','new york','orlando','san diego'])
        
        submitted = st.form_submit_button('Let\'s 🔍 Check ')
    
    input_data = pd.DataFrame({
        'AGE': age,
        'GENDER':gender,
        'RACE': race,
        'DRIVING_EXPERIENCE':drive_exp,
        'EDUCATION': education,
        'INCOME': income,
        'CREDIT_SCORE':credit_score,
        'VEHICLE_OWNERSHIP':vehicle_ownership,
        'VEHICLE_YEAR':vehicle_year,
        'MARRIED':married,
        'CHILDREN': children,
        'ANNUAL_MILEAGE':annual_mileage,
        'VEHICLE_TYPE':vehicle_type,
        'SPEEDING_VIOLATIONS': speeding_violations,
        'DUIS': duis,
        'PAST_ACCIDENTS':past_accidents,
        'CITY': city
    })

    st.markdown('Syntetic Dataframe')
    st.dataframe(input_data)

    st.markdown('Prediction 👇')
    if submitted:
        prediction = model.predict(input_data)

        if prediction[0] == 0:
            st.write('❌ Customer has not filed a claim')
        else:
            st.write('✅ Customer has filed a claim')
    

if __name__=="__main__":
    run()