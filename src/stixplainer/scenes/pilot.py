from manim import *


def presenter(name, accent, position):
    """A compact, expressive stick-figure presenter with a name label."""
    head = Circle(radius=0.24, color=accent, stroke_width=4).move_to(UP * 1.05)
    left_eye = Dot(LEFT * 0.075 + UP * 1.10, radius=0.025, color=accent)
    right_eye = Dot(RIGHT * 0.075 + UP * 1.10, radius=0.025, color=accent)
    smile = Arc(radius=0.09, start_angle=PI + 0.25, angle=PI - 0.5, color=accent, stroke_width=2)
    smile.move_to(DOWN * 0.015 + UP * 0.98)
    body = Line(UP * 0.80, DOWN * 0.28, color=accent, stroke_width=4)
    left_arm = Line(UP * 0.55, LEFT * 0.48 + UP * 0.16, color=accent, stroke_width=4)
    right_arm = Line(UP * 0.55, RIGHT * 0.48 + UP * 0.16, color=accent, stroke_width=4)
    left_leg = Line(DOWN * 0.28, LEFT * 0.36 + DOWN * 0.88, color=accent, stroke_width=4)
    right_leg = Line(DOWN * 0.28, RIGHT * 0.36 + DOWN * 0.88, color=accent, stroke_width=4)
    figure = VGroup(head, left_eye, right_eye, smile, body, left_arm, right_arm, left_leg, right_leg)
    figure.move_to(position)
    label = Text(name, font_size=18, color=accent).next_to(figure, DOWN, buff=0.12)
    return VGroup(figure, label)


def caption(text):
    box = RoundedRectangle(width=11.8, height=0.78, corner_radius=0.12,
                           stroke_color=GREY_B, fill_color=BLACK, fill_opacity=0.82)
    line = Text(text, font_size=22, color=WHITE)
    if line.width > 10.8:
        line.scale_to_fit_width(10.8)
    line.move_to(box.get_center())
    group = VGroup(box, line).to_edge(DOWN, buff=0.18)
    return group


