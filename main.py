import requests
import time
from datetime import datetime, timedelta, UTC

def get_ctfs(limit=10, days_ahead=30):

    start_timestamp  = int(time.time())

    future_date = datetime.now(UTC) + timedelta(days=days_ahead)

    finish_timestamp = int(future_date.timestamp())

    url = "https://ctftime.org/api/v1/events/"

    headers = {
    "User-Agent": "Mozilla/5.0 (compatible; CTFTracker/1.0)"
    }

    params = {"limit": limit,"start": start_timestamp,"finish": finish_timestamp}

    response = requests.get(url,params=params,headers=headers)

    if response.status_code != 200:
        raise Exception(f"Error {response.status_code} - {response.text}")

    return response.json()


def print_events(events):
    if not events:
        print("Sem CTFs.")
        return

    for event in events:

        organizers = event.get("organizers",[])

        print("="*50)
        print(f"Título: {event.get('title')}")
        print(f"Link: {event.get('url')}")
        print(f"Organizadores: {organizers[0]['name']}")
        print(f"Início: {event.get('start')}")
        print(f"Localização: {event.get('location')}")
        print(f"Descrição: {event.get('description')}")
        print(f"Link no CTF time: {event.get('ctftime_url')}")
        print("="*50)


def main():
    try:
        events = get_ctfs(limit=20,days_ahead=30)
        print_events(events)
    except Exception as e:
        print(f"Erro ao realizar a requisicao: {e}")


if __name__ == "__main__":
    main()
