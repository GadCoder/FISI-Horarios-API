from tests.utils.seccion import create_random_seccion
from tests.utils.horario_seccion import create_random_horario_seccion


def test_should_create_new_horario_seccion(client, db_session):
    seccion = create_random_seccion(db=db_session)  
    data = {
        "hora_inicio": 8,
        "hora_fin": 12,
        "dia": "LUNES",
        "carrera": "SOFTWARE",
        "codigo_seccion": seccion.codigo_seccion,
        "numero_horario": 1,
        "plan": "2018"
    }
    response = client.post("/horario-seccion/create-horario-seccion/", json=data)

    assert response.status_code == 200
    assert response.json()["dia"] == "LUNES"
    assert response.json()["carrera"] == "SOFTWARE"
    assert response.json()["numero_horario"] == 1


def test_should_fetch_horario_seccion_created(client, db_session):
    horario_seccion = create_random_horario_seccion(db=db_session)
    response = client.get(f"/horario-seccion/get-horarios-from-seccion/2018/SOFTWARE/{horario_seccion.codigo_seccion}")

    assert response.status_code == 200
    assert response.json()["codigo_seccion"] == horario_seccion.codigo_seccion
    assert response.json()["horarios"][0]["dia"] == "LUNES"
