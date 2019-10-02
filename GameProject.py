class Player:
    def __init__(self):
        self.hope = 3
        self.health = 3
        self.name = ""

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def get_health(self):
        return self.health

    def get_hope(self):
        return self.hope

    def set_health(self, new_health):
        self.health = new_health

    def set_hope(self, new_hope):
        self.hope = new_hope

    def cap_attributes(self):
        if self.health < 0:
            self.health = 0
        elif self.health > 10:
            self.health = 10
        if self.hope < 0:
            self.hope = 0
        elif self.hope > 10:
            self.hope = 10


class Game:
    def __init__(self, first_ques):
        self.curr_ques = first_ques

    def game_orientation(self):
        print(player.get_name())
        print('Hope    :', '*' * player.get_hope(), '<---')
        print('This is your hope. It is {}/10'.format(player.get_hope()))
        input()
        print('Hope    :', '*' * player.get_hope())
        print('Health  :', '*' * player.get_health(), '<---')
        print('This is your health and it is {}/10'.format(player.get_health()))
        input()
        print(
            'You should keep watch of this to know your success rate. Your stats increase or decrease over the course of the game as result of your choices')
        input()
        print('Good Luck')
        print()
        print('Awoo! Awoo!')
        input()
        print()
        print('You are a Freshman BS IT student.')
        print('Objective: Survive the First Week of the Semester. ')
        input()
        print()

    def pre_game_interview(self):
        name = input('Type in your name: ')
        player.set_name(name)
        if (name == "Jeman") or (name == "Zcyrill") or (name == "Drake") or (name == "Al Brent"):
            player.set_health(10)
            player.set_hope(10)
        gender = input('Hello {}, what is your gender?(M or F) '.format(name))

        if gender == "M":
            player.set_health(player.get_health() + 1)
        elif gender == "F":
            player.set_health(player.get_health() + 2)
        else:
            print("Follow the rules!")

        rate = int(input('How will you rate you Academic Performance in Senior High?(1 to 5) '))
        if rate <= 2:
            player.set_hope(player.get_hope() + 1)
        elif rate <= 4:
            player.set_hope(player.get_hope() + 2)
        elif rate == 5:
            player.set_hope(player.get_hope() + 3)
            player.set_health(player.get_health() - 1)
        else:
            print("Follow the rules!")

        rship = input('Are you in a romantic relationship?(Y or N) ')
        if rship == "Y":
            player.set_hope(player.get_hope() + 1)
        elif rship == "N":
            player.set_health(player.get_health() + 1)
        else:
            print("Follow the rules!")

        prefCourse = input('Is this your preferred course?(Y or N) ')
        if prefCourse == "Y":
            player.set_hope(player.get_hope() + 1)
        elif prefCourse == "N":
            player.set_hope(player.get_hope() - 1)
        else:
            print("Follow the rules!")
        print()
        player.cap_attributes()

    def play(self):
        self.pre_game_interview()
        self.game_orientation()
        while (self.curr_ques is not None) and (player.get_health() > 0) and (player.get_hope() > 0):
            self.curr_ques = self.curr_ques.display()
            player.cap_attributes()
        if (player.get_health() >= 4) and (player.get_hope() >= 5) and (player.get_health() < 7) and (
                player.get_hope() < 7):
            print("You are balanced. You Passed!")
        elif (player.get_health() < 4) and (player.get_hope() >= 5):
            print("You have a good pace in Academics but you forgot your health. You failed")
        elif (player.get_health() >= 5) and (player.get_hope() < 4):
            print("You have a healthy lifestyle but you slacked in academics. You failed")
        elif (player.get_health() == 10) and (player.get_hope() == 10):
            print("Road to Summa Cum Laude")
        elif (player.get_health() >= 7) and (player.get_hope() >= 7):
            print("You are going to graduate. Outstanding. You Passed")
        else:
            print("It is time to reorganize yourself. You Failed")


class Choice:
    def __init__(self, statement, question, hope_effect, health_effect):
        self.question = question
        self.statement = statement
        self.hope_effect = hope_effect
        self.health_effect = health_effect

    def getQuestion(self):
        return self.question

    def getStatement(self):
        return self.statement

    def applyEffect(self):
        player.set_health(player.get_health() + self.health_effect)
        player.set_hope(player.get_hope() + self.hope_effect)


