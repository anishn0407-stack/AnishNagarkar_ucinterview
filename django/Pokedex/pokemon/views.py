from django.shortcuts import render
from .forms import SearchForm
import requests

def home(request):

    form = SearchForm()

    if request.method == "POST":
        form = SearchForm(request.POST)

        if form.is_valid():
            pokemon_type = form.cleaned_data["pokemon_type"]

            url = f"https://pokeapi.co/api/v2/type/{pokemon_type.lower()}"

            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()

                pokemon_list = data["pokemon"][:10]

                for pokemon in pokemon_list:
                    print(pokemon["pokemon"]["name"])

    return render(request, "pokemon/home.html", {
        "form": form
    })