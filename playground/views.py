import logging

import requests
from django.shortcuts import render
from rest_framework.views import APIView

logger = logging.getLogger(__name__)


class HelloView(APIView):
    def get(self, request):
        try:
            logger.info("Calling httpbin")
            response = requests.get("https://httpbin.org/delay/2")
            logger.info("Received the response")
            data = response.json()
            logger.info("Response data: %s", data)
        except request.ConectionError:
            logger.critical("httpbin is offline")
        return render(request, "hello.html", {"name": "Mosh"})
