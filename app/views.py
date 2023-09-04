import os
import string
import random
from app import app
from flask import render_template, request, make_response, send_file, jsonify
from werkzeug.utils import secure_filename
# from pydub import AudioSegment
import moviepy.editor as mp
import openai

openai.api_key = "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"


@app.get('/')
def index():
    """
    renders the home page"""
    return render_template("index.html")

@app.post('/process')
def process():

    """
        This function:
            1. Extracts the video from the form
            2. Converts the video to audio
            3. Transcribes the audio
            4. Summarizes the text

    """

    vid_file = request.files["fileToUpload"]

    print("file found")

    file_name = secure_filename(vid_file.filename)
    extension = file_name.rsplit('.')[-1].lower()
    destination = os.path.join(os.path.dirname(__file__), 'static', 'videos', file_name)
    vid_file.save(destination)

    print("file saved")
    print(destination)
    print(extension)

    # convert video to audio

    clip = mp.VideoFileClip(destination)


    # save audio file

    audio_p = file_name.removesuffix(extension) + 'mp3'
    audio_path = os.path.join(os.path.dirname(__file__), 'static', 'audio', audio_p)

    print(audio_path)

    clip.audio.write_audiofile(audio_path)

    # Open the audio file
    audio_file = open(audio_path, "rb")

    # transcribe using audio_file
    audio_response = openai.Audio.transcribe("whisper-1", audio_file)

    transcript = audio_response["text"]

    print(transcript)

    # Create a request to the API to identify the language spoken
    chat_response = openai.Completion.create(
        model = "text-davinci-003",
        prompt = "Summarize the following: \n" + transcript
    )
    print(chat_response["choices"][0]["text"])

    # create_download(transcript)


    return make_response(jsonify([chat_response["choices"][0]["text"], transcript]), 200)



def create_download(text):
    """
    This function takes in a string, creates a text file with the contents of the string and downloads it.

    i.e
        create_download("some meaningful text sample")
    """
    f_name = random_file_name(".txt")
    f_path = os.path.join(os.path.dirname(__file__), 'static', 'transcriptions', f_name)
    with open(f_path, 'w') as f:
        f.write(text)

    print(f_path)

    return send_file(f_path, as_attachment=True)

def random_file_name(ext):
    """ the function takes in a file extenion and returns a random filename.
    i.e 
        random_file_name(".mp4")
    """
    N = 8
    return ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=N)) + ext