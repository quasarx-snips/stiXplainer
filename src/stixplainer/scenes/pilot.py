from manim import *

# Original, reusable cartoon-stickman visual language for stiXplainer.
# Keep all important labels above the lower subtitle-safe band.

INK = "#242B35"
PAPER = "#FFF9ED"
SKY = "#B9E2F2"
BLUE_SHIRT = "#3B83C8"
BLUE_DARK = "#24527A"
LEAF = "#64A96B"
LEAF_DARK = "#397A4A"
WARM = "#F2A34A"
SUN = "#FFD45C"
ROAD = "#555D66"
CONCRETE = "#C9C8C1"


def label(text, size=28, color=INK):
    return Text(text, font_size=size, color=color, weight=BOLD)


def stickman(name, center, scale=1.0, shirt=BLUE_SHIRT):
    """Original simple cartoon character with a filled head and expressive face."""
    head = Circle(radius=.34, stroke_color=INK, stroke_width=4,
                  fill_color=PAPER, fill_opacity=1).move_to(UP*1.45)
    eyes = VGroup(
        Dot(LEFT*.105+UP*1.50, radius=.035, color=INK),
        Dot(RIGHT*.105+UP*1.50, radius=.035, color=INK))
    mouth = Arc(radius=.105, start_angle=PI+0.18, angle=PI-.36,
                color=INK, stroke_width=3).move_to(UP*1.32)
    neck = Line(UP*1.11, UP*.98, color=INK, stroke_width=4)
    torso = RoundedRectangle(width=.55, height=.76, corner_radius=.12,
                             stroke_color=INK, stroke_width=3,
                             fill_color=shirt, fill_opacity=1).move_to(UP*.58)
    arms = VGroup(
        Line(LEFT*.24+UP*.82, LEFT*.58+UP*.25, color=INK, stroke_width=5),
        Line(RIGHT*.24+UP*.82, RIGHT*.58+UP*.25, color=INK, stroke_width=5))
    hands = VGroup(
        Circle(radius=.065, color=INK, fill_color=PAPER, fill_opacity=1).move_to(LEFT*.58+UP*.25),
        Circle(radius=.065, color=INK, fill_color=PAPER, fill_opacity=1).move_to(RIGHT*.58+UP*.25))
    legs = VGroup(
        Line(DOWN*.0, LEFT*.27+DOWN*.68, color=INK, stroke_width=5),
        Line(DOWN*.0, RIGHT*.27+DOWN*.68, color=INK, stroke_width=5))
    shoes = VGroup(
        Line(LEFT*.27+DOWN*.68, LEFT*.48+DOWN*.68, color=INK, stroke_width=6),
        Line(RIGHT*.27+DOWN*.68, RIGHT*.48+DOWN*.68, color=INK, stroke_width=6))
    body = VGroup(head, eyes, mouth, neck, torso, arms, hands, legs, shoes)
    body.scale(scale).move_to(center)
    tag = Text(name, font_size=16, color=INK, weight=BOLD).next_to(body, DOWN, buff=.05)
    return VGroup(body, tag)


def tree(center, scale=1):
    trunk = Polygon(LEFT*.12+DOWN*.55, RIGHT*.12+DOWN*.55,
                    RIGHT*.08+UP*.25, LEFT*.08+UP*.25,
                    color=INK, stroke_width=2, fill_color="#986B48", fill_opacity=1)
    crown = VGroup(
        Circle(radius=.43, fill_color=LEAF, fill_opacity=1, stroke_color=LEAF_DARK, stroke_width=3),
        Circle(radius=.34, fill_color="#7CBE78", fill_opacity=1, stroke_color=LEAF_DARK, stroke_width=2).shift(LEFT*.27+UP*.17),
        Circle(radius=.32, fill_color="#79B974", fill_opacity=1, stroke_color=LEAF_DARK, stroke_width=2).shift(RIGHT*.26+UP*.16)
    ).shift(UP*.48)
    obj=VGroup(trunk,crown).scale(scale).move_to(center)
    return obj


def cloud(center, scale=1):
    parts=VGroup(
        Circle(radius=.28, fill_color=WHITE, fill_opacity=1, stroke_color=WHITE),
        Circle(radius=.38, fill_color=WHITE, fill_opacity=1, stroke_color=WHITE).shift(RIGHT*.28),
        Circle(radius=.25, fill_color=WHITE, fill_opacity=1, stroke_color=WHITE).shift(RIGHT*.58+DOWN*.05),
        Line(LEFT*.05, RIGHT*.72, color=WHITE, stroke_width=5).shift(DOWN*.2)
    ).scale(scale).move_to(center)
    return parts


