from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .data_to_app import passenger_reservationSerializer, TrainSerializer
import json
import django
class passenger_list(APIView):

        def get(self, request):
            passengers = passenger_reservation.objects.all()
            serializer = passenger_reservationSerializer(passengers, many=True)
            return Response(serializer.data)

        def post(self, request):
            # print("Working")
            print("request.data is : ")
            print(request.data)

            if request.data is None or '':
                return Response("Null Request!")

            if isinstance(request.data, django.http.request.QueryDict):
                aa = request.data.dict()
                aa = list(aa.keys())[0]
                print("aa is "+str(aa))
                print("Type of aa is "+str(type(aa)))
                json_obj = json.loads(aa)
                print("Query Dict")
            else:
                json_obj = request.data
                print("Only Dict")
            req_keys=list(json_obj.keys())
            print("JSON OBJECT IS : ")
            print(json_obj)
            print("Request Keys are : ")
            print(req_keys)
            print("Request Values are : ")
            print(list(json_obj.values()))
            if req_keys[0] == "update_values":
                try:
                    pnrs_to_update = list(json_obj.values())
                    print("pnrs_to_update is : ")
                    print(pnrs_to_update)
                    p_n_r = passenger_reservation.objects.filter(pnr=pnrs_to_update[0])
                    print("pnrs_to_update[0] is : ")

                    for i in range(len(p_n_r)):
                        p_n_r[i].verification_status='V'
                        p_n_r[i].save()
                    return Response("Updated")
                except:
                    return Response("INVALID REQUEST")
            elif req_keys[0] == "update_multiple_pnrs":
                try:
                    mutiple_pnr_verification = list(json_obj.values())[0]
                    for i in range(len(mutiple_pnr_verification)):
                        p = passenger_reservation.objects.get(**mutiple_pnr_verification[i])
                        p.verification_status='V'
                        p.save()
                    return Response("Updated")
                except:
                    return Response("Invalid Request")

            elif req_keys[0] == "train_info":
                train_no = json_obj["train_info"]
                t_r = Train.objects.filter(train_no=train_no)
                #route = t_r.stopages_list.values()
                trains = TrainSerializer(t_r, many=True)
                return Response(trains.data)
                # seriealizer = TrainSerializer()
                # return Response(serializer.data)
            elif req_keys[0] == "mark_as_vacant":
                coach_and_seat = list(json_obj.values())
                if isinstance(coach_and_seat[0], str):
                    coach_and_seat = coach_and_seat[0].split(',')
                a = passenger_reservation.objects.get(coach_no=coach_and_seat[0], seat_no=coach_and_seat[1], train_no=coach_and_seat[2])
                a.verification_status='U'
                a.save()
                return Response("CHANGED!!")
            else:
                print("LAST CONDITION")
                try:
                    passengers = passenger_reservation.objects.filter(**json_obj)
                    print("passengers is ")
                    print(passengers)
                    serializer = passenger_reservationSerializer(passengers, many=True)
                    return Response(serializer.data)
                except:
                    return Response("Invalid Request!")
