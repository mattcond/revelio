from shiny import reactive, render, ui
from revelio.components.modal import load_data_modal_ui
from revelio.core.utils import get_dummy_text, get_excel_sheets

def server(input, output, session):
    
    test_text_rv = reactive.Value("")
    modal_text_rv = reactive.Value("Testo iniziale nel modale.")
    rule_rv = reactive.Value("")

    # Change main text button handling

    @reactive.Effect
    @reactive.event(input.change_text)
    def _():
        test_text_rv.set(get_dummy_text())

    # Modal handling

    @reactive.Effect
    @reactive.event(input.load_button)
    def _():    
        ui.modal_show(load_data_modal_ui())

    @reactive.Effect
    @reactive.event(input.close_modal)
    def _():
        ui.modal_remove()

    # Modal action button handling

    @reactive.Effect
    @reactive.event(input.load_data)
    def _():
        modal_text_rv.set(get_dummy_text())

    # Outputs

    # aggiornamento dinamico del modale

    @output
    @render.ui
    def load_specifics_ui():
        if input.select_file() is None:
            return ui.p("Nessun file selezionato.")
        
        selected_file = input.select_file()[0]
        extension = selected_file['name'].split('.')[-1].lower()
        datapath = selected_file['datapath']

        if extension in ['csv', 'txt']:
            return ui.div(
                    ui.p(f"File {extension} selezionato: {selected_file['name']}"),
                    ui.row(
                        ui.column(2,ui.input_text("sep_spec", "sep")),
                        ui.column(2,ui.input_text("dec_spec", "dec"))
                    ),
                    ui.input_action_button("load_data", "Carica"),
                )
        
        elif extension in ['xlsx', 'xls']:

            sheets = get_excel_sheets(datapath)
            return ui.div(
                ui.p(f"File Excel selezionato: {selected_file['name']}"),
                ui.input_select("excel_sheet", "Seleziona foglio:", sheets),
                ui.input_action_button("load_data", "Carica"),
            )
        
        else:
            return ui.p("Tipo di file non supportato.")

    @output
    @render.text
    def main_text():
        return test_text_rv.get()
    
    @output
    @render.text
    def modal_text():
        return modal_text_rv.get()

    @output
    @render.text
    def rule_output():
        return f"Regola definita: {rule_rv.get()}"