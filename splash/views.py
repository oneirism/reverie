from django.shortcuts import render

# Create your views here.
def index(request):

    context = {
        "complete": [
            "Multi-Factor Authentication",
            "User Authentication",
            "User Registration",
            "Campaign Ownership",
            "Character Ownership",
            "Splash",
        ],
        "in_progress": [
            "Character Tracking",
            "Faction Tracking",
            "Location Tracking",
            "Deployment Pipeline",
        ],
        "backlog": [
            "Campaign Log",
            "Cross Referencing",
            "Markdown Entries",
            "Search Functionality",
            "Secret Information",
        ],
    }

    # TODO: Make this more readable.
    context["max"] = len(context["complete"]) + len(context["in_progress"]) + len(context["backlog"])

    return render(request, "splash/index.html", context)
