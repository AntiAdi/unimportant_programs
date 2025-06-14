from pydub import AudioSegment
import numpy as np
import librosa
import os

# SETTINGS
CHUNK_MS = 50             # Frame duration to analyze
THRESHOLD_DB = -35        # Below this = silence
MIN_SPEECH_MS = 300       # Minimum duration for valid speech block

def detect_speech_segments(file_path, speaker_id):
    audio = AudioSegment.from_file(file_path).set_channels(1)
    chunks = list(audio[::CHUNK_MS])
    speech_flags = []

    for chunk in chunks:
        samples = np.array(chunk.get_array_of_samples()).astype(np.float32)
        if len(samples) == 0:
            speech_flags.append(False)
            continue

        rms = librosa.feature.rms(y=samples, frame_length=len(samples), hop_length=len(samples)//2)[0][0]
        db = librosa.amplitude_to_db([rms])[0]
        speech_flags.append(db > THRESHOLD_DB)

    # Group into speech blocks
    blocks = []
    in_speech = False
    start_idx = 0

    for i, speaking in enumerate(speech_flags):
        if speaking and not in_speech:
            in_speech = True
            start_idx = i
        elif not speaking and in_speech:
            end_idx = i
            duration_ms = (end_idx - start_idx) * CHUNK_MS
            if duration_ms >= MIN_SPEECH_MS:
                blocks.append((start_idx * CHUNK_MS / 1000.0, duration_ms / 1000.0))
            in_speech = False

    # Catch end block
    if in_speech:
        end_idx = len(speech_flags)
        duration_ms = (end_idx - start_idx) * CHUNK_MS
        if duration_ms >= MIN_SPEECH_MS:
            blocks.append((start_idx * CHUNK_MS / 1000.0, duration_ms / 1000.0))

    return [(round(start, 2), speaker_id, round(dur, 2)) for start, dur in blocks]

def combine_timelines(*tracks):
    combined = sum(tracks, [])
    combined.sort(key=lambda x: x[0])  # Sort by start time
    return combined

def save_timeline(timeline):
    with open("dialogue_timeline.py", "w") as f:
        f.write("# Auto-generated by generate_timeline.py\n")
        f.write("dialogue = [\n")
        for start, speaker, dur in timeline:
            f.write(f"    ({start}, '{speaker}', {dur}),\n")
        f.write("]\n")
    print("[+] dialogue_timeline.py generated.")

if __name__ == "__main__":
    print("Analyzing audio...")

    t1 = detect_speech_segments("audio/speaker1.wav", "speaker1")
    t2 = detect_speech_segments("audio/speaker2.wav", "speaker2")
    t3 = detect_speech_segments("audio/speaker3.wav", "speaker3")

    combined = combine_timelines(t1, t2, t3)
    save_timeline(combined)