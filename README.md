# 🤟 Sign Language Detection & Speech System

Real-time sign-language recognition using **MediaPipe hand landmarks + Random Forest**, with multilingual text and speech output.

## 🎯 What the project does

The application uses a webcam to detect one or two hands, extracts **21 landmarks per hand**, converts them into a normalized **126-feature vector**, predicts the sign, displays the result, and can speak the translated word.

### Real-time example

```text
User shows:  👋  HELLO sign
        ↓
Webcam captures frame
        ↓
MediaPipe detects hand landmarks
        ↓
126 normalized features
        ↓
Random Forest prediction
        ↓
Detected sign: hello
        ↓
English: hello
Hindi: namaste
Telugu: namaste
Tamil: vanakkam
        ↓
🔊 Speech output
```

## ✨ Features

- Real-time webcam recognition
- Single- and dual-hand landmark processing
- 126 normalized landmark features
- Random Forest classifier
- Confidence threshold and temporal smoothing
- English, Hindi, Telugu and Tamil output
- Text-to-speech support
- Dataset collection utility
- Model training pipeline
- Clearly separated source, data, models, documentation and outputs

## 🧠 Technology Stack

| Area | Technology |
|---|---|
| Language | Python |
| Computer vision | OpenCV |
| Hand tracking | MediaPipe |
| Numerical processing | NumPy |
| Machine learning | scikit-learn Random Forest |
| Model storage | Joblib |
| Speech | Edge TTS / pyttsx3 |

## 📁 Professional Project Structure

```text
sign-language-detection/
│
├── README.md                 # Main project documentation
├── LICENSE                   # MIT license
├── .gitignore                # Files excluded from Git
├── requirements.txt          # Python dependencies
│
├── code/                     # All Python source code
│   ├── app/                  # Live application and testing
│   │   ├── app.py
│   │   └── test_live.py
│   ├── training/             # Training and dataset collection
│   │   ├── train_model.py
│   │   └── auto_capture.py
│   ├── services/             # Audio and language services
│   │   ├── audio_manager.py
│   │   └── language_map.py
│   └── utils/                # Reusable computer-vision utilities
│       ├── hand_tracking.py
│       └── landmarks.py
│
├── data/                     # Training-data documentation/location
│   └── README.md
│
├── models/                   # Trained model documentation/location
│   └── README.md
│
├── outputs/                  # Runtime/evaluation outputs
│   ├── README.md
│   └── examples/
│       └── prediction-output.txt
│
├── examples/                 # Demonstration workflows
│   ├── README.md
│   └── sample-workflow.md
│
└── docs/                     # Detailed documentation
    ├── README.md
    └── project-overview.md
```

## ⚙️ Installation

```bash
git clone https://github.com/Jaswanth-36/sign-language-detection.git
cd sign-language-detection
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

macOS/Linux:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## 🤖 Model Setup

Place the trained classifier at:

```text
models/sign_dual_model.pkl
```

The trained binary is intentionally excluded from the source repository. See `models/README.md` for the model workflow.

## ▶️ Run the Real-Time Application

From the repository root:

```bash
python -m code.app.app
```

For the live testing program:

```bash
python -m code.app.test_live
```

## 🎮 Real-Time Controls

| Key | Action |
|---|---|
| `1` | English |
| `2` | Hindi |
| `3` | Telugu |
| `4` | Tamil |
| `q` | Quit |

## 🧪 Training Workflow

### 1. Collect samples

Configure `SIGN_NAME` and `SAMPLES` in `code/training/auto_capture.py`, then run:

```bash
python -m code.training.auto_capture
```

Samples are generated locally under:

```text
data/dataset/<sign-name>/
```

### 2. Train the classifier

```bash
python -m code.training.train_model
```

Example training output:

```text
Accuracy: 94.25%
Model saved to models/sign_dual_model.pkl
```

> The percentage above is an example format, not a measured result for this repository. Actual accuracy depends on the dataset and train/test split.

### 3. Test live recognition

```bash
python -m code.app.test_live
```

## 📊 Real-Time Example

```text
Sign Language Detection - Live Test
1-English | 2-Hindi | 3-Telugu | 4-Tamil | q-Quit

User performs: HELLO
Prediction: hello
English: hello
Hindi: namaste
Telugu: namaste
Tamil: vanakkam
Speech: generated
```

The repository includes a representative output file at `outputs/examples/prediction-output.txt`.

## 📈 Recognition Pipeline

```text
Webcam Frame
     ↓
OpenCV
     ↓
MediaPipe Hand Tracking
     ↓
21 landmarks × 1–2 hands
     ↓
Wrist-centered normalization
     ↓
126 numerical features
     ↓
Random Forest
     ↓
Confidence filtering
     ↓
Temporal smoothing
     ↓
Sign label
     ↓
Language translation
     ↓
Text + Speech
```

## 🌐 Supported Output Languages

- English
- Hindi
- Telugu
- Tamil

The current trained label vocabulary contains 41 classes, including `hello`, `hi`, `thank_you`, `yes`, `no`, `please`, `water`, `help`, `stop`, `sorry`, `good`, `friend`, `school`, `work`, `you`, `your`, and others.

## 💾 Dataset Policy

The original project contains thousands of generated `.npy` landmark samples. These are intentionally excluded from the public Git repository to keep the project clean and manageable. The expected dataset structure and collection workflow are documented in `data/README.md`.

## 📦 Output Policy

`outputs/` is reserved for generated evaluation reports, prediction logs, screenshots and demonstrations. Temporary runtime files should not be committed.

## 🔒 Repository Hygiene

The `.gitignore` excludes Python caches, virtual environments, IDE metadata, local model artifacts, generated datasets, temporary audio and other generated files. This keeps the public repository focused on reproducible source code and documentation.

## 🚀 Future Improvements

- Automated unit and integration tests
- Confusion matrix and detailed evaluation reports
- Versioned model releases
- Web-based interface
- Improved multilingual voices
- Expanded sign vocabulary
- CI for code quality and testing

## 👨‍💻 Author

**Jaswanth Neerukattu**  
GitHub: [Jaswanth-36](https://github.com/Jaswanth-36)

## 📄 License

Released under the MIT License. See `LICENSE` for details.
