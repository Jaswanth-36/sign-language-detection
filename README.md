# 🤟 Sign Language Detection & Speech System

**Created and developed by Jaswanth Neerukattu.**

A personal machine-learning and computer-vision project for real-time sign-language recognition using a webcam, MediaPipe hand landmarks, and a Random Forest classifier, with multilingual text and speech output.

> **Authorship & provenance:** This repository is the public source repository for my original project. The source code, project organization, documentation, and development history are maintained under my GitHub account, **Jaswanth-36**. Git commits provide a public, timestamped development record.

## 👨‍💻 Author & Ownership

**Jaswanth Neerukattu**  
GitHub: [Jaswanth-36](https://github.com/Jaswanth-36)

This project is presented as my original work. If you use or reference this project, please credit **Jaswanth Neerukattu** and link back to this repository.

### Important note about proof of authorship

A public GitHub repository is useful evidence of authorship because GitHub records commits, timestamps, repository history, and the account that published them. However, a GitHub repository by itself is **not absolute legal proof** of authorship or the date the underlying work was first created. For stronger provenance, keep the original project ZIP/files, dated backups, college submissions, project reports, screenshots, and other development records in addition to this repository.

## 🎯 What the project does

The application uses a webcam to detect one or two hands, extracts **21 landmarks per hand**, converts them into a normalized **126-feature vector**, predicts the sign, displays the result, and can speak the translated word.

### Real-time example

```text
User shows: HELLO sign
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

## 🛠️ Technology Stack

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
├── README.md                 # Project overview + authorship information
├── .gitignore                # Git exclusions
├── requirements.txt          # Python dependencies
│
├── code/                     # All application source code
│   ├── app/                  # Live application and testing
│   ├── training/             # Training and dataset collection
│   ├── services/             # Audio and language services
│   └── utils/                # Computer-vision utilities
│
├── data/                     # Dataset documentation/location
├── models/                   # Trained model documentation/location
├── outputs/                  # Runtime/evaluation examples
├── examples/                 # Demonstration workflows
└── docs/                     # Detailed technical documentation
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

## 🎮 Real-Time Controls

| Key | Action |
|---|---|
| `1` | English |
| `2` | Hindi |
| `3` | Telugu |
| `4` | Tamil |
| `q` | Quit |

## 🧪 Training Workflow

1. Collect landmark samples with the dataset-collection script.
2. Samples are stored locally under `data/dataset/<sign>/`.
3. Train the Random Forest model.
4. The model is saved under `models/` locally.
5. Run live inference and evaluate supported signs.

The original project contains thousands of generated `.npy` samples. They are intentionally excluded from the public source repository to keep it maintainable.

## 📊 Current Sign Vocabulary

The trained label set contains 41 classes, including `hello`, `hi`, `thank_you`, `yes`, `no`, `please`, `water`, `help`, `stop`, `sorry`, `good`, `friend`, `school`, `work`, `you`, `your`, and others.

## 📈 Example Output

```text
Input gesture → HELLO
Prediction    → hello
English       → hello
Hindi         → namaste
Telugu        → namaste
Tamil         → vanakkam
Audio         → generated speech
```

These are representative examples, not a claim of guaranteed accuracy for every webcam frame.

## 🔒 Repository Hygiene

Large generated datasets, local model binaries, temporary audio, caches, IDE files and other generated artifacts are excluded through `.gitignore`.

## 📜 Copyright

© 2026 Jaswanth Neerukattu. All rights reserved unless otherwise stated.

This repository does **not** grant a general open-source license. Do not assume that the source code may be copied, redistributed, relicensed, or used commercially without the author's permission.

## 🚀 Future Improvements

- Add automated unit/integration tests
- Add model evaluation reports and confusion matrix
- Add a versioned model release
- Add a web interface
- Improve multilingual voices
- Expand sign vocabulary
- Add CI for code quality and testing
