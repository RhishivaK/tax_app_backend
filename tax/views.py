from datetime import datetime

from rest_framework import viewsets, generics

from tax.models import IncomeTaxPolicy, IncomeTaxRecord
from tax.serializers import (
    IncomeTaxRecordSerializer,
    IncomeTaxStatusSerializer,
    IncomeTaxPolicySerializer,
    IncomeTaxPolicyCreateSerializer
)
from utils import response


class IncomeTaxPolicyListAPIView(generics.ListAPIView):
    queryset = IncomeTaxPolicy.objects.all()
    serializer_class = IncomeTaxPolicySerializer
    page_size_query_param = 'limit'


class IncomeTaxListAPIView(generics.ListAPIView):
    queryset = IncomeTaxRecord.objects.all()
    serializer_class = IncomeTaxRecordSerializer
    page_size_query_param = 'limit'


class IncomeTaxUserListAPIView(generics.ListAPIView):
    serializer_class = IncomeTaxRecordSerializer
    page_size_query_param = 'limit'

    def get_queryset(self):
        return IncomeTaxRecord.objects.filter(
            user=self.kwargs['pk']
        ).order_by('-id')


class IncomeTaxPolicyViewset(viewsets.ViewSet):
    def create(self, request):
        serializer = IncomeTaxPolicyCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.success('income tax policy created', serializer.data)
        return response.bad_request(serializer.errors)


class IncomeTaxViewset(viewsets.ViewSet):
    def generate_record(self, request, pk):
        record = IncomeTaxRecord()
        record.save()
        return record

    def retrieve(self, request, pk):
        try:
            record = IncomeTaxRecord.objects.get(pk=pk)
        except IncomeTaxRecord.DoesNotExist:
            return response.not_found('record not found')
        return record

    def change_status(self, request, pk):
        try:
            record = IncomeTaxRecord.objects.get(pk=pk)
        except IncomeTaxRecord.DoesNotExist:
            return response.not_found('record not found')
        serializer = IncomeTaxStatusSerializer(data=request.data, instance=record)
        if serializer.is_valid():
            serializer.save()
            return response.success('status changed')

        return response.bad_request(serializer.errors)

