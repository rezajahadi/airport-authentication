# Face Detection & Verification App

A desktop application that detects and verifies passenger identities using face recognition and passport data. The app matches a live webcam image of the passenger with their stored passport photo through facial embeddings and similarity comparison.

## Overview

The system enables automated passenger identity verification by processing images through a deep learning and image-processing pipeline. The application retrieves passport data from a local database, captures a live image, and performs face verification by comparing the live image to the stored passport photo. The system also supports incremental learning, allowing new faces to be added and the model to be fine-tuned.

## Technical Details

* **Face Detection**: Performed using Haar Cascade classifiers.
* **Face Verification**: Uses facial embeddings extracted via a fine-tuned VGG-based model. Similarity between embeddings is measured using cosine similarity and Euclidean distance.
* **Model Fine-Tuning**: The app includes a training pipeline using an LBPH (Local Binary Patterns Histogram) recognizer to update the model with new faces, ensuring adaptability to new passengers.
* **Pre-trained VGG model**: You can access the pre-trained model throgh this link: https://drive.google.com/file/d/1RPuMVicG45dYBK_x5XfKOiLqLBvU8Xge/view

## How It Works

1. The user runs the application and inputs a passenger’s passport number through a GUI (built with PyQt5).
2. The app retrieves passenger details and displays them.
3. The system captures a live image of the passenger via webcam.
4. The app detects the face, extracts embeddings, and compares them with the stored passport photo.
5. If the similarity exceeds a predefined threshold, the passenger is verified.
6. New passenger faces can be added to the system and used to fine-tune the model via the integrated `face_training()` pipeline.

## Files

* `main.py` - Main GUI and application logic.
* `main_face_compare.py` - Face comparison and verification logic.
* `database.py` - Passenger database interface.
* `passengers.db` - SQLite database containing passenger information and photos.
* `trainer/` - Contains the Haar Cascade classifier and trained LBPH model.
* `face_training.py` - Script to fine-tune the LBPH recognizer on new faces.
* `dataset/` - Folder to store new training images.

## Requirements

* Python 3
* OpenCV
* PyQt5
* TensorFlow
* SQLite3
* PIL (Python Imaging Library)

## Credits

* Face detection based on Haar Cascade classifiers.
* Face embeddings extracted using a fine-tuned VGG-based model.
* LBPH recognizer used for incremental training on new faces.
