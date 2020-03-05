from django.db import models


class Voter(models.Model):
    tz = models.IntegerField(unique=True)
    name = models.TextField(max_length=60)
    voted = models.BooleanField(default=False)


class Party(models.Model):
    name = models.TextField(max_length=60)
    head = models.TextField(max_length=60, null=True)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return f'<Party: {self.name}>'

    def affiliations(self):
        affs = self.affiliation_set.all()

        return ', '.join([aff.name for aff in affs])


class Affiliation(models.Model):
    name = models.TextField(max_length=60)
    party = models.ManyToManyField(Party)

    def __str__(self):
        return f'<{self.name}>'


