# from django.db import models
# from django.conf import settings
#
#
# class Team(models.Model):
#     name = models.CharField(max_length=200, help_text='Enter a team name')
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
#
#     def __str__(self):
#         return self.name
#
#
# class Roster(models.Model):
#     team = models.OneToOneField('Team', on_delete=models.SET_NULL, null=True)
#     # player_1 = models.ForeignKey('Player', on_delete=models.SET_NULL, null=True)
#     # player_2 = models.ForeignKey('Player', on_delete=models.SET_NULL, null=True)
#     # player_3 = models.ForeignKey('Player', on_delete=models.SET_NULL, null=True)
#     # player_4 = models.ForeignKey('Player', on_delete=models.SET_NULL, null=True)
#     # player_5 = models.ForeignKey('Player', on_delete=models.SET_NULL, null=True)
#
#     def __str__(self):
#         return f"Roster#: {self.id}"
#
#
# class Player(models.Model):
#     full_name = models.CharField(max_length=200)
#     position = models.CharField(max_length=200)
#     rank = models.IntegerField()
#     batting_avg = models.FloatField()
#     slg = models.FloatField()
#     homeruns = models.IntegerField()
#     rbis = models.IntegerField()
#     obp = models.FloatField()
#     runs = models.IntegerField()
#     ab = models.IntegerField()
#     api_id = models.IntegerField()
#     batting_hand = models.CharField(max_length=200)
#     team = models.CharField(max_length=200)
#     roster = models.ForeignKey('Roster', on_delete=models.SET_NULL, null=True)
#
#     # first_name = models.CharField(max_length=200)
#     # last_name = models.CharField(max_length=200)
#     # nickname = models.CharField(max_length=200, null=True)
#     # position = models.CharField(max_length=200)
#     # age = models.IntegerField()
#     # height = models.IntegerField()
#     # weight = models.IntegerField()
#     # mlb_team = models.CharField(max_length=200, null=True)
#     # throwing_hand = models.CharField(max_length=200)
#     # batting_hand = models.CharField(max_length=200)
#     # birth_country = models.CharField(max_length=200)
#     # rating = models.IntegerField()
#     # roster = models.ForeignKey('Roster', on_delete=models.SET_NULL, null=True)
#
#     def __str__(self):
#         return f"{self.full_name}, {self.position}"