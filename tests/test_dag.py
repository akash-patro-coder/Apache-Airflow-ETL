from airflow.models import DagBag

def test_dag_loaded():
    dagbag = DagBag()
    dag = dagbag.get_dag("market_etl")
    assert dag is not None