# Text Extraction with OpenCV, EasyOCR, and Streamlit

## Overview

This project is a simple Optical Character Recognition (OCR) web application built with **Streamlit**, **OpenCV**, and **EasyOCR**. It allows users to upload an image, automatically detect a document-like region, apply perspective correction, extract text from the image, and display both the detected text and the processed image.

The application is designed to improve OCR accuracy by:

* Detecting the largest contours in an image
* Applying perspective transformation
* Rotating the transformed image when necessary
* Using adaptive thresholding for better text visibility
* Extracting text with EasyOCR

---

## Features

* Upload JPG, JPEG, and PNG images
* Automatic image resizing for large images
* Contour detection and document extraction
* Perspective correction
* OCR text extraction using EasyOCR
* Display detected text regions
* User-friendly Streamlit interface

---

## Technologies Used

* Python
* OpenCV (`cv2`)
* NumPy
* Streamlit
* EasyOCR
* Pillow (PIL)

---

## Installation

Install the required dependencies:

```bash
pip install opencv-python numpy streamlit easyocr pillow
```

---

## Running the Application

Start the Streamlit server:

```bash
streamlit run app.py
```

Then open your browser and navigate to:

```text
http://localhost:8501
```

---

## How It Works

### 1. Image Upload

The user uploads an image through the Streamlit interface.

### 2. Image Resizing

Large images are automatically resized until both dimensions are below 900 pixels.

### 3. Contour Detection

The image is converted to grayscale, blurred, and processed with Canny edge detection. External contours are then extracted and sorted by area.

### 4. Perspective Transformation

The application searches for quadrilateral contours (4-sided shapes), assuming they represent a document or text region.

### 5. OCR Processing

The transformed image is:

* Converted to grayscale
* Thresholded using adaptive thresholding
* Passed to EasyOCR for text recognition

### 6. Display Results

The application displays:

* The processed image with text bounding boxes
* Extracted text results

---

## Recommendations for Better Results

* Use high-resolution images.
* Ensure text is clearly visible.
* Minimize background clutter.
* Avoid blurry images.
* Capture documents from a straight angle when possible.
* Ensure sufficient lighting.

---

## Requirements

```text
opencv-python
numpy
streamlit
easyocr
pillow
```

---

## Limitations

This OCR system is based on traditional image preprocessing techniques and EasyOCR. While it can perform well on clear, high-quality images, its accuracy is generally lower than modern OCR solutions powered by advanced deep learning and multimodal AI models. Performance may decrease significantly when processing blurry images, complex layouts, handwritten text, or images with challenging lighting conditions.

---

## License

This project is provided for educational and learning purposes. Feel free to modify and improve it according to your needs.
