import pandas as pd
import datetime as dt
import plotly.express as px
import plotly.graph_objs as go

from database_service.ElectricityLoadResource import ElectricityLoadResource

class StreamlitComponent:
    def __init__(self):
        pass

    @classmethod
    def plot_line_chart(cls, start_date, end_date, areas, agg):

        # get load data
        df = ElectricityLoadResource._get_agg_actual_data(start_date, end_date, areas, agg)

        df = df.sort_values(by=['time_stamp'])

        fig = px.line(
            data_frame=df,
            x="time_stamp",
            y="actual_load",
            color="zone_name",
        )
        fig.update_layout(
            title_text="Electricity Demand Data",
            xaxis=dict(
                rangeslider=dict(
                    visible=True
                ),
                type="date"
            ),
        )

        return fig