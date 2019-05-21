## GoPro WiFi C++ API

#### The core idea to develop an API to make connections to GoPro WiFi access points, switch between multiple GoPro WiFi access points, send commands to the GoPro's, query the GoPro's about their status via a C++ library using the information gained through the work done in the Python API. The C++ library will also, just like the Python library, use wpa_supplicant to make connections, switch connections. For sending URL's, the plan is to use cURL.
#### The intention is to write a few basic functions like below which would form the core functionality using which more complex things can be done.

###### The plan is to have two core classes - (1) A "SystemCommand" class whose sole responsibility is to issue commands via the standard execution environment like bash and record the results; and (2) A "URLCommand" class whose responsibility it would be to send URL commands and record the results. This is the innermost layer on top of which everything else is built.

|Function | Description                                      |
|:--------|------------------------------------------------------------|
|ExecuteSystemCommand()     | Executes a command provided to it (for linux, in bash) and sends back the result |
|SendURLCommand() | Sends a URL command to a GoPro |

###### The next outer layer would be building basic functionality like in the below table using the elements of the previous layer.

|Function | Description                                      |
|:----------------------------|------------------------------------------------------------|
|CreateConnection()                   | Creates Connection based on a configuration file provided which contains SSID name and password (This config file is previously created using wpa_passphrase). Internally uses the wpa_supplicant command |
|CloseConnection() | Closes the connection by killing the current wpa_supplicant process. |
|CheckifConnected | Accepts an SSID and checks if there is a current connection which matches the SSID |
|TimeSync() | If a connection is currently established with a GoPro, then attempts to sync time of the goPro with the current system time |
|SwitchToVideoMode() | If a connection is currently established with a GoPro, switches the mode on the GoPro to Video|
|StartRecording() | If a connection is currently established with a GoPro, starts a video recording
|StopRecording()| If a connection is currently established with a GoPro, stops a video recording |


###### From the work done in gp_wifi.py, we know that the above functionality can be completely achieved if we have the "SystemCommand" and "URLCommand" classes. More importantly, if we need to add some new functionality like say, sending a "locate" command to the GoPro which makes the GoPro beep, all we need is the URL that makes it work (from the goprowifihack github page) and the two functions from the previous layer and we can "develop" the new feature of "locate GoPro".

###### The next (and final layer) is the "Application layer" where the user builds functionality like adding a few cameras, cycling between them in any order and issuing commands. For example, consider the following sample usecases (which demonstrate cycling between multiple GoPro WiFi access points and sending commands and controlling GoPro's and setting time on the GoPro's) and note how the usecase is implemented using the functions described above.

###### Use case 1
Connect GP 1 -> Sync Time with GP 1 -> Start recording on GP 1 -> Connect GP 2 -> Sync Time with GP 2 -> Start recording on GP 2 -> Connect GP 1 -> Stop Recording on GP 1 -> Connect GP 2 -> Stop Recording on GP 2

```c++
int main()
{
   GPWiFi gp_wifi = new GPWiFi();
   gp_wifi.initialize();

   gp_wifi.CreateConnection("goPro1.conf");
   gp_wifi.TimeSync();
   gp_wifi.SwitchToVideoMode();
   gp_wifi.StartRecording();

   gp_wifi.CreateConnection("goPro2.conf");
   gp_wifi.TimeSync();
   gp_wifi.SwitchToVideoMode();
   gp_wifi.StartRecording();

   gp_wifi.CreateConnection("goPro1.conf");
   gp_wifi.StopRecording();

   gp_wifi.CreateConnection("goPro2.conf");
   gp_wifi.StopRecording();

   return 0;
}
```

###### Usecase 2:
Let's assume we have a set of GoPros whose SSID's are stored in a vector. Cycle through all the GP's and send each one of them start recording command and then after 2 minutes send them all stop recording command.

```c++
int main()
{
   GPWiFi gp_wifi = new GPWiFi();
   gp_wifi.initialize();

   ....
   ....

   for(std::vector<T>::iterator it = ssid_vector.begin(); it != ssid_vector.end(); ++it)
   {
      gp_wifi.CreateConnection(confFilesMap.find(*it));
      gp_wifi.SwitchToVideoMode();
      gp_wifi.StartRecording();
   }

   sleep(2*60);

   for(std::vector<T>::iterator it = ssid_vector.begin(); it != ssid_vector.end(); ++it)
   {
      gp_wifi.CreateConnection(confFilesMap.find(*it));
      gp_wifi.SwitchToVideoMode();
      gp_wifi.StopRecording();
   }

   return 0
}

```
