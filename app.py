from shiny import App, ui
from ui import app_ui as revelio_ui
from server import server as revelio_server
from pathlib import Path

app_dir = Path(__file__).parent

app = App(revelio_ui, 
          revelio_server,
          static_assets=app_dir / "www"
          )

if __name__ == "__main__":
    app.run()