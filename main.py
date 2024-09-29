#GUI del usuario
print('¡Bienvenido(a) a Quizmania!')
userName = input('¿Cuál es su nombre?\n')
quizLength = int(input(userName + ' ¿Cuántas preguntas responderá?\n')) #agregar una función que permita convertir la primera letra en mayuscula

#condición que valida que quizLength no supere las 15 preguntas
while True:
    quizLength = int(input('El quiz no debe superar las 15 preguntas, reintente: '))
    if quizLength <= 15:
        break

#listado de preguntas para el quiz