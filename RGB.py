import flet as ft

def main(page: ft.Page):
    page.title = "Rainbow Switcher"
    page.window_width = 300
    page.window_height = 300

    slider_r = ft.Slider(min=0, max=255, value=128, divisions=255, active_color="red")
    slider_g = ft.Slider(min=0, max=255, value=128, divisions=255, active_color="green")
    slider_b = ft.Slider(min=0, max=255, value=128, divisions=255, active_color="blue")

    def update(e):
        r = int(slider_r.value)
        g = int(slider_g.value)
        b = int(slider_b.value)
        page.bgcolor = f"rgb({r}, {g}, {b})"
        page.update()

    slider_r.on_change = update
    slider_g.on_change = update
    slider_b.on_change = update

    page.add(
        ft.Text("Red"), slider_r,
        ft.Text("Green"), slider_g,
        ft.Text("Blue"), slider_b,
    )

ft.app(target=main)

