# Flask Video Transcription

![Flask Logo](https://www.fullstackpython.com/img/logos/flask.jpg)

## Overview

This Flask project allows you to transcribe videos easily. It provides a web interface where you can upload video files, and the application will transcribe the spoken content within the video into text. The transcription is then made available for download in plain text format.

## Features

- Upload video files in various formats.
- Transcribe the audio content from uploaded videos.
- Download the transcription in plain text or other popular formats.
- User-friendly web interface.

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/al-chris/Video_Transcriber.git
   cd Video_Transcriber
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```bash
     source venv/bin/activate
     ```

4. Install the project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Start the Flask application:

   ```bash
   flask run
   ```

6. Open your web browser and go to `http://localhost:5000` to use the application.

## Usage

1. Open the web application by navigating to `http://localhost:5000` in your browser.

2. Click the "Upload Video" button to select and upload your video file.

3. Once the video is uploaded, click the "Transcribe" button to start the transcription process.

4. Wait for the transcription to complete. This may take some time depending on the length of the video.

5. Once the transcription is ready, you will be able to download it as a .txt file.

## Configuration

You can configure the application by editing the `__init__.py` file. Here are some of the available configuration options:

- `UPLOAD_FOLDER`: The folder where uploaded videos are stored.
- `TRANSCRIPTION_FOLDER`: The folder where transcriptions are saved.
- `ALLOWED_EXTENSIONS`: A list of allowed file extensions for video uploads.
- `MAX_CONTENT_LENGTH`: The maximum allowed file size for uploads.

## Dependencies

This project relies on the following Python libraries:

- Flask: A micro web framework for building web applications.
- OpenAI: A library for using the OpenAI API.
- moviepy: A Python library for video editing.

Please refer to the `requirements.txt` file for a complete list of dependencies.

## Contributing

We welcome contributions to this project! If you have any ideas, bug reports, or feature requests, please open an issue on the [GitHub repository](https://github.com/al-chris/Video_Transcriber). If you'd like to contribute code, feel free to submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

This project was built with the help of various open-source libraries and resources. We would like to express our gratitude to the contributors of these projects.

---


Enjoy transcribing your videos with Flask! If you have any questions or need assistance, please don't hesitate to reach out.

[Flask](https://flask.palletsprojects.com) | [moviepy](https://zulko.github.io/moviepy/) | [OpenAI](https://platform.openai.com/)
