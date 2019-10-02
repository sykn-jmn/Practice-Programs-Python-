import turtle
import random
import Drawer
import time

don = turtle.Turtle()
don.speed(0)
don.hideturtle()
don.width(2)
screen = turtle.Screen()
screen.bgcolor('orange')
screen.colormode(255)
screen.delay(0)
screen.tracer(0)

drawer = Drawer.Drawer(don)


class Card:
    def __init__(self,color,number):
        self.face = 'up'
        self.color = color
        self.number = number

    def get_color(self):
        return self.color

    def get_number(self):
        return self.number

    def flip(self):
        if self.face == 'up':
            self.face = 'down'
        else:
            self.face = 'up'

    def face_up(self):
        self.face = 'up'
    def face_down(self):
        self.face = 'down'

    def draw(self,x,y,angle):
        don.left(angle)
        if self.face == 'up':
            drawer.draw_card(x,y,self.color,self.number,angle)
        elif self.face == 'down':
            drawer.draw_down_card(x,y,angle)

        don.right(angle)
        screen.update()


def all_face_up(cards):
    for card in cards:
        card.face_up()
def all_face_down(cards):
    for card in cards:
        card.face_down()

def get_cards():
    cards = []
    cards.append(Card('red',0))
    cards.append(Card('yellow',0))
    cards.append(Card('blue',0))
    cards.append(Card('green',0))
    for i in range(1,10):
        cards.append(Card('red',i))
        cards.append(Card('yellow', i))
        cards.append(Card('blue', i))
        cards.append(Card('green', i))
        cards.append(Card('red',i))
        cards.append(Card('yellow', i))
        cards.append(Card('blue', i))
        cards.append(Card('green', i))
    for i in range(2):
        cards.append(Card('red','draw2'))
        cards.append(Card('yellow','draw2'))
        cards.append(Card('blue','draw2'))
        cards.append(Card('green','draw2'))
    for i in range(2):
        cards.append(Card('red','reverse'))
        cards.append(Card('yellow','reverse'))
        cards.append(Card('blue','reverse'))
        cards.append(Card('green','reverse'))
    for i in range(2):
        cards.append(Card('red','skipped'))
        cards.append(Card('yellow','skipped'))
        cards.append(Card('blue','skipped'))
        cards.append(Card('green','skipped'))
    for i in range(4):
        cards.append(Card('black','wild'))
    for i in range(4):
        cards.append(Card('black','wild4'))
    random.shuffle(cards)
    return cards
def flip_deck(cards):
    for i in cards:
        i.flip()
def display_deck(cards,x,y,addx,addy,angle):
    for i in cards:
        i.draw(x,y,angle)
        x+=addx
        y+=addy
def random_display(cards,x,y):
    xAdd = 0
    yAdd = 15
    angleAdd = 24
    for i in cards:
        i.draw(x+xAdd,y+yAdd,angleAdd-40)
        xAdd+=245
        yAdd+=321
        angleAdd+=426
        while xAdd>40:
            xAdd-=24
        while yAdd>40:
            yAdd-=13
        while angleAdd>80:
            angleAdd-=67

#deck = get_cards()
#flip_deck(deck)

#display_deck(deck,-100,0)

class Player:
    def __init__(self,isAI):
        self.hand = []
        self.isAI = isAI

    def get_hand(self):
        return self.hand

    def is_AI(self):
        return self.isAI

