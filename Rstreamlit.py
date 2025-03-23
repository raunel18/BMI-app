#import the module
import streamlit as st

#title
st.title("hi raunel")

#header
st.header("This is header")

#subheading
st.subheader("This is sub header")

#text
st.text("This is simple text.")

#markdown
st.markdown("### This is markdown.")

#Success, warning, info

#success
st.success("Success")

#warning
st.warning("Warning")

#error
st.error("error")
#check box
if st.checkbox("show/hide"):

    #display the text if the checkbox return ture values
    st.text("Showing the widget")
# Radio buttons
status = st.radio("select gender:",('Male', 'Female'))

if (status == 'Male'):
    st.success("Male")
else:
    st.success("Female")

#text input
name = st.text_input("Enter your name", "Type here ...")   

if (st.button('submit')):
     result = name.title()
     st.success(result)

#slider
level = st.slider("Select the level", 1, 5)

st.text('Selected: {}' .format(level))
#Title
st.title ('welcome to BMI Calculator')

#Take weight in kgs
weight = st.number_input("Enter your weight (inkgs)")

#Take height format selection
status = st.radio ('select your height format:', ('cms', 'meters', 'feet'))

#compute BMI based on the selected format
#bmi = None

if status == 'cms':
    height = st.number_input('Enter height in centimeters')
    if height > 0:
        bmi = weight / ((height/100) **2)
    else:
        st.warning("Enter a valid height value")

elif status == 'meters':
    height = st.number_input('Enter height in meters')
    if height > 0:
        bmi = weight / (height **2) 
    else:
        st.warning("Enter valid height value")           
elif status == 'feet':
         height = st.number_input('Enter your height in feet')
         if height > 0:
            bmi = weight / ((height / 3.28)** 2)
         else:
            st.warning("Enter a valid height value")  

# check if the button is pressed
if st.button('Calculate BMI'):
    if bmi:
          st.text(f"Your BMI Index is {bmi:.2f}")

          #Interpretation fo BMI
          if bmi < 16:
               st.error ("You are extremely underweight")
          elif bmi< 18.5:
               st.warning("You are underweight")
          elif bmi < 25:
               st.success("healthy")
          elif bmi < 30:
               st.warning("You are overweight")
          else:
               st.error("Extermely Overweight")
    else:
               st.warning("Please enter a valid weight and height")                                     
  
                








