from django.db import models

# Create your models here.
# cria uma classe que herda de outra classe model do python


class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.city} ({self.code})'


class Flight(models.Model):
    # dentro de um modelo é necessário passar todos os parametros e propriedades que este modelo terá.
    # origin referenciando outra tabela (modelo) com o argumento on_delete.
    # isto é, uma restrição para quando a referência for deletada,
    # caso a tabela Airport, esse Flight também seja deletado.
    # related_name - criará dentro de Airport um atributo 'departures'.
    # sendo assim, agora a classe Airpot consegue saber todos as origens feitas por ela por cada Airport especifico.
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()

    def __str__(self):
        # função que faz uma representação de caracteres do objeto do model
        return f'{self.id}: {self.origin} to {self.destination}'