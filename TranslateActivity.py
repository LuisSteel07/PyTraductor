from googletrans import Translator
from threading import Thread
from httpcore import ConnectTimeout


class TranslateActivity:
    def __init__(self, _num_sub: int, _tempo: str, _text: str, _dest: str):
        self.num_sub = _num_sub
        self.tempo = _tempo
        self.text = _text
        self.translate_text = ""
        self.thread_activity = Thread(target=self.translate, args=(_dest, ))

    def translate(self, dest: str):
        translator = Translator()
        try:
            self.translate_text = translator.translate(self.text, dest).text
        except ConnectTimeout as err:
            print(f"Tiempo de espera agotado {err}")
        except Exception as err:
            print(f"Ha ocurrido un error general {err}")
