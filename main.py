from question import questions


print("welcome")

name = input("whats your name?")

score = 0 

for item in questions:
    answer = input(item["question"])

    if answer.lower() == item["answer"]:
        print("correct")
        score += 1
    else:
        print("wrong")

print("your score is:", score, "out of ", len(questions))

if score == len(questions):
    print("excellant job", name)
elif score >=2:
    print("good job", name)
else:
    print("keep praticking", name)

with open("results.txt", "a") as file:
    file.write(f"{name} - {score}/{len(questions)}\n")
    