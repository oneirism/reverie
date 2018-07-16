from django.shortcuts import render

# Create your views here.
def index(request):

    context = {
        "complete": [
            "Multi-Factor Authentication",
            "User Authentication",
            "User Registration",
        ],
        "in_progress": [
            "Splash",
        ],
        "backlog": [
            "Campaign Ownership",
            "Campaign Log",
            "Character Ownership",
            "Character Tracking",
            "Cross Referencing",
            "Deployment Pipeline",
            "Faction Tracking",
            "Location Tracking",
            "Markdown Entries",
            "Search Functionality",
            "Secret Information",
        ],
    }

    # TODO: Make this more readable.
    context["max"] = len(context["complete"]) + len(context["in_progress"]) + len(context["backlog"])

    return render(request, "splash/index.html", context)
