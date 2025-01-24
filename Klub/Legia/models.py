from django.db import models
import calendar

# Player, Team, Coach, Assistant, Game 
GAMES_SPOTS = (
    ('Wyjazd', 'Na wyjęździe'),
    ('Dom', "U siebie")
)

GAMES_TYPES = (
    ('Liga', 'Liga'),
    ('Puchar_Kraju', "Puchar Kraju"),
    ('CL', "Champions League"),
    ('EL', 'Europa League')
)

SPECIALIZATIONS = (
        ('BR_trener', 'Trener Bramkarzy'),
        ('O_trener', 'Trener Obrońców'),
        ('P_trener', 'Trener Pomocników'),
        ('N_trener', 'Trener Napastników'),
        ('Taktyk', 'Taktyk')
        ('Trener_motoryczny','Trener Motoryczny')
    )

POSITIONS = (
        ('BR', 'Bramkarz'),
        ('LO', 'Lewy Obrońca'),
        ('śO', 'Środkowy Obrońca'),
        ('PO', 'Prawy Obrońca'),
        ('LS', 'Lewy Skrzydłowy'),
        ('PS', 'Prawy Skrzydłowy'),
        ('OP', 'Ofensywny pomoPomocnikcnik'),
        ('DP', 'Defensywny Pomocnik'),
        ('ŚP', 'Środkowy Pomocnik'),
        ('N', 'Napastnik'),
        ('LN', 'Lewy Napastnik'),
        ('PN', 'Prawy Napastnik'),
)
TEAMS = (
    ('main', 'Wyjściowa 11')
    ('rez', 'Rezerwa')
)

PLEC = (
    ('K', 'Kobieta'),
    ('M', 'Mężczyzna'),
    ('I', 'Inne'),
)

class Team(models.Model):
    name = models.CharField(max_length=1, choices=TEAMS)

    def __str__(self):
        return f"{self.name}"
    
class Player(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    age = models.DateField()
    plec = models.CharField(max_length=1, choices=PLEC, null = True)
    position = models.CharField(max_length=1, choices=POSITIONS)
    number = models.PositiveBigIntegerField()
    signing_date = models.DateTimeField(auto_now_add=True)
    team = models.ForeignKey(Team, null=True, blank=True, on_delete=models.SET_NULL)


    def __str__(self):
        return f'{self.firstname} {self.lastname} ; {self.position}'
    

class Coach(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    age = models.DateField()
    plec = models.CharField(max_length=1, choices=PLEC, null = True)
    signing_date = models.DateTimeField(auto_now_add=True)
    team = models.ForeignKey(Team, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.firstname} {self.lastname}'

class Assistant(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    age = models.DateField()
    plec = models.CharField(max_length=1, choices=PLEC, null = True)
    signing_date = models.DateTimeField(auto_now_add=True)
    specialization = models.CharField(max_length=50)
    team = models.ForeignKey(Team, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.firstname} {self.lastname} ; specjalizacja = {self.specialization}'
    
class Games(models.Model):
    opponent = models.CharField(max_length=50)
    team = models.ForeignKey(Team, null=True, blank=True, on_delete=models.SET_NULL)
    game_spot = models.IntegerField(choices=GAMES_SPOTS.choices)
    game_type = models.IntegerField(choices=GAMES_TYPES.choices)
    score = models.CharField(max_length=50)
    