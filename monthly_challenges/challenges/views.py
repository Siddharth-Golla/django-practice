from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenge = {
    "january":"Read atleast one 300+ pages book",
    "february":"Walk for atleast 20kms",
    "march":"Learn any new programming language",
    "april":"april",
    "may": "may",
    "june": "june",
    "july": "july",
    "august": "august",
    "september": "september",
    "october": "october",
    "november": "november",
    "december": "december",
}
# Create your views here.
def monthly_challenges(request, month):
    try:
        challenge_text = monthly_challenge[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("Invalid Month")


def monthly_challenges_by_number(request, month):
    try:    
        months = list(monthly_challenge.keys())
        redirect_month = months[month - 1]
    except:
        return HttpResponseNotFound("Invalid Month")
    return HttpResponseRedirect(reverse("monthly-challenge", args=[redirect_month]))


# Same function without using redirect
# def monthly_challenges_by_number(request, month):
#     if not 1 <= month <= 12:
#         return HttpResponseNotFound("Invalid Month")
#     else:
#         challenge_text = list(monthly_challenge.values())[month - 1]
#         return HttpResponse(challenge_text)