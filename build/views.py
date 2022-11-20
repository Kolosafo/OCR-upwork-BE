from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import exceptions
from os import environ as env
from dotenv import load_dotenv

import pytesseract
from PIL import Image
import io


# Create your views here.


# LOADING ENVIRONMENT VARIABLE
load_dotenv()


@api_view(['POST'])
def main(request):
    auth_key = env['APP_AUTH_TOKEN']
    if not request.data['api_key'] == auth_key:
        raise exceptions.AuthenticationFailed("INCORRECT API KEY")

    image_data = request.data['image']

    print("READING BYTES", read_bytes)
    read_bytes = io.BytesIO(image_data.read())
    open_img = Image.open(read_bytes)
    preds = pytesseract.image_to_string(open_img)
    predictions = [x for x in preds.split("\n")]

    try:
        id = request.data['id']
        extracted = {'id': id, 'text': predictions}
    except Exception as E:
        # No ID return
        extracted = {'id': 'null', 'text': predictions}

    return Response(extracted)
