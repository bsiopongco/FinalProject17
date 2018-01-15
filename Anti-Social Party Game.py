import random
class people():
# creation of class people with characteristics of names, descriptions and responses

    def __init__(self, name, description, response):
        #Initializing new instance of Character class
        #Assigning parameters in the given function that belong to class people
        self.name = name
        self.description = description
        self.response = response

class health():
    # Creation of class health for the purpose of having initial value for Social Health


    def __init__(points, life):
        #Initializing new instance of health class
        #Assigning parameters in the given function that belong to class health
        points.life = life


Social_life = health(int(100))
# Assigning variable to be set to equal the health class

def healthbar():
    # Creation of a function that keeps track of health points
    Social_life.life = Social_life.life - random.randint(1,20)
    #Takes initial life points and subtracts it by random integer creating a new life value
    if Social_life.life > 0:
        print(f"Your Social life is currently at {Social_life.life}")
        # Game continues if life is > 0
    elif Social_life.life <= 0:
        print("Rip, the party was too much for an antisocial loser like you! You lose!")
        # Game ends if life is less than or equal to 0


Karen = people("Karen", "the snobby, popular, and annoying pretty girl who's fake and gossips.", "Oh hi Player.What are you doing here... especially with that outfit?")
Brittney = people("Brittney", "Karen's follower and idiot friend", "Why are you talking to us?")
Crush = people("Crush", "the person you've liked since the beginning of freshman year. You're not even sure if he/she notices your existence.", "Thanks! You're Player right?")
Viktor = people("Viktor", "a senior who's really down to earth. He's popular because he has a kind heart and is chill with everyone. He's in some of your classes but you haven't really talked to him.", "Hey, you're in my Calc class! You're Player, right?")
Lauren = people("Lauren", "a cute quiet girl from your math class.", "What's up?")
Jake = people("Jake", "who claims not to be from Statefarm and does not wear khakis", "Yooooo")
Dave = people("Dave", "a guy you see around in the hallways", "Sah dude?")
Rihanna = people("Rihanna", "a hot headed stubborn girl on the basketball team", "Hey.")
Marie = people("Marie", "a fellow loner and introvert who was also dragged her against her will. She's also in your art class", "Oh...hello there.")
# Assigning names, characteristics and messages for people in class people

# Create variables inside class people named 'Karen' and 'Brittney'

print("""It's Friday night and like every night, you're at home playing video games watching videos, and getting obese with some 'healthy' food.

Your best friend decides that you actually need a life and party during your senior year and drags you to a house party that's being thrown by\n one of the most popular kids in school.

When you arrive at the doorstep with your extroverted friend, he/she immediately ditches you and goes to a sketchy punch bowl. You know that you\n won't be seeing him/her for a while.

You know that if you leave now that your friend will murder you, so your only option is to stay until the party ends. You feel your heart start to\n pound... your worst nightmare is coming true
...social interaction.""")

# PROMPT


partypeople = ['Jay', 'Nadine', 'Brandon', 'John', 'Karen','Crush', 'Rihanna', 'Lauren', 'Jake', 'Viktor', 'Marie', 'Emma', 'Liz', 'Harry', 'Mat', 'Tyrone']
# Creation of a list of people that are at the party for the purpose of detail

burn = ['Justin', 'Kyle', 'Stephanie', 'Elena', 'Amanda']
# List of people player hates
print("Your social life is currently at 100.")
# Inital status of social life

groups = {"group_1" : "The popular girl group", "group_2" : "The lonely emo corner", "group_3" : "People playing a bunch of dumb high school games" }
# create a dictionary listing the groups/choices in the game


print("You notice that while you're standing in the middle of the living room, people from school start to encircle you, violating your personal bubble.\n Before doing anything you list some of your classmates' names.")
for item in partypeople:
    print(item)
#creation of for loop to print out every item in partypeople list


print(f"You see {groups}")
# Tells you which grouups are there


one = "be civil and leave"

two = "call them a bunch of impolite names that are not approved\n in a G-rated work space and resort to violence"

choice_one = "Pretend to commit seppuku right then and there \nwhile dropping to the ground into fetal positon."

