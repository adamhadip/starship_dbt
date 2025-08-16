"""

This dag for running dbt run and dbt build for localhost and fetch api

"""

import pendulum
import pandas as pd
from datetime import timedelta
from airflow.decorators import dag
from airflow.providers.standard.operators.bash import BashOperator
import logging

logging.basicConfig(level=logging.INFO)

@dag(
    default_args={
    "depend_on_past": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
    "owner": "localhost"
},
    # schedule_interval="@daily",
    start_date=pendulum.datetime(2025,1,20, tz="Asia/Jakarta"),
    doc_md=__doc__
)

def project_data_analytics():

    @task(task_id="fetch_data_api")
    
    dbt_run = BashOperator(
        task_id = 'dbt_running',
        bash_command='cd /Users/adamhadipratama/starship_dbt/ && dbt run'
    )

    hello_world >> dbt_run

project_data_analytics()

