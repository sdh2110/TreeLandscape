import turtle
import random
# Day
SKY_COLOR = (234, 222, 187)
HORIZON_COLOR = (177, 198, 239)
# Night
#SKY_COLOR = (3, 0, 15)
#HORIZON_COLOR = (20, 20, 25)
SILHOUETTE_COLOR = (4, 12, 4)

LIGHT_Y = -150
MIN_RADIUS = 300
MAX_RADIUS = 500

turtle.colormode(255)


def get_weighted_int(a, b, weight):
    """
    :param a: inclusive start of range
    :param b: inclusive end of range
    :param weight: percentage of distance the num is towards b from a
    :return: an integer between a and b determined by weight
    """
    return a + int((b - a) * weight)


def color_with_night(color, depth):
    distance = (((turtle.xcor() ** 2) + ((turtle.ycor() - LIGHT_Y) ** 2)) / (depth ** 1.5)) ** 0.5

    if distance <= MIN_RADIUS:
        return color
    elif distance >= MAX_RADIUS:
        return SILHOUETTE_COLOR
    else:
        distance -= MIN_RADIUS
        color_percent = 1 - (distance / (MAX_RADIUS - MIN_RADIUS))

        # Set the each of the color values of the new color a depth percent of the
        # original color, with the percent that is not the original color being the
        # silhouette color
        red = int((color[0] * color_percent) + (SILHOUETTE_COLOR[0] * (1 - color_percent)))
        green = int((color[1] * color_percent) + (SILHOUETTE_COLOR[1] * (1 - color_percent)))
        blue = int((color[2] * color_percent) + (SILHOUETTE_COLOR[2] * (1 - color_percent)))

        # Return the RGB value of the new color
        return red, green, blue


def color_with_depth(color, depth):
    """
    Takes a color and returns a modified version of the color that accounts for
    the depth of view.
    :param color: color to modify
    :param depth: the percentage that the object is towards the horizon
    :return:
    """
    # Get the percent of the color to be visible based on depth
    color_percent = depth ** 2

    # Set the each of the color values of the new color a depth percent of the
    # original color, with the percent that is not the original color being the
    # sky color
    red = int((color[0] * color_percent) + (HORIZON_COLOR[0] * (1 - color_percent)))
    green = int((color[1] * color_percent) + (HORIZON_COLOR[1] * (1 - color_percent)))
    blue = int((color[2] * color_percent) + (HORIZON_COLOR[2] * (1 - color_percent)))

    # Return the RGB value of the new color
    return red, green, blue


def diffuse_color(color, depth):
    return color_with_depth(color, depth)
    #return color_with_depth(color_with_night(color, depth), depth)


def get_branch_color(segments):
    """
    Generates a random color for a branch of a tree, colored brighter the
    closer to the end of the tree it is.
    :param segments: the amount of branches after the branch for which the
    color is being generated
    :return: the color of the branch
    """
    # Randomly generate a redish brown
    red = random.randint(75, 175)
    red = int(red / (segments + 4) * 4)
    green = int(red / 3) + random.randint(-20, 20)
    blue = int(green / 5) + random.randint(-10, 10)

    # Make sure that the red value is within bounds
    if red > 255:
        red = 255
    elif red < 0:
        red = 0

    # Make sure that the green value is within bounds
    if green > 255:
        green = 255
    elif green < 0:
        green = 0

    # Make sure that the blue value is within bounds
    if blue > 255:
        blue = 255
    elif blue < 0:
        blue = 0

    # Return the RGB value of the branch
    return red, green, blue


def get_flower_color():
    """
    Generates a random pink color for a flower of a tree.
    :return: the color of the flower
    """
    # Randomly generate a light pink
    red = random.randint(210, 255)
    green = random.randint(130, 200)
    blue = red + random.randint(-10, 5)

    # Make sure that the red value is within bounds
    if red > 255:
        red = 255
    elif red < 0:
        red = 0

    # Make sure that the green value is within bounds
    if green > 255:
        green = 255
    elif green < 0:
        green = 0

    # Make sure that the blue value is within bounds
    if blue > 255:
        blue = 255
    elif blue < 0:
        blue = 0

    # Return the RGB value of the flower
    return red, green, blue


