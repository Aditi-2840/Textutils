# I have created this file- Aditi
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,'index.html')

def analyze(request):
    djtext=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    spaceremover=request.POST.get('spaceremover','off')
    newlineremover=request.POST.get('newlineremover','off')
    
    print(djtext)
    #analyzed=djtext
    
    if removepunc == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        params={'purpose':'Remove punctuations','analyzed_text':analyzed}
        djtext=analyzed
        

    if fullcaps=='on':
        # analyzed=djtext1
        analyzed=""
        for i in djtext:
            if i==" ":
                analyzed=analyzed+" "
            else:
                analyzed=analyzed+i.upper()
        params={'purpose':'Capital Letter First','analyzed_text':analyzed}
        djtext=analyzed
        
    
    if spaceremover == 'on':
        analyzed=djtext.replace(" ","")
        params={'purpose':'Space Remover','analyzed_text':analyzed}
        djtext=analyzed

    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char==' ':
                analyzed=analyzed+' '
            elif char != "\n" and char!="\r":
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        

    # if charcounter == 'on':
    #     count_char=0
    #     for char in djtext:
    #         if char==" ":
    #             continue
    #         else:
    #             count_char=count_char+1
    #     params={'purpose':'Character Counter','analyzed_text':djtext}
        
    #     djtext=analyzed
        
    # if wordcounter == 'on':
    #     count_word=1
    #     for char in djtext:
    #         if char==' ':
    #             count_word=count_word+1
    #     params={'purpose':'Word Counter','analyzed_text':djtext}
    #     djtext=analyzed
        
    if removepunc!='on' and fullcaps!='on' and spaceremover!='on' and newlineremover!='on':
        return HttpResponse("Error")

    return render(request,'analyze.html',params)
    
        
    

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')
