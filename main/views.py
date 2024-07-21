from rest_framework.views import APIView, Response
from .models import Car
from .serializers import CarSerializer
from rest_framework import status


class GetAllCarsView(APIView):
    serializer_class = CarSerializer
    model = Car

    def find_car_by_model(self, car_model):
        return Car.objects.filter(model=car_model).first()

    def get(self, request, car_model=None) -> Response:

        if car_model:
            car = self.find_car_by_model(car_model)
            serializer = self.serializer_class(car)
            return Response(serializer.data)

        query_set = Car.objects.all()
        serializer_for_queryset = CarSerializer(instance=query_set, many=True)

        return Response(serializer_for_queryset.data)

    def post(self, request) -> Response:
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, car_model=None) -> Response:
        if car_model:
            car = self.find_car_by_model(car_model)
            serializer = self.serializer_class(instance=car, data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data, status=status.HTTP_201_CREATED)

            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(data={'car_model': ["car model is required"]})