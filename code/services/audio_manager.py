import asyncio
import os
import tempfile
import threading
import time

SPEAK_GAP = 1.2

try:
    import edge_tts
    import playsound
except ImportError:
    edge_tts = None
    playsound = None

try:
    import pyttsx3
except ImportError:
    pyttsx3 = None


class AudioManager:
    """Manage speech output with Edge TTS and a local fallback."""

    def __init__(self, gap=SPEAK_GAP):
        self.last_time = 0.0
        self.speak_gap = gap
        self.voice = "en-US-JennyNeural"
        self.rate = "+0%"
        self.volume = "+0%"
        self.engine = None

        if edge_tts is None or playsound is None:
            if pyttsx3 is not None:
                self.engine = pyttsx3.init()
                self.engine.setProperty("rate", 170)
                self.engine.setProperty("volume", 1.0)

    async def _generate_and_play(self, text):
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as file:
            temp_audio = file.name

        try:
            communicate = edge_tts.Communicate(
                text=text,
                voice=self.voice,
                rate=self.rate,
                volume=self.volume,
            )
            await communicate.save(temp_audio)
            playsound.playsound(temp_audio)
        finally:
            if os.path.exists(temp_audio):
                os.remove(temp_audio)

    def speak(self, text):
        if not text:
            return

        now = time.time()
        if now - self.last_time < self.speak_gap:
            return
        self.last_time = now

        if edge_tts is not None and playsound is not None:
            threading.Thread(
                target=lambda: asyncio.run(self._generate_and_play(text)),
                daemon=True,
            ).start()
        elif self.engine is not None:
            try:
                self.engine.stop()
                self.engine.say(text)
                self.engine.runAndWait()
            except RuntimeError:
                pass

    def cleanup(self):
        if self.engine is not None:
            try:
                self.engine.stop()
            except RuntimeError:
                pass
