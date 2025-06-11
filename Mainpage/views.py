from rest_framework.decorators import api_view
from rest_framework.response import Response

from Papers.models import Paper
from Papers.serializers import PaperSerializer
# Create your views here.

@api_view(['GET'])
def Main_pages(request):
    last_edition = Paper.objects.latest('created')
    last_papers = Paper.objects.order_by('-created')[:4]
    most_read = Paper.objects.order_by('-views')[:5]

    response_data = {
        'last_edition': PaperSerializer(last_edition).data,
        'last_papers': PaperSerializer(last_papers, many=True).data,
        'most_read': PaperSerializer(most_read, many=True).data
    }

    return Response(response_data)

