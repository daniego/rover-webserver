from flask import *
import os

import logging
from logging.handlers import RotatingFileHandler

UV4L_HOST = os.environ.get('UV4L_HOST')
UV4L_PORT = os.environ.get('UV4L_PORT')
ENGINE_HOST = os.environ.get('ENGINE_HOST')

SERVO_X_MIN = 730
SERVO_X_MAX = 3200
SERVO_X_START = 1950
#
SERVO_Y_MIN = 770
SERVO_Y_MAX = 2000
SERVO_Y_START = 1450

# Create flask app and global pi 'thing' object.
app = Flask(__name__)

# Define app routes.
# Index route renders the main HTML page.
@app.route("/")
def index():
    return render_template('index.html')

# @app.route('/update')
# def show_post():
#     # show the post with the given id, the id is an integer
#     return ('OK', 200)
#     # return 'Post '


@app.route('/update', methods=['POST'])
def show_post():
    # show the post with the given id, the id is an integer
    print('First: %i, Second: %s' % (request.json['first'], request.json['second']) )
    return 'Post %s' % request.json

@app.route("/view/<path:service>", methods=['GET'])
def view(service):
    # print service
    if service == 'web/fixed':
        return render_template('view_web.html',
                                uv4l_host=UV4L_HOST,
                                uv4l_port=UV4L_PORT,
                                engine_host=ENGINE_HOST,
                                servo_y_min=SERVO_Y_MIN,
                                servo_y_max=SERVO_Y_MAX,
                                servo_y_start=SERVO_Y_START,
                                servo_x_min=SERVO_X_MIN,
                                servo_x_max=SERVO_X_MAX,
                                servo_x_start=SERVO_X_START
                                )
    elif service == 'driver/mobile':
        return render_template('driver-mobile.html', switch=switch)
    elif service == 'cardboard':
        return render_template('cardboard.html')
    elif service == 'web-bluetooth-rename':
        return render_template('web-bluetooth-rename.html')
    elif service == 'glove-controller-raw':
        return render_template('glove-controller-raw.html')
    elif service == 'web-bluetooth-get':
        return render_template('web-bluetooth-get.html')
    elif service == 'web-bluetooth-get2':
        return render_template('web-bluetooth-get2.html')
    elif service == 'web-bluetooth-get3':
        return render_template('web-bluetooth-get3.html')
    elif service == 'web-bluetooth-get3_flavio':
        return render_template('web-bluetooth-get3_flavio.html')
    elif service == 'web-bluetooth-demo2':
        return render_template('web-bluetooth-demo2.html')
    else:
        return ('Unknow request', 400)

# Server-sent event endpoint that streams the thing state every second.
@app.route('/thing')
def thing():
    def get_thing_values():
        while True:
            # Build up a dict of the current thing state.
            thing_state = {
                'switch': pi_thing.read_switch(),
                # 'temperature': pi_thing.get_temperature(),
                # 'humidity': pi_thing.get_humidity()
            }
            # Send the thing state as a JSON object.
            yield('data: {0}\n\n'.format(json.dumps(thing_state)))
            # Wait a second and repeat.
            time.sleep(1.0)
    return Response(get_thing_values(), mimetype='text/event-stream')

# Start the flask debug server listening on the pi port 5000 by default.
if __name__ == "__main__":
#
    app.logger.addHandler(logging.StreamHandler())
    app.logger.setLevel(logging.INFO)
    app.run(host='0.0.0.0', port=8089, debug=True, threaded=True)
    # app.run(host='0.0.0.0', port=8089, debug=True, threaded=True, ssl_context=('ssl/cert.pem', 'ssl/key.pem'))
