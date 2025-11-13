# ui.py
from shiny import ui

rule_page = ui.page_fillable(
    ui.input_text("rule", "Definisci una regola:", width="100%"), 
    ui.output_text_verbatim("rule_output"),
    ui.input_action_button("execute_rule", "Testa regola"),
    ui.hr(),
    ui.h4("Risultato del test")

)

data_page = ui.page_fillable(
    ui.output_data_frame("data")
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
            ui.input_action_button("load_button", "Carica dati")
        ),
        navset_page,
        title="Revelio App",
        window_title="Revelio",
    )
    return app_ui

app_ui = main_ui()