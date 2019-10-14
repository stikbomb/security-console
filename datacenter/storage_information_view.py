from datacenter.models import Visit
from datacenter.models import get_duration
from datacenter.models import format_duration
from datacenter.models import is_visit_long
from django.shortcuts import render


def storage_information_view(request):
    non_closed_visits =[]

    visits = Visit.objects.filter(leaved_at=None)
    for visit in visits:
        duration = get_duration(visit)
        non_closed_visits.append(
            {
            "who_entered": visit.passcard,
            "entered_at": visit.entered_at,
            "duration": format_duration(duration),
            "is_strange": is_visit_long(duration)
            }
        )

    context = {
        "non_closed_visits": non_closed_visits
    }
    return render(request, 'storage_information.html', context)
