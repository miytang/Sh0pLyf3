def detail(request, userName_id):
    return HttpResponse("User: %s." % userName_id)

