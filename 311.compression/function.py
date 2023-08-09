import datetime
import io
import os
import shutil
import uuid
import zlib
import boto3
import time

client = boto3.client('s3')

def parse_directory(directory):

    size = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            size += os.path.getsize(os.path.join(root, file))
    return size
def unique_name(name):
        name, extension = os.path.splitext(name)
        return '{name}.{random}.{extension}'.format(
                    name=name,
                    extension=extension,
                    random=str(uuid.uuid4()).split('-')[0]
                )
def download_directory(client, bucket, prefix, path):
    objects = client.list_objects_v2(Bucket=bucket, Prefix=prefix)
    for obj in objects['Contents']:
        file_name = obj['Key']
        path_to_file = os.path.dirname(file_name)
        os.makedirs(os.path.join(path, path_to_file), exist_ok=True)
        client.download_file(bucket, file_name, os.path.join(path, file_name))
def upload(client, bucket, file, filepath):
    key_name = unique_name(file)
    client.upload_file(filepath, bucket, key_name)
    return key_name
def handler(event,context):
    start = time.time()
    input_bucket = event.get('bucket').get('input')
    output_bucket = event.get('bucket').get('output')
    key = event.get('object').get('key')
    download_path = '/tmp/{}-{}'.format(key, uuid.uuid4())
    os.makedirs(download_path)

    s3_download_begin = datetime.datetime.now()
    
    download_directory(client, input_bucket, key, download_path)
    s3_download_stop = datetime.datetime.now()
    size = parse_directory(download_path)

    compress_begin = datetime.datetime.now()
    shutil.make_archive(os.path.join(download_path, key), 'zip', root_dir=download_path)
    compress_end = datetime.datetime.now()

    s3_upload_begin = datetime.datetime.now()
    archive_name = '{}.zip'.format(key)
    archive_size = os.path.getsize(os.path.join(download_path, archive_name))
    key_name = upload(client, output_bucket, archive_name, os.path.join(download_path, archive_name))
    s3_upload_stop = datetime.datetime.now()

    download_time = (s3_download_stop - s3_download_begin) / datetime.timedelta(microseconds=1)
    upload_time = (s3_upload_stop - s3_upload_begin) / datetime.timedelta(microseconds=1)
    process_time = (compress_end - compress_begin) / datetime.timedelta(microseconds=1)
    execution_time = time.time() - start
    return {
            'result': {
                'bucket': output_bucket,
                'key': key_name
            },
            'measurement': {
                'download_time': download_time,
                'download_size': size,
                'upload_time': upload_time,
                'upload_size': archive_size,
                'compute_time': process_time,
                'execution_time': execution_time
            }
        }
