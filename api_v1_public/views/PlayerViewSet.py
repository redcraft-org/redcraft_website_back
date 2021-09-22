import datetime
from math import ceil

from django.db.models import Prefetch
from django.urls import reverse
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from core_rc.models import (
    Player,
)

from api_v1_public.serializer.PlayerSerializer import PlayerSerializer


class PlayerViewSet(viewsets.ViewSet):
    def retrieve(self, request, pk):
        try:
            donation = Player.objects.prefetch_related('languages', 'info').get(id=pk)
        except:
            return Response(status=400)

        serializer = PlayerSerializer(
            donation,
            context={'request': request}
        )
        return Response(serializer.data)

    def list(self, request):
        per_page = int(request.GET.get('per_page', 10))
        page = int(request.GET.get('page', 1))

        if page < 1:
            return Response(status=404)

        start = (page - 1) * per_page
        stop = start + per_page

        donation = Player.objects\
            .prefetch_related('languages', 'info', 'languages', 'languages__language')\
            .all()

        serializer = PlayerSerializer(
            donation[start:stop],
            context={'request': request},
            many=True
        )

        count_player = Player.objects.count()

        url = request.build_absolute_uri(reverse("player-list"))
        count_page = ceil(count_player / per_page)

        return Response({
            'current_page': page,
            'per_page': per_page,
            'links': {
                'prev_page': f'{url}?per_page={per_page}&page={page-1}' if page > 1 else None,
                'next_page': f'{url}?per_page={per_page}&page={page+1}' if page < count_page else None,
            },
            'list': serializer.data
        })
