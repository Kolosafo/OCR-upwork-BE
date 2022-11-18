from rest_framework.decorators import api_view
from rest_framework.response import Response


import pytesseract
from django.conf import settings
from PIL import Image
import io

# Create your views here.


@api_view(['POST'])
def main(request, id=None):

    image_data = request.data['image']

    read_bytes = io.BytesIO(image_data.read())
    open_img = Image.open(read_bytes)
    preds = pytesseract.image_to_string(open_img)
    predictions = [x for x in preds.split("\n").strip()]

    # print("JUST THE IMAGE", preds)

    # media_root = settings.MEDIA_ROOT

    if not id:
        extracted = {'id': 'No ID', 'text': predictions}
    else:
        extracted = {'id': id, 'text': predictions}
    # match_img = (os.path.exists(media_root + "\\" + str(image)))


    return Response(extracted)
