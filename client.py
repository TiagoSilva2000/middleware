# saved as greeting-client.py
from ctypes.wintypes import PHKEY
from pickletools import stringnl_noescape
from typing import Dict, List
from xmlrpc.client import boolean
import Pyro4
from attr import has


class User(object):
  name: str
  pets: Dict[str, Pyro4.Proxy]

  def __init__(self, name: str) -> None:
    self.name = None
    self.pets = {}

  def hasPet(self)-> boolean:
    if self.pets is None or len(self.pets) == 0:
      print("You don't own a pet yet. Try to adopt one")
      return False
    return True

  def doAction(self, action: str, pet: str):
    try:
      if (not self.hasPet()):
        return

      if action == "giveName":
        newPetName = input("Please, set another pet's name: ").strip()
        print(self.pets[pet].giveName(newPetName))
      elif action == "takeForAWalk":
        print(self.pets[pet].takeForAWalk())
      elif action == "pet":
        print(self.pets[pet].pet())
      elif action == "giveFood":
        print(self.pets[pet].giveFood())
      elif action == "takeToVet":
        print(self.pets[pet].takeToVet())
      elif action == "checkStatus":
        print(self.pets[pet].checkStatus())
      elif action == "getAge":
        print(self.pets[pet].getAge())
      elif action == "getHealth":
        print(self.pets[pet].getHealth())

      print("Invalid action")
    except Exception as e:
      print(e)


  def adopt(self):
    try:
      pet = Pyro4.Proxy(input("Insert pet uri: ").strip())
      petName = input("What name do you want to your pet? ").strip()
      print(petHouse.adopt())
      pet.giveName(petName)
      self.pets[petName] = pet
    except Exception as e:
      print("It's not possible to adopt a new pet. Try again later. Reason: \n")
      print(e)


petHouse = Pyro4.Proxy(input("Insert pet house uri: ").strip())
user = User(input("Please, insert your name: ").strip())


while True:
  print("What do you wanna do?")
  choice = int(input("1 - Adopt a new Pet\n2- Do Something to your puppy <3\n3-Exit\n").strip())

  if choice == 1:
    user.adopt()
  elif choice == 2:
    if not user.hasPet():
      continue
    action = input("Which action do you want to do? ").strip()
    petsName = input("Which pet do you want to do an action? ").strip()
    user.doAction(action, petsName)
  else:
    break
