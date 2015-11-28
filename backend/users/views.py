import json
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from users.models import UserFacebookStuff
User = get_user_model()

import open_facebook

from django.views.generic.base import View
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from pubkeys.models import Pubkey

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

class profile(View):
    
    @login_required
    def get(self, request, *args, **kwargs):
        try:
            # TODO change when we want more keys per user
            pubkey = Pubkey.objects.get(user = request.user)
            return JsonResponse({'pubkey': pubkey.key)
        except ObjectDoesNotExist:
            return JsonResponse({}, status=404)
                    
    @login_required
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body.decode('utf-8'))
        try:
            # TODO change when we want more keys per user
            pubkey = Pubkey.objects.get(user = request.user)
            status = 204
        except ObjectDoesNotExist:
            pubkey = Pubkey(user=request.user)
            status = 201
        pubkey.key = data['pubkey']
        pubkey.save()
        return JsonResponse({}, status)


class friends(View):

    @login_required
    def get(self, request, *args, **kwargs):
        friends = request.user.get_friends()
        keys = []
        for friend in friends:
            try:
                pubkey = Pubkey.get_by_facebook_id(friend.id)
                keys.append({
                    'id': friend.id,
                    'key': pubkey.key,
                    'name': friend.name,
                })
            except ObjectDoesNotExist:
                pass
        return JsonRespinse(keys)
