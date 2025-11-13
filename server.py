from shiny import reactive, render, ui
from revelio.components.modal import load_data_modal_ui, insert_rule_modal_ui
from revelio.core.utils import get_dummy_text, get_excel_sheets
import pandas as pd

from io import StringIO, BytesIO

def server(input, output, session):
    
    rule_rv = reactive.Value("")
    file_rv = reactive.Value(None)
    file_extension_rv = reactive.Value(None)
    file_content_rv = reactive.Value(None)
    dataset_rv = reactive.Value(None)
    target_column_rv = reactive.Value(None)

    # aggiungo un evento per osservare il cambiamento dei valori reactive
    @reactive.effect
    def _():
        print(f"Estensione: {file_extension_rv.get()}")
        print(f"File: {file_rv.get()['datapath'] if file_rv.get() else 'Nessun file'}")
        print(f"Dimensione del df: {dataset_rv.get().shape if dataset_rv.get() is not None else 'Nessun dataset'}")
        print(f"Colonna target: {target_column_rv.get()}")
        print("-----")

    # Modal handling

    @reactive.Effect
    @reactive.event(input.load_button)
    def _():    
        ui.modal_show(load_data_modal_ui())

    @reactive.Effect
    @reactive.event(input.add_rule)
    def _():    
        ui.modal_show(insert_rule_modal_ui())

    @reactive.Effect
    @reactive.event(input.close_modal)
    def _():
        ui.modal_remove()

    # Outputs

    # aggiornamento dinamico del modale

    @reactive.Effect
    @reactive.event(input.select_csv)
    def _():
        file_rv.set(input.select_csv()[0])
        file_extension_rv.set('csv')

        with open(file_rv.get()['datapath'], 'r', encoding='utf-8') as f:
            file_content_rv.set(f.read())

    @reactive.Effect
    @reactive.event(input.select_excel)
    def _():
        file_rv.set(input.select_excel()[0])
        file_extension_rv.set('excel')

        with open(file_rv.get()['datapath'], 'rb') as f:
            file_content_rv.set(f.read())

        sheets = get_excel_sheets(file_rv.get()['datapath'])
        ui.update_select('excel_sheet', choices=sheets)

    @reactive.Effect
    @reactive.event(input.load_data)
    def load_data():

        print("Loading data...")
        if file_content_rv.get() is None:
            print("Nessun file selezionato.")
            return
        
        
        if file_extension_rv.get() == 'csv':
            print("Caricamento CSV...")
            sep = input.csv_sep() or ';'
            dec = input.csv_dec() or ','

            df = pd.read_csv(StringIO(file_content_rv.get()), sep=sep, decimal=dec)
            dataset_rv.set(df)

        elif file_extension_rv.get() == 'excel':
            print("Caricamento Excel...")
            sheet_name = input.excel_sheet() or 0
            print(f"Foglio selezionato: {sheet_name}")

            df = pd.read_excel(BytesIO(file_content_rv.get()), sheet_name=sheet_name)
            dataset_rv.set(df)
        
        else:
            print("Tipo di file non supportato.")
            return
        
        ui.update_select('target_column', choices=list(dataset_rv.get().columns))
        target_column_rv.set(input.target_column())

        ui.modal_remove()
        return

    @reactive.Effect
    @reactive.event(input.target_column)
    def _():
        target_column_rv.set(input.target_column())

    @output
    @render.data_frame
    def loaded_data():
        return dataset_rv.get()
    
    @output
    @render.text
    def rule_output():
        return f"Regola definita: {rule_rv.get()}"