"""Scene of a house in the woods."""

__author__ = "730229417"

from turtle import Turtle, colormode, done
colormode(255)


def main() -> None:
    """Entry point of cabin in the woods!"""
    tree: Turtle = Turtle()
    draw_tree(tree, -250, -250, 10)
    house: Turtle = Turtle()
    draw_house(house, -75, -250, 10)
    roof: Turtle = Turtle()
    draw_roof(roof, -75, -100, 10)
    sun: Turtle = Turtle()
    draw_sun(sun, 200, 200, 10)
    tree2: Turtle = Turtle()
    draw_tree2(tree2, 250, 250, 10)
    done()


def draw_tree(tree: Turtle, x: float, y: float, width: float) -> None:
    """Making of a tree."""
    tree.penup()
    tree.speed(100)
    tree.goto(-250, -250)
    tree.pendown()
    tree.color(16, 168, 35)
    tree.begin_fill()
    tree.left(90)
    tree.forward(25)
    tree.right(90)
    tree.forward(65)
    tree.left(110)
    tree.forward(180)
    tree.left(140)
    tree.forward(180)
    tree.left(110)
    tree.forward(65)
    tree.end_fill()


def draw_house(house: Turtle, x: float, y: float, width: float) -> None:
    """Making of a house."""
    house.penup()
    house.speed(100)
    house.goto(-75, -250)
    house.pendown()
    house.color(170, 77, 15)
    house.left(90)
    house.forward(150)
    house.right(90)
    house.forward(200)
    house.right(90)
    house.forward(150)
    house.right(90)
    house.forward(70)
    house.right(90)
    house.forward(75)
    house.left(90)
    house.forward(50)
    house.left(90)
    house.forward(75)
    house.right(90)
    house.forward(85)


def draw_roof(roof: Turtle, x: float, y: float, width: float) -> None:
    """Making of the roof."""
    roof.penup()
    roof.speed(100)
    roof.goto(-75, -100)
    roof.pendown()
    roof.begin_fill()
    roof.color(78, 78, 78)
    roof.left(45)
    roof.forward(142)
    roof.right(90)
    roof.forward(142)
    roof.end_fill()


def draw_sun(sun: Turtle, x: float, y: float, width: float) -> None:
    """Attempt at sun with concentric circles."""
    sun.penup()
    sun.speed(100)
    sun.goto(200, 200)
    sun.pendown()
    sun.color(255, 217, 22)
    for i in range(7):
        sun.circle(7 * i)


def draw_tree2(tree2: Turtle, x: float, y: float, width: float) -> None:
    """copy of the first tree"""
    tree2.penup()
    tree2.speed(100)
    tree2.goto(250, -250)
    tree2.pendown()
    tree2.color(16, 168, 35)
    tree2.begin_fill()
    tree2.left(90)
    tree2.forward(25)
    tree2.right(90)
    tree2.forward(65)
    tree2.left(110)
    tree2.forward(180)
    tree2.left(140)
    tree2.forward(180)
    tree2.left(110)
    tree2.forward(65)
    tree2.end_fill()
    

if __name__ == "__main__": 
    main()