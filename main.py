# GUI del usuario
userName = ''
quizLength = 0
nameCapitalized = ''
print('¡Bienvenido(a) a Quizmania!\n')
userName = input('¿Cuál es su nombre?: ')
nameCapitalized = userName.capitalize()
quizLength = int(input(f'¡Hola! {nameCapitalized} ¿cuántas preguntas responderá?: '))
# TODO aprender a usar el f-string para dar formatos a concatenaciones
#quizLength = int(input('¡Hola! ' + nameCapitalized + ' ¿Cuántas preguntas responderá?: '))

# valida que el quiz esté en rango de 1 y 15 preguntas
while quizLength < 1 or quizLength > 15:
    quizLength = int(input('¡El quiz debe tener entre 1 y 15 preguntas, reintente!: '))

# listado de preguntas para el quiz
questionList = [
    '¿Qué palabra clave se usa para definir una función en Python?\n a: def \n b: function \n c: define \n d: func',
    '¿Cuál de los siguientes tipos de datos es inmutable en Python?\n a: dictionary \n b: list \n c: set \n d: tuple',
    '¿Qué hace la función len() en Python?\n a:\n b:\n c:\n d:',
    '¿Cuál es el operador de igualdad en Python?\n a:\n b:\n c:\n d:',
    '¿Qué devuelve la expresión 5 // 2 en Python?\n a:\n b:\n c:\n d:',
    '¿Cómo se comenta una sola línea en Python?\n a:\n b:\n c:\n d:',
    '¿Qué estructura se utiliza para repetir un bloque de código un número específico de veces en Python?\n a:\n b:\n c:\n d:',
    '¿Cuál de los siguientes no es un tipo de dato primitivo en Python?\n a:\n b:\n c:\n d:',
    '¿Qué función convierte una cadena en un entero en Python?\n a:\n b:\n c:\n d:',
    '¿Qué palabra clave se usa para crear una clase en Python?\n a:\n b:\n c:\n d:',
    '¿Qué estructura se usa para manejar excepciones en Python?\n a:\n b:\n c:\n d:',
    '¿Qué devuelve type(42) en Python?\n a:\n b:\n c:\n d:',
    '¿Qué método se usa para agregar un elemento al final de una lista en Python?\n a:\n b:\n c:\n d:',
    '¿Cuál de las siguientes es una biblioteca popular para el manejo de datos en Python?\n a:\n b:\n c:\n d:',
    '¿Cuál es la función principal de la declaración import en Python?\n a:\n b:\n c:\n d:'
]

# listado de respuestas correctas
correctAnswers = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '']

# listado de justificaciones
justifications = [
    'Justificación: La palabra clave "def" se usa para definir funciones en Python.',
    'Justificación: Los datos de tipo "tuple" son inmutables, significa que no cambian luego de ser creados.',
    'Justificación: La función "len()" devuelve la cantidad de elementos en una secuencia.',
    'Justificación: El operador "==" se usa para comparar si dos valores son iguales.',
    'Justificación: El operador "//" se usa para devolver la parte entera del cociente.',
    'Justificación: En Python los cometarios de una línea empiezan con "#".',
    'Justificación: La estructura "for()" se usa para iterar una secuencia un número dado de veces.',
    'Justificación: El tipo de dato "object" no es primitivo en Python.',
    'Justificación: La función "int()" se usa para convertir valores a entero.',
    'Justificación: La palabra clave "class" se utiliza para definir clases en Python.',
    'Justificación: La estructura "try-except" se utiliza para manejar errores y excepciones.',
    'Justificación: La expresión "type(42)" devuelve <class "int"> porque 42 es un entero.',
    'Justificación: El método "append()" agrega un elemento al final de una lista.',
    'Justificación: Pandas es una biblioteca utilizada para analizar y manipular datos.',
    'Justificación: La función "import" se usa para modulos o bibliotecas externas en el código de Python.'
]

# aquí se genera la interfaz del quiz
print('\nPreguntas básicas sobre Python ¡empecemos!\n')

for i in range(quizLength):
    print(f'Pregunta #{i+1}: {questionList[i]}')
    answer = ''
    answer = input('Respuesta: ')
    print('')
