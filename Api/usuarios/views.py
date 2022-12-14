from django.shortcuts import render
from rest_framework import viewsets, generics
from usuarios import serializers, models


class PacienteViewSet(generics.ListCreateAPIView):
    serializer_class = serializers.PacienteSerializer
    queryset = models.Paciente.objects.all()

class PacienteViewSetRetrieve(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.PacienteSerializer
    queryset = models.Paciente.objects.all()   


class FuncionarioViewSet(generics.ListCreateAPIView):
    serializer_class = serializers.FuncionarioSerializer
    queryset = models.Funcionarios.objects.all()

class FuncionarioViewSetRetrieve(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.FuncionarioSerializer
    queryset = models.Funcionarios.objects.all()   


class ConsultaAgendadaViewSet(generics.ListCreateAPIView):
    serializer_class = serializers.ConsultaAgendadaSerializer
    queryset = models.ConsultaAgendada.objects.all()


class FuncionarioViewSetRetrieve(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.ConsultaAgendadaSerializer
    queryset = models.ConsultaAgendada.objects.all()  

class MedicamentosViewSet(generics.ListCreateAPIView):
    serializer_class = serializers.MedicamentosSerializer
    queryset = models.Medicamentos.objects.all()


class MedicamentosRetrieveViewSet(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.MedicamentosSerializer
    queryset = models.Medicamentos.objects.all()

class LaboratoriosViewSet(generics.ListCreateAPIView):
    serializer_class = serializers.LaboratoriosSerializer
    queryset = models.Laboratorios.objects.all()
    

class LaboratoriosRetrieveViewSet(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.LaboratoriosSerializer
    queryset = models.Laboratorios.objects.all()