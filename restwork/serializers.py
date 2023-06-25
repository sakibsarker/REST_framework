from rest_framework.serializers import ModelSerializer,SerializerMethodField
from .models import Advocate,Company

    # def to_representation(self, instance):
    #     data = super().to_representation(instance)
    #     data.pop('id', None)  # Exclude the 'id' field from the representation
    #     return data


class CompanySerializer(ModelSerializer):
    empolyee_count=SerializerMethodField(read_only=True)
    class Meta:
        model=Company
        fields='__all__'
    def get_empolyee_count(self,obj):
        count=obj.advocate_set.count()
        return count
class AdvocateSerializer(ModelSerializer):
    company=CompanySerializer()
    class Meta:
        model = Advocate
        fields = ['username','bio','company']