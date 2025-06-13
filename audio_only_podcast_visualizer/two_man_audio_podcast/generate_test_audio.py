# generate_test_audio.py

from gtts import gTTS
from pydub import AudioSegment
import os

def text_to_audio(text, filename):
    tts = gTTS(text)
    tts.save(filename)

def create_staggered_audio(speaker_id, times, text):
    silence = AudioSegment.silent(duration=10000)  # base 10s of silence
    voice_files = []

    for i, t in enumerate(times):
        file = f"tmp_{speaker_id}_{i}.mp3"
        text_to_audio(text, file)
        voice = AudioSegment.from_file(file)
        padding = AudioSegment.silent(duration=int(t * 1000))
        full = padding + voice
        voice_files.append(full)

    combined = silence.overlay(sum(voice_files))
    combined.export(f"audio/{speaker_id}.wav", format="wav")

    # cleanup
    for file in os.listdir():
        if file.startswith("tmp_") and file.endswith(".mp3"):
            os.remove(file)

if __name__ == "__main__":
    os.makedirs("audio", exist_ok=True)

    create_staggered_audio("speaker1", [0, 2, 4], "Hey there, I am speaker one.")
    create_staggered_audio("speaker2", [1, 3, 5], "Hello, I am speaker two.")
    
    print("[+] speaker1.wav and speaker2.wav generated in /audio")