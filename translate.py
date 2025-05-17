import whisper
from config import TRANSLATE_TO_LANG

model = whisper.load_model("medium")

def transcribe_and_translate(audio_path):
    result = model.transcribe(audio_path, task="translate", language=None)
    print("Translated text:", result["text"])
    return result["text"]
