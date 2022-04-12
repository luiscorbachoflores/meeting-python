def area_rectangulo(x,y):
    '''(num,num)-> num
    Devuelve el area de un rectangulo

    >>>area_rectangulo(2,4)
    8

    >>>area_rectangulo(5,10)
    50
    '''
    return x*y

def perimetro_rectangulo(x,y):
    '''(lado,lado)->suma de los lados
    Suma los lados para calcular su perimetro

    >>>perimetro_rectangulo(2,4)
    12

    >>>perimetro_rectangulo(5,10)
    30
    '''
    return 2*(x+y)

def perimetro_triangulo(a,b,c):
    '''(lado,lado,lado)->suma de los lados
    Suma de los lados para calcular su perimetro

    >>>perimetro_triangulo(3,4,5)
    12

    >>>5'''
    return a+b+c

def area_triangulo_rectangulo(x,y):
    '''(base,altura)-> area
    Funcion para calcular el area de un tringulo rectangulo.
    Para calcular el area de un triangulo equilatero,
    vease area_triangulo_equilatero(lado)'''
    return(x*y)/2

def fib(n):
    '''(number)-> number
    El numero introducido es el subindice que indica que numero de la sucesion seleccionar y mostrar.
    #NOTA: el primer numero en la sucesion, 0, es fib(0)

    >>> fib(3)
    2
    >>> fib(12)
    144'''
    if n<=1:
       return n
    else:
        return fib(n-1)+fib(n-2)

def cuadrado(x):
	print ("el cuadrado de", x, "es", x**2)

def a_millas(km):
    '''(km)-> millas
    Convierte la cantidad introducida de km a millas nauticas

    >>> a_millas(1)
    1 km son 0,539957 millas nauticas

    >>> a_millas(221)
    221 km son 119,33 millas nauticas'''
    mi= km*0.539957
    print (km, 'km son', mi, 'millas nauticas')

def a_km(millas):
    '''(millas)-> km
    Convierte la cantidad de millas nauticas a kilometros

    >>> a_km(10)
    10 millas nauticas son 18,52 km

    >>> a_km(20)
    20 millas nauticas son 37,04 km'''
    km=millas*1.852
    print(millas, 'millas nauticas son', km, 'km')

def sin(grados):
    '''(grados)-> seno del angulo
    Calcula el seno de un angulo.

    >>> sin(30)

    >>> sin(60)
    '''
    import math
    radianes=math.radians(grados)
    seno_rad=math.sin(radianes)
    resultado=math.degrees(seno_rad)
    print ('el seno de', grados, 'es', seno_rad)

def a_grados(rad):
    '''(rad)-> grados
    Convierte los radianes en grados.
    Se usa para las razones trigonometricas
    propias del Python, expresadas en radianes.

    >>> a_grados(2)
    2 radianes son 360 grados

    >>> a_grados(4)
    4 radianes son 720 grados'''
    grados=(rad*360)/float(2)
    print(rad, 'radianes son', grados, 'grados')

def a_rad(grados):
    '''(grados)-> radianes
    Convierte los grados a radianes.
    Se usa para las razones trigonometricas
    propias del Python, expresadas en radianes.

    >>> a_rad(360)
    360 grados son 2 radianes

    >>> a_rad(720)
    720 grados son 4 radianes'''
    import decimal
    import math
    rad=grados/float(180)
    print(grados, 'grados son', float(rad), 'radianes')

def area_triangulo_equilatero(lado):
    '''(lado)-> area
    Calcula el area de un triangulo equilatero mediante su lado.
    Para calcular el area de un triangulo rectangulo,
    vease area_triangulo_rectangulo(x,y)

    >>>area_triangulo_equilatero(20)
    la altura vale 17.320508075688775 y el area vale 346.4101615137755'''
    import math
    altura=math.sqrt((lado**2)-((lado/2)**2))
    area=lado*altura
    print('la altura vale', altura, 'y el area vale', area)

def pitagoras():
    '''Calcula de forma rapida las medidas restantes de un triangulo.
    Tambien sirve para calcular diagonales y para trigonometria.

    >>> pitagoras()

    Que quieres calcular?
        Hipotenusa o cateto? hipotenusa
    Distancia de cateto a(solo numeros)3
    Distancia de cateto b(solo numeros)4
    La hipotenusa vale 5.0
    '''
    import math
    if input('''Que quieres calcular?
    Hipotenusa o cateto? ''')=='cateto':
        h=int(input('Distancia de hipotenusa (solo numeros)'))
        c1=int(input('Distancia de cateto a(solo numeros)'))
        c2=math.sqrt(int(h**2)-int(c1**2))
        print('El cateto vale', c2)
    else:
        c1=int(input('Distancia de cateto a(solo numeros)'))
        c2=int(input('Distancia de cateto b(solo numeros)'))
        h=math.sqrt(int(c2**2)+int(c1**2))
        print('La hipotenusa vale', h)

