# Projecte password  

print("Les condicions que ha de complir la contraseny són")  
# Imprimim els condicions que ha de complir el usuari quan introduïen el password. 

print("-Posició 1: Un numero major o igual 1 i menor o igual que 5 (1-5).") 
# Imprimim els condicions que ha de complir el usuari quan introduïen el password.  

print("-Posició 2: Una lletra minúscula (a-z). ")  
# Imprimim els condicions que ha de complir el usuari quan introduïen el password. 

print("-Posició 3: Una lletra majúscula (A-Z). ") 
# Imprimim els condicions que ha de complir el usuari quan introduïen el password.

print("-Posició 4: Un dels següents símbols *, _, @. ")  
# Imprimim els condicions que ha de complir el usuari quan introduïen el password.

print("-Posició 5: Una lletra minúscula (a-z). ")  
# Imprimim els condicions que ha de complir el usuari quan introduïen el password.

print("-Posició 6: Un número major o igual 6 i menor o igual que 9 (6-9). ")  
# Imprimim els condicions que ha de complir el usuari quan introduïen el password.

print("-Posició 7: Un dels següents símbols &, /, #. ")  
# Imprimim els condicions que ha de complir el usuari quan introduïen el password.

print("-Posició 8: Un numero menor o igual que 5 (0-5). ") 
# Imprimim els condicions que ha de complir el usuari quan introduïen el password. 

password=input("Introdueix el teu password: ")  
# Demanar el variable/contrasenya al usuari per verificar si es compleixen els condicions indicats.

longitud=len(password)  
# Per saber el longitud que te el password introduït per usuari 

errors=[]  
# Posem el error es igual a " ", perque si el usuari ha introduït un contrasenya erronea podem corregir-lo o tambe verificar si la contrasenya introducida es correcte.

if longitud < 6 or longitud > 8:  
# Verificació de longitud, perque si el contraseya que ha introduit el usuari es concideix amb els condicions indicats pasara a "else". Sino, el contrasenya no te el longitud indicat i acabara el programa.

    print(f"Error, el password té una longitud de {longitud} caràcters i no compleix els requisits")  
    # El contrasenya introducida per usuari no consideix amb el longitud indicat del condicio per tant aqui acaba el programa.

else: 
# El longitud de la contrasenya que ha introduit son esperats i pasara al correcio del contrasenya.

# Comprovació per cada posició del contrasenya 

    if not (password[0].isdigit() and 1<=int(password[0])<=5): 
    # Verificar si el caracter 1 de la contrasenya es un numero i que este numero sea major o igual 1 i menor o igual que 5.

        errors.append(f" Error en el caràcter 1, no es {password[0]} ha de ser un numero major o igual 1 i menor o igual que 5 (1-5)")  
        # No cumple con el condicion. Guardar el error que aparece en la cantrasenya para mostrar-lo despres i continuar el programa.

    if not (password[1].islower()):  
    # Verificar si el caracter 2 de la contrasenya es una lletra minúscula (a-z).

        errors.append(f" Error en el caràcter 2, no es {password[1]} ha de ser una lletra minúscula (a-z)")  
        # No cumple con el condicion. Guardar el error que aparece en la cantrasenya para mostrar-lo despres i continuar el programa

    if not (password[2].isupper()):  
    # Verificar si el caracter 3 de la contrasenya es una lletra majúscula (A-Z).

        errors.append(f" Error en el caràcter 3, no es {password[2]} ha de ser una lletra majúscula (A-Z)")  
        # No cumple con el condicion. Guardar el error que aparece en la cantrasenya para mostrar-lo despres i continuar el programa

    if password[3] not in ["*", "_", "@"]:  
    # Verificar si el caracter 4 de la contrasenya es un dels següents símbols *, _, @

        errors.append(f" Error en el caràcter 4, no es {password[3]} ha de ser un dels següents símbols *, _, @")  
        # No cumple con el condicion. Guardar el error que aparece en la cantrasenya para mostrar-lo despres i continuar el programa

    if not (password[4].islower()):  
    # Verificar si el caracter 5 de la contrasenya es una lletra minúscula (a-z)

        errors.append(f" Error en el caràcter 5, no es {password[4]} ha de ser una lletra minúscula (a-z)")  
        # No cumple con el condicion. Guardar el error que aparece en la cantrasenya para mostrar-lo despres i continuar el programa

    if not (password[5].isdigit() and 6 <= int(password[5]) <= 9):  
    # Verificar si el caracter 6 de la contrasenya es un número major o igual 6 i menor o igual que 9 (6-9)

        errors.append(f" Error en el caràcter 6, no es {password[5]} ha de ser un número major o igual 6 i menor o igual que 9 (6-9)")  
        # No cumple con el condicion. Guardar el error que aparece en la cantrasenya para mostrar-lo despres i continuar el programa

    if longitud == 7 and password[6] not in ["&", "/", "#"]:  
    # Verificar si el caracter 7 de la contrasenya es un dels següents símbols &, /, #

        errors.append(f" Error en el caràcter 7, no es {password[6]} ha de ser un dels següents símbols &, /, #")  
        # No cumple con el condicion. Guardar el error que aparece en la cantrasenya para mostrar-lo despres i continuar el programa

    if longitud == 8 and not (password[7].isdigit() and 0 <= int(password[7]) <= 5):  
    # Verificar si el caracter 8 de la contrasenya es un numero i que este numero sea menor o igual que 5 (0-5)

        errors.append(f" Error en el caràcter 8, no es {password[7]} ha de ser un numero menor o igual que 5 (0-5)")  
        # No cumple con el condicion. Guardar el error que aparece en la cantrasenya para mostrar-lo despres i continuar el programa

    if len(errors) == 0:  
    # Conprovació de longitud que te el variable "error" si no hi ha ningú error guardado llavors el longitud es 0. 

        print("El format del PASSWORD és correcte")  
        # Si no hi ha ningú error imprimim que el password es correcte 

    else:  
    # El variable "error" no tenen un longitud de 0. Aixo significa que hi ha errors que ha guardat en el variable.

        print("".join(errors))  
        # Imprimim amb "join(errors) perquè així pot unir tots els errors que hem trobat en el password que ha introduït el usuari i mostrar-ho junts.