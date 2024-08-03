import turtle
import time
import random

WIDTH, HEIGHT = 500, 500
COLORS = ["red", "green", "orange", "blue", "yellow", "black", "purple", "pink", "brown", "cyan"]

def get_number_of_racers():
    racers = 0
    while True:
        racers = input("Enter the number of racers (2 - 10): ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Input is not numeric... Try again!")
            continue
        if 2 <= racers <= 10:
            return racers
        else:
            print("Number not in range 2-10. Try again!")



def race(colors):
    turtles = create_turtles(colors)

    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)

            x, y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                return colors[turtles.index(racer)]

def create_turtles(colors):
    turtles = []
    spacingx = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)  # turtle'a renk veriyoruz.
        racer.shape("turtle") # ok yerine turtle şekli veriyoruz
        racer.left(90) # varsayılan ayarda sağa dönük duruyor ->
        racer.penup() # turtle giderken arkasındaki izi siler.
        racer.setpos(-WIDTH//2 + (i +   1) * spacingx, -HEIGHT//2 + 20)  # turtle arasında mesafeyi sabit tutmak için
        racer.pendown() # turtle giderken arkasından iz gözükür.     # oordinat sistemi üzerinden düşünerek en alt taraf -250 olduğu için
        turtles.append(racer)                                        # -250 yi referans alıp 20 piksel yukarıda başlattık.
    
    return turtles

def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Race")

racers = get_number_of_racers()
init_turtle()
random.shuffle(COLORS)
colors = COLORS[:racers]

winner = race(colors)
print("The winner is the turtle with color:", winner)
time.sleep(5)