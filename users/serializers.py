from rest_framework import serializers


from users.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=10, write_only=True)

    class Meta:
        model = User
        fields = ('email', 'password', 'name')

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            name=validated_data['name']
        )
        return user

