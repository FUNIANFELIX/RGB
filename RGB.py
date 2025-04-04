import flet as ft

def main(page: ft.Page):
    page.title = "Rainbow Switcher"
    page.window.width = 300
    page.window.height = 300

    def update(e):
        r, g, b = int(slider_r.value), int(slider_g.value), int(slider_b.value)
        page.bgcolor = f"#{r:02x}{g:02x}{b:02x}"
        page.update()

    slider_r = ft.Slider(0, 255, value=128, divisions=255, on_change=update, active_color="red")
    slider_g = ft.Slider(0, 255, value=128, divisions=255, on_change=update, active_color="green")
    slider_b = ft.Slider(0, 255, value=128, divisions=255, on_change=update, active_color="blue")

    page.add(
        ft.Text("Red"), slider_r,
        ft.Text("Green"), slider_g,
        ft.Text("Blue"), slider_b,
    )

ft.app(target=main)
