from rest_framework import serializers

from tax.models import IncomeTaxPolicy, IncomeTaxRecord

class IncomeTaxPolicyCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncomeTaxPolicy
        fields = '__all__'
        # depth = 1

class IncomeTaxPolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = IncomeTaxPolicy
        fields = '__all__'
        depth = 1

class IncomeTaxRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncomeTaxRecord
        fields = '__all__'

class IncomeTaxStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncomeTaxRecord
        fields = ['status']

