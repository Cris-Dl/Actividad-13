students = {}
def add_student():
    while True:
        try:
            id_student = str(input("Ingrese el ID del estudiante: "))
            if not id_student.strip():
                raise ValueError("Error. No se puede dejar el campo vacio")
            break
        except ValueError:
            print("Error. Ingrese un ID valido")
        except Exception as e:
            print("Ha ocurrido un error, vuelva a intentar")

    while True:
        try:
            name_student = str(input("Ingrese el nombre del estudiante: "))
            if not name_student.strip():
                raise ValueError("Error. No se puede dejar el campo vacio")
            break
        except ValueError:
            print("Error. Ingrese correctamente el nombre del estudiante")
        except Exception as e:
            print("Ha ocurrido un error, vuelva a intentar")

    while True:
        try:
            degree_student = str(input("Ingrese la carrera o programa academico: "))
            if not degree_student.strip():
                raise ValueError("Error, el campo no puede estar vacio")
            break
        except ValueError:
            print("Error. Ingrese correctamente la carrera o el programa academico del estudiante")
        except Exception as e:
            print("Ha ocurrido un error, vuelva a intentar")
    students[id_student] = {"nombre":name_student, "carrera":degree_student, "cursos":{}}
    print("Se agregó al estudiante correctamente")

def add_course():
    if not students:
        print("No hay ni un estudiante registrado")
        return
    while True:
        try:
            id_search2 = str(input("Ingrese el ID del estudiante: "))
            if not id_search2.strip():
                raise ValueError("Error. El campo no puede estar vacio")
            if id_search2 not in students:
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
                course_name = str(input("Ingrese el nombre del curso: "))
                if not course_name.strip():
                    raise ValueError("Error. El campo no puede estar vacio")
                break
            except ValueError:
                print("Error. Ingrese correctamente el nombre del curso")
            except Exception:
                print("Ha ocurrido un error, vuelva a intentar")

        while True:
            try:
                final_qualification = float(input("Ingrese la nota final del estudiante: "))
                if final_qualification >= 0 and final_qualification <=100:
                    break
                else:
                    print("Error. La nota debe ser entre 0 a 100")
            except ValueError:
                print("Error. Solo se pueden ingresar numero (0 a 100)")
            except Exception as e:
                print("Ha ocurrido un error, vuelva a intentar")
        students[id_search2]['cursos'][course_name] = final_qualification
        print("Se agregó el curso y la nota correctamente")

def consult_student():
    if not students:
        print("No hay ni un estudiante registrado")
        return
    while True:
        try:
            id_search = str(input("Ingrese el ID del estudiante a consultar: "))
            if not id_search.strip():
                raise ValueError("Error. El campo no puede estar vacio")
            if id_search not in students:
                print(f"El ID {id_search}  no se encuentra en la base de datos")
            else:
                break
        except ValueError:
            print("Error. Ingrese correctamente el ID del estudiante")
        except Exception:
            print("Ha ocurrido un error, vuelva a intentar")
    if id_search in students:
        print(f"Nombre del estudiante: {students[id_search]['nombre']}")
        print(f"Carrera o programa academico: {students[id_search]['carrera']}")
        if students[id_search]['cursos']:
            print("Cursos añadidos")
            for course, qualification in students[id_search]["cursos"].items():
                print(f"Curso: {course}, Nota Final: {qualification}")
        else:
            print("No se ha añadido algún curso al estudiante")

def calculate_average():
    if not students:
        print("No hay ni un estudiante registrado")
        id_search3 = str(input("Ingrese el ID del estudiante a calcular su promedio de notas: "))
        if id_search3 in students:
            if students[id_search3]['cursos']:
                total_grade = 0
                total_course = 0
                for course, nota in students[id_search3]['cursos'].items():
                    total_course += 1
                    total_grade = total_grade + nota
                print(f"El promedio entre todos los cursos es de {total_grade/total_course}")
            else:
                print("No se ha añadido algún curso al estudiante")
        else:
            print(f"El ID {id_search3} no se ha encontrado en la base de datos")
    else:
        print("No hay ningun estudiante añadido")

def check_passes():
    if students:
        id_search4 = str(input("Ingrese el ID del estudiante a verificar si aprueba los cursos: "))
        if id_search4 in students:
            if students[id_search4]['cursos']:
                for course, qualification in students[id_search4]['cursos'].items():
                    if qualification >= 61:
                        print(f"El curso {course} se ha aprobado con una nota de {qualification}")
                    else:
                        print(f"El curso {course} no se ha aprobado ya que no alcanzó lan nota minima de 61 puntos")
            else:
                print("No se ha añadido algún curso al estudiante")
        else:
            print(f"El ID {id_search4} no se ha encontrado en la base de datos")
    else:
        print("No hay ningun estudiante añadido")

def view_info_students():
    if students:
        print("Los estudiantes registrados son los siguientes: ")
        for student, info in students.items():
            print(f"ID de estudiante: {student}")
            print(f"Nombre: {info['nombre']}")
            print(f"Carrera o programa academico: {info['carrera']}")
            print()
            if students[student]['cursos']:
                print("Cursos añadidos:")
                for course, qualification in students[student]['cursos'].items():
                    print(f"Curso: {course}. Nota: {qualification}")
                print()
            else:
                print("No se ha añadido algún curso al estudiante")
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
            calculate_average()
            print()
        case "5":
            print("Verificar si aprueba")
            check_passes()
            print()
        case "6":
            print("Mostrar a todos los estudiantes")
            view_info_students()
            print()
        case "7":
            print("Saliendo del programa, gracias por su preferencia")
            break
        case _:
            print("Valor invalido, vuelva a intentar")
            print()