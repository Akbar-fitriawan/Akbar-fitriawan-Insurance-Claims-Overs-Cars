import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px


def run():
    # Set page configuration

    # load dataset
    df = pd.read_csv('Car_Insurance_Claim_Cleaned.csv')

    st.title('Welcome to Exploratory Data Analysis :chart_with_upwards_trend:')
    st.subheader("Looking Dataframe")
    st.table(df.head(5))

    st.subheader('Summary Statistic')
    st.markdown('Summary data')
    st.write(df.describe())
    with st.expander('Explanation'):
        st.write('Check description. It can be seen that the average number of times a speeding violation has been committed is 1, meaning that the individual has "had one traffic violation for speeding", "PAST_ACCIDENT" (ever filed a claim) on average 1 time, "VEHICLE_OWNERSHIP" is not his own , and a mean Outcome "0" ("No claim").')

    st.markdown("Summary Top Frequency")
    st.write(df.describe(include=['object']))
    with st.expander('Explanation'):
        st.write('The top frequency from the dataset is women aged "26-39 years" (middle age), have driving experience of less than "10 years", with income "upper_class", cars before 2015, sedans and city cars mostly in "New York"')
    st.divider()
    
    # Visualisasi by Outcome
    st.subheader('History Outcome Car insurance')
    pie_data = df['OUTCOME'].value_counts()
    fig = px.pie(names=pie_data.index, values=pie_data.values, title='Outcome Claim or Not Claim')
    st.plotly_chart(fig)

    with st.expander('Explanation'):
        st.write('From the visualization results, it can be seen that in the Outcome column, which is our target, there are more non-claim data compared to claims. The data is quite unbalanced so balancing must be done')
    st.divider()

    st.subheader('Analyze Status Personality')

    fig_gender_outcome = px.histogram(df, x="GENDER", color="OUTCOME", barmode="group", title="Gender by Outcome")
    st.plotly_chart(fig_gender_outcome, use_container_width=True) 


    fig_married_outcome = px.histogram(df, x="MARRIED", color="OUTCOME", barmode="group", title="Married by Outcome")
    st.plotly_chart(fig_married_outcome, use_container_width=True)


    fig_children_outcome = px.histogram(df, x="CHILDREN", color="OUTCOME", barmode="group", title="Children by Outcome")
    st.plotly_chart(fig_children_outcome, use_container_width=True)


    fig_city_outcome = px.histogram(df, x="CITY", color="OUTCOME", barmode="group", title="City by Outcome")
    st.plotly_chart(fig_city_outcome, use_container_width=True)
    
    with st.expander('Explanation'):
        st.write('- Based on visualization of personal status where Outcome 1 (Claim insurance) is male, single, there is no difference "having children or not", and based on City New York is higher, followed by Orlando, San Diego, Baltimore')
        st.write('- Based on visualization of personal status where Outcome 0 (No insurance claim) tends to be female, married, has children, and the city of New York, Orlando, San Diego.')
        st.write('- Based on the City ranking, New York is in first place, Orlando is second, San Diego is third, last is Baltimore')
        st.write('- Based on Gender by Age there is no significant difference in frequency in the dataset.')
        st.write('Insights:')
        st.write('- We must improve service in the San Diego and Baltimore areas, by carrying out promotional campaigns to attract customers')


    # histogram
    fig = px.histogram(df, x="AGE", color="OUTCOME", barmode="group",title="Age by Outcome",  category_orders={"AGE": ['young', 'middle age', 'old', 'very old']})
    # pie chart
    fig_pie = px.pie(df, names="AGE", title="Frequency Age", category_orders={"AGE": ['young', 'middle age', 'old', 'very old']})
    fig_pie.update_traces(textinfo='percent+label')
    # Split the app into two columns
    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(fig, use_container_width=True)
    with col2:
        st.plotly_chart(fig_pie, use_container_width=True)
    
    with st.expander('Explanation'):
        st.write("- In the age range 16-25 years (young) there is a tendency to submit insurance claims (1), while in the age range 40-64 years (old) there is a tendency not (0)." )
        st.write("- High frequency of not submitting insurance claims in the age range 40-64 years. (old)")
        st.write("- In summary, as people get older, there is a tendency not to file insurance claims.")
    st.divider()

    fig = px.histogram(df, x='RACE', color='OUTCOME', barmode='group', title="RACE by Outcome")
    fig_pie = px.pie(df, names="RACE", title="Frequency RACE")
    col1,col2 = st.columns(2)
    with col1:
        st.plotly_chart(fig, use_container_width=True)
    with col2:
        st.plotly_chart(fig_pie, use_container_width=True)

    with st.expander('Explanation'):
        st.write('- It can be seen from the majority and minority races that Outcome 0 ("No claim insurance") is superior to Outcome 1 ("Claim insurance")')
        st.write('- majority 90.1% and minority 9.9%')
        st.write('in fact there is no correlation between the majority and the minority (if we imagine that it is very likely that the minority is more at risk or has a higher risk of Outcome 1 "Claim Insurance" namely racism)')
    st.divider()

    # Visualisasi Drive exp
    st.subheader('Driving Experience')
    # histogram
    fig = px.histogram(df, x='DRIVING_EXPERIENCE', color='OUTCOME', barmode='group', title="Driving Experience by Outcome", category_orders={"DRIVING_EXPERIENCE": ['newbie', 'amateure', 'advanced', 'expert']})
    fig_pie = px.pie(df, names="DRIVING_EXPERIENCE", title="Frequency Driving Experience")
    col1,col2 = st.columns(2)
    with col1:
        st.plotly_chart(fig, use_container_width=True)
    with col2:
        st.plotly_chart(fig_pie, use_container_width=True)

    with st.expander('Explanation'):
        st.write('- In fact, the less experienced you are in driving, the higher the claim rate insurance (Outcome 1 "Claim loan").')
        st.write('- In the dataset frequency Drive experience is high at 0-9 years, namely 35%, followed by 10-19 years is 33.0%, 20-29 years is 21.2%, 30+ years is 10.5%. by the way iam rename values ("Newbie", "Amateure", "Advanced", "Expert")')

    st.divider()

    # Visualisasi Education
    st.subheader('Looking Education')
    # histogram
    fig = px.histogram(df, x='EDUCATION', color='OUTCOME', barmode='group', title="Driving Experience by Outcome", category_orders={"EDUCATION": ['high school', 'university', 'none']})
    fig_pie = px.pie(df, names="EDUCATION", title="Frequency Education")

    col1,col2 = st.columns(2)
    with col1:
        st.plotly_chart(fig, use_container_width=True)
    with col2:
        st.plotly_chart(fig_pie, use_container_width=True)
    
    with st.expander('Explanation'):
        st.write('- The visualization shows that Outcome 1 (claim insurance) has a high frequency in "high school" while Outcome 0 (No claim insurance) in "university"')
        st.write('- And the amount of data in the dataset is 45% in high school, 39% in university and "19.1%" is none (work, etc.)')
        st.write('Relates to Age where high school education levels (aged 16-25 years) tend to submit claims (Outcome 1 "Claim insurance"), as well as high frequency in this category. and I assume that high school is in the 16-25 year age range, university is in the 26-39 year age range, and none is in the 40-65+ age range')
    st.divider()

    # Visualisasi Income
    st.subheader("Looking Income")
    # Create a subplot with Plotly Express
    fig_income_outcome = px.histogram(df, x="INCOME", color="OUTCOME", barmode="group", category_orders={"INCOME": ['poverty', 'working class', 'middle class', 'upper class']})
    fig_income_outcome.update_layout(title="Income by Outcome", xaxis_title="Income", yaxis_title="Count")

    # Create a pie chart with Plotly Express
    dist_income = df["INCOME"].value_counts()
    fig_income_frequency = px.pie(names=dist_income.index, values=dist_income.values, title="Frequency by Income", 
                                  labels={"label": "Income", "value": "Frequency"})

    # Create a grouped bar chart for Income by Age
    fig_income_age = px.bar(df, x="INCOME", color="AGE", category_orders={"INCOME": ['poverty', 'working class', 'middle class', 'upper class'], "AGE": ['young', 'middle age', 'old', 'very old']})
    fig_income_age.update_layout(title="Income by Age", xaxis_title="Income", yaxis_title="Count")

    # Create a box plot for Income by Past Accidents
    fig_income_accidents = px.box(df, x="PAST_ACCIDENTS", y="INCOME")
    fig_income_accidents.update_layout(title="Income by Past Accidents", xaxis_title="Past Accidents", yaxis_title="Income")

    # Streamlit app
    st.plotly_chart(fig_income_outcome, use_container_width=True)
    st.plotly_chart(fig_income_frequency, use_container_width=True)
    st.plotly_chart(fig_income_age, use_container_width=True)
    st.plotly_chart(fig_income_accidents, use_container_width=True)

    with st.expander('Explanation'):
        st.write("- Based on the Income by Outcome visualization, those who tend to submit claims (outcome 1) are from the 'poverty' income group.")
        st.write("- From the results of the frequency by income dataset, the upper class dominates, followed by the middle class, poverty, and working class.")
        st.write("- From the Income by Age output, it can be seen that different income groups are dominated by different age groups.")
        st.write("- From the Income by Past Accidents output, certain income groups have different patterns in past loan claims.")

        # Insights
        st.write("Insights:")
        st.write("- Based on the Outcome (claim insurance / no claim insurance) that Income 'Poverty' has the potential to submit a claim, which is dominated by teenagers. Therefore, focusing on reducing this potential by segmenting customers and targeting ages over 25 years and by looking at their income (upper class, middle class, and working class).")

    st.divider()
    # visualisasi vehicle
    st.subheader('Looking Vehicle Distribution')
    fig_vehicle_year = px.histogram(df, x="VEHICLE_YEAR", color="OUTCOME", barmode="group", title="Vehicle Years by Outcome")
    fig_vehicle_type = px.histogram(df, x="VEHICLE_TYPE", color="OUTCOME", barmode="group", title="Vehicle Type by Outcome")
    fig_vehicle_ownership_outcome = px.histogram(df, x="VEHICLE_OWNERSHIP", color="OUTCOME", barmode="group", title="Vehicle by Ownership")
    fig_vehicle_ownership_pastAccidents = px.box(df,x='VEHICLE_OWNERSHIP', y='PAST_ACCIDENTS')
    st.plotly_chart(fig_vehicle_year, use_container_width=True)
    st.plotly_chart(fig_vehicle_type, use_container_width=True)
    st.plotly_chart(fig_vehicle_ownership_outcome, use_container_width=True)
    st.plotly_chart(fig_vehicle_ownership_pastAccidents, use_container_width=True)
    st.divider()

    with st.expander('Conclusions'):



        st.write("## Data Imbalance")
        st.write("""
        Data imbalance was found in the Outcome column, which requires balancing actions to improve the accuracy of the prediction model.
        """)

        st.write("## Personality Analysis")
        st.write("Based on the results that I analyzed, there was a pattern of differences in insurance claims between customers based on gender, marital status, having children, etc. I categorize them based on outcomes as follows:")

        st.write("### In case of outcome 1 (Claim insurance)")
        st.write("""
        - Tends to be male
        - In the age range 16-25 years (young)
        - Singles
        - There is no significant difference "to have children or not"
        - Based on City, New York is higher, followed by Orlando, San Diego, and finally Baltimore
        - Based on education, high school is higher for submitting insurance claims
        - Income tends to be Poverty (unstable)
        - Driving experience, the less experienced you are, the higher you submit a claim
        """)

        st.write("### In case of outcome 0 (No insurance claim)")
        st.write("""
        - Tends to be female
        - In the age range 40-64 (old)
        - Married
        - Have children
        - Based on City High New York, Orlando, and San Diego
        - Based on Education, University tends to be high, and high school
        - Income tends to be upper class and middle class
        - Drive experience: the more experienced you are in driving, the higher the risk of filing an insurance claim
        - High credit score
        - Even though there is no correlation, the outcome is high in the majority
        """)

        st.write("""
        Based on analysis of insurance claim patterns, personal factors such as age, education and marital status influence the frequency of claims. Young drivers (16-25 years) and those with low education (high school) tend to have a higher frequency of claims. On the other hand, drivers who are older (40-64 years), have a higher education (university), are married, and have children tend to file claims less frequently.
        """)

        st.write("## Vehicle Analysis")
        st.write("As follows are the findings from the vehicle:")

        st.write("### In the case of outcome 1 (Claim Insurance)")
        st.write("""
        - Tend to be cars before 2015
        - Sedan cars tend to be taller than sports cars
        - Submission does not belong to the car itself
        - Annual mileage tends to be high
        """)

        st.write("### In case of outcome 0 (No insurance claim)")
        st.write("""
        - Car types tend to be sedans
        - Tend to be cars after 2015
        - Private property
        - Annual mileage tends to be low
        """)

        st.write("""
        The type and age of the vehicle has a big influence on insurance claim patterns. Older cars or certain types of cars, such as sedans, tend to have a higher frequency of claims.
        """)

        st.write("## Analysis of Accidents")
        st.write("From the findings, there is an influence on insurance claims based on violations or damage received as follows:")

        st.write("### In the case of outcome 1 (Claim Insurance)")
        st.write("""
        - Rarely commit speed violations
        - DUIS ("Driving Under the Influence Surcharge") rarely commits such offenses
        - Past accidents tend to have a history of fewer past accidents
        - Ages 16-25 (young) rarely commit violations
        """)

        st.write("### In case of outcome 0 (No Claim Insurance)")
        st.write("""
        - Have committed at least 1 speed violation or more
        - DUIS ("Driving Under the Influence Surcharge") often commits this violation
        - Most past accidents have a history of certain accidents
        - In the age range of 40+ years there is a higher rate of committing violations
        """)

        st.write("""
        Traffic violations and past accident history have a big influence on insurance claims. Customers with a lower history of violations and accidents tend to file claims less frequently.
        """)
        

        
        
if __name__ == "__main__":
            
        run()