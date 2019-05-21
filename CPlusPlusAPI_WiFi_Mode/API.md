GoPro WiFi C++ API (Same as Python API but in C++)

|Function | Description                                      |
|:----------------------------|------------------------------------------------------------|
|CreateConnection                   | Creates Connection based on a configuration file provided which contains SSID name and password (This config file is previously created using wpa_passphrase). Internally uses the wpa_supplicant command |
|CloseConnection | Closes the connection by killing the current wpa_supplicant process. |
|CheckifConnected | Accepts an SSID and checks if there is a current connection which matches the SSID |
|TimeSync | If a connection is currently established with a GoPro, then attempts to sync time of the goPro with the current system time |
|SwitchToVideoMode | If a connection is currently established with a GoPro, switches the mode on the GoPro to Video|
|StartRecording | If a connection is currently established with a GoPro, starts a video recording
|StopRecording| If a connection is currently established with a GoPro, stops a video recording |
