from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializer import *


class ReactView(generics.ListCreateAPIView):
    queryset = React.objects.all()
    serializer_class = ReactSerializer