choice_two = "apologize like crazy and hand them some napkins."
# setting up variables for the whole game
def scenario():
    print(f"While getting a drink, you quickly turn around and bump into someone. That person is now drenched. FRICK IT'S YOUR CRUSH! {Crush.description} and now you've just ruined their clothes.]\nYou want to commit seppuku and are extremely embarrassed. You're losing points dude.")
    healthbar()


    choice = str(input(f"What do you do? Choice one: {choice_one} or Choice two: {choice_two} (type answer in form of Choice_one or Choice_two)")).lower()
    # Creation of input function that allowers user to input their choice
    if choice == "choice_one":
    # If choice one is chosen-- the action that occurs
        print("Your crush begins to laugh at first but then helps you up. You apologize sheepishly and he/she forgives you. You can't believe you just did that\n in front of him/her. You lose points.")
    elif choice == "choice_two":
        print(f"Your crush is completely cool with it and says everything is fine.\n {Crush.response} You respond with a yes. After he/she cleans up, the two of you begin to talk. Good job! You saved the situation!")
    print("Yikes, some person showed up and is trying to hit on your crush. You flip a coin to see what you should do.")
    # If choice two is chosen, a message comes up with a new scenario where you have to flip a coin
    tries = 0
    heads = 0
    tails = 0
    # Creates variables of heads, tails, and tries
    while tries <= 2:
    #Creation of while loop for 3 toin tosses
        input("Flip the coin!")
        tries += 1
        coin = random.randint(1, 2)
        #Adds the tries to tries intial and sets coin equal to random integer of 1 or 2


        if coin == 1:
            heads += 1
            print(f"You got heads!")
        # sets condition if coin == 1
        if coin == 2:
            heads += 1
            print(f"You got tails!")
        #sets condition if coin == 2 and breaks
            break



    if heads > tails:
        print("You decide to leave them alone dammit! THEY'RE GETTING ALONG TOO! FRICKKJLKA! WHY YOU A FRIGGIN WIMP!? YOU LOSE POINTS!")
        #Condition if heads are greater than tails. Loss of life points
        healthbar()
        # INSERT LIFE HEREEEE
        print("Feeling a bit awkward and lonely, you decide to wander off for a bit and see another loner like you j chillin outside on the steps.")


        print(f"'What are you doing out here all alone? The party's in there.' You turn around to see who's calling out to you only to see {Viktor.name}, {Viktor.description}.\n Lol great more social interaction with someone who's practically a stranger to you. Life must hate you lol.")
        print("You're pretty done with everything right now, so what do you do?")
        # Introduction of new scenario

        convo = str(input("convo1: tell him that you want to be alone right now. convo2: Explain to him that parties aren't your scene.")).lower()
        # Prompts player for input


        if convo == "convo1":
            #Describes events that occur if convo1 is chosen
            print("Viktor looks a bit crestfallen but understands and gives you your personal space. You sigh in relief of being alone for once, however it doesn't last long\n Your best friend sees that you're alone and is furious! He/She beats you up and forces you to go on the dance floor!\n Welp that's two Ls for you, but this time they don't equal a dub. You just die a little on the inside.")
            print("You're panicking because your best friend put you in the middle of a dance circle! WHAT THE HECK ARE YOU GONNA DO!?")
            # Introduction of new scenario where player must dance
            dance = str(input("Dab like a maniac, or attempt to do a backflip? (type dab or flip)")).lower()
            # Asks for player's input on what they should do
            if dance == "dab":
                # Tells story if action dab is chosen
                print("Oh no you're cringey asl, but everyone is having a good time and laughs.\n Some people even join you! You get some popularity points for that buddy! You just dance and talk to people for the rest of the night! YOU SURVIVED!")
            elif dance == "flip":
                # Tells story if action flip is chosen
                print("You're actually an idiot. What made you think that you could do a backflip? You fricking tried and then landed so badly that you passed out and broke a leg\n  You had to be brought to the hospital and you kinda killed the mood of the party. THAT'S AN L, LIKE THE REST OF YOUR LIFE BECAUSE YOU LOSE!")
                print("Get rekted you weeb. Game over.")


        elif convo == "convo2":
            #describes events that occur if convo2 is chosen end of game if player and viktor hang out
            print("It turns out that Viktor is actually similar to you and needed a breather from the party.\n The two of you talk for the rest of the night (no romance whatsoever) and form a pretty solid friendship. Now your friend can't call you a loser. Congrats on winning!")
            print("*insert confetti and cheering and other stuff here*")
            # End of game


    elif tails > heads:
        #If tails > heads its the end of the game and player wins
        print("You pull your crush to the side and get that person to leave your crush alone. \n Congrats dude! You got some alone time with him/her! In fact, you actually hit it off pretty well and even got his/her number!\n You just won the game! I'm proud of you you nerd!!!")
        return


