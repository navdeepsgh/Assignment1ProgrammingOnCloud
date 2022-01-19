from flask import Flask, request
from RFW_Response import RFW_response
import protoformat_pb2


app = Flask(__name__)


@app.route('/get_batches', methods=['GET'])
def get_batches():
    batch_request_data = protoformat_pb2.Request.FromString(request.data)
    batch_response = protoformat_pb2.Data_Response()
    batch_object = RFW_response(batch_request_data.RFW_ID, batch_request_data.benchmark_type, batch_request_data.work_metric,
                                 batch_request_data.batch_unit, batch_request_data.batch_ID, batch_request_data.batch_size)
    result = batch_object.binary_data_result()
    batch_response.RFW_ID = result['rfw_id']
    batch_response.last_batch_ID = result['last_batch_id']
    batches = result['batches']
    print(batches)
    for batch in batches:
        proto_batch = protoformat_pb2.batches()
        samples_array = []
        for i in range(0, len(batch)):
            samples_array.append(batch[list(batch.keys())[i]])
        proto_batch.samples[:] = samples_array
        batch_response.batches.append(proto_batch)

    print(batch_response)

    if batch_response is not None and batch_response.last_batch_ID is not None:
        searlized_batch_res = batch_response.SerializeToString()
        return searlized_batch_res


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False, port=5000)