import random
import time 
"""
gen function is used for generate the chain you will type
inputs: dif: Difficult for your line, how many characters you will replicate
        line: this is the index you selected for typing 
"""
def gen(dif,line):
    #row type: the list of charaters selected 
    row_type=row(line)
    quan=len(row(line))
    chain=[]
    #lon: how many characters gonna be typed
    #s: "blocks" of charaters
    #example: difficult 1 will have 15 characters separated in blocks with
    #3 characters each one
    if dif==1:
        s=3
        lon=15
    elif dif==2:
        s=5
        lon=30
    elif dif==3:
        s=8
        lon=50
    #loop for generate the chain charater
    for i in range(0,lon):
        #conditional for generate the segmentation of the chain
        if i%s==0 and i!=0:
            chain.append(" ")
        #first we make a list with random order of the row selected
        x=random.randint(0,quan-1)
        chain.append(row_type[x])
    #put together all the items of the list
    chain="".join(chain)
    print("Write down the characters below:\n")
    print(chain)
    #we measure the time the user takes to write the chain since he/she 
    #see line firts time
    t=time.time()
    #output: chain is the chain character user will replicate
    #t: the moment the chain es showed
    return chain,t

"""
row function is used for saving the keyboard keys in diferent
lists and then put them inside another list called ROWS
and then we return the a row using num input from the app method.
"""
def row(num):    
    NUMBERS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    #Easy way to covert numbers' row in a list with strings
    for i in range (0,len(NUMBERS)):
        NUMBERS[i] = str(NUMBERS[i])
    TOP=['q','w','e','r','t','y','u','i','o','p']
    HOME=['a','s','d','f','g','h','j','k','l','ñ']
    BOTTOM=['z','x','c','v','b','n','m']
    ROWS=[NUMBERS,TOP,HOME,BOTTOM]
    return ROWS[num]

def app():
    #First input you select the difficult 
    print("Welcome to my type master. This program is for practicing \
    and improving your typing in a keyboard. Choose a difficult:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    dif_selected=int(input("Type the number:\n"))
    #Second input is select the keyboard row you want to practice
    print("Choose the row of your keyboard you want to practice:")
    print("0. Numbers")
    print("1. Top row")
    print("2. Home Row")
    print("3. Bottom Row")
    row_selected=int(input("Type the number:\n"))
    far,t=gen(dif_selected,row_selected)
    #user type the chain 
    insert=input()
    #comprobate if the user did well
    if insert==far:
        print("YOU DID WELL!")
        print(f"Your time was {time.time()-t}")
    else:
        print("Wrong!!")

if __name__=="__main__":
    fl=0
    while fl==0:
        app()
        #User can select if he wants to try again
        fl=int(input("Type 0 if you want to try again or 1 for exit:\n"))
    
    input("Press enter to exit\n")