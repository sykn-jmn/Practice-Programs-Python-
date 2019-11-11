import turtle
import time
import random

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def llrotate(self):
        left = self.left
        self.left = self.left.right
        left.right = self
        return left

    def rrrotate(self):
        right = self.right
        self.right = self.right.left
        right.left = self
        return right

    def lrrotate(self):
        self.left = self.left.rrrotate()
        return self.llrotate()

    def rlrotate(self):
        self.right = self.right.llrotate()
        return self.rrrotate()

    def get_height(self):
        if self.left is None:
            left_height = 1
        else:
            left_height = self.left.get_height() + 1
        if self.right is None:
            right_height = 1
        else:
            right_height = self.right.get_height() + 1

        if left_height > right_height:
            return left_height
        else:
            return right_height

    def get_balance(self):
        if self.left is None:
            left = 0
        else:
            left = self.left.get_height()
        if self.right is None:
            right = 0
        else:
            right = self.right.get_height()
        return right - left

    def print_inorder(self):
        if self.left is not None:
            self.left.print_inorder()
        print(self.data, end = ' ')
        if self.right is not None:
            self.right.print_inorder()

    def print_preorder(self):
        print(self.data, end = ' ')
        if self.left is not None:
            self.left.print_preorder()
        if self.right is not None:
            self.right.print_preorder()

    def print_postorder(self):
        if self.left is not None:
            self.left.print_postorder()
        if self.right is not None:
            self.right.print_postorder()
        print(self.data, end=' ')

    def insert(self, node):
        if node.data <= self.data:
            if self.left is None:
                self.left = node
            else:
                self.left.insert(node)
        elif node.data > self.data:
            if self.right is None:
                self.right = node
            else:
                self.right.insert(node)

    def check(self):
        if self.left is not None:
            self.left = self.left.check()
        if self.right is not None:
            self.right = self.right.check()
        return self.check_balance()

    def print(self,drawer,height,x,xdistance):
        drawer.penup()
        drawer.setpos(x,height)
        drawer.pendown()
        for i in range(0,4):
            drawer.forward(15)
            drawer.left(90)
        drawer.forward(3)
        drawer.write(self.data)
        if self.left is not None:
            self.left.print(drawer,height-50,x-xdistance,xdistance/2)
        if self.right is not None:
            self.right.print(drawer,height-50,x+xdistance,xdistance/2)

    def check_balance(self):
        if self.get_balance() == -2:
            if self.left.get_balance() == -1:
                return self.llrotate()
            elif self.left.get_balance() == 1:
                return self.lrrotate()
            else:
                print('Howdahek1: ', self.left.get_balance())
                time.sleep(1)
                return self
        elif self.get_balance() == 2:
            if self.right.get_balance() == -1:
                return self.rlrotate()
            elif self.right.get_balance() == 1:
                return self.rrrotate()
            else:
                print('Howdahek2: ', self.right.get_balance())
                time.sleep(2)
                return self
        else:
            return self



class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, data):
        print('Inserting ',data)
        don.clear()
        if self.size == 0:
            self.root = Node(data)
        else:
            self.root.insert(Node(data))
        self.size+=1
        self.print_tree(don)
        time.sleep(0.2)
        don.clear()
        self.root = self.root.check()
        self.print_tree(don)
        screen.update()
        time.sleep(0.2)

    def get_height(self):
        return self.root.get_height()

    def get_balance(self):
        return self.root.get_balance()

    def rotate(self):
        self.root = self.root.rlrotate()

    def print(self):
        print('Inorder:   ', end = ' ')
        self.root.print_inorder()
        print()
        print('Preorder:  ', end=' ')
        self.root.print_preorder()
        print()
        print('Postorder: ', end=' ')
        self.root.print_postorder()
        print()

    def print_tree(self, drawer):
        self.root.print(drawer,250,0,150)


don = turtle.Turtle()
screen = turtle.Screen()
don.speed(0)
don.hideturtle()
screen.tracer(0,0)


bst = BinarySearchTree()
while True:
    for i in range(0,25):
        bst.insert(random.randint(0,99))
        bst.print_tree(don)
    time.sleep(3)
    print('------')
    bst = BinarySearchTree()

screen.exitonclick()



