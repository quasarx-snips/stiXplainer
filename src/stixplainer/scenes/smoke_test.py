from manim import *


def stick_figure(color=WHITE, scale=1.0):
    """Create a simple reusable stick-figure character."""
    head = Circle(radius=0.22, color=color, stroke_width=4)
    head.move_to(UP * 1.05)
    body = Line(UP * 0.82, DOWN * 0.25, color=color, stroke_width=4)
    left_arm = Line(UP * 0.55, LEFT * 0.48 + UP * 0.12, color=color, stroke_width=4)
    right_arm = Line(UP * 0.55, RIGHT * 0.48 + UP * 0.12, color=color, stroke_width=4)
    left_leg = Line(DOWN * 0.25, LEFT * 0.38 + DOWN * 0.85, color=color, stroke_width=4)
    right_leg = Line(DOWN * 0.25, RIGHT * 0.38 + DOWN * 0.85, color=color, stroke_width=4)
    figure = VGroup(head, body, left_arm, right_arm, left_leg, right_leg)
    figure.scale(scale)
    return figure


class StudioSmokeTest(Scene):
    """A short animated proof with two presenters and a city heat visual."""

    def construct(self):
        title = Text("stiXplainer", font_size=48, weight=BOLD)
        subtitle = Text("Stories, explained through motion.", font_size=22)
        subtitle.next_to(title, DOWN, buff=0.25)
        self.play(Write(title), FadeIn(subtitle, shift=UP * 0.15), run_time=2)
        self.wait(0.5)
        self.play(FadeOut(VGroup(title, subtitle)), run_time=0.6)

        presenter_a = stick_figure(BLUE).move_to(LEFT * 3.7 + DOWN * 0.25)
        presenter_b = stick_figure(GREEN).move_to(RIGHT * 3.7 + DOWN * 0.25)
        label_a = Text("MAYA", font_size=18, color=BLUE).next_to(presenter_a, DOWN, buff=0.15)
        label_b = Text("LEO", font_size=18, color=GREEN).next_to(presenter_b, DOWN, buff=0.15)

        sun = Circle(radius=0.42, color=YELLOW, fill_color=YELLOW, fill_opacity=1)
        sun.move_to(UP * 2.5 + RIGHT * 4.7)
        rays = VGroup(*[
            Line(
                sun.get_center() + 0.58 * np.array([np.cos(a), np.sin(a), 0]),
                sun.get_center() + 0.82 * np.array([np.cos(a), np.sin(a), 0]),
                color=YELLOW, stroke_width=3
            )
            for a in np.linspace(0, TAU, 12, endpoint=False)
        ])

        buildings = VGroup(
            Rectangle(width=1.0, height=2.0, color=GREY_B, fill_color=GREY_E, fill_opacity=1).move_to(LEFT * 1.5 + DOWN * 1.1),
            Rectangle(width=1.15, height=2.8, color=GREY_B, fill_color=GREY_D, fill_opacity=1).move_to(DOWN * 0.7),
            Rectangle(width=0.9, height=1.7, color=GREY_B, fill_color=GREY_E, fill_opacity=1).move_to(RIGHT * 1.45 + DOWN * 1.25),
        )
        windows = VGroup()
        for building in buildings:
            for x in np.linspace(building.get_left()[0] + 0.22, building.get_right()[0] - 0.22, 2):
                for y in np.linspace(building.get_bottom()[1] + 0.35, building.get_top()[1] - 0.35, 3):
                    windows.add(Square(side_length=0.10, color=YELLOW, fill_opacity=0.75).move_to([x, y, 0]))

        ground = Line(LEFT * 5.8 + DOWN * 2.05, RIGHT * 5.8 + DOWN * 2.05, color=GREY_B)
        heat_label = Text("THE URBAN HEAT ISLAND", font_size=25, weight=BOLD)
        heat_label.to_edge(UP, buff=0.35)

        heat_waves = VGroup(*[
            ParametricFunction(
                lambda t, x=x: np.array([x + 0.10 * np.sin(5 * t), t, 0]),
                t_range=[-1.65, -0.65],
                color=ORANGE,
                stroke_width=4
            )
            for x in [-1.9, -0.5, 0.9]
        ])

        self.play(
            FadeIn(presenter_a), FadeIn(presenter_b),
            FadeIn(label_a), FadeIn(label_b),
            FadeIn(sun), Create(rays), run_time=1.2
        )
        self.play(Write(heat_label), run_time=0.8)
        self.play(Create(ground), FadeIn(buildings), FadeIn(windows), run_time=1.2)
        self.play(LaggedStart(*[Create(wave) for wave in heat_waves], lag_ratio=0.2), run_time=1.5)
        self.play(presenter_a.animate.shift(UP * 0.18), presenter_b.animate.shift(UP * 0.18), run_time=0.4)
        self.wait(1)
        self.play(FadeOut(VGroup(
            presenter_a, presenter_b, label_a, label_b, sun, rays,
            buildings, windows, ground, heat_waves, heat_label
        )), run_time=1)
        end_card = Text("A little science. A clearer picture.", font_size=30)
        self.play(FadeIn(end_card), run_time=0.8)
        self.wait(1)
