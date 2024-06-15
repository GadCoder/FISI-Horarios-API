from tests.utils.curso import create_random_curso


def test_should_create_new_curso(client):
    data = {
        "carrera": "SOFTWARE",
        "ciclo": 5,
        "nombre_curso": "ESTRUCTURA DE DATOS",
        "codigo_curso": "202W0505",
        "creditaje": 4,
        "plan": "2018"
    }

    response = client.post("/cursos/create-curso/", json=data)

    assert response.status_code == 200



def test_should_fetch_curso_created(client, db_session):
    curso = create_random_curso(db=db_session)
    response = client.get(f"/cursos/get-curso/{curso.codigo_curso}")
    
    assert response.status_code == 200
    assert response.json()["nombre_curso"] == "ESTRUCTURA DE DATOS"