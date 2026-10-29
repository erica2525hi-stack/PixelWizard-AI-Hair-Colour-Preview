# Pixel Wizard - AI Hair Color Preview

Pixel Wizard is an AI-based project that identifies hair regions in a photo and applies a new color to preview different hair-color options. The goal is to help users explore possible hair colors before deciding to dye their hair.

## About the Project

It can be difficult to know how a hair color will look before actually dyeing your hair. Pixel Wizard was created to explore a simple solution: detect the hair region in an image, apply a selected color, and let users view the result.

During development, I found that applying color was only part of the problem. The hair mask also needed to avoid areas such as the eyebrows and eyes, where unwanted color changes could make the result look unnatural.

## Features

- Hair-color preview using an image
- AI-based hair segmentation
- Color application limited to the detected hair region
- Visual comparison with the original image
- Hair-mask adjustments to reduce unwanted color changes

## Development and Improvements

The project was improved through testing and debugging.

### 1. Hair Segmentation

I used MediaPipe hair segmentation to identify hair regions. The model's confidence values were used to create a binary mask, and the threshold was adjusted to control which pixels were treated as hair.

### 2. Mask Refinement

The initial mask did not always isolate the hair cleanly. Some nearby areas could also be affected by the new color. I experimented with mask refinement and morphological operations to reduce unwanted regions.

### 3. Protecting Eyebrows and Eyes

During testing, I noticed that color could affect the eyebrows and pupils. I adjusted the mask threshold and refinement process, and experimented with excluding specific areas. This showed that accurately separating hair from other facial features is just as important as applying the color itself.

The results can still vary depending on the image, lighting, hairstyle, and camera angle. Protecting every non-hair region perfectly remains an area for further improvement.

### 4. Testing and Debugging

The development process involved fixing issues such as undefined variables, image-path errors, and inconsistencies between mask variables. Instead of treating the first working result as finished, I tested the output, identified problems, and made changes step by step.

## Tech Stack

- Python
- Streamlit
- MediaPipe
- NumPy
- Pillow
- SciPy
- Google Colab

## How to Run

1. Clone the repository.

   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Install the required libraries.

   ```bash
   pip install streamlit mediapipe numpy pillow scipy
   ```

3. Run the Streamlit application. Replace `app.py` with the actual name of the app file if it is different.

   ```bash
   streamlit run app.py
   ```

Additional configuration may be required depending on the library versions. Check the files and dependencies included in the repository before running the application.

## Future Improvements

- Improve the separation between hair and facial features
- Reduce unwanted color changes on eyebrows, pupils, and skin
- Test the application with different hairstyles and lighting conditions
- Make color selection and previewing easier
- Improve the interface for comparing the original and edited images
- Make the applied colors look more natural

## What I Learned

This project taught me that using an AI model's output directly is not always enough. Getting a useful result also requires checking predictions, refining the mask, testing different images, and fixing issues as they appear.

Pixel Wizard is an ongoing project that improves through experimentation and iteration.

## Test Image and Usage

A photo of Choi San, a member of ATEEZ, was used during development to test the hair-color preview feature and evaluate hair segmentation.

The image may be subject to copyright held by its original rights holder. The rights to the image are separate from the project code. Before publishing the image in a public repository or service, its source and applicable usage permissions should be checked.
