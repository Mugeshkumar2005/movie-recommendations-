import pandas as pd
from django.shortcuts import render

movies = pd.read_csv(r"D:/mugesh/mugesh/movieai/tamil_movies.csv")

def home(request):
    recommendations = []

    if request.method == "POST":
        movie_name = request.POST.get("movie", "").strip()

        if movie_name:
            movie = movies[
                movies["Movie"].astype(str).str.lower() == movie_name.lower()
            ]

            if not movie.empty:
                genre = movie.iloc[0]["Genre"]

                recommendations = movies[
                    (movies["Genre"].astype(str).str.lower() == str(genre).lower()) &
                    (movies["Movie"].astype(str).str.lower() != movie_name.lower())
                ].head(5).to_dict("records")

    return render(request, "home.html", {
        "recommendations": recommendations
    })