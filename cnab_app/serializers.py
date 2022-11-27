from rest_framework import serializers

from cnab_app.models import Cnab


class FileSerializer(serializers.Serializer):
    file = serializers.FileField(write_only=True)


class CnabSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        file, _ = Cnab.objects.get_or_create(**validated_data)
        return file

    class Meta:
        model = Cnab
        fields = "__all__"
