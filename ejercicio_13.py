students = {}
notas = {}
def add_student():
    id_student = str(input("Ingrese el ID del eestudiante: "))
    name_student = str(input("Ingrese el nombre del estudiante: "))
    course_student = str(input("Ingrese el curso o programa academico: "))
    students[id_student] = {"nombre":name_student, "curso":course_student}

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
        case "2":
            print("Agregar Curso con Nota")
        case "3":
            print("Consultar Estudiante")
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