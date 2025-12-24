def answer(q,x,a,y):
    print(q)
    if (x==int(a)):
        print("your answer is correct")
        y+=10
    else:
        print("your answer is wrong")
    return y
y=0
q1="""Which is the largest planet in our Solar System?
A. Earth
B.Jupiter
C. Saturn
D. Neptune"""
a1=2
print(q1)
x1=int(input("Enter your answer:",))
y=answer(q1,x1,a1,y)
q2="""Who was the first President of India?
A) Dr. Rajendra Prasad
B) S. Radhakrishnan
C) Jawaharlal Nehru
D) C. Rajagopalachari"""
a2=1
print(q2)
x2=int(input("Enter your answer:",))
y=answer(q2,x2,a2,y)
q3="""The currency of Japan is:
A) Yen
B) Won
C) Yuan
D) Ringgit"""
a3=1
print(q3)
x3=int(input("Enter your answer:",))
y=answer(q3,x3,a3,y)
q4="""Which is the longest river in the world?
A) Amazon
B) Nile
C) Ganga
D) Yangtze"""
a4=2
print(q4)
x4=int(input("Enter your answer:",))
y=answer(q4,x4,a4,y)
q5="""Who is known as the “Missile Man of India”?
A) Homi J. Bhabha
B) Dr. A.P.J. Abdul Kalam
C) Vikram Sarabhaii
D) Satish Dhawan"""
a5=2
print(q5)
x5=int(input("Enter your answer:",))
y=answer(q5,x5,a5,y)
print("Final score:",y)