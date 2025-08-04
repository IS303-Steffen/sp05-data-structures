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
You're tracking grades for 2 classes using a dictionary.

1. Create a dictionary called `grades` with keys "Math" and "History"
   and values as the current grade (e.g., 95, 88).
2. Print the dictionary.
3. Ask the user for their new Math grade and update the dictionary.
4. Print just the updated Math grade.
'''

# Here is one potential solution. Remember there are often many different
# ways to solve a problem, so your solution may not look exactly the same.

grades = {
    "Math": 95,
    "History": 88
}

print(grades)

new_math = int(input("What is your new Math grade? "))
grades["Math"] = new_math

print("Updated Math grade:", grades["Math"])
