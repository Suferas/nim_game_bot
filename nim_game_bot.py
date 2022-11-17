def computer_chooses_move(n, m):
    #the computer always leaves a multiple of (m+1) pieces on the board, and if it can't, it just takes the maximum number of pieces
    if m>=n:
        return n
    else:
        for i in range(n, -1, -1):
            for j in range(1, n):
                if i == j*(m+1):
                    return n-i

def user_chooses_move(n, m):
    while True:
        global global_pieces_taken
        global_pieces_taken = int(input("\nHow many pieces will you take? "))
        if global_pieces_taken<=m and global_pieces_taken<=n and global_pieces_taken>0:
            return global_pieces_taken
        else:
            print("\nOops! Unexpected move. Try again!")

def match():
    print("\nWelcome to NIM game! Choose:")
    game_mode = input("\n1 - Isolated match \n2 - Championship\n")
    if game_mode == '1':
        print("\n You chose an isolated match")
    elif game_mode == '2':
        print("\nYou chose a championship.")
        computer = 0
        user = 0
        counter = 1
    else:
        print("\nUnexpected value. Please, choose from one of the two")
        return False

    while True:
        if game_mode == '2' and counter == 4:
            #checking if the championship is over
            print("\n**** End of the championship! ****")
            print("\nScoreboard: You", user, "X", computer,"Computer")
            break
        elif game_mode == '2':
            #displaying the round number
            print("\n**** Round",counter,"****")
        n = int(input("\nHow many pieces? "))
        m = int(input("Maximum of pieces per move? "))
        if m<1 or n<1:
            print("\nInvalid value. Choose a positive integer for both variables.")
            continue
            
        if n%(m+1) == 0:
            #if n is multiple of (m+1), the user must begin so that the computer wins
            c = 0
            print("\nYou begin!")
            while True:
                c+=1
                if c%2 ==0:
                    if computer_chooses_move(n, m) < 2:
                        print("\nThe computer took one piece.")
                    else:
                        print("\nThe computer took",computer_chooses_move(n, m),"pieces.")
                    n = n - computer_chooses_move(n, m)
                    if n == 0: 
                        if game_mode == '1':
                            #if the game mode is an isolated match, there'll be one round only
                            print("\nEnd of the game. Computer wins!")
                            print("Thank you for playing!")
                            return True
                        elif game_mode == '2':
                            #if the game mode is a championship, it'll go to the next round
                            print("\nEnd of match. Computer wins!")
                            computer+=1
                            counter+=1
                            break
                    elif n < 2:
                        print("Now there is only one piece on the board.") 
                    else:
                        print("Now there are",n,"pieces on the board.")
                    
                else:
                    if user_chooses_move(n, m) < 2:
                        print("\nYou took one piece.")
                    else:
                        print("\nYou took",global_pieces_taken, "pieces.")
                    n = n - global_pieces_taken
                    if n == 0:
                        return "how"
                    elif n < 2:
                        print("Now there is only one piece on the board.")
                    else:
                        print("Now there are",n,"pieces on the board.")
        else:
            #if n isn't multiple of (m+1), the computer must begin so that it wins
            c = 0
            print("\nThe computer begins!")
            while True:
                c+=1
                if c%2 ==0:
                    if user_chooses_move(n, m) < 2:
                        print("\nYou took one piece.")
                    else:
                        print("\nYou took",global_pieces_taken, "pieces.")
                    n = n - global_pieces_taken
                    if n == 0:
                        return "how"
                    elif n < 2:
                        print("Now there is only one piece on the board.")
                    else:
                        print("Now there are",n, "pieces on the board.")

                        
                else:
                    if computer_chooses_move(n, m) < 2:
                        print("\nThe computer took one piece.")
                    else:
                        print("\nThe computer took",computer_chooses_move(n, m),"pieces.")
                    n = n - computer_chooses_move(n, m)
                    if n == 0:
                        if game_mode == '1':
                            print("\nEnd of the game. Computer wins!")
                            print("Thank you for playing!")
                            return True
                        elif game_mode == '2':
                            print("\nEnd of round. Computer wins!")
                            computer+=1
                            counter+=1
                            break
                    elif n < 2:
                        print("Now there is only one piece on the board.")
                    else:
                        print("Now there are",n, "pieces on the board.")
match()