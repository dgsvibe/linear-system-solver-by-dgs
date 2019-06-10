import numpy
import os
def clear_screen():
    print("\n" * os.get_terminal_size().lines)
    print("\x1b[2J\x1b[1;1H")
def drawing_matrix(matrix_order):
    var_to_range=matrix_order+1
    for i in range(var_to_range): #matrix lines iteration
        for j in range(var_to_range): #matrix columns iteration
            if j == 0:
                print("|a"+str(i+1)+str(j+1)+"   ")
                print("")
            if j == var_to_range:
                print("|")
def header():
    print("\033[1;91m           .: Developed by D. Viana :.")
    print("\033[0;93m")
    print("              Line@r System Solv&r")
    print("        :: For science and engineering ::")
    print("\033[1;92m")
    print("                       ____")
    print("                    _.' :  `.\\")
    print("                .-.'`.  ;   .'`.-.")
    print("       __      / : ___\\ ;  /___ ; \\      __")
    print("     ,'_ ""--.:__;''.-.'';: :''.-.'':__;.--'' _`,")
    print("     :' `.t""--.. '&lt;@.`;_  ',@&gt;` ..--""j.' `;")
    print("          `:-.._J '-.-'L__ `-- ' L_..-;'")
    print("            ''-.__ ;  .-''  ''-.  : __.-"'')
    print("                L ' /.------.\\ ' J")
    print("                 ''-.   ''--''   .-''         Please, Dude, send nudes")
    print("                __.l'-:_JL_;-'';.__           Or press '1' to continue...")
    print("             .-j/'.;  ;''''  / .'\\''-." )
    print("           .' /:`. ''-.:     .-'' .';  `.")
    print("        .-''  / ;  ''-. ''-..-'' .-''  :  ''-.")
    print("     .+''-.  : :      ''-.__.-''      ;-._   \\")
    """    print("     ; \\  `.; ;                      : : ''+. ;")
    print("     :  ;   ; ;                       : ;  : \\:")
    print("     ;  :   ; :                        ;:   ;  :")
    print("    : \\  ;  :  ;                     : ;  /  ::")
    print("    ;  ; :   ; :                      ;   :   ;:")
    print("    :  :  ;  :  ;                    : :  ;  : ;")
    print("    ;\\    :   ; :                   ; ;     ; ;")
    print("    : `.''-;   :  ;                 :  ;    /  ;")
    print("     ;    -:   ; :                 ;  : .-''   :")
    print("     :\\     \\  :  ;               : \\.-''    :")
    print("      ;`.    \\  ; :                 ;.'_..--  / ;")
    print("      :  ''-.  ''-:  ;         :/.''       .'  :")
    print("       \\         \\ :          ;/  __         :")
    print("        \\       .-`.\\       /t-''  '':-+.   :")
    print("         `.  .-'''    `l  __/ /`. :  ; ; \\  ;")
    print("           \\   .-'' .-''-.-''  .' .''j \/;/")
    print("            \\ / .-''   /.     .'.' ;_:' ;")
    print("             :-""-.`./-.'     /    `.___.'")
    print("                   \\ `t  ._  /")
    print("                    ''-.t-._:'")
    """

    confirmation = int(input())
    if confirmation == 1:
        clear_screen()
    else:
        print("Bye!")
        return 0

def calc():
    print("	\033[1;93m")
    matrix_order = int(input("Type the coefficients matrix order: "))
    q = matrix_order
    for (i) in range(q):
        for (j) in range(q):
            c_matrix = [].append(int(input("Insert the element A"+str(i+1)+str(j+1)+":")))
    print(c_matrix)
    return 0

calc()


#coefficients_matrix = numpy.array([[-1,1],[1,1]])
#scalars_matrix = numpy.array([4,5])

#result = numpy.linalg.solve(coefficients_matrix, scalars_matrix)
#print(result)
