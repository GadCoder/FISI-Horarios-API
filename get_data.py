import requests
import json


def get_auth_token(usuario, clave):
    url = 'https://sumvirtual.unmsm.edu.pe/sumapi/loguearse'
    headers = {
        'accept': 'application/json',
        'Accept-Encoding': 'gzip',
        'authorization': 'AUTH TOKEN',
        'Connection': 'Keep-Alive',
        'Content-Length': '52',
        'Content-Type': 'application/json',
        'Host': 'sumvirtual.unmsm.edu.pe',
        'User-Agent': 'okhttp/4.9.2'
    }
    data = {
        'usuario': usuario,
        'clave': clave
    }
    request = requests.post(url, headers=headers, json=data)
    status = request.status_code
    if status != 200:
        print(f"Error with login")
        return None
    data = request.json()
    token = data['data'][-1]['token']

    cookies = request.cookies
    cookie_dict = {}
    for cookie in cookies:
        cookie_dict[cookie.name] = cookie.value

    return token, cookie_dict



def get_programacion(token: str, cookies: dict, plan: str, carrera: str):
    url = 'https://sumvirtual.unmsm.edu.pe/sumapi/matricula/obtenerProgramacionCursos'
    headers = {
        'accept': 'application/json',
        'Accept-Encoding': 'gzip',
        'authorization': f'Bearer {token}',
        'Connection': 'Keep-Alive',
        'Content-Length': '52',
        'Content-Type': 'application/json',
        'Host': 'sumvirtual.unmsm.edu.pe',
        'User-Agent': 'okhttp/4.9.2'
    }

    request = requests.get(url, headers=headers, cookies=cookies)
    print(request.status_code)
    with open(f"{carrera}_{plan}.json", "w", encoding="utf-8") as file:
        data = request.json()
        json.dump(data, file)


def main():
    usuario = ''
    password = ''
    token, cookies = get_auth_token(usuario=usuario, clave=password)
    get_programacion(token=token, cookies=cookies, plan='2018', carrera="software")


if __name__ == "__main__":
    main()
