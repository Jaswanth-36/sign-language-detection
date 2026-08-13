# Example Workflow

## Real-time detection

1. Start the webcam application.
2. Show a supported hand sign.
3. MediaPipe extracts the hand landmarks.
4. The landmarks are normalized into a 126-feature vector.
5. The Random Forest model predicts the class.
6. The application displays the translated result.
7. The audio service speaks the result.

### Example

```text
HELLO gesture
    ↓
hello
    ↓
English: hello
Hindi: namaste
Telugu: namaste
Tamil: vanakkam
    ↓
Speech output
```
