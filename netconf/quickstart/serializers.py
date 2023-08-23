from rest_framework import serializers

class myDataSerializer(serializers.Serializer):
   linkedin = serializers.CharField()
   github = serializers.CharField()
   my_website = serializers.CharField()
   medium = serializers.CharField()

class myNetconfSerializer(serializers.Serializer):
   capability = serializers.CharField()

class getNetconfSerializer(serializers.Serializer):
   data = serializers.JSONField()