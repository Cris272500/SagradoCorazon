from django.db import models

# Create your models here.
class Paciente(models.Model):
    cedula = models.CharField(max_length=20, primary_key=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    password = models.CharField(max_length=128)
    fecha_nacimiento = models.DateField()
    genero = models.CharField(max_length=10, choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino')], null=True)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"

class Alergia(models.Model):
    codigo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class PacienteAlergia(models.Model):
    cedula = models.ForeignKey(Paciente, on_delete=models.CASCADE) # FK a Paciente
    codigo = models.ForeignKey(Alergia, on_delete=models.CASCADE) # FK a Alergia

    class Meta:
        unique_together = ('cedula', 'codigo')

    def __str__(self):
        return f"{self.cedula} - {self.codigo}"

class Medico(models.Model):
    id_medico = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    genero = models.CharField(max_length=10, choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino')])
    telefono = models.CharField(max_length=15, blank=True, null=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"

class Especialidad(models.Model):
    id_especialidad = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class MedicoEspecialidad(models.Model):
    id_medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    id_especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('id_medico', 'id_especialidad')

    def __str__(self):
        return f"{self.id_medico} - {self.id_especialidad}"

class Cita(models.Model):
    id_cita = models.AutoField(primary_key=True)
    id_paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    id_medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    id_especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()

    def __str__(self):
        return f"{self.id_paciente} - {self.id_medico} - {self.fecha} - {self.hora}"
    
class Enfermedad(models.Model):
    id_enfermedad = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class Registro(models.Model):
    id_registro = models.AutoField(primary_key=True)
    motivo = models.TextField()
    observaciones = models.TextField()
    id_cita = models.ForeignKey(Cita, on_delete=models.CASCADE)
    id_enfermedad = models.ForeignKey(Enfermedad, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id_registro} - {self.id_enfermedad}"

class Tratamiento(models.Model):
    id_tratamiento = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class TratamientoEnfermedad(models.Model):
    id_tratamiento = models.ForeignKey(Tratamiento, on_delete=models.CASCADE)
    id_enfermedad = models.ForeignKey(Enfermedad, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('id_tratamiento', 'id_enfermedad')

    def __str__(self):
        return f"{self.id_tratamiento} - {self.id_enfermedad}"

class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    marca = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class RegistroProducto(models.Model):
    id_registro = models.ForeignKey(Registro, on_delete=models.CASCADE)
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('id_registro', 'id_producto')

    def __str__(self):
        return f"{self.id_registro} - {self.id_producto}"