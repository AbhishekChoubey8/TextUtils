# i have created this view.py files.
from django.http import HttpResponse
from django.shortcuts import render

# def nav(request):
#     return HttpResponse('''<h1>Personal Navigator:</h1> <a href="https://filmyzilla.com.ag/">Filmyzilla</a> <br> 
#                         <a href="https://www.justwatch.com/in/movies">Justwatch</a><br>
# ''')

#pipeline

def index(request):
    return render(request, 'index.html')
    # return HttpResponse("Home")

def analyze(request):
     #get the text
    djtext = request.GET.get('text', 'default')

    #check checkbox values
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    newlineremover = request.GET.get('newlineremover','off')
    exspaceremover = request.GET.get('exspaceremover','off')
    #check which checkbox is on or off
    if removepunc == "on":

        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = " "
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed+char
        #analyze the text
        params ={'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}

        return render(request, 'analyze.html', params)
    
    elif(fullcaps=="on"):
        analyzed=" "
        for char in djtext:
            analyzed=analyzed + char.upper()

        params ={'purpose': 'changed to uppercase', 'analyzed_text': analyzed}

        return render(request, 'analyze.html', params)
    
    elif(newlineremover=="on"):
        analyzed=" "
        for char in djtext:
            if char !="\n":
                analyzed=analyzed + char

        params ={'purpose': 'remove new line', 'analyzed_text': analyzed}

        return render(request, 'analyze.html', params)

    elif(exspaceremover=="on"):
        analyzed=" "
        for index,char in enumerate(djtext):
            if not (djtext[index]==" " and djtext[index+1]==" "):
                analyzed=analyzed + char

        params ={'purpose': 'remove extra space', 'analyzed_text': analyzed}

        return render(request, 'analyze.html', params)


    else:
        return HttpResponse("Opps! Error")