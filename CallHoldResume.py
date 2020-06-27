from Basiccall import Phonecall
from sqldb import Getphones

if __name__ == "__main__":
    dut = Getphones("VVX350")
    helperPhone = Getphones("VVX501")
    dutIP = dut.getIP()
    helperIP = helperPhone.getIP()
    call = Phonecall(dutIP,helperIP)
    call.placeCall()
    call.answerCall()
    call.hasTwowayAudio()
    call.holdCall()
    call.resumeCall()
    call.endCall()
