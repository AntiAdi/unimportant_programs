import sys
import os
from manim import *

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from dialogue_timeline import dialogue

class TalkingShapes(Scene):
    def construct(self):
        square = Square(side_length=2).set_stroke(WHITE, width=8).move_to(LEFT * 3)
        triangle = Triangle().scale(1.5).set_stroke(RED, width=8).move_to(RIGHT * 3)

        self.add(square, triangle)

        # Merge speaking intervals per speaker
        def merge_intervals(intervals):
            intervals.sort()
            merged = []
            for start, end in intervals:
                if merged and start <= merged[-1][1]:
                    merged[-1] = (merged[-1][0], max(merged[-1][1], end))
                else:
                    merged.append((start, end))
            return merged

        speaker_times = {"speaker1": [], "speaker2": []}
        for start, speaker, dur in dialogue:
            speaker_times[speaker].append((start, start + dur))
        for speaker in speaker_times:
            speaker_times[speaker] = merge_intervals(speaker_times[speaker])

        # Timeline of fill state changes
        events = []
        for speaker, intervals in speaker_times.items():
            for start, end in intervals:
                events.append((start, speaker, True))
                events.append((end, speaker, False))
        events.sort()

        current_time = 0.0
        state = {"speaker1": False, "speaker2": False}

        for event_time, speaker, is_start in events:
            delta = event_time - current_time
            if delta > 0:
                # Fill based on speaking state
                square_fill = RED if state["speaker1"] else None
                triangle_fill = WHITE if state["speaker2"] else None

                square.set_fill(square_fill, opacity=0.8 if square_fill else 0.0)
                triangle.set_fill(triangle_fill, opacity=0.8 if triangle_fill else 0.0)

                # Wait for the actual audio duration
                self.wait(delta)

            state[speaker] = is_start
            current_time = event_time

        # Reset shapes to unlit
        square.set_fill(None, opacity=0.0)
        triangle.set_fill(None, opacity=0.0)