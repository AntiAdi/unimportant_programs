# Podcast Visualizer

2-shape animated visual for podcast where shapes glow when each speaker talks.


pip install -r requirements.txt



Steps :

1. put two speakers as speaker1.wav and speaker2.wav and speaker3.wav in audio file.
2. run the generate_timeline.py
3. manim -pqh visuals/talking_shapes.py TalkingShapes    : To generate the video.
4. python render_and_merge.py  : To get audio mixed into one.
5. python final.py  : To get output
