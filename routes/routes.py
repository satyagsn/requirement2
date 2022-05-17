from config import app,client
from flask import request

@app.route('/upload',methods=['POST'])
def upload_image():
    bucket='terraform13'
    content_type=request.mimetype
    obj=request.files['file']
    filename=obj.filename
    client.put_object(Body=obj,
          Bucket=bucket,
          Key=filename,
          ContentType=content_type
    )

    return {'message': 'file uploaded'}, 200