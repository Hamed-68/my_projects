##you can test your ability in Multiplication 

import time
from random import randint

right_answer = 0  ##all of your right answer
wrong_answer = 0  ##all of your wrong answer

for i in range(10):
    a = randint(1, 10)
    b = randint(1, 10)

    t1 = time.perf_counter() ##START TIME
    print(f"{a} * {b}")
    answer = int(input())
    t2 = time.perf_counter() ##END TIME

    if (t2 - t1) <= 3 and answer == (a * b): ## 3 SECOND TIME TO TYPE RIGHT ANSWER
        print("right answer!!!")
        right_answer += 1
    elif (t2 - t1) <= 3 and answer != a * b:
        print("wrong answer!!!")
        wrong_answer += 1
    elif (t2 - t1) > 3 and answer == a * b:
        print("you lose time!!!")
        wrong_answer += 1
        print(t2 - t1)
    elif (t2 - t1) > 3 and answer != a * b:
        print("wrong answer!! lose time!!")
        wrong_answer += 1
        print(t2 - t1)
print("Right answers :", right_answer, "Wrong answers :", wrong_answer)
if right_answer == 10:
    print("CONGRATIOLATION!!! YOU ARE PROFESHIONAL")
else:
    print("YOU NEED MORE PRACTICE")
