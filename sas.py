
import serial
import time

NO_SYNC = 0

POLLING_INTERVAL = .200



class Sas:

    def __init__(self, sas_adr, tty, ):
        self.serial = serial.Serial(port=tty, baudrate=19200)
        self.sas_adr = sas_adr

        self.gp_state = 1
        self.p_time = time.time()

    def polling(self):
        gp = 0x80
        gp_adr = 0x80 + self.sas_adr
        if self.gp_state:
            self.serial.write(gp_adr)
            print(hex(gp_adr))
            if not NO_SYNC:
                self.gp_state = 0
        else:
            self.serial.write(gp)
            print(hex(gp))
            self.gp_state = 1

    def polling_cycle(self):
        trigger_t = self.p_time + POLLING_INTERVAL
        if float(trigger_t) < float(time.time()):
            self.p_time = time.time()
            self.polling()


sas = Sas(1, '/dev/ttyS0')

while True:
    sas.polling_cycle()


