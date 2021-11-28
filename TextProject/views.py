

from django.http.response import HttpResponse
from django.shortcuts import HttpResponse, render

def home(request):
    return render(request,'Home.html')


def analyze(request):
    currText= request.POST.get('text','default')
    
    # Features
    remPunc= request.POST.get('removepunc','off')
    remSpc= request.POST.get('removespace','off')
    remLine= request.POST.get('removenewline','off')
    CapChar= request.POST.get('capchars','off')
   
    
    if remPunc== "on":
        finalText=""
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for ch in currText:
            if ch not in punctuations:
                finalText+=ch
        parameters={"analyzedText":finalText}
        currText=finalText

    if remSpc=="on":
        finalText=""
        for index, char in enumerate(currText):
            if not(currText[index] == " " and currText[index+1]==" "):
                finalText += char
        parameters={"analyzedText":finalText}
        currText=finalText

    
    if remLine=="on":
        finalText=""
        for char in currText:
            if char != "\n" and char!="\r":
                finalText+=char
        parameters={"analyzedText":finalText}
        currText=finalText

    if CapChar=="on":
        finalText=""
        for ch in currText:
            finalText+= ch.upper()
        parameters={"analyzedText":finalText}
        currText=finalText

    if(remLine !="on" and remPunc !="on" and remSpc !="on" and CapChar !="on"):
        return HttpResponse("<h1>please select any operation and try again</h1>")

    return render(request,'analyze.html',parameters)