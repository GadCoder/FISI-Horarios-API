import json
import requests


def make_post_request(data: dict, url: str):
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json'
    }
    request = requests.post(url, json=data, headers=headers)
    return request


def open_carrera_json(carrera, plan):
    file = open(f"info/{plan}/{carrera.lower()}.json")
    info_json = json.load(file)
    return info_json


def insert_curso(carrera, ciclo, nombre_curso, codigo_curso, creditaje, plan):
    url = "http://127.0.0.1:8000/cursos/create-curso/"
    data = {
        "carrera": carrera,
        "ciclo": ciclo,
        "nombre_curso": nombre_curso,
        "codigo_curso": codigo_curso,
        "creditaje": creditaje,
        "plan": plan
    }
    request = make_post_request(data=data, url=url)
    if request.status_code == 200:
        print(f"Curso {nombre_curso} insertado con éxito")


def insert_cursos_from_carrera(plan: str, carrera: str):
    info_json = open_carrera_json(carrera, plan)
    for index, ciclo in enumerate(info_json["data"]):
        print(f"Ciclo : {index + 1}")
        for curso in ciclo["asignatura"]:
            carrera = carrera
            ciclo = index + 1
            nombre_curso = curso["desAsignatura"]
            codigo_curso = carrera[:4] + "-" + str(curso["codAsignatura"])
            creditaje = curso["numCreditaje"]
            insert_curso(carrera=carrera,
                         ciclo=ciclo,
                         nombre_curso=nombre_curso,
                         codigo_curso=codigo_curso,
                         creditaje=creditaje,
                         plan=plan)


def insert_docente(codigo_docente: str, nombre_docente: str, apellido_paterno: str, apellido_materno: str):
    url = "http://127.0.0.1:8000/docentes/create-docente/"
    data = {
        "codigo_docente": codigo_docente,
        "nombre": nombre_docente,
        "apellido_paterno": apellido_paterno,
        "apellido_materno": apellido_materno
    }
    request = make_post_request(data=data, url=url)
    if request.status_code == 200:
        print(f"Docente {nombre_docente} {apellido_paterno} insertado con éxito")
    elif request.status_code == 409:
        print(f"Docente {nombre_docente} {apellido_paterno} ya existe en la bd")


def insert_docentes_from_carrera(plan: str, carrera: str):
    info_json = open_carrera_json(carrera, plan)
    for ciclo in info_json["data"]:
        for curso in ciclo["asignatura"]:
            for seccion in curso["seccion"]:
                codigo_docente = str(seccion["codDocente"])
                nombre_docente = seccion["nomDocente"]
                apellido_paterno = seccion["apePaterno"]
                apellido_materno = seccion["apeMaterno"]
                if nombre_docente == "--" or codigo_docente == "--":
                    continue
                insert_docente(
                    codigo_docente=codigo_docente,
                    nombre_docente=nombre_docente,
                    apellido_paterno=apellido_paterno,
                    apellido_materno=apellido_materno
                )


def insert_seccion(codigo_curso: str, codigo_docente: str, codigo_seccion: str, numero_seccion: int, carrera: str, plan: str):
    url = f'http://127.0.0.1:8000/secciones/create-seccion/{codigo_curso}/{codigo_docente}'
    data = {
      "codigo_seccion": codigo_seccion,
      "numero_seccion": numero_seccion,
      "carrera": carrera,
      "plan": plan
    }

    request = make_post_request(data=data, url=url)
    if request.status_code == 200:
        print(f"Seccion {numero_seccion } del curso {codigo_curso} insertada con éxito")


def insert_secciones_from_carrera(plan: str, carrera):
    info_json = open_carrera_json(carrera, plan)
    for ciclo in info_json["data"]:
        for curso in ciclo["asignatura"]:
            codigo_curso = carrera[:4] + "-" + str(curso["codAsignatura"])
            for seccion in curso["seccion"]:
                codigo_docente = str(seccion["codDocente"])
                numero_seccion = seccion["codSeccion"]
                codigo_seccion = str(codigo_curso + "-" + str(numero_seccion))
                insert_seccion(codigo_curso=codigo_curso,
                               codigo_docente=codigo_docente if codigo_docente != "--" else None,
                               codigo_seccion=codigo_seccion,
                               numero_seccion=numero_seccion,
                               carrera=carrera,
                               plan=plan)


def obtener_hora_en_int(hora_str: str):
    return int(hora_str.split(":")[0])


def insert_horario_for_seccion(hora_inicio: int, hora_fin: int, dia: str, carrera: str, codigo_seccion: str, numero_horario: int, plan: str):
    url = 'http://127.0.0.1:8000/horario-seccion/create-horario-seccion/'
    data = {
      "hora_inicio": hora_inicio,
      "hora_fin": hora_fin,
      "dia": dia,
      "carrera": carrera,
      "codigo_seccion": codigo_seccion,
      "numero_horario": numero_horario,
      "plan": plan
    }

    request = make_post_request(data=data, url=url)
    if request.status_code == 200:
        print(f"Horario {numero_horario} de la seccion {codigo_seccion} insertado con éxito")


def insert_horarios_from_secciones(plan: str, carrera):
    info_json = open_carrera_json(carrera, plan)
    for ciclo in info_json["data"]:
        for curso in ciclo["asignatura"]:
            codigo_curso = carrera[:4] + "-" + str(curso["codAsignatura"])
            for seccion in curso["seccion"]:
                numero_seccion = seccion["codSeccion"]
                codigo_seccion = str(codigo_curso + "-" + str(numero_seccion))
                for horario in seccion["horarios"]:
                    hora_inicio = obtener_hora_en_int(horario["horaInicio"])
                    hora_fin = obtener_hora_en_int(horario["horaFin"])
                    dia = horario["dia"]
                    numero_horario = horario["codHorario"]
                    insert_horario_for_seccion(
                        hora_inicio=hora_inicio,
                        hora_fin=hora_fin,
                        dia=dia,
                        carrera=carrera,
                        codigo_seccion=codigo_seccion,
                        numero_horario=numero_horario,
                        plan=plan
                    )


def main():
    planes = ["2023", "2018"]
    try:
        for plan in planes:
            carreras = ["SOFTWARE", "SISTEMAS"]
            for carrera in carreras:
                print(f"Inserting data for plan {plan} carrera {carrera}")
                insert_cursos_from_carrera(plan, carrera)
                insert_docentes_from_carrera(plan, carrera)
                insert_secciones_from_carrera(plan, carrera)
                insert_horarios_from_secciones(plan, carrera)
    except Exception as e:
        print(f"-> Error: {e}")


if __name__ == "__main__":
    main()
