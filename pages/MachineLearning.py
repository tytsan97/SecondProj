import pandas as pd
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report,confusion_matrix,accuracy_score
rfmodel= st.sidebar.checkbox('Random Forest Classification')
data = pd.read_csv('water_potability.csv')
if rfmodel: 
    with st.form("my_form1"):     
        st.title('Classify the water potatbility')
        ph = st.number_input("Enter pH Level:")
        hard = st.number_input("Enter Amount of Hardness:")
        solid = st.number_input("Enter Amount of Solids:")
        ch4 = st.number_input("Enter Amount of Chloromines:")
        so4 = st.number_input("Enter Amount of Sulfate:")
        conduct = st.number_input("Enter Amount of Conductivity:")
        carbon = st.number_input("Enter Amount of Organic Carbon:")
        trihalo = st.number_input("Enter Amount of Trihalomethanes:")
        turbi = st.number_input("Enter Amount of Turbidity:")
        submitted = st.form_submit_button("Submit")
        if submitted:
          inputdata = {'ph':ph,'Hardness':hard,'Solids':solid,'Chloramines':ch4,'Sulfate':so4,'Conductivity':conduct,
                      'Organic_carbon':carbon,'Trihalomethanes':trihalo,'Turbidity':turbi}                  
          features = pd.DataFrame(inputdata,index=[0])         
          x=data.drop("Potability",axis=1)
          y=data["Potability"]
          X_train, X_test, Y_train, Y_test = train_test_split(x,y,test_size=0.25, random_state=25)
          rdm_model = RandomForestClassifier()
          rdm_model.fit(X_train,Y_train)                 
          testsdata2 =  features.reindex(columns =  X_train.columns, fill_value=0)
          y_pred = rdm_model.predict(testsdata2)
          if y_pred==1 :
              st.write("This is pure water that can drink.")
          else:
              st.subheader("This is not pure water that can happen disadvantages.")
          st.header("Accuracy Score")
          rfc_accuracy = accuracy_score(Y_test,y_pred)
          st.subheader(rfc_accuracy)
                   
