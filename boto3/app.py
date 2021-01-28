import json
from boto3.session import Session
from botocore.client import Config

session = Session()
config = Config(connect_timeout=10, read_timeout=310)
client = session.client('lambda', config=config)

lambda_payload = {
    'locustfile': 'locustfile_example.py',
    'host': 'https://69213ac33716.ngrok.io',
    'num_users': '1',
    'spawn_rate': 1,
    'run_time':'30s'
}

response = client.invoke(FunctionName='lambda_locust', Payload=json.dumps(lambda_payload))
k = json.loads(response['Payload'].read())

print(k) 