import pickle
import streamlit as st
import time
from streamlit_option_menu import option_menu

#Load models
diabetes_model = pickle.load(open('models/diabetes_prediction_model.pkl', 'rb'))
heart_model = pickle.load(open('models/heart_disease_prediction.pkl', 'rb'))
breast_model = pickle.load(open('models/breast_cancer_prediction_model.pkl', 'rb'))

#create sidebar
with st.sidebar:
    
    selected = option_menu("E-Doctor - Predicts your Diabetes,Heart related Disease and Breast cancer",                         
                           ["Diabetes prediction",
                            "Heart disease prediction",
                            "Breast cancer prediction"],
                           icons=['activity','heart','person'],
                           default_index=0)
    

 #Diabetes prediction page   
if selected == "Diabetes prediction":

    st.title("Diabetes Prediction")
    
    col1,col2,col3 = st.columns(3)
    with col1:
        Pregnancies = st.number_input("Number of Pregnancies",0,20)
    with col2:
        Glucose = st.number_input("Glucose level",0,200)
    with col3:
        BloodPressure = st.number_input("Blood Pressure Value",0,150)
    with col1:
        SkinThickness = st.number_input("SkinThickness value",0,100)
    with col2:
        Insulin = st.number_input("Insulin level",0,200)
    with col3:
        BMI = st.number_input("BMI value",0,60)
    with col1:
        DiabetesPedigreeFunction = st.number_input("DiabetesPedigreeFunction value",0.0,2.0)
    with col2:
        Age = st.number_input("Age of the person",0,120)


#predicting diabetes
    diab_diagnosis = ''
    if st.button("Predict the Diabetes Test Results"):
        
        with st.spinner('Analyzing patient data...'):
            time.sleep(2)
            diab_prediction = diabetes_model.predict(
                [[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]]
                )
            
            if (diab_prediction[0] == 1):
                st.error('The person is diabetic')
            else:
                st.success('The person is not diabetic')
    
    
#Heart disease prediction page   
if selected == "Heart disease prediction":

    st.title("Heart disease Prediction")
    
    col1,col2,col3 = st.columns(3)
    with col1:
        age = st.number_input("Age of the person",0,120)
    with col2:
        sex = st.number_input("Gender (1 = Male, 0 = Female)")
    with col3:
        cp = st.number_input("Chest Pain Type",0,3)
    with col1:
        trestbps = st.number_input("Resting Blood Pressure",0,200)
    with col2:
        chol = st.number_input("Serum Cholesterol",0,400)
    with col3:
        fbs = st.number_input("Fasting Blood Sugar",0,200)
    with col1:
        restecg = st.number_input("Resting ECG Results",0,2)
    with col2:
        thalach = st.number_input("Maximum Heart Rate Achieved",0,250)
    with col3:
        exang = st.number_input("Exercise-Induced Angina",0,1)
    with col1:
        oldpeak = st.number_input("ST Depression Induced by Exercise",0.0,10.0)
    with col2:
        slope = st.number_input("Slope of Peak Exercise ST Segment",0,2)
    with col3:
        thal = st.number_input("Thalassemia Type",0,3)
    with col1:
        ca = st.number_input("Number of Major Vessels Colored by Fluoroscopy",0,3)



#predicting heart disease
    heart_diagnosis = ''
    if st.button("Predict the Heart Test Results"):
        
        with st.spinner("Analyzing patient data..."):
            time.sleep(2)
            heart_prediction = heart_model.predict(
                [[age, sex, cp, trestbps, chol, fbs, restecg, thalach,	exang, oldpeak, slope, ca, thal]]
            )
            
            if (heart_prediction[0] == 1):
                st.error('The person has heart disease')
            else:
                st.success('The person has not heart disease')
            

    

