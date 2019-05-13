class Camera:
    name = ''
    password = ''
    commands = []
    state = 0

def readConfig(Cameras):
    conf = open("goProAccessPt.conf", mode='r')
    confLines = conf.readlines()
    tempCamera = Camera()
    for x in range(0, len(confLines)):
        if confLines[x][0:3] == '[GP': #Start of configuration
            if len(tempCamera.commands) > 0:
                Cameras.append(tempCamera)
                tempCamera = Camera()
                tempCamera.commands = []
        else:
            splitconf = confLines[x].split('=') #Read the name
            if splitconf[0].replace(" ", "") == 'Access_pt_name':
                tempCamera.name = splitconf[1].replace(" ", "").replace("\n", "")
            elif splitconf[0].replace(" ", "") == 'Access_pt_password':
                tempCamera.password = splitconf[1].replace(" ", "").replace("\n", "")
            else:
                command = confLines[x].replace(" ", "").replace("\n", "")
                if len(command) > 0 :
                    (tempCamera.commands).append(command)
    conf.close()
    Cameras.append(tempCamera)
