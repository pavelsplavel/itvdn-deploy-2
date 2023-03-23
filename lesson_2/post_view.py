from django.http import HttpResponse
from django.views.generic import TemplateView

class MyTemplateView(TemplateView):
    template_name ="post_page.html"

    def get_context_data(self, **kwargs):
       return{ "latest_question_list" : [
        {'id' : 1,
         'question_text' : 'How are you?'},
        {'id': 2,
         'question_text': 'How old are you?'},
        {'id': 3,
         'question_text': 'Where are you from?'},
        {'id': 4,
         'question_text': None},
    ]}

def post_page(request, number):
    if number == 1:
        return HttpResponse('Text for first')
    elif number == 2:
        return HttpResponse('Text for second')
    elif number == 3:
        return HttpResponse('Text for third')
    else:
        return HttpResponse("Other text")

