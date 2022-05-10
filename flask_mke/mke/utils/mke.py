import base64
import io

import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt

EPS = 120
COORD_EPS = -1
X_OFFSET = 572
Y_OFFSET = 312
X_SCALE = 105 / 25
Y_SCALE = 93 / 10


def draw_mke(items, id=-1):
    new_dots_x = list()
    new_dots_y = list()
    img = io.BytesIO()
    for item in items:
        dots_x = [item["x1"], item["x2"], item["x3"], item["x1"]]
        dots_y = [item["y1"], item["y2"], item["y3"], item["y1"]]
        if item['id'] == id:
            new_dots_x = [item["x1"], item["x2"], item["x3"], item["x1"]]
            new_dots_y = [item["y1"], item["y2"], item["y3"], item["y1"]]

        plt.plot(dots_x, dots_y, color="black")
    if new_dots_x:
        plt.plot(new_dots_x, new_dots_y, color="red")

    plt.grid(True)
    plt.savefig(img, format='png')
    plot_url = base64.b64encode(img.getvalue()).decode()

    return plot_url


def redraw_elem(items, x, y):
    for item in items:
        if is_on_line(item, x, y):
            url = draw_mke(items, item['id'])

            return url

    url = draw_mke(items)

    return url


def is_on_line(item, x, y):
    x -= X_OFFSET
    y -= Y_OFFSET
    y *= -1
    x = x / X_SCALE
    y = y / Y_SCALE

    print(x, y)
    if (COORD_EPS <= (x - item['x1']) * (item['x2'] - x) <= (item['x1'] - item['x2']) ** 2) \
            and (COORD_EPS <= (y - item['y1']) * (item['y2'] - y) <= (item['y1'] - item['y2']) ** 2):
        val = (x - item['x1']) * (item['y2'] - item['y1']) - (item['x2'] - item['x1']) * (y - item['y1'])

        if val ** 2 <= EPS ** 2:
            return True

    elif (COORD_EPS <= (x - item['x2']) * (item['x3'] - x) <= (item['x2'] - item['x3']) ** 2) \
            and (COORD_EPS <= (y - item['y2']) * (item['y3'] - y) <= (item['y2'] - item['y3']) ** 2):
        val = (x - item['x2']) * (item['y3'] - item['y2']) - (item['x3'] - item['x2']) * (y - item['y3'])

        if val ** 2 <= EPS ** 2:
            return True

    elif (COORD_EPS <= (x - item['x3']) * (item['x1'] - x) <= (item['x3'] - item['x1']) ** 2) \
            and (COORD_EPS <= (y - item['y3']) * (item['y1'] - y) <= (item['y3'] - item['y1']) ** 2):
        val = (x - item['x3']) * (item['y1'] - item['y3']) - (item['x1'] - item['x3']) * (y - item['y3'])

        if val ** 2 <= EPS ** 2:
            return True

    return False
