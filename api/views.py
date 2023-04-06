from django.shortcuts import render
from django.http import HttpResponse,JsonResponse


import openai

openai.api_key="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"

# Create your views here.
def getResponse(request, user_message):
    response = openai.Completion.create(
        engine = "text-davinci-003",
        prompt = user_message,
        max_tokens = 4000,
        n = 1,
        stop=None,
        temperature=0.5,
    )
    return JsonResponse({"response":response["choices"][0]["text"]})
