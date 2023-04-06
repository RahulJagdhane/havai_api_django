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
