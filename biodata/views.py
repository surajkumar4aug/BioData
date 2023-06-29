from rest_framework import viewsets, response
from rest_framework.views import APIView
from .models import MarriageBiodata
from .serial import MarriageBiodataSerializer
from django.http import HttpResponse
from django.http import HttpResponseRedirect

class MarriageBiodataViewSet(viewsets.ModelViewSet):
    queryset = MarriageBiodata.objects.all()
    serializer_class = MarriageBiodataSerializer
    print(serializer_class)
from django.shortcuts import render

class MarriageBiodataAPIView(APIView):
    def post(self, request):
        print(request.POST.get('name'))
        serializer = MarriageBiodataSerializer(data=request.data)
        if serializer.is_valid():
            # Save the data or perform any other operations
            return render(request,'items.html',{"marriage_biodata":serializer.data})
        print(serializer.errors)
        return HttpResponseRedirect('/') 
def html_file_view(request):
    return render(request, 'biodataform.html')