class UrbanHeatIslandPilot(Scene):
    """An approximately 80-second visual pilot; narration is recorded separately."""

    def construct(self):
        maya = presenter("MAYA", BLUE, LEFT * 4.25 + DOWN * 0.45)
        leo = presenter("LEO", GREEN, RIGHT * 4.25 + DOWN * 0.45)

        # Opening: the evening still feels hot.
        title = Text("WHY IS THE CITY STILL HOT?", font_size=34, weight=BOLD)
        title.to_edge(UP, buff=0.35)
        road = Rectangle(width=12.2, height=0.42, fill_color=GREY_D,
                         fill_opacity=1, stroke_color=GREY_B).to_edge(DOWN, buff=0.0)
        sun = Circle(radius=0.42, color=YELLOW, fill_color=YELLOW, fill_opacity=1)
        sun.to_corner(UR, buff=0.7)
        sky = Text("AFTER SUNSET", font_size=20, color=YELLOW).next_to(sun, DOWN)
        shimmer = VGroup(*[
            Arc(radius=0.35, start_angle=0.15, angle=PI * 0.72,
                color=ORANGE, stroke_width=4).move_to(LEFT * 2.1 + UP * y)
            for y in [0.0, 0.5, 1.0]
        ])
        opening_caption = caption("The sun has set. So why does the street still feel like an oven?")
        self.play(Write(title), FadeIn(maya), FadeIn(leo), FadeIn(road), FadeIn(sun), FadeIn(sky), run_time=2)
        self.play(FadeIn(shimmer), FadeIn(opening_caption), maya[0].animate.shift(UP * 0.18), run_time=2)
        self.wait(4)
        self.play(FadeOut(VGroup(title, maya, leo, road, sun, sky, shimmer, opening_caption)), run_time=1)

        # Beat 2: hard surfaces absorb and slowly release heat.
        day_sun = Circle(radius=0.5, color=YELLOW, fill_color=YELLOW, fill_opacity=1).to_corner(UL)
        roof = Rectangle(width=3.0, height=0.45, fill_color=GREY_D, fill_opacity=1, stroke_color=GREY_B).move_to(DOWN * 1.0)
        wall = Rectangle(width=3.0, height=2.0, fill_color=GREY_E, fill_opacity=1, stroke_color=GREY_B).next_to(roof, DOWN, buff=0)
        rays = VGroup(*[Line(day_sun.get_right() + DOWN * k * 0.18,
                             roof.get_top() + RIGHT * (k - 1) * 0.55,
                             color=YELLOW, stroke_width=4) for k in range(4)])
        heat = VGroup(*[
            Arrow(roof.get_top() + RIGHT * x, roof.get_top() + RIGHT * x + UP * 1.1,
                  color=ORANGE, buff=0, stroke_width=4, max_tip_length_to_length_ratio=0.15)
            for x in [-0.8, 0, 0.8]
        ])
        heading = Text("1. THE CITY STORES HEAT", font_size=30, weight=BOLD).to_edge(UP)
        c = caption("Roofs, roads and walls absorb energy, then release heat after sunset.")
        self.play(FadeIn(day_sun), FadeIn(roof), FadeIn(wall), Create(rays), Write(heading), run_time=2)
        self.play(FadeOut(day_sun), FadeOut(rays), FadeIn(heat), FadeIn(c), run_time=2)
        self.wait(5)
        self.play(FadeOut(VGroup(roof, wall, heat, heading, c)), run_time=1)

        # Beat 3: shade and evapotranspiration.
        heading = Text("2. LESS GREEN, LESS NATURAL COOLING", font_size=28, weight=BOLD).to_edge(UP)
        trunk = Line(DOWN * 1.6, UP * 0.25, color=GREY_BROWN, stroke_width=12)
        canopy = VGroup(*[
            Circle(radius=0.55, fill_color=GREEN, fill_opacity=0.85, stroke_color=GREEN)
            .move_to(UP * 0.55 + RIGHT * x)
            for x in [-0.45, 0, 0.45]
        ])
        tree = VGroup(trunk, canopy).move_to(LEFT * 3 + DOWN * 0.2)
        pavement = Rectangle(width=3.0, height=0.38, fill_color=GREY_D, fill_opacity=1).move_to(LEFT * 3 + DOWN * 1.8)
        bare = Rectangle(width=3.0, height=0.38, fill_color=GREY_D, fill_opacity=1).move_to(RIGHT * 3 + DOWN * 1.8)
        vapor = VGroup(*[
            Arrow(tree.get_top() + RIGHT * x, tree.get_top() + RIGHT * x + UP * 0.8,
                  color=BLUE_B, buff=0, stroke_width=3)
            for x in [-0.4, 0, 0.4]
        ])
        label_tree = Text("SHADE + WATER", font_size=20, color=GREEN).next_to(pavement, DOWN)
        label_bare = Text("BARE PAVEMENT", font_size=20, color=ORANGE).next_to(bare, DOWN)
        c = caption("Trees shade streets and cool the air as water evaporates from leaves.")
        self.play(Write(heading), FadeIn(tree), FadeIn(pavement), FadeIn(bare),
                  FadeIn(label_tree), FadeIn(label_bare), run_time=2)
        self.play(GrowArrow(vapor[0]), GrowArrow(vapor[1]), GrowArrow(vapor[2]), FadeIn(c), run_time=2)
        self.wait(5)
        self.play(FadeOut(VGroup(heading, tree, pavement, bare, vapor, label_tree, label_bare, c)), run_time=1)

        # Beat 4: different places within one city have different conditions.
        heading = Text("3. NOT EVERY STREET IS THE SAME", font_size=30, weight=BOLD).to_edge(UP)
        park = RoundedRectangle(width=3.1, height=3.0, corner_radius=0.15, fill_color=GREEN_E, fill_opacity=0.35)
        street = RoundedRectangle(width=3.1, height=3.0, corner_radius=0.15, fill_color=GREY_E, fill_opacity=0.8)
        carpark = RoundedRectangle(width=3.1, height=3.0, corner_radius=0.15, fill_color=GREY_D, fill_opacity=0.8)
        park.move_to(LEFT * 4)
        street.move_to(ORIGIN)
        carpark.move_to(RIGHT * 4)
        tree_icon = VGroup(Circle(radius=0.55, color=GREEN, fill_color=GREEN, fill_opacity=1),
                           Line(DOWN * 0.1, DOWN * 0.9, color=GREY_BROWN, stroke_width=8)).move_to(park.get_center())
        towers = VGroup(*[
            Rectangle(width=0.7, height=h, fill_color=GREY_B, fill_opacity=1, stroke_color=GREY_A)
            .move_to(street.get_center() + RIGHT * x + UP * (h / 2 - 0.6))
            for x, h in [(-0.85, 2.0), (0, 2.5), (0.85, 1.8)]
        ])
        car = VGroup(Rectangle(width=1.2, height=0.45, fill_color=BLUE_D, fill_opacity=1),
                     Circle(radius=0.16, fill_color=BLACK, fill_opacity=1).move_to(LEFT * 0.35 + DOWN * 0.22),
                     Circle(radius=0.16, fill_color=BLACK, fill_opacity=1).move_to(RIGHT * 0.35 + DOWN * 0.22)).move_to(carpark.get_center())
        labels = VGroup(Text("SHADED PARK", font_size=18, color=GREEN),
                        Text("STREET CANYON", font_size=18),
                        Text("OPEN CAR PARK", font_size=18)).arrange(DOWN, buff=0.1)
        labels[0].next_to(park, DOWN, buff=0.18)
        labels[1].next_to(street, DOWN, buff=0.18)
        labels[2].next_to(carpark, DOWN, buff=0.18)
        c = caption("Shade, building layout and airflow make temperatures vary across a city.")
        self.play(Write(heading), FadeIn(park), FadeIn(street), FadeIn(carpark),
                  FadeIn(tree_icon), FadeIn(towers), FadeIn(car), FadeIn(labels), run_time=2)
        self.play(FadeIn(c), run_time=0.5)
        self.wait(5)
        self.play(FadeOut(VGroup(heading, park, street, carpark, tree_icon, towers, car, labels, c)), run_time=1)

        # Beat 5: waste heat adds to the picture.
        heading = Text("4. OUR ACTIVITIES ADD HEAT TOO", font_size=30, weight=BOLD).to_edge(UP)
        icons = VGroup(
            Text("CAR", font_size=30, color=BLUE),
            Text("BUILDING", font_size=26, color=GREY_B),
            Text("AIR CON", font_size=26, color=TEAL)
        ).arrange(RIGHT, buff=1.0).move_to(UP * 0.5)
        arrows = VGroup(*[
            Arrow(icon.get_bottom(), icon.get_bottom() + DOWN * 1.0,
                  color=ORANGE, buff=0, stroke_width=4)
            for icon in icons
        ])
        c = caption("Vehicles, buildings and air-conditioning can release waste heat.")
        self.play(Write(heading), FadeIn(icons), run_time=1.5)
        self.play(LaggedStart(*[GrowArrow(a) for a in arrows], lag_ratio=0.25), FadeIn(c), run_time=2)
        self.wait(5)
        self.play(FadeOut(VGroup(heading, icons, arrows, c)), run_time=1)

        # Beat 6: possible interventions.
        heading = Text("5. DESIGN CAN HELP COOL THE CITY", font_size=30, weight=BOLD).to_edge(UP)
        block = Rectangle(width=7.0, height=2.3, fill_color=GREY_E, fill_opacity=1, stroke_color=GREY_B).move_to(DOWN * 0.6)
        roofline = Line(block.get_top() + LEFT * 3.5, block.get_top() + RIGHT * 3.5, color=WHITE, stroke_width=5)
        green_roof = VGroup(*[
            Circle(radius=0.22, fill_color=GREEN, fill_opacity=1, stroke_color=GREEN)
            .move_to(block.get_top() + RIGHT * x + UP * 0.18)
            for x in [-2.7, -2.1, -1.5, 1.5, 2.1, 2.7]
        ])
        street_trees = VGroup(*[
            VGroup(Circle(radius=0.4, fill_color=GREEN, fill_opacity=1, stroke_color=GREEN),
                   Line(DOWN * 0.1, DOWN * 0.8, color=GREY_BROWN, stroke_width=7))
            .move_to(LEFT * x + DOWN * 1.25)
            for x in [4.7, 5.6]
        ])
        cool_roof = Text("REFLECTIVE ROOF", font_size=18, color=YELLOW).next_to(block, UP, buff=0.2)
        c = caption("More shade, vegetation and suitable reflective materials can reduce heat.")
        self.play(Write(heading), FadeIn(block), Create(roofline), FadeIn(cool_roof), run_time=2)
        self.play(FadeIn(green_roof), FadeIn(street_trees), FadeIn(c), run_time=2)
        self.wait(5)
        self.play(FadeOut(VGroup(heading, block, roofline, green_roof, street_trees, cool_roof, c)), run_time=1)

        # Closing: return to the presenters.
        final_line = Text("THE HEAT IS ALSO IN WHAT WE BUILD.", font_size=32, weight=BOLD)
        final_line.move_to(UP * 1.0)
        maya = presenter("MAYA", BLUE, LEFT * 2.4 + DOWN * 0.5)
        leo = presenter("LEO", GREEN, RIGHT * 2.4 + DOWN * 0.5)
        end_card = Text("A little science. A clearer picture.", font_size=24, color=YELLOW).to_edge(DOWN)
        self.play(Write(final_line), FadeIn(maya), FadeIn(leo), run_time=2)
        self.play(FadeIn(end_card), maya[0].animate.shift(UP * 0.15), leo[0].animate.shift(UP * 0.15), run_time=1)
        self.wait(4)
