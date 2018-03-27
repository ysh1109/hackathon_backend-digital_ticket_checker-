from rest_framework import serializers
from .models import *

class passenger_reservationSerializer(serializers.ModelSerializer):
    class Meta:
            model = passenger_reservation
            # fields = ('pnr', 'train_no', 'boarding_station', 'coach_no', 'se')
            fields = '__all__'
class TrainSerializer(serializers.ModelSerializer):
    class Meta:
            model = Train

            fields = '__all__'
