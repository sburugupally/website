from django.shortcuts import render
from django.views import View
from  django.http import HttpResponse,JsonResponse
from .models import Post

# Create your views here.
class webpage(View):
    def get(self,request):

        return render(request,'base.html' )

class PostData(View):
    def post(self,request):
        try:
            print('working')
            name=request.POST.get('name')
            email_id=request.POST.get('emailId')
            country=request.POST.get('country')
            data_object = Post.objects.create(name=name, email=email_id, nationality=country)
            data_object.save()
            return JsonResponse({'success':True, 'message':"**Subscribed Successfully**"})
        except Exception as e:
            print(e)
            return JsonResponse({'success': False, 'message': "**Subscribed Unsuccessfully**"})

