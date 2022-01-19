
from flask import Flask, request, json
from RFW_Response import RFW_response

app = Flask(__name__)
app.secret_key = 'hello'

@app.route('/get_batches', methods=['GET'])
def get_batches():

    id = request.json['id']
    bench_type = request.json['bench_type']
    metric = request.json['metric']
    batch_unit = request.json['batch_unit']
    batch_id = request.json['batch_id']
    batch_size = request.json['batch_size']
    batch_object = RFW_response(id, bench_type, metric, batch_unit, batch_id, batch_size)
    result = batch_object.send_json_data_results()

    if result is not None:
        json_object = json.dumps(result)
        with open("Json_Data.json", "w") as outfile:
            outfile.write(json_object)
        return json_object



if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='0.0.0.0', debug=False, port=5000)
    # app.run(debug=True)