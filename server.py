import Pyro4
from numpy import double

@Pyro4.expose
@Pyro4.behavior(instance_mode="session")
class Pet(object):
  name: str
  happiness: int
  age: double
  health: int

  def __init__(self) -> None:
    self.name = ""
    self.happiness = 25
    self.health = 100
    self.age = 0

  def __getOlder(self, time=0.2):
    self.age += time
    self.__setHealth(-1)

    return self.age

  def __setHappiness(self, v):
    if self.happiness + v <= 0:
      print("your pet got a mental disease")
      self.happiness = 0
      self.__setHealth(-50)
      return

    self.happiness += v

    return self.happiness

  def __setHealth(self, v):
    if self.health - v <= 0:
      print("YOUR PET DIED\nGAME OVER")
      raise Exception()

    self.health += v
    return self.health

  def giveName(self, name: str):
    if len(self.name) == 0:
      self.name = name
      self.__setHappiness(25)
      return self.name

    self.name = name
    self.__setHappiness(-25)
    return self.__getGeneralState()

  def takeForAWalk(self):
    self.__setHappiness(10)
    self.__getOlder();

    return self.__getGeneralState()

  def pet(self):
    self.__setHappiness(5)
    self.__getOlder(0.1)

    return self.__getGeneralState()

  def giveFood(self):
    self.__setHappiness(10)
    self.__getOlder()

    return self.__getGeneralState()

  def takeToVet(self):
    self.__setHappiness(-15)
    self.__setHappiness(5)
    self.__getOlder(0.4)

    return self.__getGeneralState()

  def checkStatus(self):
    if self.happiness > 1 and self.happiness <= 25:
      return "BAD"
    elif self.happiness > 25 and self.happiness <= 50:
      return "OK"
    elif self.happiness > 50 and self.happiness <= 75:
      return "NICE"

    return "HAPPY";

  def getAge(self):
    return self.age

  def getHealth(self):
    if self.health > 1 and self.health <= 25:
      return "SICK"
    elif self.health > 25 and self.health <= 50:
      return "OK"
    elif self.health > 50 and self.health <= 75:
      return "HEALTHY"

    return "SUPER HEALTHY";

  def __getGeneralState(self):
    return self.name.capitalize() + " is " + str(self.age) + " years old. It's " + self.checkStatus() + " about in happiness, and " + self.getHealth() + " in health.\n"

daemon = Pyro4.Daemon()
uri = daemon.register(Pet)

print("Ready. pet uri =", uri)
daemon.requestLoop()