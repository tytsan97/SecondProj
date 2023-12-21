import streamlit as st
import pandas as pd
data=pd.read_csv("water_potability.csv")
rfmodel= st.sidebar.checkbox('Naive Bayesian Classification')
data = pd.read_csv('water_potability.csv')
if rfmodel: 
    with st.form("my_form1"):     
        st.title('Classify the water potability')
        st.subheader("Please Choose all features for predicting good result")
        logic_rate=st.number_input('Pick a number for Logical Rating',1,9)
        hack_rate = st.number_input('Pick a number for hackathons',0,6)
        code_rate = st.number_input('Pick a number for coding skills rating',1,9)
        speak_rate = st.number_input('Pick a number for public speaking points',1,9)
        
        submitted = st.form_submit_button("Submit")
        if submitted:
            inputdata = {}                  
            features = pd.DataFrame(inputdata,index=[0])         
            x=data.drop("",axis=1)
            y=data[""]
            
            x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.25, random_state=25)
            filename = ''
            with open(filename, 'rb') as f:
                u = pickle._Unpickler(f)
                
                p = u.load()
  

            
            testsdata2 =  features.reindex(columns =  x_train.columns, fill_value=0)
            y_pred = p.predict(testsdata2)
            if y_pred==1:
              st.subheader("This water can drink")
            else:
              st.subheader("This water can not drink")        
                
