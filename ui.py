# ui.py
from shiny import ui
import faicons as fa
import shinyswatch
from pathlib import Path

app_dir = Path(__file__).parent

rule_page = ui.page_fluid(
    ui.row(
        ui.layout_columns(
            ui.span(),
            ui.h5('Select rule:'),
            ui.input_select('rule_id', None, [], width='100%'),
            ui.input_action_button("test_rule", "Test", width='100%', icon=fa.icon_svg("play")),
            ui.input_switch('is_trading_data', 'Quant-mode', False),
            col_widths=(6, 1, 3, 1, 1)
        )
    ),
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
    app_ui = ui.page_fluid(
        # ui.layout_column_wrap(
        #     #ui.nav_control(ui.img(src="logo.png", width="100%")),
        #     ui.column(
        #         12,
        ui.card(
            ui.layout_columns(

                ui.img(src="logo.png", width="100%"), # width 1
                ui.input_action_button("load_button", label='Upload', icon=fa.icon_svg("folder-open")), # width 1
                ui.input_action_button("add_rule", label='Rule', icon=fa.icon_svg("terminal")), # width 1
                ui.span(), # width 4
                ui.h4("Target:"), # width 1
                ui.input_select('target_column', None, [],width='100%'), # width 2
                # ui.span(), # width 1
                # ui.input_action_button("test_rule", "Test rule", width='100%'), # width 2
                col_widths=(1, 1, 1, 5, 1, 3), 
                row_heights='auto', 

            ),
        ),
        navset_page,
        #     )
        # ),
        title='re>el!o',
        # window_title="re>",
        lang='it',
        theme=shinyswatch.theme.flatly
    )

    return app_ui

app_ui = main_ui()