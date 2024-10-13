# GUI del usuario
userName = ''
quizLength = 0
nameCapitalized = ''

print('¡Bienvenido(a) a Quizmania!\n')

userName = input('¿Cuál es su nombre?: ')
nameCapitalized = userName.capitalize()

quizLength = int(input(f'¡Hola! {nameCapitalized}! ¿Cuántas preguntas responderá?: '))

# Valida que el quiz esté en rango de 5 y 10 preguntas
while quizLength < 5 or quizLength > 10:
    quizLength = int(input('¡El quiz debe tener entre 5 y 10 preguntas, reintente!: '))

# Listado de preguntas para el quiz
questionList = [
    '¿Qué palabra clave se usa para definir una función en Python?\n a: def \n b: function \n c: define \n d: func',
    '¿Cuál de los siguientes tipos de datos es inmutable en Python?\n a: dictionary \n b: list \n c: set \n d: tuple',
    '¿Qué hace la función len() en Python?\n a: Convierte un número en cadena \n b: Devuelve la longitud de una cadena \n c: Devuelve el último elemento de una lista \n d: Devuelve el tipo de dato de una variable',
    '¿Cuál es el operador de igualdad en Python?\n a: != \n b: = \n c: == \n d: >',
    '¿Qué devuelve la expresión 5 // 2 en Python?\n a: 0 \n b: 2.5 \n c: 3 \n d: 2',
    '¿Cómo se comenta una sola línea en Python?\n a: # Comentario \n b: // Comentario \n c: /* Comentario */ \n d: <!- Comentario -->',
    '¿Qué estructura se utiliza para repetir un bloque de código un número específico de veces en Python?\n a: for \n b: while \n c: repeat \n d: loop',
    '¿Cuál de los siguientes no es un tipo de dato primitivo en Python?\n a: str \n b: int \n c: object \n d: float',
    '¿Qué función convierte una cadena en un entero en Python?\n a: float() \n b: int() \n c: str() \n d: convert() ',
    '¿Qué palabra clave se usa para crear una clase en Python?\n a: new \n b: create \n c: function \n d: class'
]

# Listado de respuestas correctas
correctAnswers = [
    'a', 'd', 'b', 'c', 'd', 
    'a', 'a', 'c', 'b', 'd'
]

# Listado de justificaciones
justifications = [
    'Justificación: La palabra clave "def" se usa para definir funciones en Python.',
    'Justificación: Los datos de tipo "tuple" son inmutables, significa que no cambian luego de ser creados.',
    'Justificación: La función "len()" devuelve la cantidad de elementos en una secuencia.',
    'Justificación: El operador "==" se usa para comparar si dos valores son iguales.',
    'Justificación: El operador "//" se usa para devolver la parte entera del cociente.',
    'Justificación: En Python, los comentarios de una línea empiezan con "#".',
    'Justificación: La estructura "for()" se usa para iterar una secuencia un número dado de veces.',
    'Justificación: El tipo de dato "object" no es primitivo en Python.',
    'Justificación: La función "int()" se usa para convertir valores a entero.',
    'Justificación: La palabra clave "class" se utiliza para definir clases en Python.',
]

# Aquí se genera la interfaz del quiz
print('\nPreguntas básicas sobre Python. ¡Empecemos!\n')

correctCount = 0
userAnswers = []  # Lista para almacenar las respuestas del usuario

for i in range(quizLength):
    print(f'Pregunta #{i + 1}: {questionList[i]}')
    answer = input('Respuesta: ').lower()

    # Guardamos la respuesta del usuario
    userAnswers.append(answer)

    if answer == correctAnswers[i]:
        print('¡Correcto!\n')
        correctCount += 1
    else:
        print(f'¡Incorrecto!\n{justifications[i]}\n')
    
    # Calculamos y mostramos el progreso basado en la cantidad de preguntas respondidas
    progreso = ((i + 1) / quizLength) * 100  # Incremento de progreso basado en las preguntas respondidas
    print(f'Progreso: {progreso:.2f}% completado.\n')

# Mostramos el resumen final
print(f'Has respondido correctamente {correctCount} de {quizLength} preguntas.')
scorePercentage = (correctCount / quizLength) * 100
print(f'Tu puntuación final es {scorePercentage:.2f}%.\n')

# Mostramos las respuestas dadas por el usuario
print(f'Aquí están tus respuestas, {nameCapitalized}:')
for i in range(quizLength):
    print(f'Pregunta #{i + 1}: {userAnswers[i]}')

print(f'\nGracias por participar, {nameCapitalized}!')
