import random
when = ["Day before yesterday", "On January 31st", "Last week", "During Christmas Eve", "Few years ago"]
who = [" A rabbit", "A cat", "A lion", "An Elephant", "A tiny turtle"]
name = ["Rahul", "Simba", " Bella", " Daisy", "Oreo"]
residence = ["India", "Germany", "Barcelona", "Italy", "Ohio"]
went = ["School", "House", "Univeristy", "Apartment", "Eiffel Tower"]
happened = ["made a ruckus", "slept for a long time", "made friends", "scared a man", "ate a Burger"]
print(random.choice(when) + ', ' + random.choice(who) + ' named ' + random.choice(name) + 
      ' that lived in ' + random.choice(residence) + ', went to the ' + random.choice(went) + 
      ' and ' + random.choice(happened) + '.')