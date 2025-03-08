from manim import *

CUSTOM_BLUE = "#AAC7FE"
class EloGraph12(Scene):
    def construct(self):
        # Create a graph of Elo ratings over time

        # Create a graph of Elo ratings over time
        # Create axes with custom range and length
        
        axes = Axes(
            x_range=[-800, 800, 400],  # [min, max, step]
            y_range=[0, 1, 0.25],
            x_length=12,
            y_length=6,
            axis_config={
                "stroke_width": 6,
                "include_numbers": True,
                "include_ticks": True,
                "color": CUSTOM_BLUE
            },
        ).add_coordinates()

        # Add labels
        x_label = MathTex(r"\Delta \textbf{Elo}", font_size=48, color=CUSTOM_BLUE).next_to(axes.x_axis, DOWN*0.01).shift(RIGHT*5)
        y_label = Text("P", font_size=48, weight=BOLD, color=CUSTOM_BLUE).next_to(axes.y_axis, UP*0.01)

        # Create graph group
        graph = VGroup(axes, x_label, y_label)
        
        # Center the graph in the scene
        graph.center()

        # Add to scene
        self.add(axes, x_label, y_label)
        
        # Plot point (400, 0.909)
        # p1 = Dot(axes.c2p(400, 0.909), color=CUSTOM_BLUE, stroke_width=10)
        # lp1 = MathTex(r"(400, \frac{11-1}{11})", font_size=48, color=CUSTOM_BLUE).next_to(p1, RIGHT+DOWN*0.5)
        # lp1_2 = MathTex(r"(400, 0.909)", font_size=48, color=CUSTOM_BLUE).next_to(p1, RIGHT+DOWN*0.5)
        # self.play(Create(p1), Write(lp1))
        # self.play(FadeTransform(lp1, lp1_2))
        # self.wait(1)
        # self.add(p1, lp1_2)

        # p2 = Dot(axes.c2p(0, 0.50), color=CUSTOM_BLUE, stroke_width=10)
        # lp1 = MathTex(r"(400, \frac{11-1}{11})", font_size=48, color=CUSTOM_BLUE).next_to(p1, RIGHT+DOWN*0.5)
        # lp2 = MathTex(r"(0, 0.50)", font_size=48, color=CUSTOM_BLUE).next_to(p2, RIGHT+DOWN*0.5)
        # self.add(p2, lp2)
        # self.play(FadeTransform(lp1, lp1_2))
        # self.wait(1)

        # Add horizontal line at y=1
        h_line = DashedLine(
            axes.c2p(-800, 1),  # Start point using the x-range minimum
            axes.c2p(800, 1),   # End point using the x-range maximum
            color=CUSTOM_BLUE,
            stroke_width=6
        )
        self.add(h_line)
        # self.wait()

        h_line_lab = Text("y=1", font_size=40, weight=BOLD, color=CUSTOM_BLUE).next_to(h_line, UP*0.75).shift(RIGHT*4)
        self.add(h_line_lab)

        # Create logistic function graph
        # logistic_curve_asymp = axes.plot(
        #     lambda x: 1 / (1 + 10**(-x/400)),
        #     x_range=[400, 800],
        #     color=ORANGE,
        #     stroke_width=6
        # )
        
        # # Animate the curve being drawn
        # self.add(logistic_curve_asymp)


        # logistic_curve_asymp2 = axes.plot(
        #     lambda x: 1 / (1 + 10**(-x/400)),
        #     x_range=[-800, -400],
        #     color=ORANGE,
        #     stroke_width=6
        # )
        
        # # Animate the curve being drawn
        # self.add(logistic_curve_asymp2)
        # # self.wait(1)

        # logistic_curve = axes.plot(
        #     lambda x: 1 / (1 + 10**(-x/400)),
        #     x_range=[-400, 400],
        #     color=ORANGE,
        #     stroke_width=6
        # )
        
        # # Animate the curve being drawn
        # self.play(Create(logistic_curve))
        # self.wait(4)

        # logi_form = MathTex(r"y = \frac{1}{1 + 10^{-\frac{\Delta \textbf{Elo}}{S}}}", 
        #                     font_size=64, color=CUSTOM_BLUE).shift(LEFT*3.5).shift(UP*2)
        # self.add(logi_form)
        
        # logi_form_lab1 = MathTex(r"\mu = \textbf{0}", font_size=64, color=CUSTOM_BLUE).next_to(logi_form, DOWN*1.5)
        # logi_form_lab2 = MathTex(r"S = \text{?}", font_size=64, color=CUSTOM_BLUE).next_to(logi_form_lab1, DOWN)
        # self.add(logi_form_lab1)
        # self.add(logi_form_lab2)

        mu = 0
        mean = Dot(axes.c2p(mu, 0.5), stroke_width=10)
        mean_lab = Text(r"(" + str(mu) + ", 0.50)", font_size=24, font="Noto Sans").next_to(mean, RIGHT+DOWN*0.5)
        self.add(mean, mean_lab)

        diff400 = Dot(axes.c2p(400, 0.909), stroke_width=10)
        diff400_lab = Text(r"(400, 0.909)", font_size=24, font="Noto Sans").next_to(diff400, RIGHT+DOWN*0.5)
        self.add(diff400, diff400_lab)

        # s_range = [i for i in range(100, 700, 30)] + [i for i in range(700, 100, -10)]
        # for i in s_range:
        #     s = i
        #     self.remove(logi_form_lab1)
        #     self.remove(logi_form_lab2)
        #     logi_form_lab1 = MathTex(r"\mu = " + str(mu), font_size=64, color=CUSTOM_BLUE).next_to(logi_form, DOWN*1.5)
        #     logi_form_lab2 = MathTex(r"S = " + str(s), font_size=64).next_to(logi_form_lab1, DOWN)
        #     logistic_curve_i = axes.plot(
        #         lambda x: 1 / (1 + 10**(-(x-mu)/s)),
        #         x_range=[-800, 800],
        #         color=ORANGE,
        #         stroke_width=6
        #     )
        #     self.add(logistic_curve_i, logi_form_lab1, logi_form_lab2)
        #     self.wait(0.1)
        #     self.remove(logistic_curve_i)

        mu = 0
        s = 400
        # self.remove(logi_form_lab1)
        # self.remove(logi_form_lab2)
        # logi_form_lab1 = MathTex(r"\mu = " + str(mu), font_size=64, ).next_to(logi_form, DOWN*1.5)
        # logi_form_lab2 = MathTex(r"S = " + str(s), font_size=64, color=CUSTOM_BLUE).next_to(logi_form_lab1, DOWN)
        logistic_curve_i = axes.plot(
            lambda x: 1 / (1 + 10**(-(x-mu)/s)),
            x_range=[-800, 800],
            color=ORANGE,
            stroke_width=6
        )
        # self.add(logi_form_lab1, logi_form_lab2, mean, mean_lab)
        self.add(logistic_curve_i)

        # logi_form_1 = MathTex(r"y = \frac{1}{1 + 10^{-\frac{-(x-\textbf{0})}{S}}}", 
        #                     font_size=64, color=CUSTOM_BLUE).shift(LEFT*3.5).shift(UP*2)
        # logi_form_1[0][13:14].set_color(WHITE)
        # self.play(FadeTransform(logi_form, logi_form_1))
        # self.wait()

        # logi_form_2 = MathTex(r"y = \frac{1}{1 + 10^{-\frac{\Delta \textbf{Elo}}{S}}}", 
        #                     font_size=64, color=CUSTOM_BLUE).shift(LEFT*3.5).shift(UP*2)
        # logi_form_2[0][13:14].set_color(WHITE)
        # self.play(FadeTransform(logi_form_1, logi_form_2))
        # self.wait()

        # self.play(logi_form.animate.shift(DOWN*3.5+RIGHT*7))
        # self.wait(0.5)

        # logi_form_3 = MathTex(r"0.909 = \frac{1}{1 + 10^{-\frac{400}{S}}}", 
        #                     font_size=64, color=CUSTOM_BLUE).next_to(logi_form, DOWN*0)
        
        # self.play(FadeTransform(logi_form, logi_form_3))
        # self.wait(0.5)

        # logi_form_4 = MathTex(r"10^{-\frac{400}{S}} = \frac{1}{0.909}-1", 
        #                       font_size=64, color=CUSTOM_BLUE).next_to(logi_form_3, DOWN*0)
        # self.play(FadeTransform(logi_form_3, logi_form_4))
        # self.wait(0.5)

        # logi_form_5 = Text("S = 400", 
        #                       font_size=64).next_to(logi_form_4, DOWN*0)
        # self.play(FadeTransform(logi_form_4, logi_form_5))
        # self.wait(0.5)

        # logi_form_lab2_2 = MathTex(r"S = \text{400}", font_size=64).next_to(logi_form_lab1, DOWN)
        # self.play(FadeTransform(logi_form_lab2, logi_form_lab2_2))
        # self.wait(0.5)

        logi_form_6 = MathTex(r"y = \frac{1}{1 + 10^{-\frac{\Delta \textbf{Elo}}{400}}}", 
                              font_size=64, color=CUSTOM_BLUE).shift(DOWN*1.5+RIGHT*3.5)
        self.add(logi_form_6)
        self.wait(7)

        logi_form_7 = MathTex(r"y = \frac{1}{1 + 10^{-\frac{\Delta \textbf{Elo=100}}{400}}}", 
                              font_size=64, color=CUSTOM_BLUE).next_to(logi_form_6, DOWN*0)
        logi_form_7[0][14:17].set_color(ORANGE)
        self.play(FadeTransform(logi_form_6, logi_form_7))
        self.wait(1)

        h_line = Line(
            axes.c2p(100, 0),  # Start point using the x-range minimum
            axes.c2p(100, 0.64),   # End point using the x-range maximum
            color=ORANGE,
            stroke_width=6
        )
        diff100 = Dot(axes.c2p(100, 0.64), stroke_width=10, color=ORANGE)
        self.play(Create(h_line))
        self.play(Create(diff100))
        self.wait()

        diff100_lab = Text(r"(100, 0.64)", font_size=24, font="Noto Sans").next_to(diff100, RIGHT+DOWN*0.3)

        logi_form_8 = MathTex(r"y = 0.64", 
                              font_size=64).next_to(logi_form_7, DOWN*0)
        self.play(FadeTransform(logi_form_7, logi_form_8), Create(diff100_lab))
        self.wait(1)

        
        
        
        
        
        
        
