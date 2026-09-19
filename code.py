import os
import django
import pandas as pd

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "movieai.settings")
django.setup()

from tamil.models import Movie

df = pd.read_csv("tamil_movies.csv")

for _, row in df.iterrows():
    Movie.objects.create(
        title=row["Movie"],
        genre=row["Genre"],
        actor="Unknown",
        director="Unknown"
    )

print("Movies inserted successfully!")