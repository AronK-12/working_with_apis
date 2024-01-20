import requests
import flet as ft

API_LINK: str = "https://randomfox.ca/floof/"

image_count: int = 0
fox_images: list = []


def update_fox_images_list():
    if len(fox_images) < 5:
        for _ in range(10):
            r = requests.get(API_LINK)
            img = r.json()['image']

            fox_images.append(img)
    else:
        return


update_fox_images_list()


def main(page: ft.Page) -> None:
    page.title = "Random Fox App"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def get_next_image():
        return fox_images.pop()

    def get_fox_image(e):
        update_fox_images_list()

        img = get_next_image()

        if img != "":
            fox_image = ft.Image(
                src=f"{img}",
                width=600,
                height=600,
                fit=ft.ImageFit.CONTAIN
            )
            page.controls.append(fox_image)

            page.update()
            page.controls.pop(-1)

    fox_btn = ft.IconButton(icon=ft.icons.ADD, on_click=get_fox_image)

    page.add(fox_btn)


ft.app(target=main)
