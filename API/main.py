import requests
import json
from typing import List
from pprint import pprint
from os import getenv

from models import YandexUploader

SUPERHERO_HOSTNAME = "https://superheroapi.com/api"
SUPERHERO_API_TOKEN = getenv("SUPERHERO_API_TOKEN")

YANDEX_HOSTNAME = "https://cloud-api.yandex.net"
YANDEX_API_TOKEN = getenv("POLIGON_API_TOKEN")


def first_task():
    heroes_dict: dict = {}
    for hero_name in ["Hulk", "Captain America", "Thanos"]:
        hero_details: dict = json.loads(
            requests.get(
                url=f"{SUPERHERO_HOSTNAME}/{SUPERHERO_API_TOKEN}/search/{hero_name.lower()}"
            ).content
        ).get("results")[0]
        heroes_dict.update({hero_details["name"]: hero_details})

    sorted_heroes: List[str] = sorted(
        heroes_dict,
        key=lambda hero: int(heroes_dict[hero]["powerstats"]["intelligence"]),
        reverse=True,
    )
    print("\nThe Most Intelligent hero is:", end="\n")
    pprint(heroes_dict[sorted_heroes[0]])


def second_task(file_path: str):
    yandex_uploader: YandexUploader = YandexUploader(hostname=YANDEX_HOSTNAME, access_token=YANDEX_API_TOKEN)
    print(yandex_uploader.upload_file(file_path))
    pprint(yandex_uploader.get_uploaded_file(file_path))


if __name__ == "__main__":
    # first_task()
    second_task(input("Input Full path to the file here -> "))

