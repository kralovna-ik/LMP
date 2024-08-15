import flet as ft

# Define translations for each language (add translations for the new page)
translations = {
    "English (United States)": {
        "title": "Home Page",
        "question": "You are?",
        "btn_technicians": "Technicians",
        "btn_clients": "Clients",
        "btn_enterprises": "Enterprises",
        "email_placeholder": "Enter your email",
        "password_placeholder": "Enter your password",
        "forgot_password": "Forgot Password?",
        "login": "Log In",
        "signup": "Don't have an account? Sign Up",
    },
    "Arabic": {
        "title": "الصفحة الرئيسية",
        "question": "من أنت؟",
        "btn_technicians": "الفنيون",
        "btn_clients": "العملاء",
        "btn_enterprises": "الشركات",
        "email_placeholder": "أدخل بريدك الإلكتروني",
        "password_placeholder": "أدخل كلمة المرور",
        "forgot_password": "نسيت كلمة المرور؟",
        "login": "تسجيل الدخول",
        "signup": "ليس لديك حساب؟ اشترك",
    },
    "French": {
        "title": "Page d'accueil",
        "question": "Vous êtes?",
        "btn_technicians": "Techniciens",
        "btn_clients": "Clients",
        "btn_enterprises": "Entreprises",
        "email_placeholder": "Entrez votre email",
        "password_placeholder": "Entrez votre mot de passe",
        "forgot_password": "Mot de passe oublié?",
        "login": "Se connecter",
        "signup": "Vous n'avez pas de compte? S'inscrire",
    }
}

def main(page: ft.Page):
    page.title = "Home Page"
    selected_language = "English (United States)"
    selected_button = None

    def create_button(text):
        return ft.ElevatedButton(
            content=ft.Row(
                [
                    ft.Text(text, expand=True),
                    ft.Icon(ft.icons.CHECK, visible=False, color="#ffffff")
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            ),
            bgcolor="#386376",
            color=ft.colors.WHITE,
            height=50,
            width=200
        )

    logo = ft.Image(src="icon1.png", width=200, height=200)
    question = ft.Text("You are?", size=32, font_family="ARIALBD 1", color="#386376", text_align="center")
    btn_technicians = create_button("Technicians")
    btn_clients = create_button("Clients")
    btn_enterprises = create_button("Enterprises")
    buttons = [btn_technicians, btn_clients, btn_enterprises]

    language_dropdown = ft.Dropdown(
        options=[
            ft.dropdown.Option("English (United States)"),
            ft.dropdown.Option("Arabic"),
            ft.dropdown.Option("French")
        ],
        value="English (United States)",
        width=200,
        bgcolor="#eff5f6",
        color="#386376",
        border_color="#386376",
        focused_border_color="#386376",
        focused_bgcolor="#eff5f6",
    )

    def update_content():
        translation = translations[selected_language]
        page.title = translation["title"]
        page.bgcolor = "#eff5f6"
        question.value = translation["question"]
        btn_technicians.content.controls[0].value = translation["btn_technicians"]
        btn_clients.content.controls[0].value = translation["btn_clients"]
        btn_enterprises.content.controls[0].value = translation["btn_enterprises"]
        
        if len(page.views) > 1 and page.views[-1].route == "/technician_login":
            update_technician_login_view()
        
        page.update()

    def on_button_click(e):
        nonlocal selected_button
        clicked_button = e.control
        
        if selected_button:
            selected_button.content.controls[1].visible = False
        
        clicked_button.content.controls[1].visible = True
        selected_button = clicked_button
        
        if clicked_button == btn_technicians:
            page.go("/technician_login")
        
        page.update()

    for button in buttons:
        button.on_click = on_button_click

    def on_language_change(e):
        nonlocal selected_language
        selected_language = language_dropdown.value
        update_content()

    language_dropdown.on_change = on_language_change

    def update_technician_login_view():
        translation = translations[selected_language]
        login_view = page.views[-1]
        
        email_field = login_view.controls[0].content.controls[1].controls[1]
        password_field = login_view.controls[0].content.controls[1].controls[2]
        forgot_password = login_view.controls[0].content.controls[1].controls[3]
        login_button = login_view.controls[0].content.controls[1].controls[4]
        signup_link = login_view.controls[0].content.controls[1].controls[5]
        
        email_field.label = translation["email_placeholder"]
        password_field.label = translation["password_placeholder"]
        forgot_password.text = translation["forgot_password"]
        login_button.text = translation["login"]
        signup_link.text = translation["signup"]

    def on_back_click(e):
        page.go("/")

    def technician_login_view():
        translation = translations[selected_language]
        
        back_button = ft.IconButton(
            icon=ft.icons.ARROW_BACK,
            on_click=on_back_click,
            icon_color="#386376"
        )
        
        login_logo = ft.Image(src="icon1.png", width=150, height=150)
        email_field = ft.TextField(
            label=translation["email_placeholder"],
            icon=ft.icons.EMAIL,
            width=300,
            border_color="#386376",
            focused_border_color="#386376",
            text_style=ft.TextStyle(color="#386376"),
            bgcolor=ft.colors.WHITE,
            cursor_color="#386376",
            focused_bgcolor="#eff5f6",
        )
        password_field = ft.TextField(
            label=translation["password_placeholder"],
            icon=ft.icons.LOCK,
            password=True,
            width=300,
            border_color="#386376",
            focused_border_color="#386376",
            text_style=ft.TextStyle(color="#386376"),
            bgcolor=ft.colors.WHITE,
            cursor_color="#386376",
            focused_bgcolor="#eff5f6",
        )
        forgot_password = ft.TextButton(
            text=translation["forgot_password"],
            style=ft.ButtonStyle(color={"": "#386376"})
        )
        login_button = ft.ElevatedButton(
            text=translation["login"],
            bgcolor="#386376",
            color=ft.colors.WHITE,
            width=300
        )
        signup_link = ft.TextButton(
            text=translation["signup"],
            style=ft.ButtonStyle(color={"": "#386376"})
        )

        return ft.View(
            "/technician_login",
            [
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Row(
                                [back_button],
                                alignment=ft.MainAxisAlignment.START
                            ),
                            ft.Column(
                                [
                                    login_logo,
                                    email_field,
                                    password_field,
                                    forgot_password,
                                    login_button,
                                    signup_link,
                                    language_dropdown
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                spacing=20
                            )
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=20
                    ),
                    padding=20
                )
            ],
            bgcolor="#eff5f6"
        )

    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    ft.Column(
                        [
                            logo,
                            question,
                            ft.Column(
                                buttons,
                                alignment=ft.MainAxisAlignment.CENTER,
                                spacing=20,
                                width=200
                            ),
                            language_dropdown
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=30
                    )
                ],
                bgcolor="#eff5f6"
            )
        )
        if page.route == "/technician_login":
            page.views.append(technician_login_view())
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

ft.app(target=main, assets_dir="assets")
