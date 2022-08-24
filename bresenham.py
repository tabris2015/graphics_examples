import tkinter
import time

PIXEL_SIZE = 20


def bresenham_line(x0, y0, x1, y1):
    points = []
    dx = x1 - x0
    dy = y1 - y0
    pk = 2 * dy - dx

    xk = x0
    yk = y0
    points.append((xk, yk))

    while xk != x1 and yk != y1:
        if pk < 0:
            pk = pk + 2 * dy
            xk = xk + 1
            yk = yk
        if pk > 0:
            pk = pk + 2 * dy - 2 * dx
            xk = xk + 1
            yk = yk + 1

        points.append((xk, yk))

    return points


def draw_line(points, canvas, window):
    for point in points:
        print(point)
        canvas.create_rectangle(
            point[0] * PIXEL_SIZE, 
            point[1] * PIXEL_SIZE, 
            point[0] * PIXEL_SIZE + PIXEL_SIZE, 
            point[1] * PIXEL_SIZE + PIXEL_SIZE,
            fill="red"
            )
        window.update()
        time.sleep(0.5)


def draw_grid(canvas):
    for x in range(0, 600, PIXEL_SIZE):
        canvas.create_line(x, 0, x, 600, fill="gray")
        canvas.create_line(0, x, 600, x, fill="gray")


def main():
    root = tkinter.Tk()
    canvas = tkinter.Canvas(root, bg="white", height=600, width=600)
    canvas.pack()

    x0 = 3
    y0 = 15
    x1 = 26
    y1 = 20

    draw_grid(canvas)
    # draw original line
    canvas.create_line(
        x0 * PIXEL_SIZE, 
        y0 * PIXEL_SIZE, 
        x1 * PIXEL_SIZE + PIXEL_SIZE, 
        y1 * PIXEL_SIZE + PIXEL_SIZE, 
        fill="green",
        width=5
        )
    line_points = bresenham_line(x0, y0, x1, y1)
    draw_line(line_points, canvas, root)
    root.mainloop()

if __name__ == "__main__":
    main()