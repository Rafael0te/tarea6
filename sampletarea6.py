while True:
    print('Seleccione el proceso que desea aplicar')
    print('1:Introducir puntos de evaluación y comentarios')
    print('2:Comprueba los resultados hasta ahora.')
    print('3:Terminar.')
    num = input()
    

    if num.isdecimal():
        num = int(num)

        if num == 1:
            while True:
                print('Por favor, introduzca una puntuación en una escala de 1 a 5')
                point = int(input())
                if 0 < point < 6:
                    print('Introduzca sus comentarios.')
                    comment = input()
                    post = f'punto: {point} comentario: {comment}'
                    file_pc = open("data.txt", 'a')
                    file_pc.write(f'{ post } \n')
                    file_pc.close()
                    break
                else:
                    print('Introduzca los puntos de valoración como números y del 1 al 5')
        elif num == 2:
          print('Resultados hasta la fecha.')
          read_file = open("data.txt", "r")
          print( read_file.read() )
          read_file.close()
        elif num == 3:
          print('Terminación.')
          break  # Sintaxis para terminar un proceso repetitivo.
        else:
            print('Introduzca de 1 a 3')
    else:
        print('Introduzca de 1 a 3')