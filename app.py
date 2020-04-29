from flask import Flask, redirect, request, url_for, jsonify
import startup
from api import getUserLibrary, getUserPlaylists, getUserPlaylistsById, getSongsInPlaylist
from flask_cors import CORS, cross_origin

app = Flask(__name__)

cors = CORS(app)

@app.route('/oauth')
def performOAuth():
    response = startup.getUser()
    return redirect(response)

@app.route('/callback/')
def handleCallback():
    startup.getUserToken(request.args['code'])

    return redirect("http://localhost:5001/select-playlist")

@app.route('/userplaylists')
def getUserPlaylistsEndpoint():
    return jsonify(getUserPlaylists())

@app.route('/playlist-by-name', methods=['POST'])
def getPlaylistByName():
    index = request.get_json().get('index')
    playlistId = getUserPlaylistsById()[index]
    return jsonify(getSongsInPlaylist(playlistId))

if __name__ == '__main__':
    app.run(debug=True)