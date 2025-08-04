'''
OPTIONAL AI GUIDANCE PROMPT:
----------------------------
I am a student in an introductory Python class. I am learning many coding
principles for the very first time. I am going to paste in the instructions to
a practice problem that my professor gave me to try before class. Please be my
kind tutor and walk me through how to solve the problem step by step.

Don't just give me the full solution all at once (unless I later ask for it).
Instead, help me work through it gradually, with clear explanations and small,
easy-to-understand examples. Please use everyday language and explain things
in a simple, friendly way.


INSTRUCTIONS:
-------------
You are asking your friend about their favorite foods.

1. Create an empty list called `favorite_foods`.
2. Use input() to ask the user for 3 favorite foods.
3. Use append() to add each food to the list.
4. Print the full list at the end.
'''

# Here is one potential solution. Remember there are often many different
# ways to solve a problem, so your solution may not look exactly the same.

favorite_foods = []

food1 = input("Enter a favorite food: ")
food2 = input("Enter another favorite food: ")
food3 = input("Enter one more favorite food: ")

favorite_foods.append(food1)
favorite_foods.append(food2)
favorite_foods.append(food3)

print(favorite_foods)
