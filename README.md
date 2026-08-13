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
├── code/                     # All application source code
│   ├── app/                  # Live application and testing
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
│   └── README.md
│
├── examples/                 # Demonstration assets
│   └── README.md
│
└── docs/                     # Detailed documentation
    ├── README.md
    └── project-overview.md
```

## ▶️ Quick Start

```bash
git clone https://github.com/Jaswanth-36/sign-language-detection.git
cd sign-language-detection
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Before running inference, place your trained model at:

```text
models/sign_dual_model.pkl
```

Then run the live application from the project root using the appropriate Python entry point documented in `code/app/`.

## 🎮 Real-Time Controls

| Key | Action |
|---|---|
| `1` | English |
| `2` | Hindi |
| `3` | Telugu |
| `4` | Tamil |
| `q` | Quit |

Example console output:

```text
Sign Language Detection - Live Test
1-English | 2-Hindi | 3-Telugu | 4-Tamil | q-Quit
Switched to Telugu
Detected sign: hello
Speech: namaste
```

> Console output is an example of the intended runtime interaction; exact predictions and accuracy depend on the webcam, environment and trained model.

## 🧪 Training Workflow

1. Collect landmark samples with `code/training/auto_capture.py`.
2. Samples are stored locally under `data/dataset/<sign>/`.
3. Train the Random Forest model with `code/training/train_model.py`.
4. The training script evaluates the held-out test split and saves `models/sign_dual_model.pkl`.
5. Run live inference and test the supported signs.

The original project contains thousands of generated `.npy` samples. They are intentionally excluded from the public source repository to keep it maintainable. The expected dataset structure is documented in `data/README.md`.

## 📊 Current Sign Vocabulary

The trained label set contains 41 classes, including common signs such as `hello`, `hi`, `thank_you`, `yes`, `no`, `please`, `water`, `help`, `stop`, `sorry`, `good`, `friend`, `school`, `work`, `you`, `your`, and others.

## 📈 Example Output

```text
Input gesture → hello
Confidence   → ≥ 0.55 threshold
Prediction   → hello
English      → hello
Hindi        → namaste
Telugu       → namaste
Tamil        → vanakkam
Audio        → generated speech
```

These are representative examples, not a claim of guaranteed accuracy for every webcam frame.

## 🔒 Repository Hygiene

Large generated datasets, local `.pkl`/`.joblib` models, temporary audio, caches, IDE files and other generated artifacts are excluded through `.gitignore`. This keeps the public repository focused on reproducible source code and documentation.

## 🚀 Future Improvements

- Add automated unit/integration tests
- Add model evaluation reports and confusion matrix
- Add a downloadable versioned model release
- Add a web interface
- Improve multilingual voices
- Expand sign vocabulary
- Add CI for code quality and testing

## 👨‍💻 Author

**Jaswanth Neerukattu**  
GitHub: [Jaswanth-36](https://github.com/Jaswanth-36)

## 📄 License

Released under the MIT License. See `LICENSE` for details.
