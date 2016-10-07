import os
import shutil
from flask import Flask, jsonify, abort, make_response, url_for
import config
from download import download_first_result
from converter import video_to_audio

app = Flask(__name__)
# songs = [
#     {
#         'id': 1,
#         'title': 'Pelican Glide',
#         'artist': 'Steve Bug',
#         'file': 'Steve_Bug__Pelican_Glide.mp3'
#     },
#     {
#         'id': 2,
#         'title': 'Gallowdance',
#         'artist': 'Lebanon Hanover',
#         'file': 'Lebanon_Hanover__Gallowdance.mp3'
#     }
#     ]
#
# @app.route('/songs/<artist_name>/<title_name>', methods=['GET'])
#
# def get_song(artist_name, title_name):
#     song = None
#     for song in songs:
#         if song['artist'] == artist_name and song['title'] == title_name:
#             song['link'] = url_for('static', filename=  song['file'])
#             return jsonify ({'song': song})
#     abort(404)
#
#
# @app.route('/songs/id/<int:song_id>', methods=['GET'])
#
# def get_song_by_id(song_id):
#         for song in songs:
#                 if song['id'] == song_id:
#                         song['link'] = url_for('static', filename=  song['file'])
#                         return jsonify ({'song': song})
#         abort(404)


@app.route('/songs/add/<artist_name>/<song_name>')

def add_song(artist_name, song_name):
        video_file = download_first_result(artist_name + ' ' + song_name)
        print("Video file name : " + video_file)
        audio_file = video_to_audio(video_file)
        new_audio_filename = config.music_folder + os.path.basename(audio_file)
        print("Audio file name" + audio_file)
        os.remove(video_file)
        shutil.move(audio_file, new_audio_filename)
        return jsonify({'ok' : new_audio_filename})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/<path:path>')
def static_file(path):
            return app.send_static_file(path)

if __name__ == '__main__':
    app.run(debug=True)
