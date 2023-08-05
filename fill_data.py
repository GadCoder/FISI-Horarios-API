import json
import requests


def insert_curso(carrera, ciclo, nombre_curso, codigo_curso, creditaje):
    url = "http://127.0.0.1:8000/create-curso/"
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json'
    }

    data = {
        "carrera": carrera,
        "ciclo": ciclo,
        "nombre_curso": nombre_curso,
        "codigo_curso": codigo_curso,
        "creditaje": creditaje
    }

    request = requests.post(url, json=data, headers=headers)
    if request.status_code == 200:
        print(f"Curso {nombre_curso} insertado con éxito")


def insert_cursos_from_carrera(carrera: str):
    file = open(f"info/programacion_{carrera}.json")
    info_json = json.load(file)
    for index, ciclo in enumerate(info_json["data"]):
        print(f"Ciclo : {index + 1}")
        for curso in ciclo["asignatura"]:
            carrera = carrera
            ciclo = index + 1
            nombre_curso = curso["desAsignatura"]
            codigo_curso = curso["codAsignatura"]
            creditaje = curso["numCreditaje"]
            insert_curso(carrera=carrera,
                         ciclo=ciclo,
                         nombre_curso=nombre_curso,
                         codigo_curso=codigo_curso,
                         creditaje=creditaje)


def insert_docente(codigo_docente: str, nombre_docente: str, apellido_paterno: str, apellido_materno: str):
    url = "http://127.0.0.1:8000/docentes/create-docente/"
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json'
    }

    data = {
        "codigo_docente": codigo_docente,
        "nombre": nombre_docente,
        "apellido_paterno": apellido_paterno,
        "apellido_materno": apellido_materno
    }

    request = requests.post(url, json=data, headers=headers)
    if request.status_code == 200:
        print(f"Docente {nombre_docente} {apellido_paterno} insertado con éxito")
    elif request.status_code == 409:
        print(f"Docente {nombre_docente} {apellido_paterno} ya existe en la bd")


def insert_docentes(carrera: str):
    file = open(f"info/programacion_{carrera}.json")
    info_json = json.load(file)
    for index, ciclo in enumerate(info_json["data"]):
        for curso in ciclo["asignatura"]:
            for seccion in curso["seccion"]:
                codigo_docente = seccion["codDocente"]
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


def main():
    carreras = ["SOFTWARE", "SISTEMAS"]
    for carrera in carreras:
        insert_docentes(carrera)


if __name__ == "__main__":
    main()