def get_yellow_leaf_color(rgb_weights = None):
    """
    Generates a random yellow color for a leaf of a tree.
    :param rgb_weights: optional sequence percents of how weighted each color of
    the RGB values of the leaf should be
    :return: the color of the leaf
    """
    # Randomly generate values for rgb_weights if not provided
    if rgb_weights is None:
        rgb_weights = (random.random(), random.random(), random.random())

    # Randomly decide if it will be a green or orange favored yellow
    is_green = random.randint(0, 1) == 0

    red = 0
    green = 0

    if is_green:
        # Generate R and G values to be green favored
        red = get_weighted_int(200, 255, rgb_weights[0])
        green = get_weighted_int(red, 255, rgb_weights[1])
    else:
        # Otherwise, generate R and G values to be orange favored
        green = get_weighted_int(200, 255, rgb_weights[1])
        red = get_weighted_int(green, 255, rgb_weights[0])

    # Generate the B value based on B weight
    blue = get_weighted_int(0, 10, rgb_weights[2])

    # Make sure that the red value is within bounds
    if red > 255:
        red = 255

    # Make sure that the green value is within bounds
    if green > 255:
        green = 255

    # Return the RGB value of the leaf
    return red, green, blue


def get_green_leaf_color(rgb_weights = None):
    """
    Generates a random green color for a leaf of a tree.
    :param rgb_weights: optional sequence percents of how weighted each color of
    the RGB values of the leaf should be
    :return: the color of the leaf
    """
    # Randomly generate values for rgb_weights if not provided
    if rgb_weights is None:
        rgb_weights = (random.random(), random.random(), random.random())

    # Randomly generate a green
    green = get_weighted_int(30, 80, rgb_weights[1])
    blue = get_weighted_int(0, 20, rgb_weights[2])
    red = blue + get_weighted_int(0, 10, rgb_weights[0])

    # Return the RGB value of the leaf
    return red, green, blue


def get_red_leaf_color(rgb_weights = None):
    """
    Generates a random red color for a leaf of a tree.
    :return: the color of the leaf
    :param rgb_weights: optional sequence percents of how weighted each color of
    the RGB values of the leaf should be
    :return: the color of the leaf
    """
    # Randomly generate values for rgb_weights if not provided
    if rgb_weights is None:
        rgb_weights = (random.random(), random.random(), random.random())

    # Randomly generate a red
    red = get_weighted_int(120, 200, rgb_weights[0])
    green = get_weighted_int(0, 50, rgb_weights[1])
    blue = get_weighted_int(0, 20, rgb_weights[2])

    # Return the RGB value of the leaf
    return red, green, blue


def get_rand_leaf_color(ygr_percents):
    """
    Generates a random natural color for a leaf of a tree.
    :param ygr_percents: the percents of each favoring in the leaf towards
    yellow, green and red as sequence
    :return: the color of the leaf
    """
    # Set the RGB weights of all YGR colors to be same so that when combined
    # they will maintain the correct contrast
    rgb_weights = (random.random(), random.random(), random.random())

    # Get the RGB values from random yellow, green and red leafs
    all_rgb = (get_yellow_leaf_color(rgb_weights),
               get_green_leaf_color(rgb_weights),
               get_red_leaf_color(rgb_weights))

    # Declare variables to store the final RGB values of the leaf
    red = 0
    green = 0
    blue = 0

    # Iterate through each YGR color, adding their influences to final color
    for ygr_index in range(3):
        red += all_rgb[ygr_index][0] * ygr_percents[ygr_index]
        green += all_rgb[ygr_index][1] * ygr_percents[ygr_index]
        blue += all_rgb[ygr_index][2] * ygr_percents[ygr_index]

    # Return the RGB value of the leaf
    return int(red), int(green), int(blue)


