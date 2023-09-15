import math
import turtle

def draw_triangle(t, length, scale, color):
    t.color(color)
    lengthA = math.sqrt(length)
    lengthB = 1
    lengthC = math.sqrt(length+1)
    angleAB = 90
    angleBC = math.degrees(math.asin(lengthB/lengthC))
    t.down()
    t.forward(lengthA*scale)
    t.left(angleAB)
    t.forward(lengthB*scale)
    t.left(angleBC+90)
    t.forward(lengthC*scale)
    t.left(180)
    t.up()

def rainbow_colors(num_colors):
    colors = []
    for i in range(num_colors):
        red = 1.0 - i / (num_colors - 1)
        green = 1.0 - abs(2 * i / (num_colors - 1) - 1)
        blue = i / (num_colors - 1)
        colors.append((red, green, blue))
    return colors

def main():
    times = int(input('Times: '))
    scale = int(input('Scale: '))
    speed = int(input('Speed: '))
    rainbow = rainbow_colors(times)
    t = turtle.Turtle()
    t.speed(speed)
    for i in range(1, times+1):
        draw_triangle(t, i, scale, rainbow[i-1])
    turtle.mainloop()

if __name__ == "__main__":
    main()
