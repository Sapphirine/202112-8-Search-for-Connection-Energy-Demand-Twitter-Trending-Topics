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
    def get_agg_daily(cls, start_date, end_date, areas):
        sql_query = f"""
            SELECT
                zone_name
                , daily_timestamp AS time_stamp
                , SUM(sum_rtd_actual_load) AS actual_load
            FROM {DB_NAME}.agg_electricity_load_data_daily 
            WHERE
                daily_timestamp >= "{start_date}"
                AND daily_timestamp <= "{end_date}"
                AND zone_name IN ({', '.join([f"'{i}'" for i in areas])})
            GROUP BY 1,2
        """

        res = pd.read_gbq(sql_query)

        return res

    @classmethod
    def get_agg_hourly(cls, start_date, end_date, areas):
        sql_query = f"""
            SELECT
                zone_name
                , hour_timestamp AS time_stamp
                , SUM(sum_rtd_actual_load) AS actual_load
            FROM {DB_NAME}.agg_electricity_load_data_hourly 
            WHERE
                hour_timestamp >= "{start_date}"
                AND hour_timestamp <= "{end_date}"
                AND zone_name IN ({', '.join([f"'{i}'" for i in areas])})
            GROUP BY 1,2
        """

        res = pd.read_gbq(sql_query)

        return res