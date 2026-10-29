
import streamlit as st

st.set_page_config(
    page_title="Pixel Wizard",
    page_icon="🪄",
    layout="wide"
)

st.title("🪄 Pixel Wizard")
st.subheader("AI Virtual Hair Color Preview")

st.write(
    "Upload a photo and preview your hair color!"
)

photo = st.file_uploader(
    "Upload your photo",
    type=["jpg", "jpeg", "png"]
)

colors = {
    "Blue": "#3C78FF",
    "Pink": "#FF64B4",
    "Purple": "#A050DC",
    "Red": "#E6323C",
    "Green": "#3CBE64",
}

color_name = st.selectbox(
    "Choose a hair color",
    list(colors.keys())
)

st.write("Selected color:", color_name)

if photo is not None:
    st.image(
        photo,
        caption="Your original photo",
        use_container_width=True
    )

    st.info(
        "Your AI hair color preview will appear here!"
    )
