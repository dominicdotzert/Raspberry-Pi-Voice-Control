import subprocess

def stop():
    subprocess.call("killall omxplayer.bin", shell=True)

if __name__ == "__main__":
    stop()
