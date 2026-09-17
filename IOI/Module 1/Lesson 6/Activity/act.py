# ================================================
#  ACTIVITY - CYBER LOTUS

# PART 1 - IMPORT AND SCREEN SETUP
# turtle.Screen() creates the canvas we draw on.
# bgcolor("midnightblue") gives a deep cosmic backdrop for neon strokes.
# title() sets the text shown in the window's title bar.
import turtle
screen = turtle.Screen()
screen.bgcolor("midnightblue")
screen.title("Cyber Lotus")

# PART 2 - CREATE THE TURTLE PEN
# turtle.Turtle() creates our drawing pen.
# speed("fastest") skips the slow animation so it draws instantly.
# hideturtle() hides the arrow shape -- only the art is visible.
artist = turtle.Turtle()
artist.speed("fastest")
artist.hideturtle()

# PART 3 - OUTER DOTTED RING (MOVEMENT + LOOP + COLOR)
# The turtle shoots outward 240 px, stamps a dot, returns, and rotates 5 degrees.
# Repeating 72 times (72 x 5 = 360) forms a perfect ring of glowing beads.
# colors[i % len(colors)] cycles through the palette endlessly.
dot_colors = ["gold", "orange", "tomato", "hotpink", "violet", "cyan", "aqua", "white"]
artist.penup()
for k in range(72):
    artist.color(dot_colors[k % len(dot_colors)])
    artist.forward(240)
    artist.dot(8)
    artist.backward(240)
    artist.right(5)

# PART 4 - MIDDLE HEXAGON FLOWER (PEN CONTROL + NESTED-STYLE LOOP + FILL)
# penup() lifts the pen so moving doesn't draw a line.
# goto(0, 0) returns the turtle to the exact center of the canvas.
# setheading() aims the turtle outward at a fresh angle each round.
# begin_fill() + end_fill() fills each hexagon with two colors (outline, fill).
# Rotating 30 degrees for 12 rounds spreads the hexagons into a flower shape.
hex_colors = ["cyan", "lime", "yellow", "deeppink", "violet", "orange"]
for h in range(12):
    artist.penup()
    artist.goto(0, 0)
    artist.setheading(h * 30)
    artist.forward(40)
    artist.pendown()
    artist.color(hex_colors[h % len(hex_colors)],
                 hex_colors[(h + 3) % len(hex_colors)])
    artist.begin_fill()
    for side in range(6):
        artist.forward(70)
        artist.right(60)
    artist.end_fill()

# PART 5 - CENTER TRIANGLE SUNBURST (NESTED LOOP + FILL)
# The outer loop spins around 360 degrees (18 rays x 20 degrees each).
# The inner loop draws one filled triangle each rotation.
# Nesting loops inside loops is how complex patterns are built!
artist.penup()
artist.goto(0, 0)
artist.pendown()
ray_colors = ["gold", "yellow", "orange", "red"]
for r in range(18):
    artist.color(ray_colors[r % len(ray_colors)],
                 ray_colors[(r + 1) % len(ray_colors)])
    artist.begin_fill()
    for t in range(3):
        artist.forward(35)
        artist.right(120)
    artist.end_fill()
    artist.right(20)

# KEEP WINDOW OPEN
turtle.done()