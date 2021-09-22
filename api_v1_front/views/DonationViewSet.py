import datetime
from math import ceil

from django.urls import reverse
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from core_rc.models import (
    Donation,
)

from api_v1_front.serializer.DonationSerializer import DonationSerializer


class DonationViewSet(viewsets.ViewSet):
    def retrieve(self, request, pk):
        try:
            donation = Donation.objects\
                .select_related('player', 'gifter')\
                .prefetch_related('player__languages', 'player__info', 'player__languages__language')\
                .prefetch_related('gifter__languages', 'gifter__info', 'gifter__languages__language')\
                .get(id=pk)
        except:
            return Response(status=404)

        serializer = DonationSerializer(
            donation,
            context={'request': request}
        )
        return Response(serializer.data)

    def list(self, request):
        per_page = int(request.GET.get('per_page', 10))
        page = int(request.GET.get('page', 1))

        if page < 1:
            return Response(status=404)

        donation = Donation.objects\
            .select_related('player', 'gifter', 'discount')\
            .prefetch_related('player__languages', 'player__info', 'player__languages__language')\
            .prefetch_related('gifter__languages', 'gifter__info', 'gifter__languages__language')\
            .all()

        serializer = DonationSerializer(
            donation,
            context={'request': request},
            many=True
        )

        count_donation = Donation.objects.count()

        url = request.build_absolute_uri(reverse("donation-list"))
        count_page = ceil(count_donation / per_page)

        return Response({
            'current_page': page,
            'per_page': per_page,
            'links': {
                'prev_page': f'{url}?per_page={per_page}&page={page-1}' if page > 1 else None,
                'next_page': f'{url}?per_page={per_page}&page={page+1}' if page < count_page else None,
            },
            'list': serializer.data
        })


    @action(detail=False)
    def last(self, request):
        count = int(request.GET.get('count', 5))

        donation = Donation.objects.select_related('player').all()[:count]

        serializer = DonationSerializer(donation, many=True)
        return Response(serializer.data)
