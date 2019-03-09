def tic_tac_toe():
    choices = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    end = False
    combinations = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

    def function():
        print([choices[0], choices[1], choices[2]])
        print([choices[3], choices[4], choices[5]])
        print([choices[6], choices[7], choices[8]])

    def func1():
        n = choose_no()
        if choices[n+1] ==1 or choices[n+1] ==2:
            print("\nYou can't go there. Try again\n")
            func1()
        else:
            choices[n+1] = 1

    def func2():
        n = choose_no()
        if choices[n+1] ==1 or choices[n+1] ==2:
            print("\nYou can't go there. Try again\n")
            func2()
        else:
            choices[n+1] = 2

    def choose_no():
        while True:
            while True:
                a = input()
                try:
                    a  = int(a)
                    a -= 1
                    if a in range(-1,8):
                        return a
                    else:
                        print("\nYou chose something else from 0-8. Try again\n")
                        continue
                except ValueError:
                   continue

    def check_choices():
        value = 0
        for a in combinations:
            if choices[a[0]] == choices[a[1]] == choices[a[2]] ==1:
                print("player one, Wins\n")
                return True

            if choices[a[0]] == choices[a[1]] == choices[a[2]] ==2:
                print("player two, Wins\n")
                return True
        for a in range(-1,8):
            if choices[a] ==1 or choices[a] == 2:
                value += 1
            if value == 9:
                print("The Game end in a DRAW\n")
                return True

    while not end:
        function()
        end = check_choices()
        if end == True:
            break
        print("\nplayer one choose where to place 1  \n")
        func1()
        function()
        end = check_choices()
        if end == True:
            break
        print("\nplayer two choose where to place 2 \n")
        func2()

   
print('Game Format and Intial Format of Tic-Tac-Toe \n')
list1 = [0,1,2]
list2 = [3,4,5]
list3 = [6,7,8]
print(list1)
print(list2)
print(list3)
print("\n")
print(tic_tac_toe())