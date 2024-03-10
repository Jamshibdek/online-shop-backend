from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "name", "slug", "price", "stock")
    def validate(self, data):
        title = data.get("name", None)
        slug =  data.get("slug", None)
        
        if not title == slug:
            raise ValidationError(
                {
                    "status":False,
                    "massage": "product nomi va slug bir hil bolishi kerak"
                }
            )
        if not title.isalpha():
            
            raise ValidationError(
                {
                    "status":False,
                    "massage": "Kitobni sarlavhasi va muolifi bir hil bolgan kitob yuklay olmaysz"
                }
            )
        return data