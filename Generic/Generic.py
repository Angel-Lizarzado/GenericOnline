import reflex as rx
from Generic.components.navbar import navbar


class User(rx.Model, table=True):
 username: str
 password: str

with rx.session() as session:
    result = session.execute("SELECT * FROM Account.dbo.tUser")
    for row in result:
        print(row)

def index() -> rx.Component:
    return rx.center(
        #rx.theme_panel(),
        navbar(),
        
        height="100vh",
    )


app = rx.App(
   
    theme=rx.theme(
        appearance="dark",
        has_background=True,
        radius="large",
        accent_color="orange",
    )
)
app.add_page(index)
