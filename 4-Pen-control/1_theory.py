from tkinter import W
from turtle import *
# Drawing state

# - pendown() | pd() | down() | Đặt bút xuống
# - penup() | pu() | up() | Nhấc bút lên
# - pensize() | width() | Độ đậm của nét vẽ
# - pen() | Cấu hình các thuộc tính của pen
# - isdown()
# pen(shown=False, pencolor='green', fillcolor='violet')
# width(4)
# forward(100)

# penup()
# print("Pen")
# print(isdown())

# setpos(0, 100)

# pendown()
# print("Pen")
# print(isdown())

# forward(100)
# home()

# Color control

# - color()
# - pencolor()

# color("blue", "yellow")
# width(4)
# forward(100)

# penup()
# setpos(0, 100)
# pencolor("green")
# pendown()
# forward(100)
# pencolor("red")
# home()

# - fillcolor()
# - begin_fill()
# - end_fill()
color('red', 'green')
fillcolor('blue')
width(5)
begin_fill()
circle(100, 360, 3)
end_fill()

done()
