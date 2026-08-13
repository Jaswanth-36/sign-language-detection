# Dataset

The original project uses generated MediaPipe hand-landmark samples stored as `.npy` files. The cleaned public repository intentionally does not commit the full generated dataset because it contains thousands of training artifacts and would make the source repository unnecessarily large.

## Expected layout

```text
data/
└── dataset/
    ├── hello/
    ├── hi/
    ├── thank_you/
    └── ...
```

Each sample is a normalized landmark vector used by `train_model.py`.

To collect new samples, configure `auto_capture.py` and run it with a webcam. Then retrain the model with `train_model.py`.
