import turtle
import tree
import grass


def init():
    turtle.hideturtle()
    turtle.bgcolor(tree.SKY_COLOR)
    turtle.up()
    turtle.left(90)


def draw_single_tree(ygr_code):
    turtle.forward(4)
    tree.draw_tree(6, 50, 1, ygr_code)
    turtle.backward(4)
    grass.draw_grass_patch(100, 9, 2, ygr_code)


def main():
    turtle.tracer(0, 0)
    init()

    x_gap = 300
    y_gap = 150

    red_ygr = (0.007856560215651814, 0.08883187848093152, 0.9033115613034166)
    brown_green_ygr = (0.19691200394851957, 0.5329294406610857, 0.2701585553903946)
    greenish_yellow_ygr = (0.5925192542645047, 0.35562845498283124, 0.05185229075266416)
    orange_ygr = (0.2864249770024942, 0.0095798075157614, 0.7039952154813828)
    deep_green_ygr = (0.05904052405700462, 0.8714904869125044, 0.06946898903049084)
    yellow_ygr = (0.6813928359983732, 0.001117895226064104, 0.3174892687755627)

    ygr_percents = (red_ygr, brown_green_ygr, greenish_yellow_ygr, orange_ygr, deep_green_ygr, yellow_ygr)

    tree_on = 0

    for x in range(-x_gap, x_gap + 1, x_gap):
        for y in range(y_gap - 69, -y_gap - 70, -y_gap * 2):
            turtle.goto(x, y)

            #ygr = tree.get_random_ygr_percents()
            #print(x, y, ygr)
            #draw_single_tree(ygr)

            draw_single_tree(ygr_percents[tree_on])
            tree_on += 1

            turtle.update()

    turtle.done()


main()