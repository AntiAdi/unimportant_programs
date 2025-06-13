from gtts import gTTS
from pydub import AudioSegment
import os

def text_to_audio(text, filename):
    tts = gTTS(text)
    tts.save(filename)

def create_staggered_audio(speaker_id, times, text):
    silence = AudioSegment.silent(duration=20000)  # Base 20s of silence
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

    # Cleanup
    for file in os.listdir():
        if file.startswith("tmp_") and file.endswith(".mp3"):
            os.remove(file)

if __name__ == "__main__":
    os.makedirs("audio", exist_ok=True)

    create_staggered_audio("speaker1", [0, 4, 8], "Hey there, I am speaker one.")
    create_staggered_audio("speaker2", [2, 6, 10], "Hello, I am speaker two.")
    create_staggered_audio("speaker3", [1, 5, 9], "Yo, this is speaker three.")

    print("[+] speaker1.wav, speaker2.wav, and speaker3.wav generated in /audio")