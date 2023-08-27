import requests
from requests.auth import HTTPBasicAuth

basic = HTTPBasicAuth('airflow', 'airflow')
x = requests.get('http://localhost:8080/api/v1/dags', auth=basic)
print(x.text)