from django.shortcuts import render
from django.http import HttpResponse

monthly_challenge = {
    "january":"Read atleast one 300+ pages book",
    "february":"Walk for atleast 20kms",
    "march":"Learn any new programming language",
    "april":"",
    "may": "",
    "june": "",
    "july": "",
    "august": "",
    "september": "",
    "october": "",
    "november": "",
    "december": "",

}
# Create your views here.
def monthly_challenges(request, month):
    challenge_text = monthly_challenge[month]
    return HttpResponse(challenge_text)