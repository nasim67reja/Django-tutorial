from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.


monthly_challenges = {
    "january": "Eat no meat for the entire month",
    "february": "Read a book every week",
    "march": "Start a daily jogging routine",
    "april": "Learn a new programming language",
    "may": "Take a photo every day",
    "june": "Learn to play a musical instrument",
    "july": "Write a short story",
    "august": "Try a new recipe each week",
    "september": "Take an online course",
    "october": "Visit a new place every weekend",
    "november": "Practice meditation daily",
    "december": "Volunteer for a local charity",
}


def index(request):
    list_items = ""
    months = monthly_challenges.keys()

    for month in months:
        redirect_url = reverse('month_by_string', args=[month])
        list_items += f"<li><a href=\"{redirect_url}\">{
            month.capitalize()}</a></li>"

    response_data = f"<ul>{list_items}</ul>"

    return HttpResponse(response_data)


def month_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid Month!")

    redirect_month = months[month-1]
    redirect_url = reverse('month_by_string', args=[redirect_month])
    return HttpResponseRedirect(redirect_url)


def month(request, month):
    try:
        challenge_text = monthly_challenges[month]
        redirect_url = reverse("challenges_base_path")
        # response_data = render_to_string("challenges/challenge.html")
        # return HttpResponse(response_data)
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month.capitalize(),
        })
    except KeyError:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")


def january(request):
    print("request ", request)
    return HttpResponse("Eat no meat for the entire month")


def february(request):
    return HttpResponse("Walk for at least 20 minutes every day")
