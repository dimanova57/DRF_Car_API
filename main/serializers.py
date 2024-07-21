from rest_framework import serializers
from .models import Car
from rest_framework.validators import UniqueValidator

class CarSerializer(serializers.Serializer):
    model = serializers.CharField(max_length=200, validators=[UniqueValidator(queryset=Car.objects.all())])
    year = serializers.IntegerField()

    def validate_year(self, value):
        if not (1884 < value < 2025):
            raise serializers.ValidationError("Year must be possible, because first"
                                              " car was invented in 1885 and now is 2024")
        return value

    def create(self, validated_data):
        return Car.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.model = validated_data.get('model', instance.model)
        instance.year = validated_data.get('year', instance.year)
        instance.save()
        return instance