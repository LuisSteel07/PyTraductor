import flet as ft
from time import sleep, time
from utility import create_activities, save_translate, have_internet


def main(page: ft.Page):
    page.title = "PyTraductorSRT"
    page.update()
    page.theme_mode = ft.ThemeMode.DARK

    file_srt_path = ft.TextField()
    label_porcent = ft.Text("")

    state_process = ft.ProgressRing(visible=False)

    language_options_out = ft.Dropdown(
        width=180,
        tooltip="Idioma del subtítulo destino",
        options=[
            ft.dropdown.Option('es', 'Español'),
            ft.dropdown.Option('en', 'Inglés'),
            ft.dropdown.Option('de', 'Alemán'),
            ft.dropdown.Option('ar', 'Árabe'),
            ft.dropdown.Option('ko', 'Coreano'),
            ft.dropdown.Option('fr', 'Francés'),
            ft.dropdown.Option('it', 'Italiano'),
            ft.dropdown.Option('pt', 'Portugués'),
            ft.dropdown.Option('ru', 'Ruso'),
            ft.dropdown.Option('ja', 'Japonés'),
            ft.dropdown.Option('hi', 'Hindi'),
        ]
    )

    def error_dialog(text: str):
        alert = ft.AlertDialog(
            modal=True,
            adaptive=True,
            title=ft.Text("Error"),
            content=ft.Text(text),
            actions=[
                ft.TextButton("Cerrar", on_click=lambda e: page.close(alert)),
            ],
        )

        return alert

    def translate_file(file_path: str):
        try:
            if not have_internet():
                raise ConnectionError
            if file_path == "":
                raise RuntimeError
            if language_options_out.value is None:
                raise AttributeError

            list_activities = create_activities(file_path, language_options_out.value)
            cant_activities = 0
            finish_activities = 0

            language_options_out.disabled = True
            button_traducer.disabled = True
            file_srt_path.disabled = True
            state_process.visible = True
            page.update()

            start_time = time()
            for i in list_activities:
                cant_activities = cant_activities + 1
                if cant_activities == 20:
                    sleep(10)
                    cant_activities = 0
                i.thread_activity.start()

            for i in list_activities:
                i.thread_activity.join()
                finish_activities = finish_activities + 1
                label_porcent.value = f"{(finish_activities / len(list_activities) * 100):.2f} %"
                page.update()

            finish_time = time()
            tiempo = finish_time - start_time
            label_porcent.value = label_porcent.value + f" in {round(tiempo)} seg"

            language_options_out.disabled = False
            button_traducer.disabled = False
            file_srt_path.disabled = False
            state_process.visible = False
            page.update()

            save_translate(file_path, language_options_out.value, list_activities)
        except RuntimeError:
            page.open(error_dialog("Debe de colocar una ruta"))
        except PermissionError:
            page.open(error_dialog("Debe de seleccionar un archivo .srt específico"))
        except ValueError:
            page.open(error_dialog("Sólo se permiten archivos .srt"))
        except FileNotFoundError:
            page.open(error_dialog("El archivo especificado no se encontró"))
        except ConnectionError:
            page.open(error_dialog("No tiene conexión a Internet"))
        except AttributeError:
            page.open(error_dialog("Debe de seleccionar el idioma actual y el destinado"))

    button_traducer = ft.IconButton(icon=ft.icons.TRANSLATE, on_click=lambda e: translate_file(file_srt_path.value))

    page.appbar = ft.AppBar(
        title=ft.Text(value="PyTraductor", size=30, weight=ft.FontWeight.BOLD),
        leading=ft.Container(content=ft.Image("./python.png", width=120), padding=20),
        leading_width=100,
        center_title=False,
        toolbar_height=75,
    )

    page.add(
        ft.Column(
            [
                ft.Row(
                    [
                        file_srt_path,
                        language_options_out,
                        button_traducer,
                        state_process
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER
                ),
                label_porcent
            ],
            spacing=10,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER
        )
    )
    page.update()


ft.app(main)
