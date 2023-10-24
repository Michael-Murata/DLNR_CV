import boto3
import csv
from PIL import Image, ImageDraw, ImageFont
import io

def json(detect_objects):
    print(detect_objects)

def labels(detect_objects):
    for label in detect_objects['Labels']:
        print(label['Name'])

def bounding_box(detect_objects):
    image = Image.open(io.BytesIO(source_bytes))
    draw = ImageDraw.Draw(image)
    for label in detect_objects['Labels']:
        for instances in label['Instances']:
            if 'BoundingBox' in instances:
                box = instances['BoundingBox']
                left = image.width * box['Left']
                top = image.height * box['Top']
                width = image.width * box['Width']
                height = image.height * box['Height']
                points = ((left, top), (left + width, top), (left + width,
                                                             top + height),
                          (left, top + height), (left, top))
                draw.line(points, width = 5, fill = "#FF0000")
                shape = [(left - 2, top - 35), (width + 2 + left, top)]
                draw.rectangle(shape, fill = "#FF0000")
                font = ImageFont.truetype("arial.ttf", 30)
                draw.text((left + 10, top - 30), label['Name'], font =
                font, fill = "#000000")
    image.show()

if __name__ == "__main__":
    with open('test_1_accessKeys.csv', 'r') as file:
        next(file)
        reader = csv.reader(file)
        for line in reader:
            access_key_id = line[0]
            secret_access_key = line[1]
    client = boto3.client('rekognition', region_name='us-east-1', \
                          aws_access_key_id= \
                              access_key_id,
                          aws_secret_access_key=secret_access_key)
    photo = 'octopus_image.jpg'
    with open(photo, 'rb') as image_file:
        source_bytes = image_file.read()
    detect_objects = client.detect_labels(Image={'Bytes': source_bytes})
    # print(json(detect_objects))
    # print(labels(detect_objects))
    print(bounding_box(detect_objects))