from manim import *
# Set custom color for all elements
# CUSTOM_BLUE = rgb_to_color([170/255, 199/255, 254/255])
# Convert CUSTOM_BLUE to string hex color code
CUSTOM_BLUE = "#AAC7FE"

class EloProbCalcAnim2(Scene):
    def construct(self):
        # Create a text object
        text = Text("Elo Calculator", font_size=50, color=CUSTOM_BLUE).shift(UP*2)
        # Create a box around the text
        box = SurroundingRectangle(text, buff=0.5, color=CUSTOM_BLUE, stroke_width=10)
        
        # Create a group with text and box
        text_group = VGroup(text, box)
        
        # Add both objects to scene
        self.play(Create(text_group))
        self.wait(1)

        left_player_rating = Text("2000", font_size=48, weight=BOLD, color=CUSTOM_BLUE).next_to(text_group, LEFT, buff=3)
        left_player_name = Text("Player 1", font_size=30, weight=BOLD, color=CUSTOM_BLUE).next_to(left_player_rating, UP, buff=0.3)
        right_player_rating = Text("1600", font_size=48, weight=BOLD, color=CUSTOM_BLUE).next_to(text_group, RIGHT, buff=3)
        right_player_name = Text("Player 2", font_size=30, weight=BOLD, color=CUSTOM_BLUE).next_to(right_player_rating, UP, buff=0.3)

        self.play(Write(left_player_rating), Write(left_player_name), Write(right_player_rating), Write(right_player_name))
        self.wait(1)

        # Create arrows pointing from ratings to calculator box
        left_arrow = Arrow(
            start=left_player_rating.get_right(),
            end=box.get_left(),
            color=CUSTOM_BLUE,
            stroke_width=6,
            buff=0.1
        )
        
        right_arrow = Arrow(
            start=right_player_rating.get_left(), 
            end=box.get_right(),
            color=CUSTOM_BLUE,
            stroke_width=6,
            buff=0.1
        )

        # Animate the arrows appearing
        self.play(Create(left_arrow), Create(right_arrow))
        self.wait(1)

        elo_diff = Text("Difference: 400", font_size=44, weight=BOLD, color=CUSTOM_BLUE, t2c={"400": RED}).next_to(text_group, UP, buff=0.3)
        self.play(Write(elo_diff))
        self.wait(1)

        bottom_arrow = Arrow(
            start=box.get_bottom(),
            end=box.get_bottom()+DOWN*1.3,
            color=CUSTOM_BLUE,
            stroke_width=6,
            buff=0.1
        )

        self.play(Create(bottom_arrow))
        self.wait(0.2)

        prob_text = Text("Player 1 will win 10 out of 11 games", font_size=40, color=CUSTOM_BLUE).next_to(bottom_arrow, DOWN, buff=0.1)
        self.play(Write(prob_text))
        self.wait(1)

        bottom_arrow2 = Arrow(
            start=prob_text.get_bottom(),
            end=prob_text.get_bottom()+DOWN*1.3,
            color=CUSTOM_BLUE,
            stroke_width=6,
            buff=0.1
        )

        self.play(Create(bottom_arrow2))
        self.wait(0.2)

        prob_text2 = MathTex(r'\text{Player 1 win probability} = \bold{\frac{10}{11}}\approx 0.909 (90.9\%)', color=CUSTOM_BLUE).next_to(bottom_arrow2, DOWN, buff=0.1)
        # self.add(index_labels(prob_text2[0]))
        prob_text2[0][21:27].set_color(GREEN_D)
        self.play(Write(prob_text2))
        self.wait(1)