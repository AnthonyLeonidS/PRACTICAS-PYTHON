###STRINGS###


#FORMATEO DE STRINGS
name,surname,age= "Anthony","Martinez",25
print("Mi nombre es %s y mi edad es %d".format(name, surname, age))#PARA FORMATEAR DATOS
print("Mi nombre es %s y mi edad es %s".format(name, surname, age))#PARA FORMATEAR DATOS 
print("Mi nombre es {} {} y mi edad es {}".format(name,surname,age))#LA FORMA ADECUADA

name,surname,age="Antonio","Martinez",54
print("Mi nombre es {} {} y mi edad es {}".format(name,surname,age) )

# INFERENCIA DE DATOS(METIENDO LOS DATOS DENTRO )
name, surname, age = " Anthony", "Martinez", 25
print("Mi nombre es {name} {surname} y mi edad es {age}")

# No sirve porque le falta un caracter especial (f)


"PRIMERO CREAMOS LA VARIABLE (language) "

language = "Games"

a, b, c, d, e = language# aqui tenemos que añadir tantas variables como caracteres tenga a lo que se quiere igualar
print(a)
print(b)

# DIVISION
"Creamos variable"
language_slice = language[0:5]  # el uso de[n:n] nos indica de donde a donde va
print(language_slice)
language_slice = language[1:3]
print(language_slice)
