#!/usr/bin/env python2

import boto
import boto.s3
import sys
import os

from boto.s3.key import Key

def percent_cb(complete, total):
    sys.stdout.write('.')
    sys.stdout.flush()


def upload_to_s3(bucket, file_to_be_sent):
    k = Key(bucket)
    k.key = file_to_be_sent
    k.set_contents_from_filename(file_to_be_sent cb=percent_cb, num_cb=10)


try:
    AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
    AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
except KeyError:
    from secret import *

conn = boto.connect_s3(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
bucket = conn.get_bucket('learning-model')


for folder_name in os.listdir('logs'):
    for file_name in os.listdir('logs/'+folder_name):
        upload_to_s3(bucket, 'logs/'+folder_name+'/'+file_name)