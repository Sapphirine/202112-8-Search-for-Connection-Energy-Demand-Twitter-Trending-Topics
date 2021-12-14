import pandas as pd
import pandas_gbq
from google.oauth2 import service_account
import datetime as dt
import os

credential_location = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', '..', 'credentials', 'big-data-6893-326515-2aa820b557cd.json'))

# Setting Credentials
CREDENTIALS = service_account.Credentials.from_service_account_file(credential_location)
PROJECT_NAME = "big-data-6893-326515"

# Setting DB Context
pandas_gbq.context.credentials = CREDENTIALS
pandas_gbq.context.project = PROJECT_NAME
DB_NAME = "project_dataset"


class ElectricityLoadResource:
    def __init__(self):
        pass

    @classmethod
    def _get_agg_actual_data(cls, start_date, end_date, areas, agg):

        if type(areas) == list:
            args_area = ', '.join([f"'{area}'" for area in areas])
        else:
            args_area = f"'{areas}'"

        # generate query
        sql_query = f"""
            SELECT
                zone_name
                , {agg}_timestamp AS time_stamp
                , SUM(sum_rtd_actual_load) AS actual_load
            FROM {DB_NAME}.agg_electricity_load_data_{agg}
            WHERE
                {agg}_timestamp >= "{start_date}"
                AND {agg}_timestamp <= "{end_date}"
                AND zone_name IN ({args_area})
            GROUP BY 1,2
        """

        res = pd.read_gbq(sql_query)

        return res