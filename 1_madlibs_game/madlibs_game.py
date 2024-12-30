# A mad libs game is a word game where you can create an story with random words

# First let's ask for some adjectives and nouns
print("Let's play a mad libs game 🥳")
adjective1 = input("Give me a random adjective (An adjective is a description of something 😉): ")
noun1 = input("Give a random noun (A noun could be a person, animal, place or thing 😏): ")
adjective2 = input("Give me another random adjective: ")
verb1 = input("Give me a verb (A verb is an action like running, swimming or sleeping 😴): ")
adjective3 = input("Now give me a last adjective: ")

# Not let's create a short story
print(f'Today my family went to a {adjective1} cinema')
print(f'They saw a movie where the actor was {noun1}')
print(f'{noun1} was {adjective2} and {verb1}')
print(f'They were {adjective3}')