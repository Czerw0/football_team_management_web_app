from django.db import models
import calendar
from django.core.exceptions import ValidationError


GAMES_SPOTS = (
    ('Na wyjeździe', 'Na wyjeździe'),
    ('U siebie', "U siebie")
)

GAMES_TYPES = (
    ('Liga', 'Liga'),
    ('Puchar Kraju', "Puchar Kraju"),
    ('Champions League', "Champions League"),
    ('Europa League', 'Europa League'),
    ('Spotkanie Towarzyskie', 'Spotkanie Towarzyskie'),
)

SPECIALIZATIONS = (
        ('Trener Bramkarzy', 'Trener Bramkarzy'),
        ('Trener Obrońców', 'Trener Obrońców'),
        ('Trener Pomocników', 'Trener Pomocników'),
        ('Trener Napastników', 'Trener Napastników'),
        ('Taktyk', 'Taktyk'),
        ('Trener Motoryczny', 'Trener Motoryczny'),
    )

POSITIONS = (
        ('BR', 'Bramkarz'),
        ('LO', 'Lewy Obrońca'),
        ('śO', 'Środkowy Obrońca'),
        ('PO', 'Prawy Obrońca'),
        ('LS', 'Lewy Skrzydłowy'),
        ('PS', 'Prawy Skrzydłowy'),
        ('OP', 'Ofensywny Pomocnik'),
        ('DP', 'Defensywny Pomocnik'),
        ('ŚP', 'Środkowy Pomocnik'),
        ('N', 'Napastnik'),
        ('LN', 'Lewy Napastnik'),
        ('PN', 'Prawy Napastnik'),
)
TEAMS = (
    ('Wyjściowa 11', 'Wyjściowa 11'),
    ('Rezerwa', 'Rezerwa'),
    ('Druga Drużyna', 'Druga Dużyna'),
    ('Akademia Juniorska', 'Akademia Juniorska')
)

PLEC = (
    ('K', 'Kobieta'),
    ('M', 'Mężczyzna'),
    ('I', 'Inne'),
)

class Team(models.Model):
    name = models.CharField(max_length=100, choices=TEAMS)
    capacity = models.PositiveBigIntegerField(null = True)  

    def __str__(self):
        return f"{self.name}"

    def current_player_count(self):
        """Zwraca aktualną liczbę zawodników w drużynie."""
        return self.player_set.count()


class Player(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    birth = models.DateField()
    plec = models.CharField(max_length=100, choices=PLEC, null=True)
    position = models.CharField(max_length=100, choices=POSITIONS)
    number = models.PositiveBigIntegerField()
    signing_date = models.DateTimeField(auto_now_add=True)
    team = models.ForeignKey(Team, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.firstname} {self.lastname} ; {self.position} ; {self.team}'

    class Meta:
        ordering = ['team','position']

    def save(self, *args, **kwargs):
        """Sprawdź, czy drużyna ma miejsce przed zapisaniem zawodnika."""
        if self.team:
            if self.team.current_player_count() >= self.team.capacity:
                raise ValidationError(f"Drużyna {self.team.name} osiągnęła maksymalną liczbę zawodników ({self.team.capacity}).")
        super().save(*args, **kwargs)
    

class Coach(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    birth = models.DateField()
    plec = models.CharField(max_length=100, choices=PLEC, null = True)
    signing_date = models.DateTimeField(auto_now_add=True)
    team = models.ForeignKey(Team, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.firstname} {self.lastname}'

class Assistant(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    birth = models.DateField()
    plec = models.CharField(max_length=100, choices=PLEC, null = True)
    signing_date = models.DateTimeField(auto_now_add=True)
    specialization = models.CharField(max_length=50, choices=SPECIALIZATIONS)
    team = models.ForeignKey(Team, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.firstname} {self.lastname} ; {self.specialization} ; {self.team}'
    
    class Meta:
        ordering = ['lastname']

class Game(models.Model):
    opponent = models.CharField(max_length=50)
    team = models.ForeignKey(Team, null=True, blank=True, on_delete=models.SET_NULL)
    game_spot = models.CharField(max_length=50, choices=GAMES_SPOTS, null = True)
    game_type = models.CharField(max_length=50, choices=GAMES_TYPES, null = True)
    date = models.DateField()
    score_legia = models.CharField(max_length=50,null = True)
    score_opponent = models.CharField(max_length=50,null = True)

    def __str__(self):
        return f'Legia Warszawa     {self.score_legia} - {self.score_opponent}     {self.opponent} ; {self.date}'
    
    class Meta:
        ordering = ['date']