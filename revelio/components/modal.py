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

def load_data_modal_ui():

    navset_page = ui.navset_card_underline(
        ui.nav_panel("Excel", load_excel_page()),
        ui.nav_panel("CSV", load_csv_page()),
        footer=None,
        title=None,
    )

    modal = ui.modal(
        navset_page,
        ui.input_switch('is_trading_data', 'Sono candele?', False),
        title='Carica',
        easy_close=False, 
        footer=ui.tags.div(
            ui.input_action_link("close_modal", "Chiudi")
        )
    )
    
    return modal