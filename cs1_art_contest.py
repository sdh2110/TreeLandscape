"""
File : cs1_art_contest.py
Language : python3
Author : Steven Hulbert <sdh2110@rit.edu>
Purpose : Uses turtle graphics to draw six uniquely colored and shaped trees.
"""
import turtle
import random

SKY_COLOR = (234, 222, 187)

# These two constants can be set to true to make the drawing randomized
COLORS_ARE_RANDOM = False
TREES_ARE_RANDOM = False

# Set this to true if you want the info on each tree drawn
TEST_INFO_ON = False


def init():
    """ Initializes turtle settings
    """
    turtle.title("Steven Hulbert")
    turtle.hideturtle()
    turtle.colormode(255)
    turtle.bgcolor(SKY_COLOR)
    turtle.up()
    turtle.left(90)


def get_weighted_int(a, b, weight):
    """
    :param a: inclusive start of range
    :param b: inclusive end of range
    :param weight: percentage of distance the num is towards b from a
    :return: an integer between a and b determined by weight
    """
    return a + int((b - a) * weight)


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
    # Draw a leaf instead of a branch if at the end of a branch
    if segments == 0 or size < 1:
        turtle.color(get_rand_leaf_color(ygr_percents))
        draw_leaf(10 * depth)
    # Otherwise draw a branch
    else:
        # Draw the current main branch
        turtle.down()
        turtle.pensize((size ** 0.8) * 0.25)
        turtle.pencolor(get_branch_color(segments))
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


def draw_half_row_grass(row_width, blade_length, direction, ygr_percents):
    """
    Draws a half of one row of grass in a grass patch.
    :param row_width: width of the row
    :param blade_length: length of each blade of grass
    :param direction: 1 if drawing right, -1 if drawing left
    :param ygr_percents: percents of yellow, green and red in the grass
    """
    # Determine the steps to move from one blade to next
    step_size = turtle.width() * 3
    step_count = row_width // step_size + 1
    degree_step = 90 / step_count

    # Account for drawing direction
    step_size *= direction
    degree_step *= direction

    # Save where the turtle starts so that it can be returned to when finished
    x_start = turtle.xcor()

    # Draw the grass blades
    turtle.down()
    for i in range(step_count):
        # Set this blades color randomly based on YGR percents
        turtle.color(get_rand_leaf_color(ygr_percents))

        # Draw one blade of grass
        turtle.forward(blade_length)
        turtle.backward(blade_length)

        # Reposition to draw next one, angling it closer to ground than previous
        turtle.right(degree_step)
        turtle.goto(turtle.xcor() + step_size, turtle.ycor())

    # Return turtle to starting position
    turtle.up()
    turtle.goto(x_start, turtle.ycor())
    turtle.left(90 * direction)


