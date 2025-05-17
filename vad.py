import torchaudio

def apply_vad(audio_path):
    # Using torchaudio's simple VAD
    waveform, sample_rate = torchaudio.load(audio_path)
    vad = torchaudio.transforms.Vad(sample_rate=sample_rate)
    speech = vad(waveform)
    torchaudio.save("vad_output.wav", speech, sample_rate)
    return "vad_output.wav"
