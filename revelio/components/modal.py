from shiny import ui

def modal_ui():

    modal = ui.modal(
        ui.input_file("select_file", 
                      "File:", 
                      accept=[".xlsx", ".xls", ".csv", ".txt"]),
        ui.output_ui("load_specifics_ui"),
        title="Carica i dati",
        easy_close=False,  # se True puoi chiudere cliccando fuori
        footer=ui.tags.div(
            ui.input_action_link("close_modal", "Chiudi")
        )
    )
    
    return modal