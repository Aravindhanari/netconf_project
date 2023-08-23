from rest_framework import serializers

class myNetconfSerializer(serializers.Serializer):
   capability = serializers.CharField()

class getNetconfSerializer(serializers.Serializer):
   data = serializers.JSONField()