from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.conf import settings
import pathlib
from PIL import Image

from os import environ as env
from dotenv import load_dotenv


# LOADING ENVIRONMENT VARIABLE
load_dotenv()


# Create your tests here.
api_key = env['APP_AUTH_TOKEN']
url = reverse("main", kwargs={'api_key': api_key})
MEDIA_ROOT = pathlib.Path(settings.MEDIA_ROOT + "\\images")


class Development_Extraction_TestCase(APITestCase):
    def test_extraction(self):
        for image in MEDIA_ROOT.glob("*"):
            print("I DEY CHECK IMAGE", image)
            try:
                img_exists = Image.open(image)
            except:
                img_exists = None
            # open(image, 'rb')
            # print("media root ->", image)
            response = self.client.post(
                url, data={"image": open(image, 'rb'), "api_key": api_key})

        if img_exists is None:
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        else:
            # Returning a valid image
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            data = response.json()
            print("NO ID", data)

    def test_multiple_image_extractions(self):
        extractions = []
        content_type = 'text/html'
        for index, image in enumerate(MEDIA_ROOT.glob("*")):
            try:
                img_exists = Image.open(image)
            except:
                img_exists = None
            response = self.client.post(
                url, data={"image": open(image, 'rb'), "id": index, "api_key": api_key})
            extractions.append(response.json())
        # we need multiple images (more than 1)
        print("EXTRACTED", extractions)
        if img_exists is None or len(extractions) < 2:
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        else:
            # Returning a valid image
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            data = response.json()
