import sys
import spotipy
import spotipy.util as util
import startup


def getUserLibrary():
    sp = spotipy.Spotify(auth=startup.getAccessToken()[0])

    results = sp.current_user_saved_tracks()
    output = []

    for item in results['items']:
        track = item['track']
        output.append(track['name'] + ' - ' + track['artists'][0]['name'])
    
    return output

def getUserPlaylists():
    sp = spotipy.Spotify(auth=startup.getAccessToken()[0])

    playlists = sp.current_user_playlists()
    output = []

    for playlist in playlists['items']:
        name = playlist['name']
        output.append(name)

    print(output)
    return output

def getUserPlaylistsById():
    sp = spotipy.Spotify(auth=startup.getAccessToken()[0])

    playlists = sp.current_user_playlists()
    output = []

    for playlist in playlists['items']:
        name = playlist['id']
        output.append(name)

    return output

def getSongsInPlaylist(id):
    sp = spotipy.Spotify(auth=startup.getAccessToken()[0])

    playlist = sp.playlist_tracks(id)
    output = []

    for track in playlist['items']:
        output.append(track['track']['name'] + " by " + track['track']['artists'][0]['name'])# + " by " + track['artists'][0]['name'])

    print(output)
    return output