class Game:

    def __init__(self,players):
        self.players = players
        pass

    def play(self):
        discard_pile = []
        draw_pile = get_cards()
        flip_deck(draw_pile)
        for player in self.players:
            for i in range(7):
                self.draw(draw_pile,player.get_hand())

        self.draw(draw_pile,discard_pile)
        all_face_up(discard_pile)
        turn = random.randint(0,3)
        direction = 1
        if discard_pile[len(discard_pile)-1].get_color() == 'black':
            current_color = random.choice(['red', 'yellow', 'blue', 'green'])
        else:
            current_color = discard_pile[len(discard_pile)-1].get_color()
        current_number = discard_pile[len(discard_pile)-1].get_number()
        while True:
            play_cards = self.players[turn].get_hand()
            if current_number == 'draw2':
                play_cards.append(draw_pile.pop())
                play_cards.append(draw_pile.pop())
            elif current_number == 'wild4':
                for i in range(4):
                    play_cards.append(draw_pile.pop())
            self.refresh(discard_pile,draw_pile,self.players)
            self.show_turn(turn,current_color)
            if self.players[turn].is_AI():
                time.sleep(1)
                size = len(play_cards)
                for card in play_cards:
                    if (card.get_color() == current_color) or (card.get_number() == current_number) or (card.get_color() == 'black'):
                        card.face_up()
                        play_cards.remove(card)
                        discard_pile.append(card)
                        if card.get_color() == 'black':
                            current_color = random.choice(['red','yellow','blue','green'])
                        else:
                            current_color = card.get_color()
                        current_number = card.get_number()
                        if card.get_number()=='reverse':
                            direction = direction*-1
                        if card.get_number()=='skipped':
                            turn = turn+direction
                        break
                if len(play_cards) == size:
                    self.draw(draw_pile,play_cards)
            else:
                card_number = int(screen.numinput('Input', 'Enter the card number to play(0 for draw):', 0, 0,
                                              len(play_cards)))
                while True:
                    if card_number == 0:
                        self.draw(draw_pile, play_cards)
                        break
                    else:
                        card1 = play_cards[card_number-1]
                        if (card1.get_color() == current_color) or (card1.get_number() == current_number) or (
                                card1.get_color() == 'black'):
                            card1.face_up()
                            play_cards.remove(card1)
                            discard_pile.append(card1)
                            if card1.get_color() == 'black':
                                current_color = screen.textinput('Color Picker', 'Enter Color:')
                                current_color = current_color.lower()
                            else:
                                current_color = card1.get_color()
                            current_number = card1.get_number()
                            if card1.get_number() == 'reverse':
                                direction = direction * -1
                            if card1.get_number() == 'skipped':
                                turn = turn + direction
                            break
                        card_number = int(screen.numinput('Unplayable Card','Card is not playable, pick another:', 0, 0,
                                              len(play_cards)))

            if len(play_cards) == 0:
                break

            if len(discard_pile) > 10:
                for i in range(10):
                    firstcard = discard_pile[0]
                    firstcard.face_down()
                    draw_pile.insert(0,firstcard)
                    discard_pile.remove(firstcard)


            self.refresh(discard_pile, draw_pile, self.players)
            time.sleep(2)

            turn = self.next_turn(turn,direction)
            self.show_turn(turn, current_color)

        self.refresh(discard_pile, draw_pile, self.players)
        if turn == 0:
            screen.textinput('YOU WIN', 'YOU WIN')
        else:
            screen.textinput('YOU LOSE', 'YOU LOSE')

    def next_turn(self,turn,add):
        turn1 = turn + add
        if turn1>3:
            turn1 = turn1-4
        if turn1<0:
            turn1 = turn1+4
        return turn1

    def show_turn(self,turn,color):
        don.pencolor('black')
        don.fillcolor(color)
        don.begin_fill()
        if turn == 0:
            drawer.drawRectangle(-50,-150,10,100,0)
        if turn == 1:
            drawer.drawRectangle(-240,-40,100,10,0)
        if turn == 2:
            drawer.drawRectangle(-40, 180, 10, 100, 0)
        if turn == 3:
            drawer.drawRectangle(230, -40, 100, 10, 0)
        don.end_fill()
        screen.update()

    def refresh(self, discard, drawpile, players):
        don.clear()
        x = 10
        x1 = -120
        for i in range(0,len(drawpile)):
            x += 1
            if x > 10:
                drawpile[i].draw(x1,60,0)
                x = 0
                x1 += 4

        random_display(discard, 40, -70)
        all_face_up(players[0].get_hand())
        display_deck(players[3].get_hand(),     250,    -150,   0,                                  300/(len(players[3].get_hand())+1),-90)
        display_deck(players[2].get_hand(),     -200,   300,    400/(len(players[2].get_hand())+1),     0,180)
        display_deck(players[1].get_hand(),     -250,   -100,   0,                                  300/(len(players[1].get_hand())+1),90)
        display_deck(players[0].get_hand(),     -120,   -260,   400/(len(players[0].get_hand())+1),     0,0)


    def draw(self,from_pile,to_pile):
        to_pile.append(from_pile.pop())












player1 = Player(False)
player2 = Player(True)
player3 = Player(True)
player4 = Player(True)
gameplayers = [player1,player2,player3,player4]

game = Game(gameplayers)

game.play()






screen.exitonclick()