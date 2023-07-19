
import datetime
import os
import uuid
import boto3
import urllib.request

client = boto3.client('s3')

def unique_name(name):
    name, extension = os.path.splitext(name)
    return '{name}.{random}.{extension}'.format(
                    name=name,
                    extension=extension,
                    random=str(uuid.uuid4()).split('-')[0]
                )
def handler(event, context):
  
    output_bucket = event.get('bucket').get('output')
    url = event.get('object').get('url')
    name = os.path.basename(url)
    download_path = '/tmp/{}'.format(name)

    process_begin = datetime.datetime.now()
    urllib.request.urlretrieve(url, filename=download_path)
    size = os.path.getsize(download_path)
    process_end = datetime.datetime.now()

    upload_begin = datetime.datetime.now()
    key_name = unique_name(name)
    client.upload_file(download_path,output_bucket,key_name)
    upload_end = datetime.datetime.now()

    process_time = (process_end - process_begin) / datetime.timedelta(microseconds=1)
    upload_time = (upload_end - upload_begin) / datetime.timedelta(microseconds=1)
    return {
            'result': {
                'bucket': output_bucket,
                'url': url,
                'key': key_name
            },
            'measurement': {
                'download_time': 0,
                'download_size': 0,
                'upload_time': upload_time,
                'upload_size': size,
                'compute_time': process_time
            }
    }
