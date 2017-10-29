from flask import *
import os

# print(os.getenv('SWARM_IP'))
# print(os.environ.get('SWARM_IP'))
#
# # SWARM_IP = os.environ.get("SWARM_IP") + ":8099"
# # SWARM_IP = sSWARM_IP)
# print(SWARM_IP)
# define servo range
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

@app.route("/view/<path:service>", methods=['GET'])
def view(service):
    # print service
    if service == 'driver/full':
        return render_template('driver-full.html',
                                swarm_ip=SWARM_IP,
                                servo_y_min=SERVO_Y_MIN,
                                servo_y_max=SERVO_Y_MAX,
                                servo_y_start=SERVO_Y_START,
                                servo_x_min=SERVO_X_MIN,
                                servo_x_max=SERVO_X_MAX,
                                servo_x_start=SERVO_X_START)
    elif service == 'driver/mobile':
        return render_template('driver-mobile.html', switch=switch)
    elif service == 'cardboard':
        return render_template('cardboard.html')
    elif service == 'web-bluetooth-demo':
        return render_template('web-bluetooth-demo.html')
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
    app.run(host='0.0.0.0', port=8089, debug=False, threaded=True)
