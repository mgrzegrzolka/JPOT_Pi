"""
Main process for jpot pi

    ----------- History -----------------
    08.02.2021 Mariusz Grzegrzolka
                Create repository. Main class for jpot pi. First config file.
"""
import json
import os
import random


class JpotM:

    def __init__(self):
        self.main_settings = {
            "mysteryValueMin": 0,
            "mysteryValueMax": 0,
            "minBet": 0,
            "restartValue": 0
        }


    def read_config_file(self):
        with open ('config.json', 'r') as config_json_f:
            config = json.load(config_json_f)
            config = config["config"]["main_settings"]
            self.main_settings["mysteryValueMin"] = config["mysteryValueMin"]
            self.main_settings["mysteryValueMax"] = config["mysteryValueMax"]
            self.main_settings["minBet"] = config["minBet"]
            self.main_settings["restartValue"] = config["restartValue"]

    def start_jp_cycle(self):
        instance = JpotInstance(self.main_settings)
        instance.start_instance()


class JpotInstance:

    def __init__(self, config):
        self.inst_config = config
        self.jpValue = self.inst_config["restartValue"]

    def start_instance(self):
        while True:
            self.listen_jp_interface()
            self.check_win()
        print("destroy instance")

    def listen_jp_interface(self):
        while True:
            print("1. Bet - 20")
            print("2. Bet - 50")
            print("3. Bet - 100")
            print("4. Bet - 200")
            print("5. Bet - 500")
            set_bet = input("Enter your bet value (1-5):")
            if set_bet == 1:
                bet = 20
            if set_bet == 2:
                bet = 50
            if set_bet == 3:
                bet = 100
            if set_bet == 4:
                bet = 200
            if set_bet == 5:
                bet = 500
            if bet:
                if bet < self.inst_config["minBet"]:
                    print("Bet did exceed the minBet2")
                    continue
                self.update_jp_value(bet)
                break

    def update_jp_value(self, bet):
        self.jpValue += bet

    def check_win(self):
        print("")
        print("==========JPOT-PI============")
        print("Jp value = %d" % self.jpValue)
        print("Jp MIN = %d" % self.inst_config["mysteryValueMin"])
        print("Jp MAX = %d" % self.inst_config["mysteryValueMax"])
        print("=============================")
        if self.jpValue < self.inst_config["mysteryValueMin"]:
            return 0
        elif self.jpValue >= self.inst_config["mysteryValueMax"]:
            return 1
        else:
            min_bet = self.inst_config["minBet"]
            mystery_value_max = self.inst_config["mysteryValueMax"]
            prob_of_win = ((min_bet*100)/((mystery_value_max-self.jpValue) + min_bet))
            print prob_of_win
            if random.randint(0, 100) < prob_of_win:
                return 1
jpot = JpotM()
jpot.read_config_file()
jpot.start_jp_cycle()
