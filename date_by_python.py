from datetime import datetime,timedelta
from pytz import timezone
from airflow import DAG
from airflow.operators.python import PythonOperator
import subprocess
local_tz = timezone('Asia/Kolkata') 
def write_date():
    file=open('/home/krrish/py_date.txt','a+')
    file.write(subprocess.getoutput('date')+'\n')
    file.close()
default_args = {
    'owner': 'krrish',
    'start_date': local_tz.localize(datetime(2023,4,20,17,27)),
    'retries': 1,
    'retry_delay': timedelta(minutes=2),
}

with DAG(
    dag_id='time_by_py',
    default_args=default_args,
    description='My third DAG',
    schedule_interval=timedelta(minutes=5),
) as dag:
     task1=PythonOperator(
        task_id='task01',
        python_callable=write_date
    )
task1
