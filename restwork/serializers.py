from rest_framework.serializers import ModelSerializer
from .models import Advocate

class AdvocateSerializer(ModelSerializer):
    class Meta:
        model = Advocate
        fields = '__all__'
    # def to_representation(self, instance):
    #     data = super().to_representation(instance)
    #     data.pop('id', None)  # Exclude the 'id' field from the representation
    #     return data