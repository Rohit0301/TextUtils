from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'homepage.html')
    # return HttpResponse('Home')

def Analyze(request):
    #get the text
    djtext=request.POST.get('text','default')

    #checkboxes values
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    charcounter=request.POST.get('charcounter','off')

    #check which checkbox is selected
    featues=0

    if removepunc=="on":
        featues=1
        analyzed=""
        Punctuations='''!()-[]{}:;'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in Punctuations:
                analyzed=analyzed+char
        params={'purpose':'Removed Punctuation','analyzed_text':analyzed}
        djtext=analyzed
        #return render(request,'analyze.html',params)

    if fullcaps=="on":
        featues=1
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params={'purpose':'Changed to uppercase','analyzed_text':analyzed}
        djtext=analyzed
        # return render(request,'analyze.html',params)

    if newlineremover=="on":
        featues=1
        analyzed=""
        for char in djtext:
            if char!="\n" and char!="\r":
                analyzed=analyzed+char
        params={'purpose':'Removed newLine','analyzed_text':analyzed}
        djtext=analyzed
        # return render(request,'analyze.html',params)

    if extraspaceremover=="on":
        featues=1
        analyzed=""
        for index,char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]==" "):
                analyzed=analyzed+djtext[index]
                
        params={'purpose':'Removed Extra space','analyzed_text':analyzed}
        djtext=analyzed
        # return render(request,'analyze.html',params)

    if charcounter=="on":
        featues=1
        counter=0;
        for char in djtext:
            counter=counter+1;
        analyzed="Total characters are {}".format(counter) 
                
        params={'purpose':'Characters Counted','analyzed_text':analyzed}
       
        # return render(request,'analyze.html',params)
    if featues==0:
        return HttpResponse('<h1><strong>Error!</strong> please select any operation</h1>')
    return render(request,'analyze.html',params)