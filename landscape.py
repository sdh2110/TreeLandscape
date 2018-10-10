import random
import turtle
import tree


def generate_random_layer(data_points):
    """
    Generates a random landscape layer.
    :param data_points: amount of data points in the layer
    :return: the layer data points
    """
    layer_data = []

    # Generate data_points amount of data points
    for i in range(data_points):
        layer_data += [random.randint(-20, 20)]

    return layer_data


def draw_layer(layer, depth, width):
    turtle.tracer(0,0)
    # Find a reference point for the y cordinate for this layer
    base_y = turtle.ycor()
    width *= depth

    # Find x distance between each data point
    x_distance = width / len(layer)

    # Goto left edge of layer
    turtle.goto(-width / 2, base_y)

    # Draw top edge of layer based on data points
    for point in layer:
        turtle.down()
        turtle.goto(turtle.xcor() + x_distance, base_y + point)
        tree.draw_tree(6, 100 * depth, depth, tree.get_random_ygr_percents())
        turtle.update()


def test():
    turtle.up()
    turtle.left(90)
    draw_layer(generate_random_layer(10), 1, 2000)
    turtle.done()


test()
