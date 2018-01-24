import random
# importing random function
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
    Social_life.life = Social_life.life - random.randint(1,25)
    #Takes initial life points and subtracts it by random integer creating a new life value
    if Social_life.life > 0:
        print(f"Your Social life is currently at {Social_life.life}")
        # Game continues if life is > 0
    elif Social_life.life <= 0:
        print("Rip, the party was too much for an antisocial loser like you! You lose!")
        # Game ends if life is less than or equal to 0


Karen = people("Karen", "the snobby, popular, and annoying pretty girl who's fake and gossips.", "Oh hi Player. What are you doing here... especially with that outfit?")
Brittney = people("Brittney", "Karen's follower and idiot friend", "Why are you talking to us?")
Crush = people(f"Crush", "the person you've liked since the beginning of freshman year. You're not even sure if he/she notices your existence.", "Thanks! You're Player right?")
Viktor = people(f"Viktor", "a senior who's really down to earth. He's popular because he has a kind heart and is chill with everyone. He's in some of your classes but you haven't really talked to him.", "Hey, you're in my Calc class! You're Player, right?")
Lauren = people("Lauren", "a cute quiet girl from your math class.", "What's up?")
Jake = people("Jake", "who claims not to be from Statefarm and does not wear khakis", "Yooooo")
Dave = people("Dave", "a guy you see around in the hallways", "Sah dude?")
Rihanna = people("Rihanna", "a hot headed stubborn girl on the basketball team", "Hey.")
Marie = people("Marie", "a fellow loner and introvert who was also dragged her against her will. She's also in your art class", "Oh...hello there.")
Mark = people("Mark", "he's the grade's class clown but is really cringey. He always makes things interesting though.", "What up Player!")
Jeff = people("Jeff", "the stereotypical good-looking and dumb quarterback of the football team. He has a lot of anger issues and overreacts to everything, but is somehow popular.", "*he's currently flirting with a cheerleader*")
# Assigning names, characteristics and messages for people in class people

# Create variables inside class people named 'Karen' and 'Brittney'
bets = {"bet 1": "Tackle Jeff, " + Jeff.description, "bet 2": "Mark: Bet you won't make out with me right now."}

print("""It's Friday night and like every night, you're at home playing video games, watching videos, and getting obese with some 'healthy' food.

Your best friend decides that you actually need a life and need to party during your senior year, so he/she drags you to a house party that's being thrown by\n one of the most popular kids in school.

When you arrive at the doorstep with your extroverted friend, he/she immediately ditches you and goes to a sketchy punch bowl. You know that you\n won't be seeing him/her for a while.

You also know that if you leave now, your friend will murder you, so your only option is to stay until the party ends.


--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


You feel your heart start to\n pound... your worst nightmare is coming true
...social interaction.
...
...
...
Your 'Social Life' bar is currently at 100.""")

# Prompt of story and current status of player

partypeople = ['Jay', 'Nadine', 'Brandon', 'John', 'Karen', 'Rihanna', 'Lauren', 'Jake', 'Marie', 'Emma', 'Harry']

burn = ['Justin', 'Kyle', 'Stephanie', 'Elena', 'Amanda']
# List of people player hates

groups = {"group_1" : "The popular girl group",  "group_2" : "People playing a bunch of dumb high school games" }
# create a dictionary listing the groups/choices in the game


print(f"You see {groups} which one would you like to join?")
# Tells you which grouups are there


one = "be civil and leave"

two = "call them a bunch of impolite names that are not approved\n in a G-rated work space and resort to violence"

choice_one = "Pretend to commit seppuku right then and there \nwhile dropping to the ground into fetal positon."

choice_two = "apologize like crazy and hand them some napkins."
# setting up variables for the whole game


def scenario():
    print(f"While getting a drink, you quickly turn around and bump into someone. That person is now drenched. FRICK IT'S YOUR CRUSH! {Crush.description} and now you've just ruined their clothes.]\nYou want to commit seppuku and are extremely embarrassed. You're losing points dude.")
    healthbar()
    #input the healthbar function into scenario function so that healthbar decreases throughout game
    choice = str(input(f"What do you do? Choice one: {choice_one} or Choice two: {choice_two} (type answer in form of Choice_one or Choice_two)")).lower()
    # Creation of input function that allowers user to input their choice
    if choice == "choice_one":
    # If choice one is chosen-- the action that occurs
        print("Your crush begins to laugh at first but then helps you up. You apologize sheepishly and he/she forgives you. You can't believe you just did that\n in front of him/her. You lose points.")
    elif choice == "choice_two":
        print(f"Your crush is completely cool with it and says everything is fine.\n {Crush.response} You respond with a yes. After he/she cleans up, the two of you begin to talk. Good job! You saved the situation!")
    print("Yikes, some person showed up and is trying to hit on your crush. You flip a coin a few times to see what you should do.")
    # If choice two is chosen, a message comes up with a new scenario where you have to flip a coin


    tries = 0
    heads = 0
    tails = 0
    # Creates variables of heads, tails, and tries
    while tries <= 3:
    #Creation of while loop for 3 toin tosses
        input("Flip the coin! (type 'flip')")
        tries += 1
        coin = random.randint(1, 2)
        #Adds the tries to tries intial and sets coin equal to random integer of 1 or 2


        if coin == 1:
            heads += 1
            print(f"You got heads!")
        # sets condition if coin == 1
        if coin == 2:
            tails += 1
            print(f"You got tails!")
        break
        #sets condition if coin == 2 and breaks




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
                print("You're actually an idiot. What made you think that you could do a backflip? You fricking tried and then landed so badly that you passed out and broke a leg\n  You had to be brought to the hospital and you kinda killed the mood of the party. THAT'S AN L, LIKE THE REST OF YOUR LIFE! YOU LOSE!")
                print("Get rekted. Game over.")


        elif convo == "convo2":
            #describes events that occur if convo2 is chosen end of game if player and viktor hang out
            print("It turns out that Viktor is actually similar to you and needed a breather from the party.\n The two of you talk for the rest of the night (no romance whatsoever) and form a pretty solid friendship. Now your friend can't call you a loser. Congrats on winning!")
            print("*insert confetti and cheering and other stuff here*")
            # End of game


    elif tails > heads:
        #If tails > heads its the end of the game and player wins
        print("You pull your crush to the side and get that person to leave your crush alone. \n Congrats dude! You got some alone time with him/her! In fact, you actually hit it off pretty well and even got his/her number!\n You just won the game! I'm proud of you, you nerd!!!")
        return

