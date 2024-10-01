# GUI del usuario
print('¡Bienvenido(a) a Quizmania!')
userName = str(input('¿Cuál es su nombre?\n'))
quizLength = int(input(userName + ' ¿Cuántas preguntas responderá?\n'))

# valida que el quiz no supere las 15 preguntas
while quizLength > 15:
    quizLength = int(input('¡El quiz no debe exceder las 15 preguntas, reintente!: '))

# listado de preguntas para el quiz
for i in range(1, quizLength + 1):
    print('Pregunta #' + str(i))
    # TODO agregar las preguntas que están en el archivo questions.txt; ahí mismo están las respuestas y justificación