def draw_grass_patch(patch_width, blade_length, blade_width, ygr_percents):
    """
    Draws a patch of grass.
    :param patch_width: width of patch to be drawn
    :param blade_length: maximum length of grass
    :param blade_width: width of each blade of grass
    :param ygr_percents: percents of yellow, green and red in the grass
    :return:
    """
    # Modify YGR percents for grass instead of leaves
    yellow = ygr_percents[0] + (ygr_percents[2] / 2)
    green = ygr_percents[1] * 2 + (ygr_percents[0] / 2) + (ygr_percents[2] / 3)
    red = ygr_percents[2] / 2

    total = yellow + green + red

    yellow /= total
    green /= total
    red /= total

    ygr_percents = (yellow, green, red)

    # Draw many rows of grass, slowly shrinking the size of each row and it's
    # blades of grass
    turtle.width(blade_width)

    while patch_width > 0 and blade_length > 0:
        # Overlap the two half rows and draw the right half row
        turtle.goto(turtle.xcor() - 6, turtle.ycor())
        draw_half_row_grass(patch_width // 2, blade_length, 1, ygr_percents)

        # Overlap the two half rows and draw the left half row
        turtle.goto(turtle.xcor() + 12, turtle.ycor())
        draw_half_row_grass(patch_width // 2, blade_length, -1, ygr_percents)

        # Return turtle to middle
        turtle.goto(turtle.xcor() - 6, turtle.ycor())

        # Decrement patch width and blade length
        patch_width -= 2
        blade_length -= 0.1


def draw_single_tree(ygr_code, seed):
    """
    Draws a single tree in a patch of grass.
    :param ygr_code: percents of yellow, green and red in the grass
    :param seed: seed for the randomizer for this tree
    """
    # If testing info is on, print the location of the tree and its seed
    if TEST_INFO_ON:
        print("Seed for", turtle.xcor(), turtle.ycor(), "is", seed, end = "\n\n")

    # Seed the randomizer
    random.seed(seed)

    # Move turtle up so that base of tree doesn't stick out from under the grass
    turtle.forward(4)

    # Draw the tree
    draw_tree(6, 60, 1, ygr_code)

    # Return to original location and draw grass
    turtle.backward(4)
    draw_grass_patch(100, 9, 1, ygr_code)


def main():
    """
    Draws six evenly spaced trees of varying color.
    """
    # Set up the turtle
    turtle.tracer(0, 0)
    init()

    # Set up constant properties of the drawing
    x_gap = 300
    y_gap = 150

    # Set the colors for the trees
    ygr_percents = []

    if COLORS_ARE_RANDOM:
        for i in range(8):
            ygr_percents += [get_random_ygr_percents()]
    else:
        #red_ygr = (0.007856560215651814, 0.08883187848093152, 0.9033115613034166)
        #brown_green_ygr = (0.19691200394851957, 0.5329294406610857, 0.2701585553903946)
        #greenish_yellow_ygr = (0.5925192542645047, 0.35562845498283124, 0.05185229075266416)
        #orange_ygr = (0.2864249770024942, 0.0095798075157614, 0.7039952154813828)
        #deep_green_ygr = (0.05904052405700462, 0.8714904869125044, 0.06946898903049084)
        #yellow_ygr = (0.6813928359983732, 0.001117895226064104, 0.3174892687755627)

        #ygr_percents = [red_ygr, brown_green_ygr, greenish_yellow_ygr, orange_ygr, yellow_ygr, deep_green_ygr]

        ygr_percents = [(0.687390817297809, 0.06921813742051153, 0.24339104528167943), \
                        (0.3521624677097417, 0.28197959749056073, 0.3658579347996974), \
                        (0.7307845186239004, 0.26389452324517193, 0.005320958130927567), \
                        (0.36400220768470376, 0.06240828459048513, 0.573589507724811), \
                        (0.6215509535861138, 0.0014602145083451607, 0.37698883190554106), \
                        (0.0357246424749472, 0.1257617700003828, 0.8385135875246701)]

    # Set randomizer seed values for the trees
    seeds = []
    if TREES_ARE_RANDOM:
        for i in range(6):
            seeds += [random.random()]
    else:
        seeds = [0.6949645564908562, 0.2101112103860796, \
                 0.8108582792844496, 0.30008455289154545, \
                 0.6117587272073434, 0.17641037341619425]

    # Track which tree, as in color, is being drawn
    tree_on = 0

    # Draw the trees
    for x in range(-x_gap, x_gap + 1, x_gap):
        for y in range(y_gap - 109, -y_gap - 110, -y_gap * 2):
            turtle.goto(x, y)

            # If testing info is on, print the location of the tree and the YGR
            # code used for it
            if TEST_INFO_ON:
                print("Color for", x, y, "is", ygr_percents[tree_on])

            # Draw a tree
            draw_single_tree(ygr_percents[tree_on], seeds[tree_on])

            # Increment which tree is being drawn
            tree_on += 1

            # Update the screen
            turtle.update()

    # Alert user that the drawing is complete
    print("Turtle has finished drawing.")

    # Pause program till user closes the turtle window
    turtle.done()


# Run the program
main()
