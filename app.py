
import os
from io import BytesIO
from urllib.request import urlretrieve

import streamlit as st
import numpy as np
from PIL import Image
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision


st.set_page_config(
    page_title="Pixel Wizard",
    page_icon="🪄",
    layout="wide"
)

st.title("🪄 Pixel Wizard")
st.subheader("AI Virtual Hair Color Preview")
st.write("Upload a photo and preview a new hair color!")

MODEL_PATH = "hair_segmenter.tflite"
MODEL_URL = (
    "https://storage.googleapis.com/mediapipe-models/"
    "image_segmenter/hair_segmenter/float32/latest/"
    "hair_segmenter.tflite"
)

COLORS = {
    "💙 Blue": (60, 120, 255),
    "🩷 Pink": (255, 100, 180),
    "💜 Purple": (160, 80, 220),
    "❤️ Red": (230, 50, 60),
    "💚 Green": (60, 190, 100),
    "🩶 Silver": (180, 185, 200),
    "🖤 Black": (35, 30, 30),
    "🤍 White" : (0, 0, 0),
    "🤎 Dark Brown": (75, 45, 30),
    "💛 Golden Blonde": (220, 180, 90),
    "🧡 Orange": (240, 125, 45),
    
     # Natural browns
    "Chocolate Brown": (105, 65, 45),
    "Milk Tea Brown": (180, 140, 100),
    "Caramel Brown": (190, 125, 65),
    "Ash Brown": (125, 115, 105),
    "Light Brown": (160, 110, 70),

    # Blonde colors
    "Beige Blonde": (210, 190, 155),
    "Ash Blonde": (175, 170, 155),

    # Cool colors
    "Blue": (60, 120, 255),
    "🩵 Sky Blue": (100, 190, 255),
    "Navy Blue": (35, 50, 110),
    "Purple": (160, 80, 220),
    "Lavender": (190, 150, 230),
    "Pink": (255, 100, 180),
    "Pastel Pink": (255, 175, 205),

    # Vivid colors
    "Red": (230, 50, 60),
    "Burgundy": (120, 30, 55),
    "Green": (60, 190, 100),
    "Mint": (125, 220, 185),

    # Neutral colors
    "Silver": (180, 185, 200),
    "Ash Gray": (115, 120, 130),
   
}


@st.cache_resource
def load_segmenter():
    if not os.path.exists(MODEL_PATH):
        urlretrieve(MODEL_URL, MODEL_PATH)

    options = vision.ImageSegmenterOptions(
        base_options=python.BaseOptions(
            model_asset_path=MODEL_PATH
        ),
        output_confidence_masks=True
    )

    return vision.ImageSegmenter.create_from_options(options)


uploaded_file = st.file_uploader(
    "📷 Upload your photo",
    type=["jpg", "jpeg", "png"]
)

selected_color = st.selectbox(
    "🎨 Choose a hair color",
    list(COLORS.keys())
)

strength = st.slider(
    "Color intensity",
    min_value=0.1,
    max_value=1.0,
    value=0.5,
    step=0.1
)

if uploaded_file is not None:
    try:
        img = Image.open(uploaded_file).convert("RGB")

        st.image(
            img,
            caption="Original photo",
            use_container_width=True
        )

        if st.button("✨ Change Hair Color", type="primary"):
            with st.spinner("AI is detecting your hair..."):
                image_array = np.array(img)

                mp_image = mp.Image(
                    image_format=mp.ImageFormat.SRGB,
                    data=image_array
                )

                segmenter = load_segmenter()
                result = segmenter.segment(mp_image)

                if (
                    result.confidence_masks is None
                    or len(result.confidence_masks) < 2
                ):
                    st.error("Could not detect the hair mask.")
                    st.stop()

                hair_probability = np.squeeze(
                    result.confidence_masks[1].numpy_view()
                )

                # Select pixels likely to be hair
                hair_mask = hair_probability >= 0.75

                original = np.array(img).astype(np.float32)
                output = original.copy()

                target_color = np.array(
                    COLORS[selected_color],
                    dtype=np.float32
                )

                # Blend the selected color with the original hair
                output[hair_mask] = (
                    original[hair_mask] * (1 - strength)
                    + target_color * strength
                )

                output = np.clip(output, 0, 255).astype(np.uint8)
                result_image = Image.fromarray(output)

            st.success("Hair color preview is ready!")

            left, right = st.columns(2)

            with left:
                st.image(
                    img,
                    caption="Before",
                    use_container_width=True
                )

            with right:
                st.image(
                    result_image,
                    caption=f"After — {selected_color}",
                    use_container_width=True
                )

            buffer = BytesIO()
            result_image.save(buffer, format="PNG")

            st.download_button(
                "📥 Download result",
                data=buffer.getvalue(),
                file_name="pixel_wizard_result.png",
                mime="image/png"
            )

    except Exception as error:
        st.error(
            "Something went wrong. Please try again."
        )
        st.code(str(error))
