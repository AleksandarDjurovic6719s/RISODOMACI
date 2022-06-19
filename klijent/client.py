import requests
import json

zahtevi = [
    {"ime": "Maja","prezime": "Subotic","username": "maja_Subotic","smer": "IT","predmeti":[{"ime": "ri2", "espb": "6"},{"ime": "r2", "espb": "2"},{"ime": "r3", "espb": "1"}]},
    {"ime": "Nikola","prezime": "Radjen","username": "nikola_Radjen","smer": "IT","predmeti":[{"ime": "it1", "espb": "3"}]},
    {"ime": "Ana","prezime": "Kokic","username": "ana_kokic","smer": "IT","predmeti":[{"ime": "rn1", "espb": "6"},{"ime": "rn2", "espb": "4"}]},
]
endpoint = "http://localhost:8081/users"

for zahtev in zahtevi:
    requests.post(endpoint, json=zahtev)
