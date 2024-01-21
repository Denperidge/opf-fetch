from requests import get as _get

def _request(url: str):
    request = _get(url)
    if request.status_code >= 400:
        return False
    else:
        return request.json()

def isrc_to_opf(isrc: str):
    data = _request("https://api.deezer.com/2.0/track/isrc:" + isrc)
    if not data:
        return False
    if data.get("error"):
        return False
    return {
            "isrc": data["isrc"],
            "song_name": data["title"],
            "artist_name": data["artist"]["name"],
            "image": data["album"]["cover_xl"]
        }

def names_to_opf(artist_name: str, song_name: str):
    data = _request(f"https://api.deezer.com/2.0/search?q={artist_name} {song_name}")
    if not data:
        return False

    # Re-request with deezer id, as this has an isrc
    deezer_id = data["data"][0]["id"]
    data = _request(f"https://api.deezer.com/2.0/track/{deezer_id}")
    if not data:
        return False

    return {
            "isrc": data["isrc"],
            "song_name": data["title"],
            "artist_name": data["artist"]["name"],
            "image": data["album"]["cover_xl"]
        }
    