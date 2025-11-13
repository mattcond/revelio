from shiny import App, ui
from revelio.ui import app_ui as revelio_ui
from revelio.server import server as revelio_server



app = App(revelio_ui, 
          revelio_server)

if __name__ == "__main__":
    app.run()