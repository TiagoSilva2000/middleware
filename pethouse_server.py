import Pyro4

@Pyro4.expose
@Pyro4.behavior(instance_mode="single")
class PetHouse(object):
  currentPets: int

  def __init__(self) -> None:
    self.currentPets = 5

  def adopt(self):
    if self.currentPets == 0:
      raise Exception("It's not possible do adopt more pets")

    self.currentPets -= 1
    msg = "Successfully adopted a new pet. Remaining pets " + str(self.currentPets) + "\n"
    print(msg)

    return msg

daemon = Pyro4.Daemon()
uri = daemon.register(PetHouse)

print("Ready. PetHouse uri =", uri)
daemon.requestLoop()