import datetime
import json
import os
from io import BytesIO
import boto3
# Using python image library for image compression
import PIL
from PIL import Image

def resized_image_url(resized_key, bucket, region):
    return "https://s3-{region}.amazonaws.com/{bucket}/{resized_key}".format(
        bucket=bucket, region=region, resized_key=resized_key
    )
