import random


def game():

    print("Lets Play a game :  ")
    news_score=random.randint(0,100)

    print("Well Played")

    with open('hiscore.txt') as f:
        high_score=f.read()
        if high_score!="":
            high_score=int(high_score)
        else:
            high_score=0
    print(f"Your score is {news_score}")

    if news_score>high_score:
        with open("hiscore.txt","w") as f:
            f.write(str(news_score))
    return news_score

game()