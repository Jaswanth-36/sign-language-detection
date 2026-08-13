import asyncio
import os
import tempfile
import threading
import time

USE_EDGE_TTS = True
SPEAK_GAP = 1.2

if USE_EDGE_TTS:
    import edge_tts
    import playsound

    class AudioManager:
        def __init__(self, gap=SPEAK_GAP):
            self.last_time = 0
            self.speak_gap = gap
            self.voice = "en-US-JennyNeural"
            self.rate = "+0%"
            self.volume = "+0%"

        async def _generate_and_play(self, text):
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as f:
                temp_audio = f.name

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
            now = time.time()
            if now - self.last_time < self.speak_gap:
                return

            self.last_time = now
            threading.Thread(
                target=lambda: asyncio.run(self._generate_and_play(text)),
                daemon=True,
            ).start()

        def cleanup(self):
            pass
else:
    import pyttsx3

    class AudioManager:
        def __init__(self, rate=170, gap=SPEAK_GAP):
            self.engine = pyttsx3.init(driverName="sapi5")
            self.engine.setProperty("rate", rate)
            self.engine.setProperty("volume", 1.0)
            self.last_time = 0
            self.speak_gap = gap

        def speak(self, text):
            now = time.time()
            if now - self.last_time >= self.speak_gap:
                try:
                    self.engine.stop()
                    self.engine.say(text)
                    self.engine.runAndWait()
                    self.last_time = now
                except RuntimeError:
                    pass

        def cleanup(self):
            self.engine.stop()
