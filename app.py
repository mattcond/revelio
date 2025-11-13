from shiny import App, ui
from ui import app_ui as revelio_ui
from server import server as revelio_server



app = App(revelio_ui, 
          revelio_server)

if __name__ == "__main__":
    app.run()