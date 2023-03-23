from django.shortcuts import render
from django.http import FileResponse, HttpResponse, HttpResponseRedirect, HttpResponseNotAllowed, JsonResponse
from django.templatetags.static import static
from django.views import View
from django.template import loader

class MyView(View):

    def get(self, request):
        if request.GET.get('type') == 'text':
            return HttpResponse("TEXT")
        elif request.GET.get('type') == 'json':
            return JsonResponse({i: i + i for i in range(1, 20)}, safe = False)
        elif request.GET.get('type') == 'redirect':
            return HttpResponseRedirect("http://127.0.0.1:8000/admin/")
        else:
            return HttpResponse("Response not allowed")

    def post(self, request):
        print(request.POST)
        return HttpResponse("This is POST")

    def delete(self, request):
        print(request.POST)
        return HttpResponse("This is POST")

def main(request):
    # test_template = loader.get_template(template_name="templates_example.html")
    # select_template = loader.select_template(template_name_list=["test", "templates_example.html"])
    test_template = loader.render_to_string("templates_example.html", context={"str":"Test string",
                                                                               "int":12})
    print(test_template)
    # return render(request, 'templates_example.html')
    # return HttpResponse(test_template.render)
    # return HttpResponse(select_template.render())
    return HttpResponse(test_template)

def text(request):
    return HttpResponse("This is text from backend to user interface")

def file(request):
    print(static('img.jpg'))
    return FileResponse(open(static('img/img.jpg'), "rb+"))

def redirect(request):
    return HttpResponseRedirect("http://www.google.com")

def not_allowed(request):
    return HttpResponseNotAllowed("You shall not pass!")

def json(request):
    return JsonResponse({i: i + i for i in range(1, 20)}, safe = False)
