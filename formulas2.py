from manim import *

CUSTOM_BLUE = "#AAC7FE"
class Formulas3(Scene):
    def construct(self):
        # Create a graph of Elo ratings over time
        fs = 56

        txt1 = MathTex("\\text{S: Real Score}", font_size=fs, color=CUSTOM_BLUE).shift(UP*3+LEFT*3)
        txt2 = MathTex("\\text{E: Expected Score}", font_size=fs, color=CUSTOM_BLUE).shift(UP*3+RIGHT*3)

        form1 = MathTex(
            "R^{\prime} = R + K (S - E)",
            font_size=fs,
            color=CUSTOM_BLUE
        ).shift(UP)

        form2 = MathTex(
            "E = \\frac{1}{1 + 10^{-\\frac{\Delta R}{400}}}",
            font_size=fs+12,
            color=CUSTOM_BLUE
        ).next_to(form1, DOWN)

        form3 = MathTex(
            "R^{\prime} = \\text{New Rating}",
            font_size=fs,
            color=CUSTOM_BLUE
        ).shift(DOWN*3+LEFT*3)

        form4 = MathTex(
            "R = \\text{Current Rating}",
            font_size=fs,
            color=CUSTOM_BLUE
        ).shift(DOWN*3+RIGHT*3)
        
        form5 = MathTex(
            "\\Delta R = \\text{Rating Difference}",
            font_size=42,
            color=CUSTOM_BLUE
        ).next_to(form2, DOWN)
        
        grp1 = VGroup(form2, form3, form4, form5, txt1, txt2)
        self.add(grp1, form1)

        form1_2 = MathTex(
            "R^{\prime} = R + K (S - E)",
            font_size=fs*2,
            color=CUSTOM_BLUE
        )

        form1_2[0][5:6].set_color(WHITE)

        self.play(FadeOut(grp1), FadeTransform(form1, form1_2), run_time=4)
        self.wait(10)

        