students = {}
def add_student(): #Función para añadir estudiantes
    while True:
        try:
            id_student = str(input("Ingrese el ID del estudiante: ")) #Variable que guarda el ID del estudiante
            if not id_student.strip(): #Condicional por si no hay ningun valor en la variable id_student
                raise ValueError("Error. No se puede dejar el campo vacio")
            if id_student in students: #Condicional por si eel ID ya tiene un estudiante asignado
                print("Este ID ya lo tiene un estudiante, ingrese uno nuevo")
            else:
                break
        except ValueError:
            print("Error. Ingrese un ID valido")
        except Exception as e:
            print("Ha ocurrido un error, vuelva a intentar")

    while True:
        try:
            name_student = str(input("Ingrese el nombre del estudiante: ")) #Variable que guarda el nombre del estudiante
            if not name_student.strip(): #Condicional por si no hay ningun valor en la variable name_student
                raise ValueError("Error. No se puede dejar el campo vacio")
            break
        except ValueError:
            print("Error. Ingrese correctamente el nombre del estudiante")
        except Exception as e:
            print("Ha ocurrido un error, vuelva a intentar")

    while True:
        try:
            degree_student = str(input("Ingrese la carrera o programa academico: ")) #Variable que guarda la carrerra o el campo academico del estudiante
            if not degree_student.strip(): #Condicional por si no hay ningun valor en la variable degree_student
                raise ValueError("Error, el campo no puede estar vacio")
            break
        except ValueError:
            print("Error. Ingrese correctamente la carrera o el programa academico del estudiante")
        except Exception as e:
            print("Ha ocurrido un error, vuelva a intentar")
    students[id_student] = {"nombre":name_student, "carrera":degree_student, "cursos":{}} #Toda la información se agrega al diccionarrio donde en la misma se crea un subdiccionarrio para agregar los cursos
    print("Se agregó al estudiante correctamente")

def add_course(): #Función para añadir curso y su nota
    if not students: #Condicional por si esta vacio el diccionario
        print("No hay ni un estudiante registrado")
        return #Retorna hacia el menú
    while True:
        try:
            id_search2 = str(input("Ingrese el ID del estudiante: ")) #Variable que guarda el ID del estudiante a buscar
            if not id_search2.strip(): #Condicional por si no hay ningun valor en la variable id_search
                raise ValueError("Error. El campo no puede estar vacio")
            if id_search2 not in students: #Condicional por si el ID buscado no esta en el diccionario
                print(f"El ID {id_search2} no se encuentra en la base de datos")
            else:
                break
        except ValueError:
            print("Error. Ingrese correctamente el ID del estudiante")
        except Exception as e:
            print("Ha ocurrido un error, vuelva a intentar")

    if id_search2 in students:
        while True:
            try:
                course_name = str(input("Ingrese el nombre del curso: ")) #Varible que guarda el nombre del curso
                if not course_name.strip(): #Condicional por si no hay ningun valor en la variable coursse_name
                    raise ValueError("Error. El campo no puede estar vacio")
                break
            except ValueError:
                print("Error. Ingrese correctamente el nombre del curso")
            except Exception:
                print("Ha ocurrido un error, vuelva a intentar")

        while True:
            try:
                final_qualification = float(input("Ingrese la nota final del estudiante: ")) #Variable que guarda la nota final del curso
                if final_qualification >= 0 and final_qualification <=100: #Condicional para que las notas ingresadas esten en el rago requerido
                    break
                else:
                    print("Error. La nota debe ser entre 0 a 100")
            except ValueError:
                print("Error. Solo se pueden ingresar numero (0 a 100)")
            except Exception as e:
                print("Ha ocurrido un error, vuelva a intentar")
        students[id_search2]['cursos'][course_name] = final_qualification #Se agrega la información del curso y su nota al subdiccionario
        print("Se agregó el curso y la nota correctamente")

def consult_student(): #Función para consultar información de los estudiantes
    if not students: #Condicional por si esta vacio el diccionario
        print("No hay ni un estudiante registrado")
        return
    while True:
        try:
            id_search = str(input("Ingrese el ID del estudiante a consultar: ")) #Variable que guarda el ID del estudiante a buscar
            if not id_search.strip(): #Condicional por si no hay ningun valor en la variable id_search
                raise ValueError("Error. El campo no puede estar vacio")
            if id_search not in students: #Condicional por si el ID no esta en el diccionario
                print(f"El ID {id_search}  no se encuentra en la base de datos")
            else:
                break
        except ValueError:
            print("Error. Ingrese correctamente el ID del estudiante")
        except Exception as e:
            print("Ha ocurrido un error, vuelva a intentar")
    if id_search in students: #Condicional por si el ID si esta en el diccionario
        print(f"Nombre del estudiante: {students[id_search]['nombre']}")
        print(f"Carrera o programa academico: {students[id_search]['carrera']}")
        if students[id_search]['cursos']: #Condicional si es que hay cursos asignados al estudiante
            print("Cursos añadidos")
            for course, qualification in students[id_search]["cursos"].items(): #Ciclo para poder tener el curso y su nota moviendose en el subdiccionario
                print(f"Curso: {course}, Nota Final: {qualification}")
        else:
            print("No se ha añadido algún curso al estudiante")

