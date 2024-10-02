from rest_framework.request import HttpRequest
from rest_framework.views import APIView
from rest_framework.response import Response

from api.log import MyLogger
from api.serializers import ProductSerializer
from website.models import Product

logger = MyLogger(name=__name__)()


class ProductsView(APIView):
    def get(self, _: HttpRequest):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)

        return Response(data=serializer.data, status=200)

    def post(self, request: HttpRequest):
        payload = request.POST
        product_name = payload.get("name")
        product_price = payload.get("price")

        product = Product(name=product_name, price=product_price)

        product.save()

        serializer = ProductSerializer(product)

        return Response(
            data={"error": False, "message": "", "data": serializer.data}, status=200
        )


class ProductView(APIView):
    def get(self, request: HttpRequest, product_id: int):
        product = Product.objects.filter(id=product_id).first()
        
        logger.info(f"Requesting Product {product_id} via {request.path}")

        if not product:
            logger.warning(f"Product {product_id} not found for {request.path}")

            return Response(
                data={"error": True, "message": "Product does not exist", "data": {}},
                status=404,
            )

        serializer = ProductSerializer(product)

        return Response(
            data={"error": False, "message": "", "data": serializer.data}, status=200
        )
