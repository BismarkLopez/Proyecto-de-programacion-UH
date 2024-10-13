# GUI del usuario
userName = ''
quizLength = 0
nameCapitalized = ''

print('¡Bienvenido(a) a Quizmania!\n')

userName = input('¿Cuál es su nombre?: ')
nameCapitalized = userName.capitalize()

quizLength = int(input(f'¡Hola! {nameCapitalized}! ¿Cuántas preguntas responderá?: '))

# Valida que el quiz esté en rango de 5 y 15 preguntas
while quizLength < 5 or quizLength > 15:
    quizLength = int(input('¡El quiz debe tener entre 5 y 15 preguntas, reintente!: '))

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
    '¿Qué palabra clave se usa para crear una clase en Python?\n a: new \n b: create \n c: function \n d: class',
    '¿Qué estructura se usa para manejar excepciones en Python?\n a: switch-case \n b: if-else \n c: try-except \n d: catch-finally',
    '¿Qué devuelve type(42) en Python?\n a: integer \n b: int \n c: <class "int">\n d: number',
    '¿Qué método se usa para agregar un elemento al final de una lista en Python?\n a: add() \n b: append() \n c: insert() \n d: push()',
    '¿Cuál de las siguientes es una biblioteca popular para el manejo de datos en Python?\n a: matplotlib \n b: numpy \n c: scikit-learn \n d: pandas',
    '¿Cuál es la función principal de la declaración import en Python?\n a: Asignar valores a una variable \n b: Crear una nueva variable \n c: Definir una función \n d: Incluir módulos externos en el código'
]

# Listado de respuestas correctas
correctAnswers = [
    'a', 'd', 'b', 'c', 'd', 
    'a', 'a', 'c', 'b', 'd', 
    'c', 'c', 'b', 'd', 'd'
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
    'Justificación: La estructura "try-except" se utiliza para manejar errores y excepciones.',
    'Justificación: La expresión "type(42)" devuelve <class "int"> porque 42 es un entero.',
    'Justificación: El método "append()" agrega un elemento al final de una lista.',
    'Justificación: Pandas es una biblioteca utilizada para analizar y manipular datos.',
    'Justificación: La función "import" se usa para módulos o bibliotecas externas en el código.'
]

# Aquí se genera la interfaz del quiz
print('\nPreguntas básicas sobre Python. ¡Empecemos!\n')

correctCount = 0

for i in range(quizLength):
    print(f'Pregunta #{i + 1}: {questionList[i]}')
    
    answer = input('Respuesta (a/b/c/d): ').lower()
    
    if answer == correctAnswers[i]:
        print('¡Correcto!\n')
        correctCount += 1
    else:
        print(f'Incorrecto. {justifications[i]}\n')

# Calculamos y mostrar el progreso
scorePercentage = (correctCount / quizLength) * 100

print(f'Has respondido correctamente {correctCount} de {quizLength} preguntas.')
print(f'Tu puntuación es {scorePercentage:.2f}%.')
print(f'\nGracias por participar, {nameCapitalized}!')
