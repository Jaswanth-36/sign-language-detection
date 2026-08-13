# Project Overview

## Objective

Recognize predefined hand signs from a live webcam feed and provide a readable and spoken interpretation.

## Processing Pipeline

1. Capture webcam frames with OpenCV.
2. Detect hands with MediaPipe.
3. Extract 21 landmarks per hand.
4. Normalize landmarks around the wrist.
5. Build a 126-value feature vector for up to two hands.
6. Classify the vector with a Random Forest model.
7. Apply confidence filtering and temporal stabilization.
8. Display the detected sign and optionally speak the translated phrase.

## Main Components

- `app.py`: production-style live inference loop.
- `train_model.py`: dataset loading, train/test split, training, evaluation, and model export.
- `auto_capture.py`: collection of normalized landmark samples.
- `test_live.py`: live prediction/testing workflow.
- `audio_manager.py`: text-to-speech and playback support.
- `language_map.py`: multilingual label mapping.
- `utils/hand_tracking.py`: MediaPipe tracking.
- `utils/landmarks.py`: feature extraction and normalization.

## Reproducibility

The source repository keeps generated datasets and local model binaries outside Git. This keeps the repository focused on maintainable source code while allowing the model and dataset to be regenerated or supplied separately.