def calculate_average(): #Función para calcular el promedio de notas del estudiante
    if not students: #Condicional por si esta vacio el diccionario
        print("No hay ni un estudiante registrado")
        return
    while True:
        try:
            id_search3 = str(input("Ingrese el ID del estudiante a calcular su promedio de notas: ")) #Variable que guarda el ID del estudiante a buscar
            if not id_search3.strip(): #Condicional por si no hay ningun valor en el diccionario
                raise ValueError("Error. El campo no puede estar vacio")
            if id_search3 not in students: #Condicional por si el ID no esta en el diccionario
                print(f"El ID {id_search3} no se encuentra en la base de datos")
            else:
                break
        except ValueError:
            print("Error. Ingrese el ID del estudiante correctamente")
        except Exception as e:
            print("Ha ocurrido un error, vuelve a intentar")

    if id_search3 in students: #Condicional por si el ID esta en el diccionario
        if students[id_search3]['cursos']: #Condicional por si el estudiante tiene cursos asignados
            total_grade = 0
            total_course = 0
            for course, nota in students[id_search3]['cursos'].items(): #Ciclo para poder tener el curso y su nota moviendose en el subdiccionario
                total_course += 1
                total_grade = total_grade + nota
            print(f"El promedio entre todos los cursos es de {total_grade/total_course}")
        else:
            print("No se ha añadido algún curso al estudiante")


def check_passes(): #Función para ver si el estudiante aprobó los cursos asignados
    if not students: #Condicional por si esta vacio el diccionario
        print("No hay ni un estudiante registrado")
        return
    while True:
        try:
            id_search4 = str(input("Ingrese el ID del estudiante a verificar si aprueba los cursos: ")) #Variable que guarda el ID del estudiante a buscar
            if not id_search4.strip(): #Condicional por si no hay ningun valor en el diccionario
                raise ValueError("Error. El campo no puede estar vacio")
            if id_search4 not in students: #Condicional por si el ID no se encuentra en el diccionario
                print(f"El ID {id_search4} no se encuentra en la base de datos")
            else:
                break
        except ValueError:
            print("Error. Ingrese el ID del estudiante correctamente")
        except Exception as e:
            print("Ha ocurrido un error, vuelva a intentar")

    if id_search4 in students: #Condicional por si el ID se encuentra en el diccionario
        if students[id_search4]['cursos']: #Condicional por si el estudiante tiene cursos asignados
            for course, qualification in students[id_search4]['cursos'].items(): #Ciclo para poder tener el curso y su nota moviendose en el subdiccionario
                if qualification >= 61: #Condicional para comprobar si la nota es aprobatoria
                    print(f"El curso {course} se ha aprobado con una nota de {qualification}")
                else:
                    print(f"El curso {course} no se ha aprobado ya que no alcanzó lan nota minima de 61 puntos")
        else:
            print("No se ha añadido algún curso al estudiante")

def view_info_students():
    if not students: #Condicional por si esta vacio el diccionario
        print("No hay ni un estudiante registrado")
        return
    else:
        print("Los estudiantes registrados son los siguientes: ")
        for student, info in students.items(): #Ciclo para poder tener el ID, nombre y carrera del estudiante
            print(f"ID de estudiante: {student}")
            print(f"Nombre: {info['nombre']}")
            print(f"Carrera o programa academico: {info['carrera']}")
            print()
            if students[student]['cursos']:
                print("Cursos añadidos:")
                for course, qualification in students[student]['cursos'].items(): #Ciclo para poder tener el curso y su nota moviendose en el subdiccionario
                    print(f"Curso: {course}. Nota: {qualification}")
                print()
            else:
                print("No se ha añadido algún curso al estudiante")

while True: #Ciclo para poder mostrar el menú
    print("--Menú--")
    print("1.- Agregar estudiante")
    print("2.- Agregar curso con nota")
    print("3.- Consultar estudiante")
    print("4.- Calcular promedio del estudiante")
    print("5.- Verificar si aprueba")
    print("6.- Mostrar a todos los estudiantes")
    print("7.- Salir del programa")
    menu_option = input("Ingrese el número de la opción que quiera escoger: ") #Variable que guardda el número de opción quee haya seleccionado el usuario
    print()
    match menu_option: #Match case para poder almacenar las opciones del men´´u
        case "1":
            print("Agregar Estudiante")
            add_student() #Se llama a la función para poder añadir al estudiante
            print()
        case "2":
            print("Agregar Curso con Nota")
            add_course() #Se llama a la función para poder añadir el curso y su nota
            print()
        case "3":
            print("Consultar Estudiante")
            consult_student() #Se llama a la función para poder consultar la información de estudiante
            print()
        case "4":
            print("Calcular promedio del estudiante")
            calculate_average() #Se llama a la función para poder calcular el promedio de notas
            print()
        case "5":
            print("Verificar si aprueba")
            check_passes() #Se llama a la función para poder ver si la nota es aprobatoria o no
            print()
        case "6":
            print("Mostrar a todos los estudiantes")
            view_info_students() #Se llama a la función para poder visualizar a todos los estudiantes
            print()
        case "7":
            print("Saliendo del programa, gracias por su preferencia")
            break
        case _:
            print("Valor invalido, vuelva a intentar")
            print()