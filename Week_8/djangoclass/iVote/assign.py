import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'iVote.settings')
django.setup()

from app.models import Party, Affiliation

affiliations = {"Likud": "Right", "Blue&White": "Center",
                "Emet": "Left", "Shas": "Right",
                "Joint-list": "Left", "Yemina": "Right",
                "Israel-Beitenu": "Right", "Otzma": "Right"}

heads = {"Likud": "Benjamin Netanyahu", "Blue&White": "Benny Gantz",
                "Emet": "Amir Peretz", "Shas": "Arieh Derhy",
                "Joint-list": "Aiman Oudeh", "Yemina": "Naftali Bennet",
                "Israel-Beitenu": "Avigdor Liebermann", "Otzma": "Itamar Ben-Gvir"}

# for party, affiliation in affiliations.items():
#     p = Party.objects.get(name=party) #query from db
#     aff, _ = Affiliation.objects.get_or_create(name=affiliation)
#     #function gives us value stored as aff
#     #if already existed, returns bool False else returns bool True (represented by underscore) that it was just created
#
#     aff.save()
#     p.affiliation_set.add(aff) #add to db
#     p.save()
#
# print('Done')


for party, head in heads.items():
    p = Party.objects.get(name=party) #query from db
    p.head = head
    p.save()

print('Done')