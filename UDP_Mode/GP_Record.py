from goprocam import GoProCamera
from goprocam import constants

import sys

if len(sys.argv) != 2:
	print("Usage: python GP_Record.py <r/s/o/t>  \n r = start recording \n s = stop recording \n o = power off \n t = sync time")
	exit()

camera = GoProCamera.GoPro()

if sys.argv[1] == "o":
	camera.power_off()
elif sys.argv[1] == "s":
	if camera.IsRecording() == 0:
		print("No recording is in progress. Nothing to stop.")
		exit()
	else:
		print("Stopping Camera")
		camera.shutter(constants.stop)
elif sys.argv[1] == "s":
	camera.syncTime()
elif sys.argv[1] == "r":
	if camera.IsRecording() == 0:
		print("A recording is in progress. Cannot start a new recording.")
	else:
			camera.mode(constants.Mode.VideoMode)
			camera.syncTime()
			camera.shoot_video(0)	

