from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class stopages_station(models.Model):
    station_code = models.CharField(max_length = 5,primary_key = True, default='')
    station_name = models.CharField(max_length = 30, default='')
    def __str__(self):
        return str(self.station_code)+' - '+str(self.station_name)
class Train(models.Model):
    train_no = models.IntegerField(primary_key = True)
    train_name = models.CharField(max_length=60, default='')
    route_origin_code = models.CharField(max_length=5, default='')
    route_destination_code = models.CharField(max_length=5, default='')
    region = models.CharField(max_length=3)
    no_of_stopages = models.IntegerField(default=2)
    stopages_list = models.ManyToManyField(stopages_station)
    def __str__(self):
        return str(self.train_no)+' - '+str(self.train_name)+' - '+str(self.route_origin_code)+' - '+str(self.route_destination_code)


class passenger_reservation(models.Model):
    pnr = models.BigIntegerField()
    train_no = models.ForeignKey(Train,on_delete= models.CASCADE, null=True)
    boarding_station = models.ForeignKey(stopages_station,on_delete = models.CASCADE, null=True, related_name='boarding_station')
    destination_station = models.ForeignKey(stopages_station, on_delete=models.CASCADE, null=True, related_name='upto_station')
    coach_no = models.CharField(max_length=4, default='')
    seat_no = models.CharField(max_length=6, default='')
    passenger_name = models.CharField(max_length=20)
    passenger_age = models.IntegerField(default='')
    gender_choices = (('M', "Male"), ('F', "Female"), ('O', "Others"))
    gender = models.CharField(max_length=1, choices=gender_choices, default="Male")
    contact_no = models.BigIntegerField()
    status_choices=(
    ('Available 01', 'Available_01'),
    ('Available 02', 'Available_02'),
    ('RAC 01', 'Reservation_against_cancellation_01'),
    ('RAC 02', 'Reservation_against_cancellation_02'),
    ('RAC 03', 'Reservation_against_cancellation_03'),
    ('RAC 04', 'Reservation_against_cancellation_04'),
    ('WL 01', 'Waiting_list_01'), ('WL 02', 'Waiting_list_02')
       )
    reservation_choices = (('P',"Pending"),('U',"Unallocated"),('V',"Verified"))
    ticket_status=models.CharField(max_length=15, choices=status_choices, default='Available_01', null=True)
    verification_status = models.CharField(max_length=1,choices=reservation_choices,default="Pending")

    def __str__(self):
        return str(self.passenger_name)+' - '+str(self.coach_no)+' - '+str(self.seat_no)+' - '+str(self.boarding_station)+' - '+str(self.train_no)

class TC_Info(models.Model):
    tc_id=models.CharField(max_length=15, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