#Breast cancer prediction page   
if selected == "Breast cancer prediction":

    st.title("Breast cancer prediction")
    
    col1,col2,col3,col4,col5,col6 = st.columns(6)
    with col1:
        meanradius = st.number_input("Average distance from center ",0.0,100.0)
    with col2:
        meantexture = st.number_input("Variation in gray-scale values",0.0,100.0)
    with col3:
        meanperimeter = st.number_input("Average perimeter ",0.0,100.0)
    with col4:
        meanarea = st.number_input("Average area of the cell",0.0,100.0)
    with col5:
        meansmoothness = st.number_input("Local variation in radius lengths",0.0,1.0)
    with col6:
        meancompactness = st.number_input("Perimeter² / Area - 1",0.0,1.0)
    with col1:
        meanconcavity = st.number_input("Severity of concave portions",0.0,1.0)
    with col2:
        meanconcavepoints = st.number_input("Number of concave portions",0.0,1.0)
    with col3:
        meansymmetry = st.number_input("Average Cell symmetry",0.0,1.0)
    with col4:
        meanfractaldimension = st.number_input("Complexity of cell boundary",0.0,1.0)
    with col5:
        radiuserror = st.number_input("Standard error of radius",0.0,100.0)
    with col6:
        textureerror = st.number_input("Standard error of texture",0.0,100.0)
    with col1:
        perimetererror = st.number_input("Standard error of perimeter",0.0,100.0)
    with col2:
        areaerror = st.number_input("Standard error of area",0.0,100.0)
    with col3:
        smoothnesserror = st.number_input("Standard error of smoothness",0.0,1.0)
    with col4:
        compactnesserror = st.number_input("Standard error of compactness",0.0,1.0)
    with col5:
        concavityerror = st.number_input("Standard error of concavity",0.0,1.0)
    with col6:
        concavepointserror = st.number_input("Standard error of concave points",0.0,1.0)
    with col1:
        symmetryerror = st.number_input("Standard error of symmetry",0.0,1.0)
    with col2:
        fractaldimensionerror = st.number_input("Standard error of fractal dimension",0.0,1.0)
    with col3:
        worstsmoothness = st.number_input("Worst smoothness ",0.0,1.0)
    with col4:
        worstcompactness = st.number_input("Worst compactness ",0.0,1.0)
    with col5:
        worstconcavepoint = st.number_input("Worst concave points ",0.0,1.0)
    with col6:
        worstfractaldimension = st.number_input("Worst fractal dimension ",0.0,1.0)
    with col1:
        worstradius = st.number_input("Worst radius ",0.0,100.0)
    with col2:
        worsttexture = st.number_input("Worst texture ",0.0,100.0)
    with col3:
        worstconcavity = st.number_input("Worst concavity ",0.0,1.0)
    with col4:
        worstperimeter = st.number_input("Worst perimeter ",0.0,100.0)
    with col5:
        worstsymmetry = st.number_input("Worst symmetry ",0.0,1.0)
    with col6:
        worstarea = st.number_input("Worst area ",0.0,100.0)



#predicting breast disease
    breast_cancer_diagnosis = ''
    if st.button("Predict the Breast cancer Test Results"):
        
        with st.spinner('Analyzing patient data...'):
            time.sleep(2)
            
            breast_cancer_prediction = breast_model.predict(
                [[meanradius, meantexture, meanperimeter, meanarea, meansmoothness, meancompactness, meanconcavity, meanconcavepoint, meansymmetry, meanfractaldimension,
                  radiuserror, textureerror, perimetererror, areaerror, smoothnesserror, compactnesserror, concavityerror, concavepointerror, symmetryerror, fractaldimensionerror,
                  worstradius, worsttexture, worstperimeter, worstarea, worstsmoothness, worstcompactness, worstconcavity, worstconcavepoint, worstsymmetry, worstfractaldimension]]
                )
            
            if (breast_cancer_prediction[0] == 1):
                st.error('The person has Breast cancer')
            else:
                st.success('The person has not Breast cancer')
