import boto3

s3 = boto3.resource('s3')

# Get list of objects for indexing
images=[('image1.jpeg','Mahesh'),
      ('image2.jpeg','Mahesh'),
      ('image3.jpeg','Shourya'),
      ('image4.jpeg','Shourya'),
      ('image5.jpeg','Samantha'),
      ('image6.jpeg','Samantha'),
      ('image7.jpeg','Varun'),
      ('image8.jpeg','Varun'),
      ('image9.jpeg','Saipallavi'),
      ('image10.jpeg','Saipallavi')
      ]

# Iterate through list to upload objects to S3   
for image in images:
    file = open(image[0],'rb')
    object = s3.Object('projectsmarthomesurvaillance-images','index/'+ image[0])
    ret = object.put(Body=file,
                    Metadata={'FullName':image[1]})
