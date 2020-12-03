from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html')
    # return HttpResponse('Home')

def Analyze(request):
    djtext=request.GET.get('text','default')
    removepunc=request.GET.get('removepunc','off')
    print(removepunc)
    if removepunc=="on":
        analyzed=""
        Punctuations='''!()-[]{}:;'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in Punctuations:
                analyzed=analyzed+char
        params={'purpose':'Removed Punctuation','analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    else :
        return HttpResponse('Error')
