from tests.utils.docente import create_random_docente


def test_should_create_new_docente(client):
    data = {
        "codigo_docente": "2020123",
        "nombre": "JAIME",
        "apellido_paterno": "PARIONA",
        "apellido_materno": "QUISPE"
    }

    response = client.post("/docentes/create-docente/", json=data)

    assert response.status_code == 200
    assert response.json()["apellido_paterno"] == "PARIONA"


def test_should_fetch_docente_created(client, db_session):
    docente = create_random_docente(db=db_session)
    response = client.get(f"/docentes/get-docente/{docente.id}")
    
    assert response.status_code == 200
    assert response.json()["apellido_paterno"] == "PARIONA"