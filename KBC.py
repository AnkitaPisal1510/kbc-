question=[
    "1.how many continents are there ?",
    "2.what is the capital of india ?",
"3.ng mai kon se course phadhaya jata hai ?"
]
option=[
    ["1.four","2.nine","3.seven","4.eight"],
["1.kopi","2.bhopal","3.pune","4.delhi"],
["1.software Engineering/cooding","2.zagda karna truth and dare khelna","3.bavarchi/blmajduri","4.zadhu poccha"]
]
solution=[3,4,1]
Z=[["1.four","3.seven"],["1.khopi","4.delhi"],["1.software Engineering/cooding","4.zadu pochha"]]
print(                       " 😎😎🤗🤗🤗 WELCOME TO KBC🤗🤗🤗😎😎                              ")
i=0
count=0
sum=0
while i<len(question):
    print(question[i]) 
    j=0
    while j<len(option[i]):
        print(option[i][j])
        j+=1
    num=int(input("enter your answer"))
    j=input("👩‍💻are you sure about your answer I don't thik so👩‍💻🙄🙄")
    if j=="no":
        print("ok")
        lifeline=input("👩‍💻👩‍do to you want any lifeline👩‍💻👩‍")
        if lifeline=="yes":
                use=int(input("🤔🤔which lifeline you want🤔🤔 "))
                if use==5050:
                    print("👉ok👈")
                if count<1:
                    print(Z[i])
                    count+=1
                    num=int(input("🙄🙄🤔🤔enter the answer🤔🤔🙄🙄"))
                    if num==solution[i]:
                        print("😁your answer is correct😁")
                        print()
                        sum+=10000
                        print(sum,"🤑🤑🤑👏👏👏you won that much amount👏👏👏🤑🤑🤑")
                        print()
                    else:
                        print("😔🥺game over🥺😔")
                        print("you have to return with this amount",sum)
                        break
                else:
                    print(" opps! 😔😔you cant use lifeline again😔😔")
                    num=int(input("enter your answer"))
                    if num==solution[i]:
                        print("right answer😁")
                        print()
                        sum+=100000
                        print(sum,"🤑🤑🤑👏👏👏congrats you won👏👏👏🤑🤑🤑")
                        print()
                    else:
                        print('🥺you lost🥺')
                        print('you have to return with this amount',sum)
                        break
                        
    else:
        if num==solution[i]:
            print("right answer😁‍")
            print()
            sum+=1000000
            print(sum,"🤑🤑🤑🥳🤗🤗👏👏congrats👏👏🤗🤗🥳🤑🤑🤑")
            print()
        else:
            print("🥺😔😔game over🥺😔😔")
            print("you have to return with this amount",sum)
            break
    i+=1
else:
    print()
    print("🥳🥳🥳🥳💐💐💐🤩🤩🤩👏👏👏congrats you won the KBC👏👏👏🤩🤩🤩 💐💐💐🥳🥳🥳🥳")
    

        

    
        