from datetime import datetime

from rest_framework import viewsets, generics

from tax.models import CorporateTaxPolicy, CorporateTaxRecord
from tax.serializers import (
    CorporateTaxRecordSerializer,
    CorporateTaxStatusSerializer,
    CorporateTaxPolicySerializer,
    CorporateTaxPolicyCreateSerializer
)
from utils import response


class CorporateTaxPolicyListAPIView(generics.ListAPIView):
    queryset = CorporateTaxPolicy.objects.all()
    serializer_class = CorporateTaxPolicySerializer
    page_size_query_param = 'limit'


class CorporateTaxListAPIView(generics.ListAPIView):
    queryset = CorporateTaxRecord.objects.all()
    serializer_class = CorporateTaxRecordSerializer
    page_size_query_param = 'limit'


class CorporateTaxUserListAPIView(generics.ListAPIView):
    serializer_class = CorporateTaxRecordSerializer
    page_size_query_param = 'limit'

    def get_queryset(self):
        return CorporateTaxRecord.objects.filter(
            user=self.kwargs['pk']
        ).order_by('-id')


class CorporateTaxPolicyViewset(viewsets.ViewSet):
    def create(self, request):
        serializer = CorporateTaxPolicyCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.success('corporate tax policy created', serializer.data)
        return response.bad_request(serializer.errors)


class CorporateTaxViewset(viewsets.ViewSet):
    def generate_record(self, request, pk):
        record = CorporateTaxRecord()
        record.save()
        return record

    def retrieve(self, request, pk):
        try:
            record = CorporateTaxRecord.objects.get(pk=pk)
        except CorporateTaxRecord.DoesNotExist:
            return response.not_found('record not found')
        return record

    def change_status(self, request, pk):
        try:
            record = CorporateTaxRecord.objects.get(pk=pk)
        except CorporateTaxRecord.DoesNotExist:
            return response.not_found('record not found')
        serializer = CorporateTaxStatusSerializer(data=request.data, instance=record)
        if serializer.is_valid():
            serializer.save()
            return response.success('status changed')

        return response.bad_request(serializer.errors)



