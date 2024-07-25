import random

MoveArray = {"R":"Rock","S":"Scissor","P":"Paper"}
beat = {"Rock":"Scissor","Paper":"Rock","Scissor":"Paper"}
def getMove():
    move=input("Enter your move: ").strip().upper()

    while move not in MoveArray:
        move = input("invalid input enter R S or P > ")

    return MoveArray[move]
    

def cpuMove():
    print('CPU is selecting its moves....')


    cpuMove = random.choice(list(MoveArray.values()))
    return cpuMove



def DecideWinner(PlayerMove,cpuMove):
    

    if PlayerMove == cpuMove:
        return 't'
    elif beat[PlayerMove] == cpuMove:
        return 'p'
    else:
        return 'c'
def printMatchInfo(PlayerWins,ComputerWins,Ties):
    print(f'Players Wins:{PlayerWins}\tComputer Wins:{ComputerWins}\tTies:{Ties}')       


def main():
    
    PlayerWins = 0
    ComputerWins = 0
    Ties = 0
    previousComputerMove = ''
    print("Rock Paper, Scissors\nCreated By Rafay Ahmad Raza")
    print("Hello Welcome to my simple rock paper scissors game!\nThe Moves can be written in short form\nR\tRock\nS\tScissor\nP\tPaper")
    while True:
        
        PlayerMove = getMove()
        ComputerMove= cpuMove()
        print(PlayerMove,ComputerMove)
        Winner = DecideWinner(PlayerMove,ComputerMove)

        while previousComputerMove == ComputerMove:
            ComputerMove = cpuMove()

        if Winner == 'p':
            print("Congrats! You have won!\n Do you want to play again? y/n")
            PlayerWins+=1
            if input(">").lower() != 'y':
                print("Bye Bye!")
                printMatchInfo(PlayerWins,ComputerWins,Ties)
                break
        elif Winner == 'c':
            print("Drats you lost. better luck next time!\nDo you want to play again? y/n")
            ComputerWins+=1
            if input(">").lower() != 'y':
                print("Bye Bye!")
                printMatchInfo(PlayerWins,ComputerWins,Ties)
                break
        elif Winner == 't':
            print("It a TIE!\nDo you want to play again? y/n")
            Ties+=1
            if input(">").lower() != 'y':
                print("Bye Bye!")
                printMatchInfo(PlayerWins,ComputerWins,Ties)
                break
        printMatchInfo(PlayerWins,ComputerWins,Ties)
        previousComputerMove = ComputerMove
if __name__ == '__main__':
    main()


