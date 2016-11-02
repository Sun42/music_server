import os
import shutil
import logging

from flask import Flask, jsonify, abort, make_response, url_for, request
from flask_cors import CORS, cross_origin
from objbrowser import browse

import util
import config
from youtube_search import YoutubeSearch
from youtube_download import YoutubeDownload
from converter import video_to_audio


logging.basicConfig(filename = config.application_path + 'music_server.log' ,format='%(asctime)s %(levelname)s %(message)s', level=logging.DEBUG)

app = Flask(__name__)
CORS(app)

@app.route('/search_and_download/<path:search_query>')
def search_and_download(search_query):
    logging.info("Search and download : " + search_query)
    video_url = YoutubeSearch(search_query).video_ids[0]
    logging.info("Found first result : " + video_url)
    return download("https://youtube.com/watch?v=" + video_url)

@app.route('/download/<path:url>')
def download(url):
    logging.info("Download : " + url)
    video_full_path = YoutubeDownload(url).download(config.tmp_folder)
    audio_full_path = video_to_audio(video_full_path, config.music_folder)
    os.remove(video_full_path)
    audio_url = request.url_root + 'music/' + util.extract_filename(audio_full_path)
    logging.info("Audio url : " + audio_url)
    return jsonify({'ok' : audio_url})

@app.route('/search/<path:search_query>')
def search(search_query):
    logging.info("Search : " + search_query)
    return jsonify({'ok' : YoutubeSearch(search_query).video_ids})

@app.errorhandler(500)
def internal_error(error):
    logging.exception("message")
    return make_response(jsonify({'error': 'Oops!'}), 500)

@app.errorhandler(404)
def not_found(error):
    logging.exception("message")
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug=True)
