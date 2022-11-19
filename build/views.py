from rest_framework.decorators import api_view
from rest_framework.response import Response


import pytesseract
from PIL import Image
import io


# Create your views here.


@api_view(['POST'])
def main(request):

    image_data = request.data['image']

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
        pass

    return Response(extracted)
