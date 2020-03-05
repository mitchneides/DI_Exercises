import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'iVote.settings')
django.setup()

from app.models import Party

parties = ["Likud", "Blue&White", "Emet", "Shas", "Joint-list", "Yemina", "Israel-Beitenu", "Otzma"]

print('Populating Party table...')
for party in parties:
    p = Party(name=party)
    p.save()
print('Done')