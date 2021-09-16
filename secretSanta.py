import random

participants = ["Michael", "Alice", "Bob", "Charlie", "Denis"]


def getOffset(_participants):
    return random.randint(1,len(_participants))

def getReceiverIndex(_senderIndex, _offset, _numParticipants):
    return ((_senderIndex + _offset) % _numParticipants)


def secretSantaIt(_participants):
    offset = getOffset(_participants)
    for index, participant in enumerate(_participants):
        print(_participants[index], _participants[getReceiverIndex(index, offset, len(_participants))], sep=" -> ")

secretSantaIt(participants)