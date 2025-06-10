# Face Detection App

This project uses image processing and deep learning to detect faces in passengers' photos and compare them against a database of stored photos. 

## Overview

The app loads a deep learning model trained to detect faces in images. When a new passenger photo is input, the model detects any faces and extracts facial embeddings. These embeddings are compared against stored embeddings for known passengers using cosine similarity. If a match is found, the passenger is identified.

## Usage

1. Ensure you have Python 3 and the requirements installed.

2. Download the pre-trained face detection model from [Google Drive](https://drive.google.com/file/d/1RPuMVicG45dYBK_x5XfKOiLqLBvU8Xge/view?usp=sharing) and place in the `trainer` folder. 
3. Run `python app.py` to start the app. 

4. Input a passenger photo file path when prompted. 

5. The app will detect any faces, extract embeddings, compare against known passengers in `passengers.db` and output the identified passenger name if a match is found.

## Files

- `app.py` - Main application logic
- `detect.py` - Functions for face detection and embedding
- `database.py` - Passenger database interface
- `passengers.db` - SQLite database containing passenger names and facial embeddings
- `trainer/` - Folder containing pre-trained face detection model files

## Requirements

- Python 3
- OpenCV 
- SQLite3
- Tensorflow

## Credits

The face detection model is a [pre-trained ResNet model](https://drive.google.com/file/d/1CPSeum3HpopfomUEK1gybeuIVoeJT_Eo/view) from Anthropic. The database stores facial embeddings extracted using this model.
