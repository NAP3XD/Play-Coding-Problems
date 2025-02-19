print("# DRY, KISS, NO DOC")
import random
head = 1
tail = 0
other_head = True
other_tail = False
u_score = random.randint(0, 1)
u_score += random.randint(0, 1)
u_score += random.randint(0, 1)
print("Welcome to Doggo's Coin Flip GAme! Flip 3 times to see how many heads you can get against the Computer! A tie goes to the House! Good Lucky!")
print(f"User got {u_score} Heads!")
c_1 = random.randint(0, 1)
c_2 = random.randint(0, 1)
c_score = 0
if c_1 > c_2:
    c_score += 1
if c_1 == c_2:
    c_score += 1
c_1 = random.randint(0, 1)
c_2 = random.randint(0, 1)
if c_1 > c_2:
    c_score += 1
if c_1 == c_2:
    c_score += 1
c_1 = random.randint(0, 1)
c_2 = random.randint(0, 1)
if c_1 > c_2:
    c_score += 1
if c_1 == c_2:
    c_score += 1
print(f"Computer got {c_score} Heads!")
if u_score > c_score:
    print("YOu Win!")
if c_score >= u_score:
    print("YOU LoST!")
