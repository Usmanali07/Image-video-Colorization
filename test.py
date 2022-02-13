 
from flask import Flask
from flask import request
from flask import  send_file
import base64

app = Flask(__name__)


# define a predict function as an endpoint
@app.route("/process", methods=["POST", "GET"])
def process_video():
    file = request.files['file']
    z = file.save("data/textTest.txt")
    text ="data/textTest.txt"

    fh = open("vdeo.mp4", "wb")
    fh.write(base64.b64decode(text))
    fh.close()

    return "done"


if __name__ == '__main__':
    port = 5000
    host = "0.0.0.0"
    app.run(host=host, port=port, threaded=False)
