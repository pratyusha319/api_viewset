from django.shortcuts import render
from app.models import *
from rest_framework.response import Response
from app.serializers import *
from rest_framework.viewsets import ViewSet


class productjd(ViewSet):
    def list(self,request):
        PQS=Product.objects.all()
        PQD=Product_s(PQS,many=True)
        return Response(PQD.data)
    

    def create(self,request):
        pmsd=Product_s(data=request.data)
        if pmsd.is_valid():
            pmsd.save()
            return Response({'message':'product is created'})
       
        return Response({'message':'product creation is failed'})
    def retrieve(self,request,pk):
        po=Product.objects.get(pk=pk)
        pmsd=Product_s(po)
    
        return Response(pmsd.data)
      


    def update(self,request,pk):
     
        po=Product.objects.get(pk=pk)
        upo=Product_s(po,data=request.data)
      
        if upo.is_valid():
            upo.save()
            return Response({'message':'product is updated'})
       
        return Response({'message':'product updation is failed'})

    def partial_update(self, request,pk):
     
        po=Product.objects.get(pk=pk)
        upo=Product_s(po,data=request.data,partial=True)
      
        if upo.is_valid():
            upo.save()
            return Response({'message':'product is updated'})
       
        return Response({'message':'product updation is failed'})

        

    def destroy(self,request,pk):
        
        Product.objects.get(pk=pk).delete()
       
        return Response({'success': 'Product is deleted'})
