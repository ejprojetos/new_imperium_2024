from rest_framework import serializers
from .models import Room


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['uuid', 'clinic', 'number', 'description']
        extra_kwargs = {
            'clinic': {'read_only': True}  # O ID da clínica será passado pela URL, não pelo corpo da requisição
        }

    def validate_number(self, value):
        clinic = self.context['clinic']
        room_id = self.instance.id if self.instance else None
        
        # Verifica se há outra sala com o mesmo número na clínica, ignorando a sala atual
        if Room.objects.filter(clinic=clinic, number=value).exclude(id=room_id).exists():
            raise serializers.ValidationError("A room with this number already exists in this clinic.")
        
        return value
