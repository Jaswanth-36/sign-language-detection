# Sign Language Detection & Speech System

A real-time computer-vision application that recognizes hand signs from a webcam using MediaPipe hand landmarks and a Random Forest classifier, then displays and speaks the recognized meaning in multiple languages.

## ✨ Features

- Real-time webcam-based sign recognition
- Dual-hand landmark processing (126 normalized features)
- MediaPipe hand landmark tracking
- Random Forest classification
- Prediction confidence thresholding and temporal smoothing
- Text-to-speech output
- Language switching between English, Hindi, Telugu, and Tamil
- Dataset collection utility for creating new training samples
- Separate training and live-inference scripts

## 🧠 How It Works

```text
Webcam
  ↓
MediaPipe Hand Tracking
  ↓
21 landmarks × up to 2 hands
  ↓
Wrist-centered normalization
  ↓
126-feature vector
  ↓
Random Forest classifier
  ↓
Stable sign prediction
  ↓
Translated text + speech
```

The application uses normalized hand landmarks instead of raw images. This makes the model lightweight and reduces dependence on background and lighting compared with image-only approaches.

## 🛠️ Technologies

- Python
- OpenCV
- MediaPipe
- NumPy
- scikit-learn
- Joblib
- Edge TTS
- Playsound

## 📁 Project Structure

```text
sign-language-detection/
├── README.md
├── LICENSE
├── .gitignore
├── requirements.txt
├── app.py                 # Main real-time application
├── test_live.py           # Live inference/testing script
├── train_model.py         # Model training pipeline
├── auto_capture.py        # Webcam dataset collection utility
├── audio_manager.py       # Text-to-speech handling
├── language_map.py        # Multilingual sign translations
├── utils/
│   ├── __init__.py
│   ├── hand_tracking.py   # MediaPipe hand tracking
│   └── landmarks.py       # Landmark normalization
├── models/
│   └── README.md          # Model artifact instructions
├── data/
│   └── README.md          # Dataset instructions
└── docs/
    └── project-overview.md
```

## 🌐 Supported Signs

The current trained label set contains 41 classes:

`Home`, `bad`, `call`, `completed`, `dislike`, `done`, `eat`, `friend`, `go`, `good`, `hello`, `help`, `hi`, `how`, `i don't know`, `is`, `keep quite`, `listen`, `more`, `my`, `name`, `need`, `nice to meet you`, `no`, `peace`, `please`, `school`, `sorry`, `stop`, `super`, `thank_you`, `there`, `wait`, `water`, `what`, `where`, `why`, `work`, `yes`, `you`, `your`.

> Note: the label `keep quite` is retained because it is part of the existing trained dataset; it can be renamed in a future retraining pass if desired.

## ⚙️ Installation

Python 3.10 or 3.11 is recommended for the current MediaPipe/scikit-learn stack.

```bash
git clone https://github.com/Jaswanth-36/sign-language-detection.git
cd sign-language-detection
python -m venv .venv
```

### Windows

```bash
.venv\Scripts\activate
```

### macOS / Linux

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## 🤖 Model

The application expects the trained model at:

```text
models/sign_dual_model.pkl
```

The trained model is a binary artifact and is intentionally kept out of the source-code commit in this cleaned repository. See `models/README.md` for how to add or regenerate it.

## ▶️ Run the Application

After placing the trained model at `models/sign_dual_model.pkl`:

```bash
python app.py
```

Keyboard controls:

| Key | Language |
|---|---|
| `1` | English |
| `2` | Hindi |
| `3` | Telugu |
| `4` | Tamil |
| `q` | Quit |

## 🧪 Train the Model

Place landmark `.npy` samples under:

```text
data/dataset/<sign-name>/
```

Then run:

```bash
python train_model.py
```

The training script loads 126-feature landmark vectors, performs a stratified train/test split, trains a Random Forest classifier, reports test accuracy, and saves the model as `models/sign_dual_model.pkl`.

## 📷 Collect New Training Samples

Edit `SIGN_NAME` and `SAMPLES` in `auto_capture.py`, then run:

```bash
python auto_capture.py
```

The webcam utility saves normalized landmark vectors as `.npy` files under the selected sign directory.

## 🔊 Speech Output

The application uses Edge TTS with a neural English voice by default and `playsound` for playback. An internet connection may be required when Edge TTS generates speech.

## 📊 Dataset

The original project contains a large collection of landmark `.npy` samples. These generated training artifacts are intentionally not committed to the public source repository. See `data/README.md` for the recommended dataset workflow.

## 🚀 Future Improvements

- Add a reproducible dataset download/versioning workflow
- Add automated evaluation metrics and a confusion matrix
- Add configurable confidence thresholds
- Improve multilingual speech voices
- Add a graphical user interface
- Package the application for Windows
- Add automated tests and CI
- Version trained models separately from source code

## 👨‍💻 Author

**Jaswanth Neerukattu**

GitHub: [@Jaswanth-36](https://github.com/Jaswanth-36)

---

This project is intended for educational and research purposes.
