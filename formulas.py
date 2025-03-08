from manim import *  

# The error is occurring because MathTex doesn't need the $ symbols - they are automatically added
# Also, align* environment was causing issues in the error log
# Here's the corrected class:

class formulae6(Scene):
    def construct(self):
        # First equation with colored "Rating"
        fs1 = 72    
        txt1 = MathTex(r'\frac{1}{n}\sum_{i=1}^{n} {\text{ELO}_i} = 1500', font_size=fs1)
        # self.add(index_labels(txt1[0]))
        txt1[0][8:11].set_color(ORANGE)
        txt1[0][13:17].set_color(GREEN)
        self.play(Write(txt1))

        # Create a box around the text
        box = SurroundingRectangle(txt1, buff=0.5, color=BLUE, stroke_width=10)
        
        # Add box to scene
        self.play(Create(box))

        txt2 = Text("Average rating", font_size=fs1//1.5, weight=BOLD)
        txt2.next_to(txt1, UP*2.5)
        self.play(Write(txt2))
        self.wait(13)