group = input("Which group do you join? (type group_1 or group_2 for example)")
# asks you which group you want to join
if group == 'group_1':
    print(f"""You see {Karen.name}, {Karen.description} and {Brittney.name}, {Brittney.description}.
    They're both looking you up and down and silently judging.""")
    # Introduces group 1 scenario with Karen and Brittney with their names and desrciptions


    print(f"Karen:{Karen.response}")
    print(f"Brittney:{Brittney.response}")
    # Print the conversation between player and Karen and Brittney


    print(f"You can either: one: {one}, or two: {two}")
    #Shows choices to player and what they do


    answer = str(input("What do you do? (type one or two)")).lower()
    # Input for user answer


    if answer == "one":
        #Creation of if statement if response is one
        print("You finally got away from the girls, but they may spread rumors about you or give you a hard time in school now. Rip...oh well it can't be helped just add them to your burn list.")
        for person in burn:
            #Creates a for loop to print out the names of the people in burn list
            print(person)
        burn.append(input("Who do you want to add?"))
        burn.append(input("Who else do you want to add?"))
        #Adds input at the end of the burn list
        print(f"Now your burn list consists of {burn}")
        #prints out new burn list


        print(f"A person goes up to you and offers you a suspicious drink. What do you do?")
        #Statement puts up new situation
        action = str(input("Drink or Don't drink it? (type in form of yes or no)")).lower()
        # Asks user for input of yes or no to decide what will happen next
        if action == "yes":
            print("That sus drink made you act funny for the entire party! People were snapping you and posted you on their stories.\n EXPOSED! You completely embarrassed yourself and are the talk of the school on Monday... yikes GG man. You lost.")
            #if action == yes, the player automatically loses
        elif action == "no":
            print("You say no and immediately skirt to another part of the house.\n You see the living room where some people are dancing like crazy!!! Dude... there's a fricking chandelier hanging in front of you.\nDo you swing from it and follow your dreams or nahhh?")
            swing = str(input("HECK YEAH! or nahhh (type HECK YEAH! or nahhh)")).lower()
            # Asks user for input for case of swinging on the chandelier
            if swing == "heck yeah!":
                print("Bruh you wild. Unfortunately your wildness equals stupidity.\nWhat were you thinking!? The chandelier breaks, you get hurt, everyone gets mad, and the host of the party is now in trouble with his parents.\n Now everyone thinks your an idiot and a jerk. EVEN I DO!.")
                print("GUESS WHAT FOR THAT CHOICE YOU AUTOMATICALLY LOSE! NO MORE CHANCES YOU DIE!")
                # Ends game if the user says yes
            else:
                print("Because you stood there for too long, contemplating your choices you get pushed into the middle of a dance circle. What do you do?")
                # If user says no, a dance scenario is brought up




    elif answer == "two":
        print("It was honestly worth fighting them; now everyone is watching you in either disbelief or respect.\n You're getting embarassed and lose ___ points. \n You decide to hide out with the food")
    #If-elif used over here to demonstrate the different scenarios
    healthbar()
    scenario()
        # Use of function scenario()




elif group == 'group_2':
# Scenario for group 2
    print("Now you look like a loner and feel awkward as heck. Menos puntos!\n Time to stress eat! You're now going to the food area.")
    healthbar()
    #lose points HERE CREATE FUNCTION TO CALCULATE THE NEW LIFE POINT
    # Describes the situation with crush and who they are
    # INSERT MINUS POINTS HEREEEEE
    scenario()
    # use of function scenario()


