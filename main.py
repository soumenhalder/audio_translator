from audio_input import record_audio
from vad import apply_vad
from speaker_filter import filter_by_speaker
from translate import transcribe_and_translate
from output import output_text

def run_pipeline():
    raw_audio = record_audio()
    speech_audio = apply_vad(raw_audio)
    filtered_audio = filter_by_speaker(speech_audio)
    translated_text = transcribe_and_translate(filtered_audio)
    output_text(translated_text)

if __name__ == "__main__":
    run_pipeline()
