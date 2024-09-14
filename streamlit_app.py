import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel file
df = pd.read_excel('Revised-Data.xlsx')

# Format Store IDs (name in your case) to avoid comma separation
df['Name'] = df['Name'].astype(str)

# Define pages
def store_details():
    st.sidebar.header('Select Employee Name')
    store_name = st.sidebar.selectbox('Employee Name', df['Name'].unique())

    # Filter data for the selected store
    store_data = df[df['Name'] == store_name].iloc[0]

    # Display store attributes
    st.header(f'Employee: {store_name}')
    st.write('### Employee Details')
    st.write(f"Code:  {store_data['Code']}")
    st.write(f"Code:  {store_data['Code']}")
     st.write(f"Code:  {store_data['Code']}")
 st.write(f"Code:  {store_data['Code']}")
 st.write(f"Code:  {store_data['Code']}")

 #st.write(f"ESIC NO: {store_data['ESICNO']}")
 #st.write(f"UAN NO.: {store_data['UANNO']}")
 #st.write(f"Basic: {store_data['Basic']}")
 #st.write(f"HRA: {store_data['HRA']}")
 #st.write(f"TpT: {store_data['TpT']}")
 #st.write(f"Edu: {store_data['Edu']}")
 #st.write(f"Medical: {store_data['Medical']}")
 #st.write(f"Other Allowance: {store_data['OtherAllowance']}")
 #st.write(f"GROSS SALARY: {store_data['GROSSSALARY']}")
 #st.write(f"Total CTC: {store_data['TotalCTC']}")

  

# Create a navigation menu
st.sidebar.title('Navigation')
page = st.sidebar.radio('Go to', ['Employee Details', 'Employee Statistics', 'Employee Comparison'])

st.markdown(
    """
    <style>
    [data-testid="stElementToolbar"] {
        display: none;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Render the selected page
if page == 'Employee Details':
    store_details()
elif page == 'Employee Statistics':
    store_details()
elif page == 'Employee Comparison':
    store_details()
