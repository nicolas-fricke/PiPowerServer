import flask
import os

app = flask.Flask(__name__)

@app.route('/')
def index():
  return flask.render_template('control.html')

@app.route('/switch_socket', methods=['POST'])
def switch_socket():
  system_code = flask.request.form['system']
  socket_code = flask.request.form['socket']
  on_off      = flask.request.form['on_off']
  os.system('/home/pi/Projects/rcswitch-pi/send %s %s %s' % (system_code, socket_code, on_off))
  return flask.Response(status=204)

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')
