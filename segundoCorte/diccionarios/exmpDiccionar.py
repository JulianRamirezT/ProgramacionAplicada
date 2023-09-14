#Diccionarios: Se encierran en corchetes, cada elemento tiene una palabra clave y un valor, y están separados por coma.

sensors =  {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22}  #Valor de tipo numérico.
num_cameras = {"backyard": 6,  "garage": 2, "driveway": 1}  #Valor de tipo numérico.

print(sensors)
print(num_cameras)

translations = {"mountain":	"orod", "bread":	"bass", "friend":	"mellon", "horse":	"roch" } #Valor de tipo String.
print(translations)

children = {"von Trapp": ["Johannes", "Rosmarie", "Eleonore"] , "Corleone": ["Sonny", "Fredo", "Michael"] , "20192005117":123456} #Valor de tipo lista y un elemento con valor numerico.
print(children)


#--------------------------------------------------------------------------------------#
my_empty_dictionary = {}  #Se define un diccionario vacio
print(my_empty_dictionary)
my_empty_dictionary["Dinosaurios"] = 0  #Syntax para agregar un elemento al diccionario 
print(my_empty_dictionary)


#---------------------------------------------------------------------------------------#
animals_in_zoo = {"zebras": 8, "monkeys": 12}
animals_in_zoo["dinosaurs"] =  0
print(animals_in_zoo)

menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
print(menu)
menu["cheesecake"] = 8
print(menu)
animals_in_zoo = {"dinosaurs": 0}  #Asigna hacia una estructura de datos, se daña el diccionario anterior 
animals_in_zoo = {"dinosaurs": 0}
print(animals_in_zoo)


#---------------------------------------------------------------------------------------#
user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}
print(user_ids)
user_ids.update({"theLooper": 138475, "stringQueen": 85739}) #Mediante update se agrega un diccionario (ya que esta en corchetes) al diccionario deseado
print(user_ids)

#---------------------------------------------------------------------------------------#
oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}
print(oscar_winners)
oscar_winners.update({"Supporting Actress": "Viola Davis"}) #Se agrega un diccionario
oscar_winners["Best Picture"] = "Moonlight"                 #Se cambia el valor del elemento                            
oscar_winners["Animated Feature"] = "Shrek"                 #Se cambia el valor del elemento 
print(oscar_winners)


#---------------------------------------------------------------------------------------#
#Con listas, generar un diccionario
drinks = ["expresso", "chaí", "decaf", "drip"]
caffeine=[64, 40, 0, 120]
zipped_drinks = zip(drinks,caffeine)
drinks_to_caffeine={key:value for key, value in zipped_drinks}
print(drinks_to_caffeine)

#Se cambian el orden de los argumentos de las listas 
drinks2 = ["expresso", "chaí", "decaf", "drip"]  #Se puede utilizar la misma variable drinks del primer ejemplo
codes=["64", "40", "0", "120"]
zipped_drinks2 = zip(codes,drinks2) #Agrupa listas
code_to_drinks = {key : value for key, value in zipped_drinks2} #Genera el diccionario con las listas agrupadas
print(code_to_drinks)
