import json
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from users.models import UserFacebookStuff
User = get_user_model()

import open_facebook


# Create your views here.
JsonResponse = lambda data, status=200: HttpResponse(
    json.dumps(data),
    status=status,
    content_type="application/json"
)
ErrorResponse = lambda msg: JsonResponse(msg, status=500)

def auth(request):
    # data = json.loads(request.body)
    data = json.loads( request.body.decode('utf-8') )

    try:
        uid = data["clientId"]
        token = data["code"]
    except KeyError:
        return ErrorResponse("clientId and code are required")

    try:
        # test token validity
        api = open_facebook.OpenFacebook(token)
        user = api.get('/me')
        assert user["id"] == uid
    except open_facebook.exceptions.OAuthException as e:
        return ErrorResponse(str(e))
    except AssertionError:
        ErrorResponse("Token doesn't match user")

    fbp = UserFacebookStuff.objects.filter(facebook_id=uid).first()

    if not fbp:
        fbp = UserFacebookStuff()
        user = User()
        fbp = UserFacebookStuff()
        fbp.facebook_id = uid
        user.save()
    fbp.access_token = token
    fbp.user = user
    fbp.save()

    return JsonResponse("Logged in")


