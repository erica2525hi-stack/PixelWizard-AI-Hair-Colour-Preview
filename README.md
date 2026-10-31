# 🪄 Pixel Wizard – AI Hair Colour Preview

사진 속 머리카락 영역을 AI로 인식하고 원하는 색상으로 바꿔 볼 수 있는 가상 염색 미리보기 프로젝트입니다.  
MediaPipe Hair Segmentation을 활용해 머리카락 영역을 분할하고, 선택한 RGB 색상을 해당 영역에 적용합니다.  
Python과 Streamlit을 사용하여 이미지 업로드부터 색상 조절, 결과 비교 및 다운로드까지 가능한 애플리케이션을 구현했습니다.

---

## Overview

Pixel Wizard is an AI-based hair colour preview application built with Python. It uses MediaPipe Hair Segmentation to detect hair regions in an uploaded photo and applies a selected colour to those regions.

Users can choose from different hair colours, adjust the colour intensity, compare the original and edited images, and download the result.

## Project Information

- **Project Period:** [2026.09 – 2026.10]
- **Development Environment:** Google Colab
- **Application Framework:** Streamlit

## Features

- Upload photos in JPG, JPEG, or PNG format
- Detect hair regions using MediaPipe Hair Segmentation
- Preview different hair colours
- Adjust colour intensity with a slider
- Compare original and edited images side by side
- Download the edited image as a PNG file

## How It Works

### 1. Hair Segmentation

The application uses MediaPipe's Hair Segmenter to identify hair regions in an image.

The model generates confidence masks, and a threshold of `0.75` is applied to select pixels classified as hair.

### 2. Hair Colour Application

The selected RGB colour is blended with the original image pixels within the detected hair mask.

The blending strength is controlled by an adjustable slider, allowing users to change the intensity of the selected colour.

### 3. Result Preview

The application displays the original and edited images side by side. Users can also download the edited image in PNG format.

## Development and Experiments

During development, I tested different segmentation approaches and explored ways to improve the quality of the hair mask.

- Explored segmentation approaches, including a SegFormer-based approach and MediaPipe Hair Segmentation.
- Experimented with confidence thresholds to control which pixels were included in the hair mask.
- Tested morphological operations, including opening and closing, to refine segmentation masks.
- Investigated unwanted segmentation around facial features, including eyebrows and eyes.
- Debugged image paths, variable definitions, and mask handling during implementation.

These experiments helped me understand that segmentation model outputs may require additional processing before they can be used in an image-editing application.

The current Streamlit application uses MediaPipe Hair Segmentation with a fixed confidence threshold of `0.75`. Additional mask-refinement experiments are documented in the Colab notebook and are not all integrated into the application.

## Tech Stack

- Python
- MediaPipe
- NumPy
- Pillow
- Streamlit
- Google Colab

## Development Workflow

The project was developed and tested in Google Colab. After implementation and experimentation, the project files were organised and uploaded to GitHub.

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/erica2525hi-stack/PixelWizard-AI-Hair-Colour-Preview.git
cd PixelWizard-AI-Hair-Colour-Preview
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the application

```bash
streamlit run app.py
```

The MediaPipe hair segmentation model is downloaded automatically when it is first needed by the application.

## Limitations and Future Improvements

- Segmentation quality may vary depending on lighting, hairstyle, and camera angle.
- The threshold-based mask may include nearby facial features.
- The current RGB blending method does not fully preserve the original hair's lighting and texture.
- More accurate hair boundaries and more natural-looking colour application could improve the results.

## What I Learned

Through this project, I gained practical experience in applying a pre-trained image segmentation model to an interactive application.

I learned how to work with confidence masks, adjust segmentation thresholds, apply image transformations to selected regions, and debug issues through iterative testing.

The project also showed me the importance of inspecting model outputs and handling their limitations when integrating machine learning models into an application.
