from airflow import DAG
from airflow.operators.dummy  import DummyOperator
import pendulum




with DAG(dag_id="Dummy", start_date=pendulum.datetime(2021, 1, 1, tz="UTC"), catchup=False, schedule_interval=None, tags=["example"]) as dag:
    
    task_1 = DummyOperator(task_id='task_1', dag=dag)
    task_2 = DummyOperator(task_id='task_2', dag=dag)

    task_1 >> task_2