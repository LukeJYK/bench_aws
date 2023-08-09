import datetime, io, json
import os
from squiggle import transform
import boto3
import uuid
import time
client = boto3.client('s3')
def unique_name(name):
    name, extension = os.path.splitext(name)
    return '{name}.{random}.{extension}'.format(
        name=name,
        extension=extension,
        random=str(uuid.uuid4()).split('-')[0]
    )
def upload_stream(client, bucket, file, data):
    key_name = unique_name(file)
    client.upload_fileobj(data, bucket, key_name)
    return key_name
def handler(event, context):
    start = time.time()
    input_bucket = event.get('bucket').get('input')
    output_bucket = event.get('bucket').get('output')
    key = event.get('object').get('key')
    download_path = '/tmp/{}'.format(key)

    download_begin = datetime.datetime.now()
    client.download_file(input_bucket, key, download_path)
    download_stop = datetime.datetime.now()
    data = open(download_path, "r").read()

    process_begin = datetime.datetime.now()
    result = transform(data)
    process_end = datetime.datetime.now()

    upload_begin = datetime.datetime.now()
    buf = io.BytesIO(json.dumps(result).encode())
    buf.seek(0)

    key_name = upload_stream(client, output_bucket, key, buf)
    upload_stop = datetime.datetime.now()
    buf.close()

    download_time = (download_stop - download_begin) / datetime.timedelta(microseconds=1)
    process_time = (process_end - process_begin) / datetime.timedelta(microseconds=1)
    exe = time.time() - start
    return {
            'result': {
                'bucket': output_bucket,
                'key': key_name
            },
            'measurement': {
                'download_time': download_time,
                'compute_time': process_time,
                'execution_time': exe
                }
    }
