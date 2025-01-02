from rest_framework import serializers
from .models import User, Ticket, Dispute


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'firstname', 'lastname', 'username', 'password', 'mobile_number', 'role']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        user = User(
            firstname=validated_data['firstname'],
            lastname=validated_data['lastname'],
            username=validated_data['username'],
            mobile_number=validated_data['mobile_number'],
            role=validated_data['role']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

class TicketSerializer(serializers.ModelSerializer):
    description = serializers.SerializerMethodField()

    class Meta:
        model = Ticket
        fields = ['id', 'license_no', 'plate_number', 'user_id', 'violation_details', 'fine_amount', 'issued_by', 'status', 'created_at', 'due_date', 'description']

    def get_description(self, obj):
        return f"Ticket #{obj.id} {obj.status} - Fine: {obj.fine_amount}"

class DisputeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dispute
        fields = ['ticket', 'filed_by', 'reason', 'created_at']
