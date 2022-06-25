

from rest_framework import serializers


class UrlShortenerSerializer(serializers.Serializer):
    url = serializers.CharField(help_text="Long Url")

    def validate(self, attrs):
        # we can give specific validations
        return super().validate(attrs)


class UrlRedirectSerializer(serializers.Serializer):
    url = serializers.CharField(help_text="Short Url")

    def validate(self, attrs):
        # we can give specific validations
        return super().validate(attrs)
