class people():
# creation of class people with characteristics of names, descriptions and responses

    def __init__(self, name, description, response):
        #Initializing new instance of Character class
        #Assigning parameters in the given function that belong to class Group On
        self.name = name
        self.description = description
        self.response = response


Karen = people("Karen", "The snobby, popular, and annoying pretty girl who's fake and gossips.", "Oh hi Player.What are you doing here... especially with that outfit?")
Brittney = people("Brittney", "Karen's follower and idiot friend", "Why are you talking to us?")
Crush = people("Crush", "The person you've liked since the beginning of freshman year. You're not even sure if he/she notices your existence.", "Oh hey, Player")
Victor = people("Victor", "A senior who's really down to earth. He's popular because he has a kind heart and is chill with everyone. He's in some of your classes but you haven't really talked to him.", "Hey, you're in my Calc class! You're Player, right?")
damage = 15
def life():
    x = 100 - damage
    Social_life = x
    print(f"your social life health is now at {x}")
    return
# Create function that tracks your life
# Create variables inside class people named 'Karen' and 'Brittney'

print("""It's Friday night and like every night, you're at home playing video games watching videos, and getting obese with some 'healthy' food.

Your best friend decides that you actually need a life and party during your senior year and drags you to a house party that's being thrown by\n one of the most popular kids in school.

When you arrive at the doorstep with your extroverted friend, he/she immediately ditches you and goes to a sketchy punch bowl. You know that you\n won't be seeing him/her for a while.

You know that if you leave now that your friend will murder you, so your only option is to stay until the party ends. You feel your heart start to\n pound... your worst nightmare is coming true
...social interaction.""")


print("Your social life is currently at 100.")

groups = {"group_1" : "The popular girl group", "group_2" : "A lonely corner"}
# create a dictionary listing the groups/choices in the game

print(f"You see {groups}")
one = "be civil and leave"
two = "call them a bunch of impolite names that are not approved\n in a G-rated work space and resort to violence"
group = input("Which group do you join? (type group_1 or group_2 for example)")
if group == 'group_1':
    print(f"""You see {Karen.name}, {Karen.description} and {Brittney.name}, {Brittney.description}.
    They're both looking you up and down and silently judging.""")
    print(f"Karen:{Karen.response}")
    print(f"Brittney:{Brittney.response}")
    # Print the conversation between player and Karen and Brittney
    print(f"You can either: one: {one}, or two: {two}")
    #Shows choices to player and what they do
    answer = str(input("What do you do? (type one or two)")).lower()
    # Input for user answer
    if answer == "one":
        print("You finally got away from the girls, but they may spread rumors about you.")
    elif answer == "two":
      print("It was honestly worth fighting them; now everyone is watching you in either disbelief or respect.\n You're getting embarassed and lose ___ points. \n You decide to hide out with the food")
    #If-elif used over here to demonstrate the different scenarios
#CALCULATE THE NEW LIFE POINTS HEREEE
else:
    print("Now you look like a loner and feel awkward as heck. Menos ___ puntos.\n Time to stress eat! You're now going to the food area.")
    #lose points HERE CREATE FUNCTION TO CALCULATE THE NEW LIFE POINT
    print(f"While getting a drink, you quickly turn around and bump into someone. That person is now drenched. FRICK IT'S YOUR CRUSH! {Crush.description}.")




#def life():
    #x = 100 - damage
    #Social_life = x
    #print(f"your social life health is now at {x}")
    #return
#Create function that tracks your life