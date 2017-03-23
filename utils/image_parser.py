from PIL import Image
import numpy
import json


def image_parser(file_path, coefficient):
    image = Image.open(file_path)
    matrix = numpy.asarray(image.convert("L"))
    matrix = matrix.tolist()
    # matrix = map(
    #     lambda y: map(
    #         lambda x:  if x > coefficient else 0,
    #         y
    #     ),
    #     matrix
    # )
    json_representation = json.dumps(matrix)

    return json_representation

st = image_parser("../ex-images/img1.gif", 50)
arr = json.loads(st)
print(len(arr))



