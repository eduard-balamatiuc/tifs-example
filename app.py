import streamlit as st
from PIL import Image
import cv2

# model = 

st.sidebar.write("## Example test app")

# Selecția paginii dorite
pages = ["Home", "Photo", "Video"]
choice = st.sidebar.selectbox("Select page", pages)

if choice == "Home":
    # Pagina principală
    st.title("Home")
    
elif choice == "Photo":
    # Pagina cu încărcare de fotografii
    st.title("Photo")
    
    # Încărcarea imaginii
    uploaded_file = st.sidebar.file_uploader("Choose a photo...", type="jpg")
    
    # Verificarea încărcării fișierului și afișarea imaginii
    if uploaded_file:
        image = Image.open(uploaded_file)
        st.write("Original photo")
        st.image(image, caption="Oarecare text", use_column_width=True)
    else:
        st.write("No photo uploaded")
        
elif choice == "Video":
    # Pagina cu încărcare de video
    st.title("Video")
    run = st.checkbox("Run")
    FRAME_WINDOW = st.image([])
    camera = cv2.VideoCapture(0)
    camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    
    while run:
        # Capturarea imaginii
        _, frame = camera.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        FRAME_WINDOW.image(frame)