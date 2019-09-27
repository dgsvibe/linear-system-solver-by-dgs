import numpy
import os

cm=''
im=''
result=''
matrix_order=''

def clear_screen():
    print("\n" * os.get_terminal_size().lines)
    print("\x1b[2J\x1b[1;1H")

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
    confirmation = int(input())
    if confirmation == 1:
        clear_screen()
    else:
        print("Bye!")
        return 0

def catch_data():
    global cm #retoma a propriedade de global da variavel da matriz dos coeficientes cm
    global im #análogo, para a matriz de entrada im
    global matrix_order #análogo, para a variavel que guarda a ordem da matriz
    print("	\033[1;93m")
    c_matrix_order = int(input("Type the coefficients matrix order (2/3): "))
    if c_matrix_order == 2:
        matrix_order = 2
        cm = [[0, 0],[0, 0]]
        im = [0, 0]
        for i in range(2):
            for j in range(2):
                cm[i][j] = complex(input('Insira o elemento C'+str(i+1)+str(j+1)+': '))
        clear_screen()
        for i in range(2):
            im[i] = complex(input('Insira o elemento I'+str(i+1)+': '))
    if c_matrix_order == 3:
        matrix_order = 3
        cm = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
        im = [0, 0, 0]
        for i in range(3):
            for j in range(3):
                cm[i][j] = complex(input('Insira o elemento A'+str(i+1)+str(j+1)+': '))
        clear_screen()
        for i in range(3):
            im[i] = complex(input('Insira o elemento I'+str(i+1)+': '))
    clear_screen()
def calc():
    catch_data()
    global cm
    global im
    global result
    coefficients_matrix = numpy.array(cm)
    scalars_matrix = numpy.array(im)
    result = numpy.linalg.solve(coefficients_matrix, scalars_matrix)
    return result

header()
res = calc()
print(res,end='\n\n\n')
