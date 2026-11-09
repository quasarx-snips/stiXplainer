from manim import *

class StudioSmokeTest(Scene):
    """Short render proving that characters and motion can be produced."""

    def construct(self):
        title = Text("stiXplainer", font_size=52, weight=BOLD)
        subtitle = Text("Stories, explained through motion.", font_size=24)
        subtitle.next_to(title, DOWN, buff=0.35)
        self.play(Write(title), run_time=1.5)
        self.play(FadeIn(subtitle, shift=UP * 0.2), run_time=1)
        self.wait(1)
        self.play(FadeOut(VGroup(title, subtitle)), run_time=1)