class Statement:
    def __init__(self, question):
        self.question = question

    def display(self):
        print(self.question)


class Question:
    def __init__(self, question, choice1, choice2):
        self.question = question
        self.choice1 = choice1
        self.choice2 = choice2

    def display(self):
        print('Hope    :', '*' * player.get_hope())
        print('Health  :', '*' * player.get_health())
        print(self.question)
        print('A.{}    B.{}'.format(self.choice1.getStatement(), self.choice2.getStatement()))
        a = input()
        if a == "A":
            self.choice1.applyEffect()
            return self.choice1.getQuestion()
        elif a == "B":
            self.choice2.applyEffect()
            return self.choice2.getQuestion()
        else:
            print('invalid option')
            return self


class Statement2:
    def __init__(self, statement, choice):
        self.choice = choice
        self.statement = statement

    def display(self):
        print('Hope    :', '*' * player.get_hope())
        print('Health  :', '*' * player.get_health())
        print(self.statement)
        print(self.choice.getStatement())
        input()
        return self.choice.getQuestion()


player = Player()
lastStatement = Statement("")
choiceend7 = Choice('Continue', lastStatement, 0, 0)
seventh_question3_endA = Statement2(
    "You spent the day hanging out with your old friends. You’ve always enjoyed their company. You all shared your \nfirst week of classes experiences.",
    choiceend7)
seventh_question3_endB = Statement2(
    "You spent the day reviewing your previous lessons. You felt the need to study to somehow boost your academic standing \nand want to make this day a little more productive",
    choiceend7)
seventh_question3_choiceA = Choice('Spend the day with some old friends', seventh_question3_endA, 0, +1)
seventh_question3_choiceB = Choice('Advance Study', seventh_question3_endB, +1, -1)
seventh_question3 = Question("You decided not to spend the day in the internet cafe playing games and thought of…",
                             seventh_question3_choiceA, seventh_question3_choiceB)
seventh_question2_end = Statement2(
    "You spent the day playing all sort of computer games. You enjoyed playing thus you’ve spent money during your stay and for your snacks",
    choiceend7)
seventh_question2_choiceA = Choice('Spend the day in the internet cafe playing games', seventh_question2_end, -1, -1)
seventh_question2_choiceB = Choice('Think of others…', seventh_question3, 0, 0)
seventh_question2 = Question("You decided not to spend the day indoors and thought of…", seventh_question2_choiceA,
                             seventh_question2_choiceB)
seventh_question1_end = Statement2(
    "You spent the day inside your boarding house. Watching movies and videos, listening to music, reading novels, cleaning, washing, etc.",
    choiceend7)
seventh_question1_choiceA = Choice("Spend the day indoors", seventh_question1_end, -1, +1)
seventh_question1_choiceB = Choice("Think of others...", seventh_question2, 0, 0)
seventh_question1 = Question(
    "It is sunday. You’re supposed to have an NSTP Orientation today but it was moved next week thus you have no agenda for today. What will you do today?",
    seventh_question1_choiceA, seventh_question1_choiceB)
choiceend6 = Choice('Continue', seventh_question1, 0, 0)
sixth_question2_endA = Statement2(
    "You won during the votations, thus you became the representative for your batch. You are then given the responsibility to fulfill your duties as an officer.",
    choiceend6)
sixth_question2_endB = Statement2(
    "You decided that being an officer is not for you and open up your time to other priorities", choiceend6)
sixth_question2_choiceA = Choice('Back out', sixth_question2_endB, 0, +1)
sixth_question2_choiceB = Choice('Run for the Position', sixth_question2_endA, +1, -1)
sixth_question2 = Question(
    "During the general assembly. The Society needs a representative for the freshmen and you are nominated. The present Society Mayor gave a choice to \nstudents who are nominated, to  back out if they do not want to take the position before the votations. \nWhat’s your decision?",
    sixth_question2_choiceA, sixth_question2_choiceB)
choiceContinue6 = Choice('Continue', sixth_question2, 0, 0)
sixth_question1_endA = Statement2(
    "You have failed to sign in but you don’t feel hungry and you arrived just in time for the general assembly.",
    choiceContinue6)
sixth_question1_endB = Statement2(
    "You have successfully signed and arrived at the general assembly on time but you felt hungry", choiceContinue6)
