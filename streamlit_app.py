import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import pyodbc

# Function to connect to SQL Server and fetch data
def get_data_from_sql():
    conn = pyodbc.connect(
        'DRIVER={SQL Server};'
        'SERVER=202.66.174.120,1232;'
        'DATABASE=vaagmndb;'
        'UID=vaagdadbusr;'
        'PWD=MefrAyu!Uw8they9ru;'
    )
	
    query = "SELECT Employee_Name, Employee_Code, Employee_Gender, Employee_DOB, GrossSalary FROM EmployeeMater"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

# Load the data from SQL Server
df = get_data_from_sql()

# Format Store IDs (name in your case) to avoid comma separation
df['Employee_Name'] = df['Employee_Name'].astype(str)

# Define pages
def store_details():
    st.sidebar.header('Select Employee Name')
    store_name = st.sidebar.selectbox('Employee Name', df['Employee_Name'].unique())

    # Filter data for the selected store
    store_data = df[df['Employee_Name'] == store_name].iloc[0]

    # Display store attributes
    st.header(f'Employee: {store_name}')
    st.write('### Employee Details')
    st.write(f"Code: {store_data['Employee_Code']}")
    st.write(f"Gender: {store_data['Employee_Gender']}")
    st.write(f"DOB: {store_data['Employee_DOB']}")
   
     #Employee_Name, Employee_Code, Employee_Gender, Employee_DOB GrossSalary
   
   

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
'''
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel file
df = pd.read_excel('VG-Revised-Data-001.xlsx')

# Format Store IDs (name in your case) to avoid comma separation
df['name'] = df['name'].astype(str)

# Define pages
def store_details():
    st.sidebar.header('Select Employee Name')
    store_name = st.sidebar.selectbox('Employee Name', df['name'].unique())

    # Filter data for the selected store
    store_data = df[df['name'] == store_name].iloc[0]

    # Display store attributes
    st.header(f'Employee: {store_name}')
    st.write('### Employee Details')
    st.write(f"Code: {store_data['code']}")
    st.write(f"Basic: {store_data['esicno']}")
    st.write(f"Code: {store_data['uanno']}")
    st.write(f"Basic: {store_data['basic']}")
    st.write(f"HRA: {store_data['hra']}")
    st.write(f"TPT: {store_data['tpt']}")
    st.write(f"Edu: {store_data['edu']}")
    st.write(f"Medical: {store_data['medical']}")
    st.write(f"Other Allowance: {store_data['otherallowance']}")
    st.write(f"Gross Salary: {store_data['grosssalary']}")
    st.write(f"Total CTC: {store_data['totalctc']}")
   
    # Pie chart for Male/Female Population
    st.write('### Employee Salary')
    labels = ['Gross Salary', 'Total CTC']
    sizes = [store_data['grosssalary'], store_data['totalctc']]
    colors = ['#ff9999', '#66b3ff']
    explode = (0.1, 0)  # explode the 1st slice

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    st.pyplot(fig1)

def summary_statistics():
    # Define custom headers for the DataFrame
    custom_headers = {
        'name': 'Employee Name',
        'code': 'Employee Code',
        'esicno': 'ESIC Number',
        'basic': 'Basic Salary',
        'hra': 'HRA',
        'tpt': 'Transport Allowance',
        'edu': 'Education Allowance',
        'medical': 'Medical Allowance',
        'otherallowance': 'Other Allowance',
        'grosssalary': 'Gross Salary',
        'totalctc': 'Total CTC'
    }

    st.header('Employee Statistics')

    st.write('### All Employee Summary')
    # Include all the requested columns in the summary
    summary = df[['name', 'code', 'esicno', 'basic', 'hra', 'tpt', 'edu', 'medical','otherallowance', 'grosssalary','totalctc']].rename(columns=custom_headers)
    # Display the DataFrame in the app
    st.dataframe(summary)  

def store_comparison():
    # Define custom headers for the DataFrame
    custom_headers = {
        'name': 'Employee Name',
        'code': 'Employee Code',
        'esicno': 'ESIC Number',
        'basic': 'Basic Salary',
        'hra': 'HRA',
        'tpt': 'Transport Allowance',
        'edu': 'Education Allowance',
        'medical': 'Medical Allowance',
        'otherallowance': 'Other Allowance',
        'grosssalary': 'Gross Salary',
        'totalctc': 'Total CTC'
    }
    st.sidebar.header('Select Employee to Compare')
    selected_stores = st.sidebar.multiselect('Employee Names', df['name'].unique())
   
    if len(selected_stores) > 1:
        st.header('Store Comparison')
        st.write('### Comparison of Selected Empolyees')

        store_data_list = []
        for store_name in selected_stores:
            #store_data.index = store_data.index.to_series().replace(custom_headers)
            store_data = df[df['name'] == store_name].T
            store_data.columns = [store_name]
            store_data_list.append(store_data)

        # Display the stores' data side by side
        for i, store_data in enumerate(store_data_list):
            if i == 0:
                comparison_df = store_data
            else:
                comparison_df = pd.concat([comparison_df, store_data], axis=1)

        st.dataframe(comparison_df)
        
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
    summary_statistics()
elif page == 'Employee Comparison':
    store_comparison()
'''
