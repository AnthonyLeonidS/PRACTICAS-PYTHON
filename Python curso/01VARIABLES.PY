#VARIABLES
myVariable="My string variable"#CAMEL CASE ()
print(myVariable)
#Seria mas correcto ecribirlo asi:
    
my_variable="my string variable"#por convención es mejor usar barrabaja para escribir una variable 
print(my_variable)
#"HAY un MONTÓN DE VARIABLES que iremos viendo poco a poco

my_int_variable=45
print(my_int_variable)
my_bool_variable=False
print(my_bool_variable)
print(type(print(type(my_int_to_str_variable))))  # tipo NoneTypemy_int_variable=45
print(my_int_variable)
my_bool_variable=False
print(my_bool_variable)
print(type(print(type(my_int_to_str_variable))))  # tipo NoneType

my_int_to_str_variable = my_variable
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

#CONCATENACION DE VARIABLES EN EL PRINT
print(myVariable,my_bool_variable)
print("este es el valor de:",my_bool_variable)




#Algunas Funciones del sistema( basicamente cuenta incluido los espacios )
print(len(my_int_to_str_variable))

#Variables en una sola linea(¡cuidado con abusar de ésta sintaxis!)
name,surname, alias, age= "Anthony","Martinez","Giggo,",35  
print("Me llamo",name,surname,"mi alias es:",alias,"de edad",age)

#Función Input
"""""
name=input("¿Cual es tu nombre?")
age=input("¿Cómo te llamas?")
print(name)
print(age)

"""""
#cambiamos su tipo
name=35 
age="Anthony"
print(name)
print(age)

#Forzamos su tipo
address:str="Mi dirección"
address=32
print(address)
