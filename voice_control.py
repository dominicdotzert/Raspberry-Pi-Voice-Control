import snowboydecoder
import sys
import signal
from toggle_light import toggle
from Random_Ross import play
from stop_ross import stop
import subprocess


interrupted = False

def signal_handler(signal, frame):
    global interrupted
    interrupted = True

def interrupt_callback():
    global interrupted
    return interrupted

if len(sys.argv) != 4:
    print("Error: need to specify 3 model names")
    print("Usage: python demo.py 1st.model 2nd.model")
    sys.exit(-1)

subprocess.call("python black_screen.py", shell=True)

models = sys.argv[1:]

# capture SIGINT signal, e.g., Ctrl+C
signal.signal(signal.SIGINT, signal_handler)

sensitivity = [0.5]*len(models)
detector = snowboydecoder.HotwordDetector(models, sensitivity=sensitivity)
callbacks = [lambda: play(),
             lambda: stop(),
             lambda: toggle()]
print('Listening... Press Ctrl+C to exit')

# main loop
# make sure you have the same numbers of callbacks and models
detector.start(detected_callback=callbacks,
               interrupt_check=interrupt_callback,
               sleep_time=0.03)

detector.terminate()
