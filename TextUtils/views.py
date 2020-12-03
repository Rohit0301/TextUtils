from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'homepage.html')
    # return HttpResponse('Home')

def Analyze(request):
    #get the text
    djtext=request.GET.get('text','default')

    #checkboxes values
    removepunc=request.GET.get('removepunc','off')
    fullcaps=request.GET.get('fullcaps','off')
    newlineremover=request.GET.get('newlineremover','off')
    extraspaceremover=request.GET.get('extraspaceremover','off')
    charcounter=request.GET.get('charcounter','off')

    #check which checkbox is selected
    if removepunc=="on":
        analyzed=""
        Punctuations='''!()-[]{}:;'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in Punctuations:
                analyzed=analyzed+char
        params={'purpose':'Removed Punctuation','analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    elif fullcaps=="on":
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params={'purpose':'Changed to uppercase','analyzed_text':analyzed}
        return render(request,'analyze.html',params)

    elif newlineremover=="on":
        analyzed=""
        for char in djtext:
            if char!="\n":
                analyzed=analyzed+char
        params={'purpose':'Removed newLine','analyzed_text':analyzed}
        return render(request,'analyze.html',params)

    elif extraspaceremover=="on":
        analyzed=""
        for index,char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]==" "):
                analyzed=analyzed+djtext[index]
                
        params={'purpose':'Removed Extra space','analyzed_text':analyzed}
        return render(request,'analyze.html',params)

    elif charcounter=="on":
        counter=0;
        for char in djtext:
            counter=counter+1;
        analyzed="Total characters are {}".format(counter) 
                
        params={'purpose':'Characters Counted','analyzed_text':analyzed}
        return render(request,'analyze.html',params)

    else :
        return HttpResponse('Error')
