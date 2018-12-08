from django.shortcuts import render


# Create your views here.
def index(request):
    context = {
        "complete": [
            "Campaign Ownership",
            "Campaign Log",
            "Character Ownership",
            "Multi-Factor Authentication",
            "Splash",
            "User Authentication",
            "User Registration",
        ],
        "in_progress": [
            "Character Tracking",
            "Faction Tracking",
            "Location Tracking",
            "Deployment Pipeline",
        ],
        "backlog": [
            "Cross Referencing",
            "Markdown Entries",
            "Search Functionality",
            "Secret Information",
        ],
    }

    # TODO: Make this more readable.
    context["max"] = len(context["complete"]) + len(context["in_progress"]) + len(context["backlog"])

    return render(request, "splash/index.html", context)
