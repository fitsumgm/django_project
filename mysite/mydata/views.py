from django.http import HttpResponse, JsonResponse


def index(request):
    data = {
        "Name":"Fitsum",
        "Track":"Backend(Python)",
        "Message":"Hi mentor, I wish you could help me with re-grading my OOP assignment",
    }
    return JsonResponse(data)