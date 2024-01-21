from flask import Flask
from requests import get
from sources import deezer

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>opf-fetch online!</h1>"

@app.route("/isrc-to-opf/<isrc>")
def isrc_to_opf(isrc: str):
    for source in [deezer]:
        data = source.isrc_to_opf(isrc)
        if data:
            return data
    return f"No data found for isrc {isrc}!"
    

@app.route("/names-to-opf/<artist_name>/<song_name>")
def names_to_opf(artist_name: str, song_name: str):
    for source in [deezer]:
        data = source.names_to_opf(artist_name, song_name)
        if data:
            return data
    return f"No data found for {artist_name} - {song_name}!"
