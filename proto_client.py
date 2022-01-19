import protoformat_pb2, requests

batch_request_data = protoformat_pb2.Request()

id = input('Enter Request For Workload (RFW) ID:')
bench_type = input('type one of the following:\n 1. DVD-testing\n 2. DVD-training\n 3. NDBench-training\n'
                   '4. NDBench-training\n')
metric = input('type one of the metrics from the following:\n'
               '1. CPUUtilization_Average\n 2. NetworkIn_Average\n 3. NetworkOut_Average\n'
               ' 4. MemoryUtilization_Average\n')
batch_id = int(input('Enter the Batch Id (from which batch you want the data to start from in integer: '))
batch_unit = int(input('Enter the number of samples you want in one batch in integer: '))
batch_size = int(input('Enter the number of batches to be returned in integer: '))

batch_request_data.RFW_ID = id
batch_request_data.benchmark_type = bench_type
batch_request_data.work_metric = metric
batch_request_data.batch_ID = batch_id
batch_request_data.batch_unit = batch_unit
batch_request_data.batch_size = batch_size

res = requests.get("http://10.10.154.110:5000/get_batches?", headers={'Content-Type': 'application/protobuf'},
                   data=batch_request_data.SerializeToString())

batch_response = protoformat_pb2.Data_Response.FromString(res.content)
file = open('Proto_DataLog', "wb")
file.write(res.content)
file.close()

print(batch_response)
