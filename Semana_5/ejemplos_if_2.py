def mensaje_negativo(numero):
    """
    (float) -> str

    Escribe un mensaje para evaluar un numero negativo

    >>> mensaje_negativo(-10.0)
    'El numero es negativo'

    >>> mensaje_negativo(898)
    'El numero es positivo'

    :param numero: num el numero a evaluar
    :return: str con el mensaje de la evaluación
    """
    if numero < 0:
        return 'El numero es negativo'
    return 'El numero es positivo'

def compara_edades(edad1, edad2):
    """
    (int, int) -> str

    Genera un mensaje segun la diferencia de edad:
    la primera o la segunda mas joven o iguales

    >>> compara_edades(10, 20)
    'El primero es mas joven'

    >>> compara_edades(89, 56)
    'El segundo es mas joven'

    >>> compara_edades(56, 56)
    'Tienen la misma edad'

    :param edad1: int la edad del primero
    :param edad2: int la edad del segundo
    :return: mensaje asociado a la diferencia de edad
    """
    if edad1 > edad2:
        return 'El segundo es mas joven'
    elif edad1 == edad2:
        return 'Tienen la misma edad'
    else:
        return 'El primero es mas joven'


def es_parentesis(caracter):
    """

    (str of len == 1) -> str

    >>> es_parentesis('(')
    'Es parentesis'
    >>> es_parentesis('x')
    'No es parentesis'
    >>> es_parentesis('xa')
    Traceback (most recent call last):
    ..
    TypeError: xa no es un parentesis

    :param caracter: str el caracter a evaluar
    :return: str el mensaje de la validacion
    """
    if len(caracter) != 1:
        raise TypeError(str(caracter) + ' no es un parentesis')
    elif caracter in '()': # caracter == '(' or caracter == ')':
        return 'Es parentesis'
    return 'No es parentesis'


def dividir(dividendo, divisor):
    '''

    (num, num) -> num

    Divide un numero entre otro

    >>> dividir(6, 2)
    3.0
    >>> dividir(1,0)
    Traceback (most recent call last):
    ..
    ZeroDivisionError: No dividiras por 0
    >>> dividir('hola', 100)
    Traceback (most recent call last):
    ..
    TypeError: hola no es un numero

    :param dividendo: num el dividendo a evaluar
    :param divisor: num el divisor a evaluar
    :return: la división entre dividendo y divisor
    '''
    if  int != type(dividendo) != float:
        raise TypeError(str(dividendo) + ' no es un numero')
    elif int != type(divisor) != float:
        raise TypeError(str(divisor) + ' no es un numero')
    elif divisor == 0:
        print('al pelo')
        raise ZeroDivisionError('No dividiras por 0')
    return dividendo / divisor

def par_impar(num):
    """
    num -> str

    Entra un numero y sale si es par o impar

    :param num: numero a ser revisado
    :return: mensaje dejando saber si es par o no

    >>> par_impar(6)
    'Es par'
    >>> par_impar(7)
    'Es impar'
    >>> par_impar('d')
    Traceback (most recent call last):
    ..
    TypeError: No es valido

    """
    if str == type(num):
        raise TypeError('No es valido')
    elif num % 2 != 0:
        return 'Es impar'
    else:
        return 'Es par'

def mitad_doble(num1,num2):
    """

    Entra un numero y se revisa si el primero es el doble del segundo

    Num -> Str

    :param num1: Numero a ser operado
    :param num2: Numero a ser revisado
    :return: Mensaje si uno es el doble del otro

    >>> mitad_doble(7,14)
    'Si es el doble de un impar'
    >>> mitad_doble(7,15)
    'No es el doble de un impar'

    """

    if num1 % 2 != 0 and num1*2 == num2:
        return 'Si es el doble de un impar'
    else:
        return 'No es el doble de un impar'

def cuadrado_primero(num1,num2):
    """

    Entran dos numeros para verificar si es el cuadrado del primero, si es mayor o menos que la misma operacion

    num -> string

    :param num1: Primer numero
    :param num2: Segundo numero
    :return: Mensaje se verificacion

    >>> cuadrado_primero(2,4)
    'Segundo cuadrado del primero'
    >>> cuadrado_primero(2,3)
    'Segundo es menor al cuadrado del primero'
    >>> cuadrado_primero(2,5)
    'Segundo es mayor al cuadrado del primero'

    """

    if num1**2 == num2:
        return 'Segundo cuadrado del primero'
    elif num1**2 > num2:
        return 'Segundo es menor al cuadrado del primero'
    elif num1**2 < num2:
        return 'Segundo es mayor al cuadrado del primero'

def es_primo(num):
    """

    Determina, a partir de un numero dado, si es primo o no

    :param num: Numero de entrada
    :return: Es primo o no

    >>> es_primo(8)
    'No es primo'
    >>> es_primo(3)
    'Es primo'
    >>> es_primo(1)
    Traceback (most recent call last):
    ..
    TypeError: No es valido

    """

    if num < 2:
        raise TypeError('No es valido')
    elif num == 2:
        return 'Es primo'
    elif num >= 2 and num%num == 0 and num%1 == 0 and num%2 != 0:
        return 'Es primo'
    else:
        return 'No es primo'

def billetes_verdes(cant):
    """

    Str -> num
    :param cant: valor de una cantidad en euros
    :return: los billetes

    >>> billetes_verdes('434')
    '2 billetes de 200 1 billete de 20 euros 1 billete de 10 euros 2 monedas de 2 euros'

    """

    billetes_200 = int(cant) // 200
    new_1 = int(cant) % 200
    billetes_20 = new_1 // 20
    new_2 = new_1 % 20
    billetes_10 = new_2 // 10
    new_3 = new_2 % 10
    monedas_2 = new_3 // 2
    new_4 = new_3 % 2

    mensaje = ''

    if (billetes_200):
        mensaje += str(billetes_200) + ' billetes de 200 '

    if (billetes_20):
        mensaje += str(billetes_20) + ' billete de 20 euros '

    if (billetes_10):
        mensaje += str(billetes_10) + ' billete de 10 euros '

    if (monedas_2):
        mensaje += str(monedas_2) + ' monedas de 2 euros'

    return ('%s' % mensaje.rstrip('\n'))