def get_random_ygr_percents():
    """
    :return: a random set of valid YGR weight percents
    """
    # Get initial proportional rates of YGR weights
    yellow = random.random() ** 1.5
    green = random.random() ** 1.5
    red = random.random() ** 1.5

    # Get total weight
    total = yellow + green + red

    # Return YGRs as percents instead of proportional rates
    return yellow / total, green / total, red / total


def get_grass_color():
    """
    Generates a random green color for grass
    :return: the color of the grass
    """
    """# Randomly generate a green
    green = random.randint(100, 165)
    blue = random.randint(0, 20)
    red = blue + random.randint(0, 10)

    # Return the RGB value of the grass
    return red, green, blue"""
    return get_rand_leaf_color((0.3, 0.6, 0.1))


def draw_leaf(size):
    """
    Draws a leaf in the direction of the turtle.
    :param size: the size of the flower to be drawn
    """
    # Begin filling the shape of the flower
    turtle.begin_fill()

    # Create the outline of the flower
    turtle.right(20)
    turtle.forward(size)
    turtle.left(40)
    turtle.forward(size)
    turtle.left(140)
    turtle.forward(size)
    turtle.left(40)
    turtle.forward(size)
    turtle.left(160)

    # Fill the outline with color
    turtle.end_fill()


def draw_tree(segments, size, depth, ygr_percents):
    """
    Through randomization, draws a unique tree using recursion.
    :param segments: amount of branch layers left to draw
    :param size: length of the current branch being drawn
    :param depth: percentage depth of the tree into the horizon
    """
    # Draw a flower instead of a branch if at the end of a branch
    if segments == 0 or size < 1:
        turtle.color(diffuse_color(get_rand_leaf_color(ygr_percents), depth))
        draw_leaf(10 * depth)
    # Otherwise draw a branch
    else:
        # Draw the current main branch
        turtle.down()
        turtle.pensize((size ** 0.8) * 0.25)
        turtle.pencolor(diffuse_color(get_branch_color(segments), depth))
        turtle.forward(size)
        turtle.up()

        # Randomly generate the angles at which the next branches will be drawn
        angle1 = 15 + random.randint(-5, 20)
        angle2 = random.randint(-15, 15)
        angle3 = 15 + random.randint(-5, 20)

        # Draw left branch set
        turtle.left(angle1 - angle2)
        draw_tree(segments - 1, size - size * (random.randint(15, 45) / 100), depth, ygr_percents)

        # Draw middle branch set
        turtle.right(angle1)
        draw_tree(segments - 1, size - size * (random.randint(15, 45) / 100), depth, ygr_percents)

        # Draw right branch set
        turtle.right(angle3)
        draw_tree(segments - 1, size - size * (random.randint(15, 45) / 100), depth, ygr_percents)

        # Return the turtle to the base of the current main branch
        turtle.left(angle3 + angle2)
        turtle.backward(size)


def test_single_tree():
    # Set up turtle window
    turtle.colormode(255)
    turtle.bgcolor(SKY_COLOR)
    turtle.tracer(1000, 0)

    # Position turtle
    turtle.up()
    turtle.left(90)
    turtle.backward(200)
    turtle.hideturtle()

    # Draw the tree
    turtle.down()
    draw_tree(8, 120, 1, get_random_ygr_percents())
    turtle.update()
    turtle.done()


def test_range_of_trees():
    # Set up turtle window
    turtle.colormode(255)
    turtle.bgcolor(SKY_COLOR)
    turtle.tracer(0, 0)

    # Position turtle
    turtle.up()
    turtle.backward(250)
    turtle.left(90)
    turtle.backward(200)
    turtle.hideturtle()

    # Draw five trees at five different distances
    for i in range(20, 101, 20):
        percent = i / 100
        turtle.down()
        draw_tree(8, 120 * percent, percent, get_random_ygr_percents())
        turtle.up()
        turtle.right(90)
        turtle.forward(150 * percent)
        turtle.left(90)
        turtle.update()

    turtle.done()