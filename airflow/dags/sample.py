from airflow import DAG
from datetime import datetime
from airflow.operators.empty import EmptyOperator

date = "{{ (execution_date + macros.timedelta(hours=33)).strftime('%Y-%m-%d') }}"

default_args = {
    'owner': 'hooniegit',
    'depends_on_past': True,
    'start_date': datetime(2023,12,31)
}

dag_name = "sample"
tags = ["sample", "dag"]

dag = DAG(
    dag_name,
	default_args=default_args,
	tags=tags,
	max_active_runs=1,
	schedule_interval="* * * * *")

start = EmptyOperator(
	task_id = 'start',
	dag=dag
)

finish = EmptyOperator(
	task_id = 'finish',
	dag = dag,
	trigger_rule='all_done'
)

start >> finish