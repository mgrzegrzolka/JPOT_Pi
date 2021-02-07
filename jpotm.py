"""
Main process for jpot pi

    ----------- History -----------------
    08.02.2021 Mariusz Grzegrzółka
                Create repository. Main class for jpot pi. First config file.
"""
import json

class JpotM:

    def __init__(self):
        self.main_settings = {
            "mysteryValueMin": 0,
            "mysteryValueMax": 0,
            "minBet": 0,
            "restartValue": 0
        }

    def readConfigFile(self):
        with open ('config.json', 'r') as config_json_f:
            config = json.load(config_json_f)
            config = config["config"]["main_settings"]
            self.main_settings["mysteryValueMin"] = config["mysteryValueMax"]
            self.main_settings["mysteryValueMax"] = config["mysteryValueMax"]
            self.main_settings["minBet"] = config["minBet"]
            self.main_settings["restartValue"] = config["restartValue"]

    def startJpCycle(self):
        instance = JpotInstance(self.main_settings)

class JpotInstance:
    def __init__(self, config):
        self.inst_config = config
    def startInstance(self):
        print("listen")
        print("update")
        print("get win")
        print("destroy instance")

jpot = JpotM()
jpot.readConfigFile()
