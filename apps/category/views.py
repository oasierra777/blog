from rest_framework import permissions
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.category.models import Category
from apps.category.serializers import CategorySerializer

class ListCategoriesView(APIView):
    
    def get(self, request, format=None):
        
        if Category.objects.all().exists():
            categories = Category.objects.all()

            result = []

            for category in categories:
                if not category.parent:
                    item = {}
                    item['id'] = category.id
                    item['name'] = category.name
                    item['thumbnail'] = category.thumbnail.url

                    item['sub_categories'] = []

                    for cat in categories:
                        sub_item = {}
                        if cat.parent and cat.parent.id == category.id:
                            sub_item['id'] = cat.id
                            sub_item['name'] = cat.name
                            sub_item['thumbnail'] = cat.thumbnail.url

                            item['sub_categories'].append(sub_item)

                    result.append(item)
                    
            return Response({'categories': result}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'La categoria no se encuentra'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)