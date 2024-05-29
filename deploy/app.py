import streamlit as st

# page
import eda
import prediction

        
page = st.sidebar.radio(label="Navigation", options=['Home Page', 'Exploratory Data Analysis', 'Prediction'])
st.sidebar.divider()

if page == "Home Page":
    st.header("Welcome Page")
    st.write('')
    st.write('Introduction')
    st.write("Name\t: Akbar Fitriawan")
    st.write("Batch\t: hacktiv8-15")
    st.write('Tujuan Milestone    : ')
    st.write('Building a Classification Model for Car Insurance Claims')
    st.caption('Silahkan pilih menu lain di Select Box pada sebelah kiri layar anda untuk memulai!')

    with st.expander("Problem Statement"):
            st.caption('Understanding Customer Behavior in Car Insurance Claims')
    with st.expander("Kesimpulan"):
        st.caption('With these strategies, we can manage risks more effectively, set premiums more accurately, and increase profits and customer satisfaction.')
elif page == 'Exploratory Data Analysis':
    eda.run()
else:
    prediction.run()