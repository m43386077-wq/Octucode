import turtle as t

screen = t.Screen()
screen.title("Get Map Coordinates")
screen.bgpic("map.png")
screen.setup(width=858, height=515)

# هذه الدالة ستطبع الإحداثيات في كل مرة تضغطين فيها بالماوس
def get_mouse_click_coor(x, y):
    print(f"{x},{y}")

t.onscreenclick(get_mouse_click_coor)

t.mainloop()