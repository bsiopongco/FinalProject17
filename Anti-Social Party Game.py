print("""It's Friday night and like every night, you're at home playing video games watching videos, and getting obese with some 'healthy' food.\n
your best friend decides that you actually need a life and party during your senior year and drags you to a house party that's being thrown by\n one of the most popular kids in school.
When you arrive at the doorstep with your extroverted friend, he/she immediately ditches you and goes to a sketchy punch bowl. You know that you\n won't be seeing him/her for a while.
You know that if you leave now that your friend will murder you, so your only option is to stay until the party ends. You feel your heart start to\n pound... your worst nightmare is coming true
social interaction.""")

Social_life = 100
#Set variable of your health bar
class people():
# creation of class people with characteristics of names, descriptions and responses
    def __init__(self, name, description, response):
        #Initializing new instance of Character class
        #Assiining parameters in the given function that belong to class Group On
        self.name = name
        self.description = description
        self.response = response
Karen = people("Katie", "The snobby, popular, and annoying pretty girl who's fake and gossips.", "Oh hi Player.What are you doing here... especially with that outfit?")
Brittney = people("Brittney", "Karen's follower and idiot friend", "Why are you talking to us?")
print(f"You see {Karen.name}, {Karen.description} and {Brittney.name}, {Brittney.description}")
print(f"{Karen.response}")
print(f"{Brittney.response}")

1 = leave
2 = call them a bunch of impolite names

# make dictionaries of groups with the people in the groups



