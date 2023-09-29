from django.db import models

# Create your models here.

class Club(models.Model):
    nom = models.CharField(max_length=50)
    logo = models.FileField(upload_to='uploads/')
    davlat = models.CharField(max_length=50)
    prezident = models.CharField(max_length=50, blank=True, null=True)
    murabbiy = models.CharField(max_length=50, blank=True, null=True)
    yil = models.DateField()
    qimmatt_tr = models.CharField(max_length=50, blank=True, null=True)
    qimmat_sotuv = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.nom
class Player(models.Model):
    ism = models.CharField(max_length=50)
    pozitsiya = models.CharField(max_length=50)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    narx = models.CharField(max_length=50)
    davlat = models.CharField(max_length=50)
    t_yil = models.DateField()

    def __str__(self):
        return self.ism

class Mavsum(models.Model):
    h_mavsum = models.PositiveIntegerField()

    def __str__(self):
        return str(self.h_mavsum)

class Transfer(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    eski = models.ForeignKey(Club, on_delete=models.CASCADE, related_name="eski_narx")
    yangi = models.ForeignKey(Club, on_delete=models.CASCADE)
    narx = models.CharField(max_length=50)
    tah_narx = models.CharField(max_length=50)
    mavsum = models.ForeignKey(Mavsum, on_delete=models.CASCADE)

    def __str__(self):
        return self.player.ism




