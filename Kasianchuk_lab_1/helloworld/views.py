from django.http import HttpResponse
from datetime import datetime

def hello_world(request):
    now = datetime.now()
    response = f"Hello, World! I'm Svyatoslav Kasianchuk. Current time: {now.strftime('%Y-%m-%d %H:%M:%S')}"
    return HttpResponse(response)
