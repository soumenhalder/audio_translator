import sounddevice as sd
import soundfile as sf

def record_audio(duration=10, samplerate=16000, output_file="temp_audio.wav"):
    print("Recording...")
    audio = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1)
    sd.wait()
    sf.write(output_file, audio, samplerate)
    print(f"Saved to {output_file}")
    return output_file
