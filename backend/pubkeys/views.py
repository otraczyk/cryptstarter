import json
from django.http import HttpResponse

# Create your views here.
JsonResponse = lambda data, status=200: HttpResponse(
    json.dumps(data),
    status=status,
    content_type="application/json"
)
