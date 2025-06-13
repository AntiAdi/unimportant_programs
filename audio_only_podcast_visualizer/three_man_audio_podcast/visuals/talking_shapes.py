import sys
import os
from manim import *

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from dialogue_timeline import dialogue

BLOOD_RED = "#8A0303"

class TalkingShapes(Scene):
    def construct(self):
        # Shape definitions with exact stroke settings
        square = Square(side_length=2).set_stroke(WHITE, width=8)
        triangle = Triangle().scale(1.5).set_stroke(BLOOD_RED, width=8)
        circle = Circle(radius=1).set_stroke(WHITE, width=8)

        # Positioning to form a triangle layout
        triangle.move_to(DOWN * 2.5)
        square.move_to(UP * 2.5 + LEFT * 3.5)
        circle.move_to(UP * 2.5 + RIGHT * 3.5)

        self.add(square, triangle, circle)

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

        speaker_times = {"speaker1": [], "speaker2": [], "speaker3": []}
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
        state = {"speaker1": False, "speaker2": False, "speaker3": False}

        for event_time, speaker, is_start in events:
            delta = event_time - current_time
            if delta > 0:
                # Fill based on speaking state
                square_fill = BLOOD_RED if state["speaker1"] else None
                triangle_fill = WHITE if state["speaker2"] else None
                circle_fill = BLOOD_RED if state["speaker3"] else None

                square.set_fill(square_fill, opacity=0.8 if square_fill else 0.0)
                triangle.set_fill(triangle_fill, opacity=0.8 if triangle_fill else 0.0)
                circle.set_fill(circle_fill, opacity=0.8 if circle_fill else 0.0)

                self.wait(delta)

            state[speaker] = is_start
            current_time = event_time

        # Reset all shapes
        square.set_fill(None, opacity=0.0)
        triangle.set_fill(None, opacity=0.0)
        circle.set_fill(None, opacity=0.0)