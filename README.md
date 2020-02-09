# Image-compression-aws
This is an image compression project implemented on Amazon Web Services using python

This project is basically about compressed an image which is uploaded in s3.

This is done using Amazon simple storage service by uploading an image, as soon as image is uploaded an trigger is happened to lambda function which basically resizes the images and send back to bucket. 

In this project , Lambda execution roles is also created and a custom policy.

Its architecture is basically uploading an image in Amazon simple storage service, then an trigger happens which basically calls lambda function to compressed the size of image and transfer the image to the bucket.

This project requires the python2.7 coding standards along with Yaml file and json.

