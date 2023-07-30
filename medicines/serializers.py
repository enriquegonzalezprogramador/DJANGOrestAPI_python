from rest_framework import serializers

from medicines.models import Medicine
from laboratories.models import Laboratory

class LaboratorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Laboratory
        fields = ['id', 'name']

class MedicineSerializerResponse(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    price = serializers.IntegerField()
    laboratory_id = serializers.IntegerField()

    Laboratory = LaboratorySerializer(read_only=True)

    def create(self, name, price, laboratory_id):
        return Medicine.objects.create(
            name=name,
            price=price,
            laboratory_id=laboratory_id
        )
    
class MedicineSerializerRequest(serializers.Serializer):
    name = serializers.CharField()
    price = serializers.IntegerField()