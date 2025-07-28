import streamlit as st 
import google.generativeai as genai
import pandas as pd
import os
from dotenv import load_dotenv
load_dotenv()

# configure the api key

key_variable = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=key_variable)


# SET UP OUR PAGE


st.title('HEALTH ASSISTANT FOR FITNESS🚀')
st.subheader('This page will help you to get information for fitness using BMI value📝')


st.sidebar.subheader('Height')
height = st.sidebar.text_input('Enter the height in meters:')

st.sidebar.subheader('Weight')
weight = st.sidebar.text_input('Enter the weight in kgs:')

## Calculating BMI values

try:
    height = pd.to_numeric(height)
    weight = pd.to_numeric(weight)
    if height > 0 and weight > 0:
        bmi = weight/(height**2)
        st.sidebar.success(f'Bmi value is :{round(bmi,2)}')
    else:
        st.sidebar.write('Please enter positive values.')
except:
    st.sidebar.info('Please enter positive values')

input = st.text_input('Ask your question here 🔍')

submit = st.button('Click here 🎯')

model = genai.GenerativeModel('gemini-1.5-flash')

def generate_result(bmi,input):
    if input is not None:
        
        prompt = f'''
        You are a health assistant now so you need to get results 
        based on the fitness or other health related questions. 
        Use the bmi value {bmi} for suggestions.
        You can suggest some diet to be followed and also
        some fitness exercises to the user.
        If any medications or medicine related questions are asked
        always mention that 'Check with the nearby doctors for the
        medications'
        '''
        
        result = model.generate_content(input+prompt)
        
    return result.text
    
if submit:
    with st.spinner('Result is loading.....'):
        response = generate_result(bmi, input)
        
    st.markdown(':green[Result]')
    st.write(response)