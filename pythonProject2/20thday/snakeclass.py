from turtle import Turtle, colormode



MOVE_DISTANCE = 13
colormode(255)
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.STARTING_POS = [(0, 0), (-20, 0), (-30, 0)]
        self.body = []
        self.create_snake()
        self.head = self.body[0]

    def create_snake(self):
        n=0
        for position in self.STARTING_POS:
            if n%2==0:
                shape ="circle"
            else:
                shape ="square"
            self.add_body(position,shape)
            n+=1


    def move(self):
        for seg_num in range(len(self.STARTING_POS)-1 , 0, -1):
            new_pos = self.body[seg_num - 1].pos()
            self.body[seg_num].goto(new_pos)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        print(self.head.heading())
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def extend(self):

        for i in range(4):
            if i%2==0:
                shape = "square"
            else:
                shape ="circle"

            self.add_body(self.body[-1].pos(),shape)
            self.STARTING_POS += [self.body[-1].pos()]


    def add_body(self,pos,shape):
        new_seg = Turtle(shape)
        new_seg.shapesize(stretch_len=0.75,stretch_wid=0.75)
        new_seg.penup()
        new_seg.setpos(pos)
        new_seg.color(255, 255, 255)
        self.body += [new_seg]
    def reset(self):
        for i in self.body:
            i.setpos(-1000,1000)
        for i in self.body:
            i.clear()

        self.STARTING_POS = [(0, 0), (-20, 0), (-30, 0)]
        self.body =[]
        self.create_snake()
        self.head = self.body[0]
