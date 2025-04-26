from django.shortcuts import render
from .forms import *
from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.core import serializers
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from .models import *
from .serializers import profileSerializer
import json
import pickle
import numpy as np
import pandas as pd
from sklearn.externals import joblib
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression


# Create your views here.

class ProfileView(viewsets.ModelViewSet):
    queryset = profile.objects.all()
    serializer_class = profileSerializer

def main_form(request):
    if request.method == "POST":
        form = MainForm(request.POST)
        if form.is_valid():
            main_form = form.save(commit=False)
        else:
            form = MainForm()