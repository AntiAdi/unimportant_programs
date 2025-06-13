import subprocess
import os

def merge_audio_video(video_path, audio_path, output_path):
    if not os.path.exists(video_path):
        raise FileNotFoundError(f"Video not found: {video_path}")
    if not os.path.exists(audio_path):
        raise FileNotFoundError(f"Audio not found: {audio_path}")
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    command = [
        "ffmpeg",
        "-y",  # overwrite output file without asking
        "-i", video_path,
        "-i", audio_path,
        "-c:v", "copy",       # copy video stream without re-encoding
        "-c:a", "aac",        # encode audio to aac for wide compatibility
        "-b:a", "192k",       # decent audio bitrate
        "-map", "0:v:0",      # take video from first input
        "-map", "1:a:0",      # take audio from second input
        "-shortest",          # stop encoding at the shortest input length
        output_path
    ]

    print(f"[+] Running ffmpeg to merge video and audio...")
    subprocess.run(command, check=True)
    print(f"[+] Merged file created at {output_path}")

if __name__ == "__main__":
    video_file = "media/videos/talking_shapes/1080p60/TalkingShapes.mp4"
    audio_file = "audio/final_audio.wav"
    output_file = "final_output/FinalVideoWithAudio.mp4"

    merge_audio_video(video_file, audio_file, output_file)