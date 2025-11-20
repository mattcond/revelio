from shiny import ui

def load_excel_page():

    excel_page_ui = ui.page_fillable(
        ui.input_file("select_excel", None , accept=[".xlsx", ".xls"], width='100%'),
        ui.input_select('excel_sheet', 'Foglio', [])
    )

    return excel_page_ui

def load_csv_page():

    csv_page_ui = ui.page_fillable(
        ui.input_file("select_csv", None , accept=[".csv", ".txt"], width='100%'),
        ui.row(
            ui.column(2, ui.input_text('csv_sep', 'Sep', ';')),
            ui.column(2, ui.input_text('csv_dec', 'Dec', ',')),
        )
    )

    return csv_page_ui

def add_rule_page():

    modal_ui = ui.page_fillable(
        ui.input_text("rule_name", "Nome regola:", width="100%"),
        ui.hr(),
        ui.input_text_area("rule_textarea", "Definisci una regola:", width="100%", rows=5),
        ui.hr(),
        ui.input_action_button("save_rule", "Salva regola"),
    )

    return modal_ui

def load_rule_page():

    modal_ui = ui.page_fillable(
        ui.input_file("load_rule_file", "Seleziona file", accept=[".xlsx", ".xls", ".csv", ".txt"], width="100%"),
        ui.input_action_button("load_rule_button", "Carica regola da file"),
    )

    return modal_ui

def edit_rule_page():

    modal_ui = ui.page_fillable(
        ui.input_select("edit_rule_select", "Seleziona regola da modificare:", choices=[] , width="100%"),
        ui.hr(),
        ui.input_text_area("edit_rule_textarea", "Modifica regola:", width="100%", rows=5),
        ui.hr(),
        ui.input_action_button("save_edited_rule", "Salva modifiche"),
    )

    return modal_ui

def load_data_modal_ui():

    navset_page = ui.navset_card_underline(
        ui.nav_panel("Excel", load_excel_page()),
        ui.nav_panel("CSV", load_csv_page()),
        footer=None,
        title=None,
    )

    modal = ui.modal(
        navset_page,
        ui.input_action_button("load_data", "Carica dati"),
        title='Carica',
        easy_close=True,
        size='l', 
        # footer=ui.tags.div(
        #     ui.input_action_link("close_modal", "Chiudi")
        # )
    )
    
    return modal

def insert_rule_modal_ui():

    navset_page = ui.navset_card_underline(
        ui.nav_panel("Add", add_rule_page()),
        ui.nav_panel("Load", load_rule_page()),
        ui.nav_panel("Edit", edit_rule_page()),
        full_screen=True,
        footer=None,
        title=None,
    )

    modal_ui = ui.modal(
        navset_page,
        title='Aggiungi regola',
        easy_close=True,
        size='l', 
        # footer=ui.tags.div(
        #     ui.input_action_link("close_modal", "Chiudi")
        # ) 
    )
    
    return modal_ui