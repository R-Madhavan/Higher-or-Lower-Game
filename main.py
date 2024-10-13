import random
from art import logo,vs
from game_data import data
print(logo)
score = 0

should_continue = True
while should_continue:
    random_data1 = random.choice(data)
    random_data2 = random.choice(data)
  
    # using while loop to not use both same data to compare.
    while random_data2 == random_data1:
        random_data2 = random.choice(data)
      
    # the "follower_count" of that game data
    optionA = random_data1["follower_count"]
    optionB = random_data2["follower_count"]
  
    # checks which followers count is higher
    print(f"Compare A: {random_data1["name"]}, a {random_data1["description"]}, from {random_data1["country"]}.")
    print(vs)
    print(f"Compare B: {random_data2["name"]}, a {random_data2["description"]}, from {random_data2["country"]}.")
    guessed_highest_follower = input('Who has more follower? Type "A" or "B": ').upper()
    print("\n"*20)
  
    # comparing optionA and optionB to check which is highest
    actual_highest_followers = ""
    if optionA > optionB:
        actual_highest_followers += "A"
    elif optionA < optionB:
        actual_highest_followers += "B"

    # comparing guessed_highest_follower with actual_highest_followers
    if guessed_highest_follower == actual_highest_followers:
        print(logo)
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        should_continue = False
        print(logo)
        print(f"Sorry, that's wrong. Final score: {score}")
