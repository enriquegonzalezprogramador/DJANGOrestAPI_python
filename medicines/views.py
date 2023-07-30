#from django.shortcuts import render

#from django.http import JsonResponse

from medicines.model import Medicine

from rest_framework.response import Response
from rest_framework.decorators import api_view

from medicines.serializers import MedicineSerializerResponse
from medicines.serializers import MedicineSerializerRequest

@api_view(['GET', 'POST'])
def medicines(request):

    if request.method == 'GET':
        medicines = Medicine.objects.all()
        serializer_medicines = MedicineSerializerResponse(medicines, many=True)

        return Response(serializer_medicines.data)
    else: 
        
        serializer_medicines = MedicineSerializerResponse(request.data)

        #serializer_medicines.create(
          #  request.data['name'],
        #    request.data['price'],
        #    request.data['laboratory_id']
       # )

        if serializer_medicines.is_valid():

            Medicine.objects.create(
                    name=request.data['name'],
                    price=request.data['price'],
                    laboratory_id=request.data['laboratory_id']
            )
        

        return Response(serializer_medicines.data)

@api_view(['GET', 'PUT', 'DELETE'])
def detail_medicine(request, pk):
    
    medicine = Medicine.objects.get(pk=pk)

    if request.method == 'GET':
       
        serializer = MedicineSerializerResponse(medicine)

    
    if request.method == 'PUT':

        serializer = MedicineSerializerRequest(request.data)

        if serializer.is_valid():

            medicine.name = request.data['name']
            medicine.price = request.price['price']

            medicine.save()

    return Response(serializer.data)        
        

    #JSON
    #medicines = Medicine.objects.all()
    
    #resultado = []
    #for medicine in medicines:
    #    m = {
    #        'id': medicine.id,
    #        'name': medicine.name,
    #        'price': medicine.price
     #   }
     #   resultado.append(m)

    #return JsonResponse({
    #    {
     #       'data': resultado,
    #        'code': 200,
    #        'message': 'ok'
   #     }
   # })