sixth_question1_choiceA = Choice('Skip breakfast to Sign in', sixth_question1_endB, +1, -1)
sixth_question1_choiceB = Choice('Have breakfast but fail to sign in', sixth_question1_endA, -1, +1)
sixth_question1 = Question(
    "It is the sixth day. Your Department General Assembly is scheduled today. You woke up a little bit late today. Sign ins are observed during events \nlike this but to be able to sign in you must skip breakfast. Since you only have little time to spare. \nWhat will you do?",
    sixth_question1_choiceA, sixth_question1_choiceB)
choiceend5 = Choice('Continue', sixth_question1, 0, 0)
fifth_question1_endA = Statement2(
    "Your teacher will give you a pre-test later. Seeing that there’s still time left you reviewed on the said topic, You go to class and met your \nteacher. He gave you all a pre-test, passing such will provide bonus points for the actual test. \nSince you reviewed for it, you passed the test.",
    choiceend5)
fifth_question1_endB = Statement2(
    "You didn’t feel the need to open such group chat since you assumed that it was just a greeting from your professor. You go to class and met your \nteacher. He gave you all a pre-test, passing such will provide bonus points for the actual test. \nYou were surprised and have no answers thus failed.",
    choiceend5)
fifth_question1_choiceA = Choice('Yes', fifth_question1_endA, +2, 0)
fifth_question1_choiceB = Choice('No', fifth_question1_endB, -2, 0)
fifth_question1 = Question(
    "You woke up fresh as ever, you felt that it is your lucky day today, it felt like good fortunes will come to you today, You checked your phone and \nnoticed that there’s a facebook messenger notification. It says, [ You are added to the group chat \nMAT104 by Prof. Litol Yu ] and sent a message. Will you open the chat?",
    fifth_question1_choiceA, fifth_question1_choiceB)
choiceend4 = Choice('Continue', fifth_question1, 0, 0)
fourth_question1_endA = Statement2(
    "After you did your laundry ,you felt like doing household so you decided to tidy up your room. You then decided to prepare yourself for school",
    choiceend4)
fourth_question1_endB = Statement2(
    "You felt rejuvenated after you slept. You then decided to prepare yourself for school", choiceend4)
fourth_question1_choiceA = Choice('Do Laundry', fourth_question1_endA, +2, -1)
fourth_question1_choiceB = Choice('Sleep', fourth_question1_endB, -1, +2)
fourth_question1 = Question(
    "It’s the fourth day. You woke up very early. You only have classes in the afternoon. You noticed that you have to do laundry but \nalso, you still want to sleep and do laundry some other time",
    fourth_question1_choiceA, fourth_question1_choiceB)
choiceend3 = Choice('Continue', fourth_question1, 0, 0)
third_question2B_endA = Statement2(
    "Just as you arrived at your boarding house, you received a text message. [ CCC100 IT1A You are marked absent.  SMS Blast. Do \nnot reply. You then went to school for your afternoon classes but the department posted an announcement that classes \nwill start next week. You decided to go home",
    choiceend3)
third_question2B_endB = Statement2(
    "The professor arrived and she noticed that only few are left . She approached the room and opened it and told everyone that \nshe will still have a class. You then went for your afternoon classes but the department posted an announcement that \nclasses will start next week. You decided to go home",
    choiceend3)
third_question2B_choiceA = Choice('Yes', third_question2B_endA, -2, +1)
third_question2B_choiceB = Choice('No', third_question2B_endB, +1, 0)
third_question2B = Question(
    '“Your blockmates started leaving one by one. You concluded that the teacher is absent for today. Will you go home?',
    third_question2B_choiceA, third_question2B_choiceB)
third_question2A_endA = Statement2(
    "Just as you arrived at your boarding house, you received a text message. [ CCC100 IT1A You are marked absent.  SMS Blast. Do \nnot replyYou then went to school for your afternoon classes but the department posted an announcement that classes \nwill start next week. You decided to go home",
    choiceend3)
third_question2A_endB = Statement2(
    "The professor arrived and she noticed that you are the only one left . She approached you and asked about your blockmates. You \ntold the professor the situation. She then told you that since you were the only one present, She won’t have class \nand you get bonus points for the next quiz. You then went for your afternoon classes but the department posted an announcement \nthat classes will start next week. You decided to go home",
    choiceend3)
