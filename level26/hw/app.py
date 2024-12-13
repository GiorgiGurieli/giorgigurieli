# def ფუნქციის სახელი () :
# def ---- ჩაშენებული სიტყვა როგორც მაგალითად: for, while , if , elif , else , or , def...
# def ---- ქმნის ფუნქციას: 

#def ixvis_tolma():
    #print("იხვის ტოლმა ბაჟეში!")
    #print("იხვის ტოლმა ბაჟეში!")
#ixvis_tolma()
#ixvis_tolma()

# ფუნქციას სანამ არ შევქმნით მისი გამოძახება შეუძლებელია python-ში
from turtle import *
# walk() ❌
def walk():
    forward(200)

def fall_back():
    left(180)
    forward(200)

def წავიდეს_საქეიფოდ(raodenoba):
    for i in range(raodenoba):
        walk()
        fall_back()    

# ფუნქციის სახელს რომ ვწერთ და
# მრგვალ ფრჩხილებს ვუწერთ ()  "ვიძახებთ ფუნქციას" / "CALL FUNCTION"
width(12)
walk()
color('red')
fall_back()
წავიდეს_საქეიფოდ()


exitonclick()