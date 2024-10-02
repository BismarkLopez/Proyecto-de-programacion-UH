# GUI del usuario
userName = ''
quizLength = 0
nameCapitalized = ''
print('¡Bienvenido(a) a Quizmania!\n')
userName = str(input('¿Cuál es su nombre?: '))
nameCapitalized = userName.capitalize()
quizLength = int(input(nameCapitalized + ' ¿Cuántas preguntas responderá? '))

# valida que el quiz esté en rango de 1 y 15 preguntas
while quizLength < 1 or quizLength > 15:
    quizLength = int(input('¡El quiz debe tener entre 1 y 15 preguntas, reintente!: '))

# listado de preguntas para el quiz
# TODO agregar las preguntas que están en el archivo questions.txt; ahí mismo están las respuestas y justificación
questionList = [
    '¿Qué palabra clave se usa para definir una función en Python?\n a: def \n b: function \n c: define \n d: func',
    '¿Cuál de los siguientes tipos de datos es inmutable en Python?\n a: \n b: \n c: \n d: ',
    '¿Qué hace la función len() en Python?\n a: \n b: \n c: \n d: ',
    '¿Cuál es el operador de igualdad en Python?\n a: \n b: \n c: \n d: ',
    '¿Qué devuelve la expresión 5 // 2 en Python?\n a: \n b: \n c: \n d: ',
    '¿Cómo se comenta una sola línea en Python?\n a: \n b: \n c: \n d: ',
    '¿Qué estructura se utiliza para repetir un bloque de código un número específico de veces en Python?\n a: \n b: \n c: \n d: ',
    '¿Cuál de los siguientes no es un tipo de dato primitivo en Python?\n a: \n b: \n c: \n d: ',
    '¿Qué función convierte una cadena en un entero en Python?\n a: \n b: \n c: \n d: ',
    '¿Qué palabra clave se usa para crear una clase en Python?\n a: \n b: \n c: \n d: ',
    '¿Qué estructura se usa para manejar excepciones en Python?\n a: \n b: \n c: \n d: ',
    '¿Qué devuelve type(42) en Python?\n a: \n b: \n c: \n d: ',
    '¿Qué método se usa para agregar un elemento al final de una lista en Python?\n a: \n b: \n c: \n d: ',
    '¿Cuál de las siguientes es una biblioteca popular para el manejo de datos en Python?\n a: \n b: \n c: \n d: ',
    '¿Cuál es la función principal de la declaración import en Python?\n a: \n b: \n c: \n d: '
]

# aquí se genera la interfaz del quiz
print('Preguntas básicas sobre Python ¡empecemos!\n')

for i in range(quizLength):
    print(f'Pregunta #{i+1}: {questionList[i]}')
    answer = ''
    answer = str(input('Respuesta: '))
    print('')
