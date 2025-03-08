# Import the manim library and all its contents
import manim
from manim import *

class EloTSPlot(Scene):
    def construct(self):
        # Create a time series plot of Elo ratings

        # Create axes with specified ranges and styling
        axes = Axes(
            x_range=[0, 10, 1],      # x-axis from 0 to 10 with step size 1
            y_range=[800, 3000, 500], # y-axis from 1300 to 1700 with step size 100
            x_length=10,             # Width of x-axis
            y_length=6,              # Height of y-axis
            axis_config={            # Configuration for both axes
                "stroke_width": 6,   # Line thickness
                "color": BLUE,       # Axis color
                "include_numbers": True # Show numeric labels
            }
        ).center()                   # Center the axes in the scene

        # Import numpy for numerical operations
        import numpy as np
        # Create evenly spaced time points from 0 to 10
        n = 30
        t = np.linspace(0, 10, n)

        
        # Generate first random walk series starting at 1500
        # Generate a random walk by:
        # 1. Creating 100 random numbers from normal distribution with mean=0, std=30
        # 2. Taking cumulative sum to create a random walk pattern
        # 3. Adding 1500 to shift the series to start at 1500 Elo rating
        series1 = np.concatenate((np.random.normal(0, 100, 10), np.random.normal(0, 30, n-10)), axis=0) + 1500 + 1400 * t/10
        # Generate second random walk series starting at 1500
        series2 = np.random.normal(0, 30, n) + 1000 + 800 * t/10

        # Create first graph line with red color
        graph1 = axes.plot_line_graph(
            x_values=t,
            y_values=series1,
            line_color=RED,
            stroke_width=6
        )

        # Create second graph line with green color
        graph2 = axes.plot_line_graph(
            x_values=t,
            y_values=series2,
            line_color=GREEN,
            stroke_width=6
        )

        # Create and style x-axis label
        # x_label = axes.get_x_axis_label("Time")
        # # Create and style y-axis label
        # y_label = axes.get_y_axis_label("Elo")
        x_label = Text("Time", font_size=35, color=BLUE_A, font="sans-serif").next_to(axes, DOWN)
        y_label = Text("Elo", font_size=35, color=BLUE_A, font="sans-serif").next_to(axes, LEFT)

        # Add the axes and labels to the scene
        self.add(axes, x_label, y_label)

        # Create initial point for first line
        line1 = axes.plot_line_graph(
            x_values=[t[0]],         # Start with first x value
            y_values=[series1[0]],   # Start with first y value
            line_color=RED,
            stroke_width=6
        )
        # Create initial point for second line
        line2 = axes.plot_line_graph(
            x_values=[t[0]],         # Start with first x value
            y_values=[series2[0]],   # Start with first y value
            line_color=GREEN, 
            stroke_width=6
        )
        # Create dots for initial Elo ratings
        dot1 = Dot(axes.c2p(t[0], series1[0]), color=RED)
        dot2 = Dot(axes.c2p(t[0], series2[0]), color=GREEN)
        
        # Add labels for initial ratings
        label1 = Text("Player 1 initial rating: 1500", font_size=35, color=RED, font="sans-serif").next_to(dot1, RIGHT)
        label2 = Text("Player 2 initial rating: 1000", font_size=35, color=GREEN, font="sans-serif").next_to(dot2, RIGHT)
        
        # Show initial points and labels
        self.play(Create(dot1), Write(label1))
        self.play(Create(dot2), Write(label2))
        self.wait(1)

        # Add dashed line at y=2900
        dashed_line1 = DashedLine(
            start=axes.c2p(t[0], 2900),
            end=axes.c2p(t[-1], 2900),
            color=RED,
            stroke_width=6,
            dash_length=0.2
        )
        dashed_line1_label = Text("Player 1's True Rating: 2900", font_size=35, color=RED, font="sans-serif").next_to(dashed_line1, UP)
        self.play(Create(dashed_line1), Write(dashed_line1_label))

        dashed_line2 = DashedLine(
            start=axes.c2p(t[0], 1800),
            end=axes.c2p(t[-1], 1800),
            color=GREEN,
            stroke_width=6,
            dash_length=0.2
        )
        dashed_line2_label = Text("Player 2's True Rating: 1800", font_size=35, color=GREEN, font="sans-serif").next_to(dashed_line2, UP)
        self.play(Create(dashed_line2), Write(dashed_line2_label))
        self.wait(1)
        
        # Remove the labels before continuing with animation
        self.remove(label1, label2, dashed_line1_label, dashed_line2_label)
        # Add both initial points to scene
        self.add(line1, line2)

        # Animate the growth of both lines point by point
        for i in range(1, len(t)):
            # Update first line by adding new point
            line1.become(axes.plot_line_graph(
                x_values=t[:i+1],    # Use all x values up to current point
                y_values=series1[:i+1], # Use all y values up to current point
                line_color=RED,
                stroke_width=6
            ))
            # Update second line by adding new point
            line2.become(axes.plot_line_graph(
                x_values=t[:i+1],    # Use all x values up to current point
                y_values=series2[:i+1], # Use all y values up to current point
                line_color=GREEN,
                stroke_width=6
            ))
            # Wait briefly between updates for animation effect
            self.wait(0.1)