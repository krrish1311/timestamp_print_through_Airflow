from datetime import datetime,timedelta
from pytz import timezone
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
local_tz = timezone('Asia/Kolkata') 
default_args = {
    'owner': 'krrish',
    'start_date': local_tz.localize(datetime(2023,4,20,17,17)),
    'retries': 1,
    'retry_delay': timedelta(minutes=2),
}

with DAG(
    dag_id='time_stamp_dag',
    default_args=default_args,
    description='My third DAG',
    schedule_interval=timedelta(minutes=5),
) as dag:
     task1=BashOperator(
        task_id='task01',
        bash_command='date|cat>>/home/krrish/date_output.txt'
    )
task1
