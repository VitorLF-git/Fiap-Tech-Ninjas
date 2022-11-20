from rest_framework import serializers
from usuarios import models

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Paciente
        fields = "__all__"

class FuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Funcionarios
        fields = "__all__"

class ConsultaAgendadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ConsultaAgendada
        fields = "__all__"

class MedicamentosSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Medicamentos
        fields = "__all__" 

class LaboratoriosSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Laboratorios
        fields = "__all__"