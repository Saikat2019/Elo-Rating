from manim import *

class Calculation2(Scene):
    def construct(self):
        # Create a text object
        # fs = 72
        # form1 = MathTex("\Delta ELO = \\text{2200}", font_size=fs, color=WHITE)

        # form1[0][5:].set_color(ORANGE)
        # self.play(Write(form1))
        # self.wait(2)

        # form2 = MathTex("E = \\frac{1}{1 + 10^{-\\frac{2200}{400}}}", font_size=fs, color=WHITE)
        # form2[0][9:13].set_color(ORANGE)
        # self.play(FadeTransform(form1, form2))
        # self.wait(5)

        # form3 = MathTex("E = 0.999", font_size=fs, color=WHITE)
        # form3[0][2:].set_color(ORANGE)
        # self.play(FadeTransform(form2, form3))
        # self.wait(5)

        fs = 72

        form1 = MathTex("R^{\prime} = R + K (S - E)", font_size=fs, color=WHITE)

        self.play(Write(form1))
        self.wait(2)

        form2 = MathTex("R + K (S - E) \leq 0", font_size=fs, color=WHITE)
        self.play(FadeTransform(form1, form2), run_time=2)

        form3 = MathTex(" 2600 + K (0 - 0.999) \leq 0", font_size=fs, color=WHITE)
        form3[0][7].set_color(ORANGE)
        form3[0][9:14].set_color(ORANGE)
        self.play(FadeTransform(form2, form3))

        form4 = MathTex("K (0 - 0.999) \leq -2600", font_size=fs, color=WHITE)
        self.play(FadeTransform(form3, form4))

        form5 = MathTex("K \geq \\frac{2600}{0.999}", font_size=fs, color=WHITE)
        self.play(FadeTransform(form4, form5))

        form6 = MathTex("K \geq 2600", font_size=fs, color=ORANGE)
        self.play(FadeTransform(form5, form6))

        self.wait(2)
        
        
