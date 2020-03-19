from django.db import models
from django.conf import settings


class Team(models.Model):
    name = models.CharField(max_length=200, help_text='Enter a team name')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    funds = models.IntegerField(default=1000)
    in_offers = models.IntegerField(default=0)
    out_offers = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Offer(models.Model):
    CHOICES = [
        ('A', 'Accepted'),
        ('P', 'Pending'),
        ('R', 'Rejected'),
    ]

    offer_status = models.CharField(choices=CHOICES, default='P', max_length=1)
    requesting_team = models.ForeignKey('Team', on_delete=models.CASCADE, related_name='requesting_team')
    deciding_team = models.ForeignKey('Team', on_delete=models.CASCADE, related_name='deciding_team', default=None)
    money_amount = models.IntegerField(default=0)
    trade_block_player = models.ForeignKey('Player', on_delete=models.CASCADE, related_name='trade_block_player')
    offering_players = models.ManyToManyField('Player', related_name='Offers', blank=True)

    def __str__(self):
        return f"Trading {self.trade_block_player.full_name} to {self.requesting_team.name}"


class Player(models.Model):
    full_name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    rank = models.IntegerField()
    batting_avg = models.FloatField()
    slg = models.FloatField()
    homeruns = models.IntegerField()
    rbis = models.IntegerField()
    obp = models.FloatField()
    runs = models.IntegerField()
    ab = models.IntegerField()
    api_id = models.IntegerField()
    batting_hand = models.CharField(max_length=200)
    mlb_team = models.CharField(max_length=200, default='Free Agent')
    team = models.ForeignKey('Team', on_delete=models.SET_NULL, null=True)
    price = models.IntegerField(default=0)
    on_trade_block = models.BooleanField(default=False)

    # first_name = models.CharField(max_length=200)
    # last_name = models.CharField(max_length=200)
    # nickname = models.CharField(max_length=200, null=True)
    # position = models.CharField(max_length=200)
    # age = models.IntegerField()
    # height = models.IntegerField()
    # weight = models.IntegerField()
    # mlb_team = models.CharField(max_length=200, null=True)
    # throwing_hand = models.CharField(max_length=200)
    # batting_hand = models.CharField(max_length=200)
    # birth_country = models.CharField(max_length=200)
    # rating = models.IntegerField()
    # roster = models.ForeignKey('Roster', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.full_name}, {self.position}"