third_question2A_choiceA = Choice('Go home', third_question2A_endA, -2, 0)
third_question2A_choiceB = Choice('Stay', third_question2A_endB, +1, +1)
third_question2A = Question(
    'After you told them, one of your blockmates started to talk to all of you, She mentioned that since 30 mins have passed and it \nis still the first week of class, everyone should just go home. Everybody agreed with her. What will you do?',
    third_question2A_choiceA, third_question2A_choiceB)
third_question1_choiceA = Choice('Yes', third_question2A, +1, 0)
third_question1_choiceB = Choice('No', third_question2B, -1, 0)
third_question1 = Question(
    'It’s another day. You wake up early and checked your class schedule for today and saw that you have a busy schedule for today. \nBecause of this, you then immediately prepared yourself for school. As you finished preparing, you went to school. \nYou arrived at the Multimedia Room, 2nd Floor at the CCS Building for your first class CCC100 Laboratory. \nThe class is scheduled for 9:00 AM to 12:00 PM and you arrived just in time but you noticed that the room is locked and your \nblockmates are scattered in front of the room. 30 mins have passed and the teacher is still not yet around. \nYou then remember a rule regarding this, “When the teacher is not around for 30 mins without instructions, the teacher is considered absent, \ntherefore there’s no class”. You’ve also noticed that your blockmates doesn’t know about this. Will you tell them?',
    third_question1_choiceA, third_question1_choiceB)
choiceend2 = Choice('Continue', third_question1, 0, 0)
second_question1_endA = Statement2("You miss the Surprise Quiz", choiceend2)
second_question2_endB = Statement2(
    "The teacher decided that the quiz was just for attendance.After Class, you decided to stroll around the university and went home after.",
    choiceend2)
choicetoend2 = Choice('Continue', second_question2_endB, 0, 0)
second_question2_lastA = Statement2('You are correct. The Kangaroo has 3 Vagina', choicetoend2)
second_question2_lastB = Statement2('You are wrong. Read some fun facts sometimes', choicetoend2)
second_question2_choiceA = Choice('Yes', second_question2_lastA, 0, 0)
second_question2_choiceB = Choice('No', second_question2_lastB, 0, 0)
second_question2A = Question(
    "The teacher of the class was present and more than that, you have a quiz. The quiz starts and the question is: Does a kangaroo have more than 1 vagina?",
    second_question2_choiceA, second_question2_choiceB)
second_question1_choiceA = Choice('Yes', second_question2A, +1, 0)
second_question1_choiceB = Choice('No', second_question1_endA, -2, 0)
second_question1 = Question(
    "“It is the second day of school and you have a class at 7:30 AM. It crossed your mind that classes rarely start at the first week of classes. Will you go to class?”",
    second_question1_choiceA, second_question1_choiceB)
choiceend1 = Choice('Continue', second_question1, 0, 0)
first_question_endA = Statement2(
    "You got distracted with the suggestions by youtube. You were watching two indian dudes making a pool in the forest until 4:00 AM",
    choiceend1)
first_question_endB = Statement2(
    "You prepared your snacks and just as you open the site, Netflix isn't available. You then decide to review while munching your snacks.",
    choiceend1)
first_question2B_choiceA = Choice("Watch inspirational videos", first_question_endA, 0, -2)
first_question2B_choiceB = Choice("Watch Netflix", first_question_endB, 1, -1)
first_question2B = Question("You went straight to your boarding house. What do you do?", first_question2B_choiceA,
                            first_question2B_choiceB)
first_question2A_choiceA = Choice('Go with them', lastStatement, -10, -10)
first_question2A_choiceB = Choice('Say No', first_question2B, 1, 1)
first_question2A = Question(
    "It turned out you made friends with bad people. They invited you to drink outside. Go with them?",
    first_question2A_choiceA, first_question2A_choiceB)
first_question1_choiceA = Choice('Yes', first_question2A, -1, -1)
first_question1_choiceB = Choice('No', first_question2B, -1, 0)
first_question1 = Question("There are new people you do not know. Do you want to make friends with them?",
                           first_question1_choiceA, first_question1_choiceB)
game = Game(first_question1)
game.play()