from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Item
from .serializers import ItemSerializer

# 1. 內部GET請求
@api_view(['GET'])
def internal_get(request):
    return Response({"message": "內部GET請求成功"})

# 2. 外部GET請求(與內部GET相同，但通過port-forwarding訪問)
@api_view(['GET'])
def external_get(request):
    return Response({"message": "外部GET請求成功"})

# 3&4. 完整的CRUD操作視圖集
class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer