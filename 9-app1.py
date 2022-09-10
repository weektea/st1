import streamlit as st


# title
st.title("My BMI Calculator")

# height
height = st.number_input("Your height in metre:", value=1.5)

# weight
weight = st.number_input("Your weight in kg:", value=50)

# calculate bmi
bmi = weight/(height**2)
st.write("Here is Your BMI", bmi)

# message alert
# follow classifation below
# http://www.myhealth.gov.my/indeks-jisim-tubuh-ijt/
if bmi < 18.5:
    st.warning("You are underweight.")
elif bmi < 24.9:
    st.success("You have ideal weight.")
elif bmi < 30:
    st.warning("You have overweight.")
else:
    st.error("You are obese.")






# caption
