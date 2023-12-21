import streamlit as st
from prompts import description_prompts
from gemini_classes import Vision_Search
from extract_video_frames import extract_frames
import os


st.set_page_config(layout="wide",)
if 'example' not in st.session_state:
    st.session_state.example = False

if 'upload' not in st.session_state:
    st.session_state.upload = False

if "process_video" not in st.session_state:
    st.session_state.process_video = True

st.title("Visual Image Scenario Interpretation & Object Narration  (VISION)")
st.subheader("SEARCH APP")

col1, col2, col3, col4, col5 = st.columns(5)


with col2:
    


    example = st.button("Use Example Video")

    upload = st.button("Upload Your Own Video")

    if example:
        st.session_state.example = True
        st.session_state.upload = False

    if upload:
        st.session_state.example = False
        st.session_state.upload = True





    
    if st.session_state.example == True:
        st.subheader("Recommended Search terms:")
        st.write("Early in video: Bread, fan, shopping cart, coca cola.")
        st.write("Late in video: Carrots, mangos, banana, watermelon.")

        input = st.text_input("Type what you are looking for in the store.")

        example_search = st.button("Search")

        if example_search and input == "":
            st.subheader("Please enter a search term.")
        
        if example_search and input != "":
                
            with st.spinner("Searching..."):
                search_results, found, image_document = Vision_Search.describe(Vision_Search.search(description_prompts.visually_impaired_search_prompt,"video_frames", input))
            if found == True:
                st.success(f"{input.upper()} found nearby.")
                st.write(search_results)
                with col4:
                    st.write("Image when item found")
                    st.image(image_document[0].image_path)
            if found == False:
                st.error(f"{input.upper()} not found.")       

        with col3:
            st.write("Example Video")
            st.video("video/walking_through_store.mp4")





if st.session_state.upload == True:
    
    with col2:
        st.write("Upload Your Own Video: Currently works best with verticle cell phone videos.")

        uploaded_video = st.file_uploader("Upload Video", type=["mp4"])
        
        if uploaded_video is not None:
            video_content = uploaded_video.getvalue()
            save_directory = "./temp_processed/"
            os.makedirs(save_directory, exist_ok=True)
            file_name = "uploaded_video.mp4"
            file_path = os.path.join(save_directory, file_name)
            with open(file_path, "wb") as file:
                file.write(video_content)

        process_video = st.button("Process Video")
        
        if process_video:
            st.session_state.process_video = False
            with st.spinner("Processing..."):
                extract_frames("temp_processed/uploaded_video.mp4", "processed_video_frames")
            
            
        

        input = st.text_input("Type what you are searching for in the video.")

        upload_search = st.button("Search", disabled=st.session_state.process_video)
        
        if st.session_state.process_video is False:
            with col3:
                st.subheader("Your Video")
                st.video("temp_processed/uploaded_video.mp4")

        if upload_search and input == "":
            st.subheader("Please enter a search term.")
        
        if upload_search and input != "":
            with st.spinner("Searching..."):
                search_results, found, image_document = Vision_Search.describe(Vision_Search.search(description_prompts.visually_impaired_search_prompt,"processed_video_frames", input))
            if found == True:
                st.success(f"{input.upper()} found nearby.")
                st.write(search_results)
                with col4:
                    st.subheader("Image when item found")
                    st.image(image_document[0].image_path)
            if found == False:
                st.error(f"{input.upper()} not found.")