def bet():
    print(f"Unfortunately you bump into {Mark.name}, {Mark.description}. Mark: Bet you won't do: {bets}. Oh shiz, man, he bet you. You gotta do it now, or else you'll look weak. \nWhich one do you choose?")
    betting = input("bet1, or bet2 (answer as bet1 or bet2)?").lower()
    if betting == "bet1":
        print("You tackle Jeff and now you gotta face his fury! Do you run or fight?")
        fight = input("fight or run?").lower()
        if fight == "fight":
            print("Jeff knocks you out and you're sent to the hospital with a broken nose, arm, and leg. GG mate.")
        elif fight == "run":
            print("You decide to hide out with the food for a bit while avoiding Jeff.\n You were almost a goner and now everyone is talking about you. You lose some points.")
            healthbar()
            scenario()
    elif betting == "bet2":
        print(f"Dude Mark was just playing. No one actually wants to make out with your ugly face.\n Now the whole party is a bit weirded out by you. Yikes...go hide with the food man.")
        healthbar()
        scenario()
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
                dancecircle = input("Cry or dance?").lower()
                if dancecircle == "dance":
                    print("Dude you were dancing too hard and knocked everyone at the party out... what the frick???\nI mean i guess you're free to leave now so I guess that's a dub on you.")
                elif dancecircle == "cry":
                    print("Everyone slowly walks away from you because they don't know what's wrong with you, nor do they care.\n Why did you even cry in the first place?? Just get some food and walk it off soldier I won't deduct points out of pity.")
                    scenario()
                # If user says no, a dance scenario is brought up and game may possibly end




    elif answer == "two":
        print("It was honestly worth fighting them, however, now everyone is staring at you in either disbelief or respect.\n You're getting embarassed and lose points. \n You decide wander somewhere else")
    #If-elif used over here to demonstrate the different scenarios
    healthbar()
    bet()
        # Use of function scenario()


else:
#If Group Three is chosen this is the scenario that comes out of that
    print(f"Oh look they're playing truth or dare!\n You see people from class like Rihanna, {Rihanna.description} Jake {Jake.description}, Lauren,{Lauren.description}, Dave,{Dave.description}, and some other people you don't know. They ask if you want to join. What do you say?")
    invite = str(input("yes or no.")).lower()
    # Describes scenario for game of truth or dare
    if invite == "yes":
        print("A few rounds have passed and now it's your turn, so what's it going to be? Truth or dare?")
        game1 = str(input("Truth or Dare?")).lower()
        # Asks user for input
        if game1 == "truth":
            print("Rihanna: Here's a truth for you, we want you to leave.\n Damn they just kicked you out...yikes...guess you're getting food now.")
            health()
            scenario()
            # inputs health function to lose points then scenario function to continue the game


        elif game1 == "dare":
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
                            print("You're now taped onto the wall.\nThey forget about you and leave you there for the rest of the night...rip GG mate")

                            # Game goes with the scenario function
                    if dare2 == "truth":
                        print("Rihanna: Is it true that you were most likely to: 'suck eggs' in high school.")
                        # Gives scenario for dare2 if truth is chosen as option. A Truth question is given, asking user for input
                        input("A response")
                        # Regardless of response, story continues onto dance floor scenario
                        print("You had quite enough of those weirdos and decide to go dancing")
                        input("Dance move?")
                        # Asks user for what dance they want to do
                        print("Whatever you did... it was kinda decent. No points lost, but now you're hungry and want some food so let us go to the kitchen!")
                        scenario()
                elif next == "go":
                    print("You excuse yourself to get some food.")
                    scenario()

                            # End of game, user wins

            elif dare == "no":
                print("They all make fun of you and roast you so hard. Boi you looking like a peewee mothertruckin rawr xD weaboo lookin butt chicken naruto running weirdo.\n You sir, are indeed embarrassed. Feel the little social life that you had in the first place decrease.")
                healthbar()
                # INSERT LOSS OF LIFE HEREE
                print("Sigh... you go wander off to avoid everyone.")
                bet()
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
            kiss = partypeople[int(input("Pick number from -11 to 10"))]
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
                print(f"""You see a girl who was keeping to herself. You go up to her and it turns out that its Marie, {Marie.description}.\n Marie: {Marie.response}""")
                introvert = input("Do you talk to her? Yes or no?").lower()
                if introvert == "yes":
                    print("You had a great time with Marie and you became friends with her!\nYou spend the rest of the night hanging with her. Hooray you survived!")
                else:
                    print("You give her the cold shoulder... damn you're heartless and rude just for that I'm subtracting points from your life.\n Why don't you just go get food you jerk!")
                    healthbar()
                # Loss of life points
                    scenario()
                # Proceeds to scenario function

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


