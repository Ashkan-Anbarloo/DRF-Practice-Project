from rest_framework import serializers
from .models import VipUser
import re

# class VipUserSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     username = serializers.CharField(max_length=120)
#     email = serializers.CharField(max_length=120)
#     age = serializers.IntegerField()
#     phone = serializers.CharField(max_length=11)
# #در این تابع میتوانیم خروجی رو تعیین کنیم و حتی میتونیم نکات مهم و حتی امنیتی در این قسمت بررسی کنیم مثل تعدا حروف و ارقام و ...
#     # def to_internal_value(self, data):
#     #     return {
#     #         'username':data.get('username').title(),
#     #     }
#     def to_internal_value(self, data):
#         validated = super().to_internal_value(data)
#         validated['username'] = validated['username'].title()
#         return validated
    
#     def to_representation(self, instance):
#         return {
#             'id' : instance.id,
#             'username' : instance.username,
#             'email': instance.email,
#             'age': instance.age,
#             'phone': instance.phone,
#         }

#     def create(self , validated_data):
#         return VipUser.objects.create(**validated_data)
    
#     def validate_phone(self , phone):
#         pattern = r"^09\d{9}$"
#         if not re.match(pattern , phone):
#             raise serializers.ValidationError('phone number is not OK :( ')
#         return phone
    
#     def validate(self, data):
#         if data.get('age') < 18 :
#             raise serializers.ValidationError('Age must be grater than 18') 
#         return data


# def age_vali(value):
#     if value['age'] < 18:
#         raise serializers.ValidationError({'age':'سن باید بیشتر از 18 باشد.'})


class MyValidator:
    def __call__(self, data):
        age = data.get("age")
        if age < 18:
            raise serializers.ValidationError({'age':'سن باید بیشتر از 18 باشد.'})

class VipUserSerializer(serializers.ModelSerializer):
    full_age = serializers.SerializerMethodField()
    # age = serializers.IntegerField(validators=[MyValidator()])
    class Meta:
        model = VipUser
        fields = '__all__' 
        validators = [
            # age_vali
            MyValidator()
        ]

    def get_full_age(self ,obj):
        return f'{obj.username} {obj.age}'
