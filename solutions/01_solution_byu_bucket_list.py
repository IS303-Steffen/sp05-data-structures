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
You're creating a bucket list of things to do at BYU.

1. Create a list called `bucket_list` with 3 activities as strings.
2. Print the entire list.
3. Print the second item in the list.
4. Use append() to add one more activity.
5. Print the updated list.
'''

# Here is one potential solution. Remember there are often many different
# ways to solve a problem, so your solution may not look exactly the same.

bucket_list = ["Hike the Y", "Eat at the Cougareat", "Go to a football game"]
print(bucket_list)
print(bucket_list[1])
bucket_list.append("Attend a devotional")
print(bucket_list)