else:
#If Group Three is chosen this is the scenario that comes out of that
    print(f"Oh look they're playing truth or dare!\n You see people from class like Rihanna, {Rihanna.description} Jake {Jake.description}, Lauren,{Lauren.description}, Dave,{Dave.description}, and some other people you don't know. They ask if you want to join. What do you say?")
    invite = str(input("yes or no.")).lower()
    # Describes scenario for game of truth or dare
    if invite == "yes":
        print("A few rounds have passed and now it's your turn, so what's it going to be? Truth or dare?")
        game1 = str(input("Truth or Dare?")).lower()
        # Asks user for input


        if game1 == "dare":
            print("They dare you to lick the bottom of all of their shoes. Do you do it?")
            dare = str(input("yes or no?")).lower()
            # Asks user for input
            if dare == "yes":
                print("Damn they think you're daring asllll.\n Do you want to stay for another round or go?")
                # Asks user to play another round
                next = str(input("stay or go?")).lower()
                if next == "stay":
                    dare2 = str(input("It's your turn again. Truth or Dare?")).lower()
                    if dare2 == "dare":
                        print("Dave dares you to get duct tape to the wall until you can guess the secret number")
                        # Describes situation. User must guess secret number in order for the loop to break
                        tape = str(input("Accept or deny?")).lower()
                        if tape == "accept":
                            print("You're now taped onto the wall. They won't let you down until you guess the secret number.")
                            number = 9
                            while True:
                                if int(input("Guess the number from 1-10.")) == number:
                                    print("You guessed the secret number! They let you go!")
                                    break
                                if int(input("Guess the number from 1-10.")) != number:
                                    print("That wasn't the secret number. You're still stuck on the wall ya loser.")
                            print("You decide that you've had enough of truth or dare and just want some food and drinks.")
                            # While loop is used. While true the loop will continue until user guesses secret number 9
                            scenario()
                            # Game goes with the scenario function
                    if dare2 == "truth":
                        print("Rihanna: Is it true that you were most likely to: 'suck eggs' in high school.")
                        # Gives scenario for dare2 if truth is chosen as option. A Truth question is given, asking user for input
                        input("A response")
                        # Regardless of response, story continues onto dance floor scenario
                        print("You had quite enough of those weirdos. Now you wonder where you should go. Outside or to the dance floor?")
                        location = str(input("Outside or Dance?")).lower()
                        if location == "outside":
                            print("You see a couple making out, and your heart can't take the awkwardness and pda! You take cover and dash to the food.\nRip you lose some points.")
                            scenario()
                            # Scenario of what happens if you go outside with the input of location and then user leaving to go get food, proceeding with scenario function
                            healthbar()
                            # insert loss of life
                        elif location == "dance":
                            print("You made it to the dance floor... but wait!\nTHEY'RE PLAYING A SLOW SONG AND YOU'RE SOMEHOW IN THE MIDDLE OF THE ROOM AND CAN'T ESCAPE! WHAT DO YOU DO?!")
                            a = str(input("Slow dance with yourself? or Aggressively dance? (answer with slow or aggresive)")).lower()
                            # Prompts user for input of whether or not they should dance if they choose to go to the dance floor
                            if a == "slow":
                                print("you can feel people staring at you from a distance with pity. You single asl kid.")
                                healthbar()
                                # if user decides to slow dance with his or her self, he or she loses points
                                print("Someone takes pity and offers to dance with you. Do you accept or decline?")
                                dance = str(input("Accept or decline?")).lower()
                                # Situation where someone wants to dance with user and user must accept or decline
                                if dance == "accept":
                                    print("Woah this person is super cool! You have a lot in common with him/her!\n Do you hang out with him/her for the rest of the night?")
                                    stranger = str(input("yes or no?")).lower()
                                # Describes scenario with stranger
                                    if stranger == "yes":
                                        print("OH SHIZZ! Looks like that person has a jealous significant other who is a martial artist! Do you start drama or leave?")
                                        drama = str(input("start drama or leave?")).lower()
                                        # Asks player for his or her decision
                                        if drama == "start drama":
                                            print("Game over man that other kid knocked you out for the rest of the night.")
                                            # Game over if user chooses to start drama with the significant other.
                                        if drama == "leave":
                                            print("you decide to duck and leave and head for the snack table because nothing bad happens with food!")
                                            scenario()
                                        # If player leaves, the story proceeds with scenario function
                                    elif stranger == "no":
                                        print("You go get food instead")
                                        scenario()
                                        # Story proceeds with scenario function
                                elif dance == "decline":
                                    print("You say no and just awkwardly stand there until the song changes.\n Now it's a fast paced song! Which move do you bring out?")
                                    input("Dance move?")
                                    # Asks user for what dance they want to do
                                    print("Whatever you did... it was kinda decent. No points lost, but now you're hungry and want some food so let us go to the kitchen!")
                                    scenario()
                                    # regardless of user's choice, story proceeds with scenario function
                            elif a == "aggressive":
                                print("Wow... people actually started to join you in your aggresive dancing... Y'all are memes. GJ though, you're a trend setter.\n Oh well, you survived the rest of the party just by dancing so congrats to ou i guess...I kinda wished you failed...")
                            # End of game, user wins

            elif dare == "no":
                print("They all make fun of you and roast you so hard. Boi you looking like a peewee mothertruckin rawr xD weaboo lookin butt chicken naruto running weirdo.\n You sir, are indeed embarrassed. Feel the little social life that you had in the first place decrease.")
                healthbar()
                # INSERT LOSS OF LIFE HEREE
                print("Sigh... you go to the snack bar because food is your only friend at the moment.")
                scenario()
                # Story proceeds with scenario function


    elif invite == "no":
        print("They think your a wuss and are making fun of you. Rip you feel so pressured and embarrassed.\n Taking some damage already mate. In the end they somehow how force you to play and make you go first.")
        healthbar()
        # INSERT LOSS OF LIFE HEREE
        game = str(input("Truth or Dare?")).lower()
        # Game of truth or dare is still played even if user says no


        if game == "truth":

            print(f"Lauren asks you who would you kiss out of {partypeople}")
            # Lauren prompts user with a question
            kiss = partypeople[int(input("Pick number from -15 to 15"))]
            print(f"You chose {kiss} and now everyone is making fun of you for it. Yikes that's so awkward for you. You lose some points man.")
            #User blindly chooses who they would kiss with a number
            healthbar()
            # INSERT LOSS OF LIFE
            print("To avoid more awkwardness you get up to get a drink")
            scenario()
            # Game proceeds with scenario function


        elif game == "dare":
            print("Jake dares you to cut the music, grab the microphone and start free-styling. What do you do?")
            challenge = str(input("Challenge accepted or rejected? (type accepted or rejected)")).lower()
            if challenge == "accepted":
                print("You grabbed the mic and cut the music. What's your rap?")
                # User is asked to rap
                input("""Insert rap verse here""")
                # User can insert their rap here
                print("Your rap wasn't fire enough. There was no applause. In fact, people yell at you to get off the stage. \nRip you. Your social life goes down")
               # Player loses points because their rap wasn't good enough
                healthbar()
                again = str(input("You wanna try rapping again? (yes or no)")).lower()
                # Player can try again if they wish
                if again == "yes":
                    input("""Begin rapping""")
                    # Player can rap again
                    print("Wow that was even worse than the last one! You lose even more points!\n Are you crying yet? Anyways, let's proceed with the game.")
                    print(f"""You see a girl who was keeping to herself. You go up to her and it turns out that its Marie, {Marie.description}.\n Marie: {Marie.response}""")
                    introvert = input("Do you talk to her? Yes or no?").lower()
                    if introvert == "yes":
                        print("You had a great time with Marie and you became friends with her!\nYou spend the rest of the night hanging with her. Hooray you survived!")
                    else:
                        print("You give her the cold shoulder... damn you're heartless and rude just for that I'm subtracting points from your life.\n Why don't you just go get food you jerk!")
                        healthbar()
                        # Loss of life points
                        scenario()



                    # Player loses points for action
                elif again == "no":
                    print("Do you wanna scream XD into the mic just to piss them off though?")
                    # PLayer is given a choice to scream XD at party
                    XD = str(input("yes or no?")).lower()
                    if XD == "yes":
                        print("Congrats you pissed everyone off... they even tell you to leave the party\n... Rip... at least you can go home and watch some Netflix and eat some food.")
                        # Game ends because player pisses everyone at party off
                    elif XD == "no":
                        print("Fine go get some food instead you boring human.")
                        scenario()
                        # If player says no, story proceeds with scenario function

            elif challenge == "rejected":
                print("Everyone in the group kicks you out because you're no fun. Great now what are you going to do?")
                # User gets kicked out of truth or dare
                print("Pretend to die right there on the spot or get some food?")
                food = str(input("die or food?")).lower()
                # User gets to choose to pretend to die or get some food
                if food == "die":
                    print("lol you stay like that for the entire night you fricking weirdo.\nNo wonder you have no friends and no social life. Game over what do you expect?")
                elif food == "food":
                    scenario()
                # Story proceeds with scenario function
                # INSERT LIFE HEREEE


