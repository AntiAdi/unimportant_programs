from pydub import AudioSegment
import numpy as np
import os

def rms_db(audio: AudioSegment) -> float:
    """Return RMS in dBFS (decibels relative to full scale)"""
    samples = np.array(audio.get_array_of_samples()).astype(np.float32)
    if audio.channels > 1:
        samples = samples.reshape((-1, audio.channels)).mean(axis=1)
    rms = np.sqrt(np.mean(samples ** 2))
    db = 20 * np.log10(rms / (2**15)) if rms > 0 else -float("inf")
    return db

def match_target_volume(audio: AudioSegment, target_db: float) -> AudioSegment:
    """Normalize audio to target RMS dB"""
    change_in_db = target_db - rms_db(audio)
    return audio.apply_gain(change_in_db)

def load_and_balance_audio(path1: str, path2: str) -> AudioSegment:
    a1 = AudioSegment.from_file(path1).set_channels(1)
    a2 = AudioSegment.from_file(path2).set_channels(1)

    db1 = rms_db(a1)
    db2 = rms_db(a2)
    median_db = (db1 + db2) / 2

    a1_balanced = match_target_volume(a1, median_db)
    a2_balanced = match_target_volume(a2, median_db)

    print(f"[+] Volume leveling complete: speaker1 {rms_db(a1_balanced):.2f} dB, speaker2 {rms_db(a2_balanced):.2f} dB")

    return a1_balanced.overlay(a2_balanced)

if __name__ == "__main__":
    out_path = "audio/final_audio.wav"
    mixed = load_and_balance_audio("audio/speaker1.wav", "audio/speaker2.wav")
    mixed.export(out_path, format="wav")
    print(f"[+] Exported mixed audio to {out_path}")