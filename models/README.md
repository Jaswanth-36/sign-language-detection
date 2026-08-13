# Model Artifacts

The application expects the trained classifier at:

```text
models/sign_dual_model.pkl
```

The model is intentionally excluded from Git tracking by `.gitignore` because trained binary artifacts are better versioned separately from source code.

If you already have the trained model locally, place it at the path above before running `app.py`.

To regenerate it from the landmark dataset, run:

```bash
python train_model.py
```
