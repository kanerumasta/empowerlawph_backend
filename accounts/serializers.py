# serializers.py
from djoser.serializers import UserCreateSerializer,UserSerializer
from accounts.models import User

class UserCreateSerializer(UserCreateSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'first_name', 'last_name', 'occupation', 'company')

    def create(self, validated_data):
        occupation = validated_data.pop('occupation', None)
        company = validated_data.pop('company', None)

        user = super().create(validated_data)
        user.occupation = occupation
        user.company = company
        user.save()

        return user

class UserSerializer(UserSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'first_name', 'last_name', 'occupation', 'company')
