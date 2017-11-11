#!/usr/bin/env python2

import boto
import boto.s3
import sys
import os

from boto.s3.key import Key

AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
conn = boto.connect_s3(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
bucket = conn.get_bucket('learning-model')

for file_name in os.listdir('logs'):
    upload_to_s3(bucket, 'logs'+file_name)

def upload_to_s3(bucket, file_to_be_sent):
    k = Key(bucket)
    k.key = file_to_be_sent
    k.set_contents_from_filename(file_to_be_sent)
