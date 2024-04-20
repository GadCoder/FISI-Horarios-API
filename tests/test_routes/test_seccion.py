from tests.utils.docente import create_random_docente
from tests.utils.curso import create_random_curso
from tests.utils.seccion import create_random_seccion


def test_should_create_new_seccion(client, db_session):
    docente = create_random_docente(db=db_session)
    curso = create_random_curso(db=db_session)
    data = {
        "codigo_seccion": "123",
        "numero_seccion": 1,
        "carrera": "SOFTWARE",
        "plan": "2018"
    }
    response = client.post(f"/secciones/create-seccion/{curso.codigo_curso}/{docente.codigo_docente}", json=data)

    assert response.status_code == 200
    assert response.json()["codigo_seccion"] == "123"


def test_should_fetch_seccion_from_curso(client, db_session):
    seccion = create_random_seccion(db=db_session)
    response = client.get(f"/secciones/get-secciones-from-curso/{2018}/{seccion.codigo_curso}")

    assert response.status_code == 200
    assert response.json()[0]["codigo_seccion"] == "123"