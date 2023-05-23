""" Day Automata """
import random


class State:
    ''' class with all states '''
    SLEEP = 'sleep'
    EAT = 'eat'
    WASHING = 'washing'
    COMMUTE = 'commute'
    STUDYING = 'studying'
    WORKOUT = 'workout'
    WALKING_OUT = 'walking out'
    SCROLL_SOCIAL_MEDIAS = 'scroll social medias'

    END = 'end'


class Person:
    """ Class representing Person's day """
    def __init__(self) -> None:
        # default state for start of the day
        self.state = State.SLEEP

        # 0 - bad mood, 1 - good (i know, it's impossible get 1 using random)
        self.mood = random.random()

        # Use dictionaries instead of endless number of if-else statements
        self.transitions = {
            State.SLEEP: self.sleep,
            State.EAT: self.eat,
            State.WASHING: self.washing,
            State.COMMUTE: self.commute,
            State.STUDYING: self.studying,
            State.SCROLL_SOCIAL_MEDIAS: self.scroll_social_medias,
            State.WALKING_OUT: self.walking_out,
            State.WORKOUT: self.workout
        }

    def simulate_day(self):
        """ Simulate day of one person """
        counter = 0 # count every 15 minutes

        while True:
            yield
            counter += 1
            time = counter / 4

            # counter mod 4 == 0 => 00 minutes
            # counter mod 4 == 1 => 15 minutes
            # counter mod 4 == 2 => 30 minutes
            # counter mod 4 == 4 => 45 minutes
            hour = str((counter // 4) % 24).zfill(2)
            minutes = str((counter % 4) * 15).zfill(2)

            print(f"{hour}:{minutes} ", end=" ")

            if self.state == State.END:
                print("End of the day.")
                return

            self.transitions[self.state](time)

    def sleep(self, time: int):
        """sleep and go further

        Args:
            time (int): current time
        """
        if time >= 20.5:
            print("Good night, my dears.")
            self.state = State.END

        elif time >= 7.75:
            print("Duck, I overslept. Let's go washing")
            self.state = State.WASHING

        elif 7.5 <= time <= 7.75 and random.random() > 0.1:
            print("Oh, just woke in time, nice")
            self.state = State.EAT

        elif 7 <= time <= 7.5 and random.random() > 0.7:
            print("Gooooood morniiiin', Vietnam!!!")
            self.state = State.EAT

        else:
            print('Sleeping')
            self.state = State.SLEEP

    def eat(self, time: int):
        """eating and go further

        Args:
            time (int): current time
        """
        if time >= 20:
            print("Nice dinner")
            self.state = State.WASHING

        elif time >= 14:
            print("Trapezna moments")
            self.state = State.STUDYING

        elif time >= 7:
            print("Yummy, I love russian newborns for breakfast")
            self.state = State.WASHING

    def washing(self, time: int):
        """Washing and go further

        Args:
            time (int): current time
        """
        if time >= 20.5:
            print("Time to wash the teeth")

            if random.random() > 0.7:
                self.state = State.SLEEP
            else:
                self.state = State.SCROLL_SOCIAL_MEDIAS
        elif time >= 20:
            print("Yah, shower after gym, niceee")
            self.state = State.COMMUTE

        elif time >= 7:
            print("Yah, washiinggg.")
            self.state = State.COMMUTE

    def commute(self, time: int):
        """Commute

        Args:
            time (int): current time
        """
        if time >= 20:
            print('Nice, I\'m home')
            self.state = State.EAT

        elif time == 8.25:
            print('Already in UCU. What\'s for today?')
            self.state = State.STUDYING

        elif time >= 8 and self.mood > 0.6:
            print('Ahh, what a lovely weather today. Raining again.')
            self.state = State.COMMUTE

    def studying(self, time: int):
        """Studying

        Args:
            time (int): current time
        """
        if time >= 23:
            print("Enough for today")
            self.state = State.WASHING

        elif time == 17:
            print("I'm done with studying. Lets go hanging out")
            self.state = State.WALKING_OUT

        elif 14 <= time <= 15 and random.random() > 0.7:
            print("Seems i'm starving")
            self.state = State.EAT

        elif random.random() > 0.8:
            print("Let's watch some tik toks")
            self.state = State.SCROLL_SOCIAL_MEDIAS

        else:
            print("Studying (not) hard")
            self.state = State.STUDYING

    def scroll_social_medias(self, time: int):
        """Scroll social medias

        Args:
            time (int): current time
        """
        if time <= 18:
            print("Hahah that was funny, now lets return to this words")
            self.state = State.STUDYING

        elif random.random() > 0.5:
            print("Let's watch tik tok for 5 minutes")
            self.state = State.SLEEP

        else:
            print("Let's watch tik tok for 5 minutes")
            self.state = State.SCROLL_SOCIAL_MEDIAS

    def walking_out(self, time: int):
        """Walking out

        Args:
            time (int): current time
        """
        if time == 19 and random.random() > 0.7:
            print("Now let's go to the gym")
            self.state = State.WORKOUT

        elif time == 22:
            print("Shit, i said i'll be home an hour ago")
            self.state = State.COMMUTE

        elif time < 22:
            print("Walking out..")
            self.state = State.WALKING_OUT

    def workout(self, time: int):
        """simulate workout

        Args:
            time (int): current time
        """
        if time == 20:
            print("I though I was going to die")
            self.state = State.WASHING
        else:
            print("*Sounds of hard working*")
            self.state = State.WORKOUT

me = Person()

for _ in me.simulate_day():
    pass
