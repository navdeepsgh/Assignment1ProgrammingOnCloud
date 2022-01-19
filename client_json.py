import json

import requests


class Client(object):
    def __init__(self, d, bench_type, metric, batch_id, batch_unit, batch_size):
        self.d = d
        self.bench_type = bench_type
        self.metric = metric
        self.batch_id = batch_id
        self.batch_unit = batch_unit
        self.batch_size = batch_size


def serialize(Client):
    return {"id": Client.d,
            "bench_type": Client.bench_type,
            "metric": Client.metric,
            "batch_id": Client.batch_id,
            "batch_unit": Client.batch_unit,
            "batch_size": Client.batch_size}


d = input('Enter Request For Workload (RFW) ID:')
bench_type = input(
    'Enter one of the following:\n 1. DVD-testing\n 2. DVD-training\n 3. NDBench-training\n'
    '4. NDBench-training\n')
metric = input('choose one of the metrics from the following:\n'
               '1. CPUUtilization_Average\n 2. NetworkIn_Average\n 3. NetworkOut_Average\n'
               ' 4. MemoryUtilization_Average\n')
batch_id = input('Enter the Batch Id (from which batch you want the data to start from) in integer: ')
batch_unit = input('Enter the number of samples you want in one batch in integer: ')
batch_size = input('Enter the number of batches to be returned in integer: ')

req_data = Client(d, bench_type, metric, batch_id, batch_unit, batch_size)
json_req = json.dumps(req_data, default=serialize)
# response = requests.get("http://127.0.0.1:5000/get_batches?", json=serialize(req_data))
response = requests.get("http://10.10.154.110:5000/get_batches?", json=serialize(req_data))

if response.status_code == 200:
    print(" rfw_id: ", response.json()['rfw_id'])
    print(" last_batch_id: ", response.json()['last_batch_id'])
    print(" Samples Requested: ", response.json()['samples'])

    # json = {"id": req_data.d,
    #         "bench_type": req_data.bench_type,
    #         "metric": req_data.metric,
    #         "batch_id": req_data.batch_id,
    #         "batch_unit": req_data.batch_unit,
    #          "batch_size": req_data.batch_size}
