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

## 🎨 Project Visuals

### Real-time system workflow

![Real-time sign language detection workflow](docs/images/system-workflow.svg)

This diagram explains the processing pipeline from webcam input through hand landmarks, feature extraction, prediction, Romanized translation, and speech output.

### Hand landmark feature extraction

![Hand landmark feature extraction](docs/images/feature-extraction.svg)

The model pipeline represents detected hand landmarks as numeric features before classification.

### Multilingual output

![Multilingual Romanized output](docs/images/multilingual-output.svg)

Hindi, Telugu and Tamil results are displayed using **English/Roman letters**, matching the project's UI approach rather than native-script characters.

### Runtime output gallery

![Runtime output gallery](docs/images/output-gallery.svg)

The gallery documents representative labels demonstrated by the live application, including `dislike`, `call karo`, `shanti`, `kettukonga`, `done`, and `hello`.

> **Important:** These are documentation graphics based on the project's demonstrated outputs. They are not fabricated screenshots and do not claim that every displayed example was produced by the model in the same session.

## 🎯 What the project does

The application uses a webcam to detect one or two hands, extracts **21 landmarks per hand**, converts them into a normalized feature vector, predicts the sign, displays the result, and can speak the translated word.

### Real-time example

```text
User shows a supported sign
        ↓
Webcam captures frame
        ↓
MediaPipe detects hand landmarks
        ↓
Landmarks are normalized
        ↓
Random Forest prediction
        ↓
Detected sign / class
        ↓
Selected language translation
        ↓
🔊 Speech output
```

## ✨ Features

- Real-time webcam recognition
- Single- and dual-hand landmark processing
- Hand-landmark feature extraction
- Random Forest classifier
- Confidence threshold and temporal smoothing
- English, Hindi, Telugu and Tamil output
- **Romanized multilingual text** using English letters
- Text-to-speech support
- Dataset collection utility
- Model training pipeline
- Clearly separated source, data, models, documentation and outputs

## 🗣️ Multilingual Output Format

The project represents Hindi, Telugu and Tamil output using **English/Roman letters**, rather than native-script characters.

Examples from the project's language map:

| Detected sign | English | Hindi | Telugu | Tamil |
|---|---|---|---|---|
| `hello` | hello | namaste | namaste | vanakkam |
| `thank_you` | thank you | dhanyavaad | dhanyavadamulu | nandri |
| `yes` | yes | haan | avunu | aam |
| `no` | no | nahi | kaadu | illai |
| `eat` | eat | khaana | tina | sapidu |
| `water` | water | paani | neellu | thanni |
| `call` | call | call karo | call cheyandi | call seyyunga |
| `done` | done | ho gaya | aipoyindi | mudichitu irukku |
| `peace` | peace | shanti | shanti | shanthiy |
| `listen` | listen | suno | vinandi | kettukonga |
| `you` | you | aap | meeru | neengal |

All examples above are written with English/Roman letters so they remain readable without requiring native-language fonts.

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
└── docs/
    ├── README.md             # Documentation index
    ├── project-overview.md   # Technical overview
    └── images/               # Professional project visuals
        ├── system-workflow.svg
        ├── feature-extraction.svg
        ├── multilingual-output.svg
        └── output-gallery.svg
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

The original project contains generated `.npy` samples. They are intentionally excluded from the public source repository to keep it maintainable.

## 📊 Sign Vocabulary

The project language map contains a broad vocabulary including `hello`, `hi`, `thank_you`, `yes`, `no`, `please`, `what`, `eat`, `water`, `sorry`, `good`, `help`, `stop`, `wait`, `go`, `call`, `completed`, `done`, `bad`, `name`, `where`, `why`, `peace`, `dislike`, `need`, `work`, `home`, `school`, `friend`, `listen`, `super`, `more`, `my`, `is`, `how`, `you`, `your`, and `there`.

## 📈 Example Output

```text
Input gesture → supported sign
Prediction    → detected class
English       → English label
Hindi         → Romanized Hindi
Telugu        → Romanized Telugu
Tamil         → Romanized Tamil
Audio         → generated speech
```

These are representative examples; actual predictions depend on the trained model, camera conditions, hand position, lighting and background.

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