def city_background(night=False):
    sky_color = "#23364F" if night else SKY
    ground_color = "#46515B" if night else "#A5B1A8"
    sky = Rectangle(width=15, height=8.5, stroke_width=0, fill_color=sky_color, fill_opacity=1).move_to(ORIGIN)
    ground = Rectangle(width=15, height=1.05, stroke_width=0, fill_color=ground_color, fill_opacity=1).to_edge(DOWN, buff=0)
    buildings=VGroup()
    for x,w,h,c in [(-6.1,1.5,2.4,"#8798A5"),(-4.5,1.6,3.4,"#728697"),(-2.7,1.5,2.7,"#A5B1B7"),
                    (2.4,1.5,2.9,"#8A9AA6"),(4.2,1.7,3.8,"#74899A"),(6.0,1.4,2.5,"#9EADB5")]:
        b=Rectangle(width=w,height=h,stroke_color=INK,stroke_width=2,
                    fill_color=c,fill_opacity=1).move_to(RIGHT*x+DOWN*(.52-h/2))
        windows=VGroup()
        for yy in range(max(1,int(h//.65))):
            for xx in [-.35,.25]:
                win=Rectangle(width=.18,height=.25,stroke_width=0,
                              fill_color=SUN if night else "#E9F0D9",fill_opacity=1)
                win.move_to(b.get_center()+RIGHT*xx+UP*(.45+yy*.55))
                windows.add(win)
        buildings.add(VGroup(b,windows))
    return VGroup(sky,ground,buildings)


class UrbanHeatIslandPilot(Scene):
    def construct(self):
        # Opening: warm city evening, character-led hook.
        bg=city_background(night=True)
        moon=Circle(radius=.38,fill_color=SUN,fill_opacity=1,stroke_color=SUN).to_corner(UR,buff=.75)
        clouds=VGroup(cloud(LEFT*4+UP*2.3,.8),cloud(RIGHT*2.4+UP*2.7,.65))
        maya=stickman("MAYA",LEFT*2.1+DOWN*1.7,.9)
        leo=stickman("LEO",RIGHT*2.1+DOWN*1.7,.9,shirt="#E5A34C")
        heatwaves=VGroup(*[
            Arc(radius=.34, start_angle=.15, angle=PI*.72, color=WARM, stroke_width=4)
            .move_to(RIGHT*x+UP*.0)
            for x in [-.55,0,.55]])
        heading=label("WHY IS THE CITY STILL HOT?",32,PAPER).to_edge(UP,buff=.35)
        self.play(FadeIn(bg),FadeIn(moon),FadeIn(clouds),FadeIn(maya),FadeIn(leo),Write(heading),run_time=2)
        self.play(FadeIn(heatwaves),maya[0].animate.shift(UP*.12),leo[0].animate.shift(UP*.12),run_time=2)
        self.wait(7)
        self.play(FadeOut(VGroup(bg,moon,clouds,maya,leo,heatwaves,heading)),run_time=1)

        # Beat 2: hot sun warms roofs and roads; heat is stored.
        bg=city_background()
        sun=Circle(radius=.48,fill_color=SUN,fill_opacity=1,stroke_color=WARM,stroke_width=3).to_corner(UL,buff=.7)
        rays=VGroup(*[Line(sun.get_center(),sun.get_center()+RIGHT*x+DOWN*1.6,color=WARM,stroke_width=5)
                      for x in [-.4,.25,.9]])
        house=VGroup(
            Rectangle(width=3.3,height=1.8,fill_color="#E6B98A",fill_opacity=1,stroke_color=INK,stroke_width=3).move_to(DOWN*.55),
            Polygon(LEFT*1.9+UP*.35,UP*1.55,RIGHT*1.9+UP*.35,fill_color="#B85D45",fill_opacity=1,stroke_color=INK,stroke_width=3),
            Rectangle(width=.55,height=.95,fill_color="#6E8CA2",fill_opacity=1,stroke_color=INK,stroke_width=2).move_to(DOWN*.95+RIGHT*.85),
            Rectangle(width=.7,height=.6,fill_color="#A9D5E8",fill_opacity=1,stroke_color=INK,stroke_width=2).move_to(DOWN*.35+LEFT*.8))
        road=Rectangle(width=7,height=.35,fill_color=ROAD,fill_opacity=1,stroke_color=INK).to_edge(DOWN,buff=1.0)
        arrows=VGroup(*[Arrow(UP*.3+RIGHT*x,UP*1.3+RIGHT*x,color=WARM,stroke_width=5,buff=0)
                        for x in [-1.2,0,1.2]])
        h=label("ROOFS + ROADS SOAK UP SUNLIGHT",26).to_edge(UP,buff=.35)
        self.play(FadeIn(bg),FadeIn(sun),Create(rays),FadeIn(house),FadeIn(road),Write(h),run_time=2)
        self.play(FadeOut(rays),LaggedStart(*[GrowArrow(a) for a in arrows],lag_ratio=.2),run_time=2)
        self.wait(5)
        self.play(FadeOut(VGroup(bg,sun,house,road,arrows,h)),run_time=1)

        # Beat 3: green space creates shade and evapotranspirative cooling.
        bg=city_background()
        park=RoundedRectangle(width=5.5,height=3.3,corner_radius=.2,fill_color="#B8D8A5",fill_opacity=1,stroke_color=LEAF_DARK,stroke_width=3).move_to(DOWN*.25+LEFT*2.6)
        paved=RoundedRectangle(width=4.1,height=3.3,corner_radius=.2,fill_color="#B7B9B7",fill_opacity=1,stroke_color=INK,stroke_width=3).move_to(DOWN*.25+RIGHT*3.0)
        trees=VGroup(tree(LEFT*3.8+DOWN*.2,.9),tree(LEFT*2.3+DOWN*.25,.75))
        bench=VGroup(Line(LEFT*.55,RIGHT*.55,color="#805B3B",stroke_width=8),Line(LEFT*.4+DOWN*.25,RIGHT*.4+DOWN*.25,color=INK,stroke_width=4)).move_to(LEFT*1.6+DOWN*1.05)
        hotcar=VGroup(RoundedRectangle(width=1.6,height=.55,corner_radius=.15,fill_color="#D66A50",fill_opacity=1,stroke_color=INK,stroke_width=3),
                      Circle(radius=.19,fill_color=INK,fill_opacity=1).shift(LEFT*.45+DOWN*.27),
                      Circle(radius=.19,fill_color=INK,fill_opacity=1).shift(RIGHT*.45+DOWN*.27)).move_to(RIGHT*3+DOWN*.65)
        vapor=VGroup(*[Arrow(LEFT*3.0+RIGHT*x+DOWN*.1,LEFT*3.0+RIGHT*x+UP*.9,color="#4D9EC8",buff=0,stroke_width=4)
                       for x in [-.5,0,.5]])
        h=label("TREES GIVE SHADE AND HELP COOL THE AIR",25).to_edge(UP,buff=.35)
        self.play(FadeIn(bg),FadeIn(park),FadeIn(paved),FadeIn(trees),FadeIn(bench),FadeIn(hotcar),Write(h),run_time=2)
        self.play(LaggedStart(*[GrowArrow(a) for a in vapor],lag_ratio=.2),run_time=2)
        self.wait(5)
        self.play(FadeOut(VGroup(bg,park,paved,trees,bench,hotcar,vapor,h)),run_time=1)

        # Beat 4: different urban microclimates; show a visual comparison.
        bg=city_background()
        panels=VGroup(
            RoundedRectangle(width=3.55,height=3.2,corner_radius=.15,fill_color="#B5D9A4",fill_opacity=1,stroke_color=INK).move_to(LEFT*4+DOWN*.1),
            RoundedRectangle(width=3.55,height=3.2,corner_radius=.15,fill_color="#D3B28D",fill_opacity=1,stroke_color=INK).move_to(DOWN*.1),
            RoundedRectangle(width=3.55,height=3.2,corner_radius=.15,fill_color="#B9BFC2",fill_opacity=1,stroke_color=INK).move_to(RIGHT*4+DOWN*.1))
        park_tree=tree(LEFT*4+UP*.05,.85)
        towers=VGroup(*[Rectangle(width=.65,height=h,fill_color="#8398A7",fill_opacity=1,stroke_color=INK,stroke_width=2)
                        .move_to(RIGHT*x+UP*(h/2-.7))
                        for x,h in [(-.85,2.1),(0,2.7),(.85,2.2)]])
        carpark=VGroup(RoundedRectangle(width=1.7,height=.65,corner_radius=.15,fill_color=BLUE_SHIRT,fill_opacity=1,stroke_color=INK).move_to(RIGHT*4+DOWN*.5),
                       Circle(radius=.18,fill_color=INK,fill_opacity=1).move_to(RIGHT*3.5+DOWN*.8),
                       Circle(radius=.18,fill_color=INK,fill_opacity=1).move_to(RIGHT*4.5+DOWN*.8))
        tags=VGroup(label("SHADED PARK",19),label("STREET CANYON",19),label("OPEN CAR PARK",19))
        for tag,panel in zip(tags,panels): tag.next_to(panel,DOWN,buff=.15)
        h=label("NOT EVERY STREET IS THE SAME",29).to_edge(UP,buff=.35)
        self.play(FadeIn(bg),FadeIn(panels),FadeIn(park_tree),FadeIn(towers),FadeIn(carpark),FadeIn(tags),Write(h),run_time=2)
        self.wait(8)
        self.play(FadeOut(VGroup(bg,panels,park_tree,towers,carpark,tags,h)),run_time=1)

        # Beat 5: people, cars and cooling equipment add waste heat.
        bg=city_background(night=True)
        heading=label("OUR ACTIVITIES ADD HEAT TOO",30,PAPER).to_edge(UP,buff=.35)
        car=VGroup(RoundedRectangle(width=2.0,height=.65,corner_radius=.18,fill_color="#D66A50",fill_opacity=1,stroke_color=INK,stroke_width=3),
                   Circle(radius=.22,fill_color=INK,fill_opacity=1).shift(LEFT*.55+DOWN*.3),
                   Circle(radius=.22,fill_color=INK,fill_opacity=1).shift(RIGHT*.55+DOWN*.3)).move_to(LEFT*3+DOWN*.7)
        building=VGroup(Rectangle(width=1.7,height=2.4,fill_color="#91A6B7",fill_opacity=1,stroke_color=INK,stroke_width=3).move_to(DOWN*.2),
                        *[Rectangle(width=.25,height=.3,fill_color=SUN,fill_opacity=1,stroke_width=0).move_to(LEFT*.45+UP*y)
                          for y in [-.8,-.1,.6]])
        ac=VGroup(Rectangle(width=1.25,height=.7,fill_color="#DDE6E9",fill_opacity=1,stroke_color=INK,stroke_width=3),
                  *[Line(LEFT*.4+UP*y,RIGHT*.4+UP*y,color=INK,stroke_width=2) for y in [-.15,0,.15]]).move_to(RIGHT*3+DOWN*.2)
        heat=VGroup(*[Arrow(obj.get_top(),obj.get_top()+UP*.85,color=WARM,stroke_width=5,buff=0) for obj in [car,building,ac]])
        self.play(FadeIn(bg),Write(heading),FadeIn(car),FadeIn(building),FadeIn(ac),run_time=2)
        self.play(LaggedStart(*[GrowArrow(a) for a in heat],lag_ratio=.25),run_time=2)
        self.wait(5)
        self.play(FadeOut(VGroup(bg,heading,car,building,ac,heat)),run_time=1)

        # Beat 6: practical interventions, shown as a greener street.
        bg=city_background()
        heading=label("DESIGN CAN HELP COOL A CITY",30).to_edge(UP,buff=.35)
        street=Rectangle(width=13,height=.65,fill_color=ROAD,fill_opacity=1,stroke_color=INK).to_edge(DOWN,buff=.85)
        houses=VGroup(*[
            VGroup(Rectangle(width=2.2,height=1.65,fill_color="#E8C9A6",fill_opacity=1,stroke_color=INK,stroke_width=3),
                   Polygon(LEFT*1.25+UP*.8,UP*1.85,RIGHT*1.25+UP*.8,fill_color="#B96C55",fill_opacity=1,stroke_color=INK,stroke_width=3))
            .move_to(RIGHT*x+DOWN*.35)
            for x in [-4.2,0,4.2]])
        greentops=VGroup(*[tree(RIGHT*x+UP*.95,.65) for x in [-5.7,-2.1,2.1,5.7]])
        arrows=VGroup(*[Arrow(UP*1.0+RIGHT*x,UP*1.8+RIGHT*x,color="#4D9EC8",buff=0,stroke_width=4)
                        for x in [-3.8,0,3.8]])
        h2=label("SHADE  •  TREES  •  REFLECTIVE ROOFS",23,LEAF_DARK).next_to(heading,DOWN,buff=.25)
        self.play(FadeIn(bg),Write(heading),FadeIn(street),FadeIn(houses),FadeIn(greentops),FadeIn(h2),run_time=2)
        self.play(LaggedStart(*[GrowArrow(a) for a in arrows],lag_ratio=.2),run_time=2)
        self.wait(5)
        self.play(FadeOut(VGroup(bg,heading,street,houses,greentops,arrows,h2)),run_time=1)

        # Closing: return to the characters, with a clear final thought.
        bg=city_background(night=True)
        maya=stickman("MAYA",LEFT*2+DOWN*1.55,.95)
        leo=stickman("LEO",RIGHT*2+DOWN*1.55,.95,shirt="#E5A34C")
        end=label("THE CITY WE BUILD SHAPES THE HEAT WE FEEL",27,PAPER).to_edge(UP,buff=.55)
        sub=Text("A little science. A clearer picture.",font_size=23,color=SUN).next_to(end,DOWN,buff=.3)
        self.play(FadeIn(bg),FadeIn(maya),FadeIn(leo),Write(end),FadeIn(sub),run_time=2)
        self.play(maya[0].animate.shift(UP*.12),leo[0].animate.shift(UP*.12),run_time=1)
        self.wait(5)
