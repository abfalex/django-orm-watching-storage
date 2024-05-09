from datacenter.models import Visit
from django.shortcuts import render


def storage_information_view(request):
    visits = Visit.objects.filter(leaved_at__isnull=True)

    non_closed_visits = []

    for visit in visits:
        person_name = visit.passcard.owner_name
        duration = visit.format_duration(visit.get_duration())
        is_strange = visit.is_visit_long()

        non_closed_visits.append({
            'who_entered': person_name,
            'entered_at': visit.entered_at,
            'duration': duration,
            'is_strange': is_strange
        })

    context = {
        'non_closed_visits': non_closed_visits,
    }

    return render(request, 'storage_information.html', context)
