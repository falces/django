from django.http import HttpResponse, JsonResponse


def index(request):
    return HttpResponse("Hello, world. You're at the dartify index.")

def test(request):
    return JsonResponse({"status": "ok", "message": "Everything is fine!"})