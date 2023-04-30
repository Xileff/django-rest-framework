import json
from django.http import JsonResponse
from django.forms.models import model_to_dict
from products.models import Product

def api_home(request, *args, **kwargs):
    model_data = Product.objects.all().order_by("?").first() # get random product
    data = {}

    if model_data:
        data = model_to_dict(model_data, fields=['id', 'title', 'price']) # serialization
    return JsonResponse(data)

# last checkpoint : rest framework view & response

# def api_home(request, *args, **kwargs):
    # Request query params
    # print(request.GET)
    # print(request.POST)

    # # Request body
    # body = request.body # byte string of JSON data
    # data = {}
    # try:
    #     data = json.loads(body) # json -> python dict
    # except:
    #     pass

    # print(data)

    # # Build response
    # data['params'] = dict(request.GET)
    # data['headers'] = dict(request.headers)
    # data['content_type'] = request.content_type

    # # Return response
    # return JsonResponse(data)
