# ui.py
from shiny import ui
import shinyswatch
from pathlib import Path


rule_page = ui.page_fillable(
    ui.input_text("rule", "Definisci una regola:", width="100%"), 
    ui.output_text_verbatim("rule_output"),
    ui.input_action_button("execute_rule", "Testa regola"),
    ui.hr(),
    ui.h4("Risultato del test")

)

data_page = ui.page_fillable(
    ui.output_data_frame("loaded_data")
)

navset_page = ui.navset_card_underline(
    ui.nav_panel("Rule", rule_page),
    ui.nav_panel("Data", data_page),
    footer=None,
    title=None,
)


# --- UI ---
def main_ui():
    app_ui = ui.page_sidebar(
        ui.sidebar(
            ui.input_action_button("load_button", "Carica dati"), 
            ui.input_select('target_column', 'Colonna target', []),
            ui.input_action_button("add_rule", "Aggiungi regola"),
            ui.input_action_button("test_rule", "Testa regola"),
            fillable=True,
            title="Menu",
        ),
        navset_page,
        title="re>el!o",
        window_title="re>",
        fillable=True,
        fillable_mobile=True,
        # theme=shinyswatch.theme.cerulean
    )
    return app_ui

app_ui = main_ui()