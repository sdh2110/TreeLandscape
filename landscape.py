import random
import turtle
import tree

GAP_SIZE = 300
TREE_SIZE = 200


def generate_random_layer(data_points):
    """
    Generates a random landscape layer.
    :param data_points: amount of data points in the layer
    :return: the layer data points
    """
    layer_data = []

    # Generate data_points amount of data points
    for i in range(data_points):
        layer_data += [random.randint(-30, 30)]

    return layer_data


def draw_layer(layer, depth, width, detail):
    turtle.tracer(0,0)
    # Find a reference point for the y cordinate for this layer
    base_y = turtle.ycor()

    visible_count = width // int(GAP_SIZE * depth) + 1
    non_vis_count = len(layer) - visible_count

    if visible_count < len(layer):
        layer = layer[non_vis_count:non_vis_count + visible_count]

    # Find x distance between each data point
    x_distance = width / len(layer)

    # Goto left edge of layer
    turtle.goto(-width // 2, base_y)

    # Draw trees of layer based on data points
    #tree.draw_tree(detail, TREE_SIZE * depth, depth, tree.get_random_ygr_percents())
    #turtle.update()
    #for point in layer:
    #    turtle.goto(turtle.xcor() + x_distance, base_y + (point * depth))
    #    tree.draw_tree(detail, TREE_SIZE * depth, depth, tree.get_random_ygr_percents())
    #    turtle.update()


    # Draw trees of layer based on data points
    tree.draw_tree(detail, TREE_SIZE * depth, depth, tree.get_random_ygr_percents())
    turtle.update()
    for i in range(len(layer)):
        turtle.goto(turtle.xcor() + x_distance, base_y + (layer[i] * depth))
        if i != (len(layer) // 2) - 1 and i != (len(layer) // 2):
            tree.draw_tree(detail, TREE_SIZE * depth, depth, tree.get_random_ygr_percents())
            turtle.update()


    # Ready turtle to draw land
    turtle.goto(-width // 2, base_y)
    turtle.color(tree.diffuse_color(tree.get_grass_color(), depth))
    turtle.begin_fill()

    # Draw top edge of layer based on data points
    for point in layer:
        turtle.goto(turtle.xcor() + x_distance, base_y + (point * depth))

    # Draw other edges of layer
    turtle.backward(1000)
    turtle.goto(-width // 2, turtle.ycor())
    turtle.goto(-width // 2, base_y)

    # Fill land
    turtle.end_fill()
    turtle.update()


def test_single_layer():
    turtle.setundobuffer(None)
    turtle.bgcolor(tree.SKY_COLOR)
    turtle.up()
    turtle.left(90)
    turtle.backward(200)

    draw_layer(generate_random_layer(10), 1, 2000, 4)

    turtle.done()


def test_many_layers():
    turtle.setundobuffer(None)
    turtle.hideturtle()
    turtle.bgcolor(tree.SKY_COLOR)
    turtle.up()
    turtle.left(90)
    turtle.forward(200)

    # Draw five trees at five different distances
    for i in range(30, 101, 10):
        percent = i / 100
        detail = int(6 * percent) + 2

        draw_layer(generate_random_layer(200), percent ** 2, 1700, detail)
        turtle.goto(0, turtle.ycor() - (percent ** 2 * 200))

    print("Complete")
    turtle.done()


test_many_layers()