import turtle
import tree


def draw_half_row(row_width, blade_length, direction, ygr_percents):
    step_size = turtle.width() * 2
    step_count = row_width // step_size + 1
    degree_step = 90 / step_count

    step_size *= direction
    degree_step *= direction

    x_start = turtle.xcor()

    turtle.down()

    for i in range(step_count):
        turtle.color(tree.get_rand_leaf_color(ygr_percents))

        turtle.forward(blade_length)
        turtle.backward(blade_length)

        turtle.right(degree_step)
        turtle.goto(turtle.xcor() + step_size, turtle.ycor())

    turtle.up()
    turtle.goto(x_start, turtle.ycor())
    turtle.left(90 * direction)


def draw_grass_patch(patch_width, blade_length, blade_width, ygr_percents):
    # Modify YGR percents for grass instead of leaves
    yellow = ygr_percents[0] + (ygr_percents[2] / 2)
    green = ygr_percents[1] * 2 + (ygr_percents[0] / 2) + (ygr_percents[2] / 3)
    red = ygr_percents[2] / 2

    total = yellow + green + red

    yellow /= total
    green /= total
    red /= total

    ygr_percents = (yellow, green, red)

    turtle.width(blade_width)

    while patch_width > 0 and blade_length > 0:
        turtle.goto(turtle.xcor() - 6, turtle.ycor())
        draw_half_row(patch_width // 2, blade_length, 1, ygr_percents)
        turtle.goto(turtle.xcor() + 12, turtle.ycor())
        draw_half_row(patch_width // 2, blade_length, -1, ygr_percents)
        turtle.goto(turtle.xcor() - 6, turtle.ycor())

        patch_width -= 2
        blade_length -= 0.1