def estado_agua(agua):
    if(type(agua)==int) or (type(agua)==float):
        if 100>=agua>=0:
            print('El agua esta en estado liquido')
        elif agua<0:
            print('El agua esta en estado solido')
        elif agua>100:
            print('El agua esta en estado gaseoso')
        else:
            print('Hay posibilidad de explosion')
    else:
        print('No se puede comprobar el estado del agua')

def cuenta_vocales(s):
        num_vocales=0
        for a in s:#Cada caracter en s (el string anteriormente asignado)
            if a in 'AEIOUaeiouáéíóúÁÉÍÓÚ': #Si el caracter esta en el string AEIOUaeiou
                        print('La',a)
                        num_vocales=num_vocales+1#Se le suma al numero de vocales
        print('Hacen en total',num_vocales, 'vocales de', len(s), 'caracteres')

def factorial(x):
	resultado=1
	while x>1:
		resultado=x*resultado
		x=x-1
		if x==1:
			return resultado
	if x==1:
		return x
	elif x==0:
		return x
	else:
		print('Error')

def factorizar(x):
	for i in range(1,x+1):
		if x%i==0:
			print (i)

def propiedades():
	import math
	if input('¿Se trata de un cuadrado? ')==1:
		lado1=input('Lado del cuadrado ')
		print ('El area del cuadrado es ', lado1*lado1, ' y el perimetro vale ', lado1*4)
	else:
		if input('¿Se trata de un rectángulo? ')==1:
			lado21=input('Lado 1 del rectángulo ')
			lado22=input('Lado 2 del rectángulo ')
			print('El area del rectangulo es ', lado21*lado22, ' y el perimetro vale ', lado22*2+lado21*2)
		else:
			if input('¿Se trata de un triángulo? ')==1:
				lado3=input('Lado del triángulo ')
				altura=input('Altura del triángulo ')
				print('El area del rectangulo es ', lado3*altura/float(2))
			else:
				if input('¿Se trata de un (semi)círculo? ')==1:
					if input('Es un circulo? ')==1:
						radio=input('Introduce el radio del círculo ')
						print('El area del circulo es ', math.pi*radio*radio, ' y el perimetro es ', 2*math.pi*radio)
					else:
						if input('¿Es un semicírculo? ')==1:
							radio=input('Introduce el radio del círculo ')
							print('El area del semicirculo es ', (math.pi*radio*radio)/float(2), ' y el perimetro es ', math.pi*radio)
						else:
							if input('¿Es un sector circular? ')==1:
								print('Aun no está programado el cálculo del sector circular')

				else:
					if input('¿Se trata de un polígono regular? ')==1:
						apotema=input('Apotema del polígono ')
						perimetro=input('Lado del polígono ')*input('Número de lados del polígono ')
						print('El area del poligono es ', apotema*perimetro,' y el perimetro es ', perimetro)
					else:
						print('No se conoce dicha figura')


def sen(grados):
    import math
    return math.sin(math.radians(grados))

def primo(x):
	a=0
	for i in range(1,x+1):
		if x%i==0:
			print i
			a=a+1
	if a==2:
		print (x, ' es primo')
	if a>2:
		print(x, ' no es primo')

def primoshasta(x):
	for n in range(1,x+1,2):
		a=0
		for i in range(1,n+1,2):
			if n%i==0:
				a=a+1
		if a==2:
			print (n, ' es primo')

def ser_noser(x):
    #Consiste en averiguar si el numero introducido es primo o no calculando su nÃºmero de divisores.
	for n in range(1,x+1):
		a=0
		for i in range(1,n+1):
			if n%i==0:
				a=a+1
		if a==2:
			print (n, ' es primo')
		if a>2:
			print(n, ' no es primo')

def fraccequiv(x,y):
    a=x/float(y)
    for i in range(0,1081):
        z=a*i
        if float(z)==int(z):
            print(int(z),int(i))                        

def primo1(x):
	a=0
	for i in range(1,x+1):
		if x%i==0:
			a=a+1
	if a==2:
		return True
	if a>2:
		return False		

def primoshasta1(x):
        j='1,'
        for n in range(1,x+1,2):
            a=0
            for i in range(1,n+1,2):
                if n%i==0:
                    a=a+1
                if a==2:
                    j=str(j)+str(n)+','
        print j
