from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
# from django.template.loader import render_to_string
from django.urls import reverse

DAYS_PLANS = {
    "saturday": "Sleep early, we have work tomorrow",
    "sunday": "Let's put the week's plan",
    "monday": "I need tasks from other team members",
    "tuesday": "We have team sync meeting",
    "wednesday": "Just small touches to finish my tasks",
    "thursday": "My work is done, let's deliver it",
    "friday": "Hooray! weekend is here",
}


def days_list(request):
    days = list(DAYS_PLANS.keys())
    return render(request, "days_plans/all_days.html", {"days": days})


def day_order(request, order):
    if order < 1 or order > 7:
        raise Http404("Invalid day!")
    days = list(DAYS_PLANS.keys())
    redirect_day = days[order - 1]
    return HttpResponseRedirect(reverse("plans-dynamic-name", args=[redirect_day]))


def day_name(request, name):
    plan = DAYS_PLANS.get(name, None)
    # if plan is not None:
    if plan:
        # content = render_to_string("days_plans/day_plan.html")
        # return HttpResponse(content)
        return render(
            request,
            "days_plans/day_plan.html",
            {"day": name, "plan": plan}
        )
    raise Http404("Invalid day!")


def saturday(request):
    return HttpResponse("Sleep early, we have work tomorrow")


def sunday(request):
    return HttpResponse("Let's put the week's plan")


def monday(request):
    return HttpResponse("I need tasks from other team members")


def tuesday(request):
    return HttpResponse("We have team sync meeting")


def wednesday(request):
    return HttpResponse("Just small touches to finish my tasks")


def thursday(request):
    return HttpResponse("My work is done, let's deliver it")


def friday(request):
    return HttpResponse("Hooray! weekend is here")
