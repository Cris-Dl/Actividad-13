students = {}
def add_student():
    id_student = str(input("Ingrese el ID del estudiante: "))
    name_student = str(input("Ingrese el nombre del estudiante: "))
    degree_student = str(input("Ingrese la carrera o programa academico: "))
    students[id_student] = {"nombre":name_student, "carrera":degree_student, "cursos":{}}

def add_course():
    if students:
        id_search2 = str(input("Ingrese el ID del estudiante: "))
        if id_search2 in students:
            course_name = str(input("Ingrese el nombre del curso: "))
            final_qualification = float(input("Ingrese la nota final del estudiante: "))
            students[id_search2]['cursos'][course_name] = final_qualification
        else:
            print(f"El ID {id_search2} no se ha encontrado en la base de datos")
    else:
        print("No hay ningun estudiante añadido")

def consult_student():
    if students:
        id_search = str(input("Ingrese el ID del estudiante a consultar: "))
        if id_search in students:
            print(f"Nombre del estudiante: {students[id_search]['nombre']}")
            print(f"Carrera o programa academico: {students[id_search]['carrera']}")
            if students[id_search]['cursos']:
                print("Cursos añadidos")
                for course, qualification in students[id_search]["cursos"].items():
                    print(f"Curso: {course}, Nota Final: {qualification}")
            else:
                print("No se ha añadido algún curso al estudiante")
        else:
            print(f"El ID {id_search} no se ha encontrado en la base de datos")
    else:
        print("No hay ningun estudiante añadido")


while True:
    print("--Menú--")
    print("1.- Agregar estudiante")
    print("2.- Agregar curso con nota")
    print("3.- Consultar estudiante")
    print("4.- Calcular promedio del estudiante")
    print("5.- Verificar si aprueba")
    print("6.- Mostrar a todos los estudiantes")
    print("7.- Salir del programa")
    menu_option = input("Ingrese el número de la opción que quiera escoger: ")
    print()
    match menu_option:
        case "1":
            print("Agregar Estudiante")
            add_student()
            print()
        case "2":
            print("Agregar Curso con Nota")
            add_course()
            print()
        case "3":
            print("Consultar Estudiante")
            consult_student()
            print()
        case "4":
            print("Calcular promedio del estudiante")
        case "5":
            print("Verificar si aprueba")
        case "6":
            print("Mostrar a todos los estudiantes")
        case "7":
            print("Saliendo del programa, gracias por su preferencia")
            break
        case _:
            print("Valor invalido, vuelva a intentar")