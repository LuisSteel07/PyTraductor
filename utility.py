import socket
from TranslateActivity import TranslateActivity


def create_activities(path: str, dest: str) -> list[TranslateActivity]:
    list_activities: list[TranslateActivity] = []

    with open(path, 'r') as sub:
        while True:
            numero_secuencia = sub.readline().strip()
            if not numero_secuencia:
                break
            tiempos = sub.readline().strip()
            textos = []
            linea = sub.readline().strip()
            while linea:
                textos.append(linea)
                linea = sub.readline().strip()

            list_activities.append(TranslateActivity(int(numero_secuencia), tiempos, textos[0], dest))

    return list_activities


def save_translate(path: str, dest: str, list_activities: list[TranslateActivity]):
    with open(f"{path}[{dest}].srt", 'w') as output_file:
        for i in list_activities:
            try:
                output_file.write(f"{i.num_sub}\n")
                output_file.write(f"{i.tempo}\n")
                output_file.write(f"{i.translate_text}")
                output_file.write(f"\n")
            except UnicodeEncodeError:
                continue


def have_internet() -> bool:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)
    try:
        s.connect(("www.google.com", 80))
    except (socket.gaierror, socket.timeout):
        return False
    else:
        s.close()
        return True
