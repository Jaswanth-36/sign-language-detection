from pathlib import Path
import ast
import importlib

PROJECT_ROOT = Path(__file__).resolve().parents[1]


def test_python_files_compile():
    for path in PROJECT_ROOT.joinpath("code").rglob("*.py"):
        ast.parse(path.read_text(encoding="utf-8"), filename=str(path))


def test_landmark_feature_shape():
    landmarks = importlib.import_module("code.utils.landmarks")
    hand = [[float(i), float(i) * 0.1, 0.0] for i in range(21)]
    features = landmarks.normalize_landmarks_dual(hand)
    assert features is not None
    assert features.shape == (126,)


def test_language_map_keys_have_all_languages():
    language_map = importlib.import_module("code.services.language_map").LANGUAGE_MAP
    required = {"en", "hi", "te", "ta"}
    assert language_map
    for label, translations in language_map.items():
        assert required.issubset(translations), f"Missing language for {label}"


def test_required_runtime_files_exist():
    for relative in [
        "requirements.txt",
        "code/app/app.py",
        "code/app/test_live.py",
        "code/training/train_model.py",
        "code/training/auto_capture.py",
        "code/utils/hand_tracking.py",
        "code/utils/landmarks.py",
        "code/services/audio_manager.py",
        "code/services/language_map.py",
    ]:
        assert PROJECT_ROOT.joinpath(relative).is_file(), relative
