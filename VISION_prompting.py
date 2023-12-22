import streamlit as st
from call_gemini import call_gemini_vision
import os


st.title("Visual Image Scenario Interpretation & Object Narration (VISION)")
st.subheader("PROMPTING")


uploaded_image = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if uploaded_image is not None:
    image_content = uploaded_image.getvalue()
    save_directory = "./temp_image/"
    os.makedirs(save_directory, exist_ok=True)
    file_name = "uploaded_image.mp4"
    file_path = os.path.join(save_directory, file_name)
    with open(file_path, "wb") as file:
        file.write(image_content)

    input = st.text_input("Enter a prompt")

    submit = st.button('Submit')

    container = st.container()
    
    st.image(uploaded_image, caption='Uploaded Image.', use_column_width=True)

    if submit:
        response = call_gemini_vision(input, "./temp_image/")
        with container: 
            st.subheader(response)


  