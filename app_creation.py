from flask import Flask
import boto3




app=Flask(__name__)

@app.route('/')

def index():
    files=dict()
    s3_resource=boto3.client("s3")
    objects=s3_resource.list_objects(Bucket="1525")['Contents']

    for dicts in objects:
        if dicts['Size']!=0:
            temp=dicts['Key'].split('/')
            files.update({temp[0]:temp[1]})
    return files

if __name__=='__main__':
    app.run()
