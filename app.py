import os
from pathlib import Path
import subprocess as sp
from werkzeug.utils import secure_filename
from flask import Flask, request, send_from_directory


app = Flask(__name__)

@app.route("/")
def index():
    return 'Hello You'

@app.route('/uploads/<path:name>')
def download_file(name):
    return send_from_directory('./uploads/', name)


@app.route("/convert/<filetype>", methods=['POST'])
def convert_to(filetype):
    # if filetype not in ['pdf', 'html', 'docx']:
    #     return {'success':False, 'message':f'{filetype} not support'}

    if 'file' not in request.files:
        return {
            'success': False,
            'message': 'file is required.'
        }

    file = request.files['file']
    filename = f'./uploads/{secure_filename(file.filename)}'
    file.save(filename)
    output_file = os.path.splitext(filename)[0] + '.' + filetype

    media_dir = os.path.splitext(filename)[0]
    (Path(media_dir) / 'media').mkdir(parents=True, exist_ok=True)
    sp.run(["pandoc", filename, "-o", output_file, f"--extract-media={media_dir}"], check=True)
    output_file = output_file[1:]
    media_list = [f"{media_dir}/media/{i.name}"[1:] for i in Path(media_dir + '/media/').iterdir()]
    return {
        'success': True,
        'output': output_file,
        'media': media_list
    }


app.add_url_rule(
    "/uploads/<path:name>",  endpoint='download_file', build_only=True
)
