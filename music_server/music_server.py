import os
import shutil
from flask import Flask, jsonify, abort, make_response, url_for
import config
from download import download_first_result
from converter import video_to_audio
import util
import logging
from inspect import getmembers
from pprint import pprint
from flask_cors import CORS, cross_origin

logging.basicConfig(filename = config.application_path + 'music_server.log' ,format='%(asctime)s %(levelname)s %(message)s', level=logging.DEBUG)

app = Flask(__name__)
CORS(app)

@app.route('/songs/get/<artist_name>/<song_name>')

def get_song(artist_name, song_name):
        audio_name = util.make_audio_name(artist_name, song_name)
        new_audio_filename = config.music_folder + audio_name
        if not util.find_in_filesystem(config.music_folder, audio_name):
            video_file = download_first_result(artist_name + ' ' + song_name)
            logging.info("Video file name : " + video_file)
            downloaded_audio_file = video_to_audio(video_file)
            logging.info("Audio file name" + downloaded_audio_file)
            os.remove(video_file)
            shutil.move(downloaded_audio_file, new_audio_filename)
        return jsonify({'ok' : new_audio_filename})

@app.errorhandler(404)
def not_found(error):
    # logging.warning(dir(vars(error)))
    pprint(getmembers(error))
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/<path:path>')
def static_file(path):
            return app.send_static_file(path)

if __name__ == '__main__':
    app.run(debug=True)
