import streamlit as st
import pickle
import numpy as np
import base64
st.markdown("""
<style>
label {
    color: white !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>

/* Center the button */
div.stButton {
    display: flex;
    justify-content: center;
}

/* Style the button */
div.stButton > button {
    background-color: #90EE90;
    color: black;
    font-size: 18px;
    padding: 10px 30px;
    border-radius: 10px;
    border: none;
}

/* Hover effect */
div.stButton > button:hover {
    background-color: #32CD32;
    color: white;
}

</style>
""", unsafe_allow_html=True)

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image:
        encoded = base64.b64encode(image.read()).decode()
    
    bg_style = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{encoded}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    </style>
    """
    st.markdown(bg_style, unsafe_allow_html=True)

add_bg_from_local("matrix code.jpg")
#Title
model = pickle.load(open("fake_profile_model.pkl","rb"))
st.markdown("<h1 style='color:white;'>Fake Profile Detection System</h1>", unsafe_allow_html=True)

col1, col2 = st.columns(2)
#User inputs
with col1:
    profile_pic = st.selectbox("Profile Picture", ["No", "Yes"])
    profile_pic_value = 1 if profile_pic == "Yes" else 0
# Convert dropdown to numeric


    description = st.number_input("Length of Discription",min_value=0)
    posts = st.number_input("Number of Posts",min_value=0)

with col2:
    followers = st.number_input("Followers",min_value=0)
    following = st.number_input("Following",min_value=0)

#st.write("Input sent to model:", features)

#prediction = model.predict(features)
    
if st.button("Predict"):
    features = np.array([
    float(profile_pic_value),
    float(description),
    float(posts),
    float(followers),
    float(following)
]).reshape(1, -1)
    prediction = model.predict(features)

    if prediction[0] == 1:
        st.error("⚠ Fake Profile")
    else:
        st.success("✅ Real Profile")