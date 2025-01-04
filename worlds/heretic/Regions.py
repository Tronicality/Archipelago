# This file is auto generated. More info: https://github.com/Daivuk/apdoom

from typing import List
from BaseClasses import TypedDict

class ConnectionDict(TypedDict, total=False):
    target: str
    pro: bool

class RegionDict(TypedDict, total=False):
    name: str
    connects_to_hub: bool
    episode: int
    connections: List[ConnectionDict]


regions:List[RegionDict] = [
    # The Docks (E1M1)
    {"name":"The Docks (E1M1) Main",
     "connects_to_hub":True,
     "episode":1,
     "connections":[{"target":"The Docks (E1M1) Yellow","pro":False}]},
    {"name":"The Docks (E1M1) Yellow",
     "connects_to_hub":False,
     "episode":1,
     "connections":[
        {"target":"The Docks (E1M1) Main","pro":False},
        {"target":"The Docks (E1M1) Sea","pro":False}]},
    {"name":"The Docks (E1M1) Sea",
     "connects_to_hub":False,
     "episode":1,
     "connections":[{"target":"The Docks (E1M1) Main","pro":False}]},

    # The Dungeons (E1M2)
    {"name":"The Dungeons (E1M2) Main",
     "connects_to_hub":True,
     "episode":1,
     "connections":[
        {"target":"The Dungeons (E1M2) Yellow","pro":False},
        {"target":"The Dungeons (E1M2) Green","pro":False}]},
    {"name":"The Dungeons (E1M2) Blue",
     "connects_to_hub":False,
     "episode":1,
     "connections":[{"target":"The Dungeons (E1M2) Yellow","pro":False}]},
    {"name":"The Dungeons (E1M2) Yellow",
     "connects_to_hub":False,
     "episode":1,
     "connections":[
        {"target":"The Dungeons (E1M2) Main","pro":False},
        {"target":"The Dungeons (E1M2) Blue","pro":False}]},
    {"name":"The Dungeons (E1M2) Green",
     "connects_to_hub":False,
     "episode":1,
     "connections":[
        {"target":"The Dungeons (E1M2) Main","pro":False},
        {"target":"The Dungeons (E1M2) Yellow","pro":False}]},

    # The Gatehouse (E1M3)
    {"name":"The Gatehouse (E1M3) Main",
     "connects_to_hub":True,
     "episode":1,
     "connections":[
        {"target":"The Gatehouse (E1M3) Yellow","pro":False},
        {"target":"The Gatehouse (E1M3) Sea","pro":False},
        {"target":"The Gatehouse (E1M3) Green","pro":False}]},
    {"name":"The Gatehouse (E1M3) Yellow",
     "connects_to_hub":False,
     "episode":1,
     "connections":[{"target":"The Gatehouse (E1M3) Main","pro":False}]},
    {"name":"The Gatehouse (E1M3) Green",
     "connects_to_hub":False,
     "episode":1,
     "connections":[{"target":"The Gatehouse (E1M3) Main","pro":False}]},
    {"name":"The Gatehouse (E1M3) Sea",
     "connects_to_hub":False,
     "episode":1,
     "connections":[{"target":"The Gatehouse (E1M3) Main","pro":False}]},

    # The Guard Tower (E1M4)
    {"name":"The Guard Tower (E1M4) Main",
     "connects_to_hub":True,
     "episode":1,
     "connections":[{"target":"The Guard Tower (E1M4) Yellow","pro":False}]},
    {"name":"The Guard Tower (E1M4) Yellow",
     "connects_to_hub":False,
     "episode":1,
     "connections":[
        {"target":"The Guard Tower (E1M4) Green","pro":False},
        {"target":"The Guard Tower (E1M4) Main","pro":False}]},
    {"name":"The Guard Tower (E1M4) Green",
     "connects_to_hub":False,
     "episode":1,
     "connections":[{"target":"The Guard Tower (E1M4) Yellow","pro":False}]},

    # The Citadel (E1M5)
    {"name":"The Citadel (E1M5) Main",
     "connects_to_hub":True,
     "episode":1,
     "connections":[{"target":"The Citadel (E1M5) Yellow","pro":False}]},
    {"name":"The Citadel (E1M5) Blue",
     "connects_to_hub":False,
     "episode":1,
     "connections":[{"target":"The Citadel (E1M5) Green","pro":False}]},
    {"name":"The Citadel (E1M5) Yellow",
     "connects_to_hub":False,
     "episode":1,
     "connections":[
        {"target":"The Citadel (E1M5) Main","pro":False},
        {"target":"The Citadel (E1M5) Well","pro":False},
        {"target":"The Citadel (E1M5) Green","pro":False}]},
    {"name":"The Citadel (E1M5) Green",
     "connects_to_hub":False,
     "episode":1,
     "connections":[
        {"target":"The Citadel (E1M5) Main","pro":False},
        {"target":"The Citadel (E1M5) Well","pro":False},
        {"target":"The Citadel (E1M5) Blue","pro":False}]},
    {"name":"The Citadel (E1M5) Well",
     "connects_to_hub":False,
     "episode":1,
     "connections":[{"target":"The Citadel (E1M5) Main","pro":False}]},

    # The Cathedral (E1M6)
    {"name":"The Cathedral (E1M6) Main",
     "connects_to_hub":True,
     "episode":1,
     "connections":[{"target":"The Cathedral (E1M6) Yellow","pro":False}]},
    {"name":"The Cathedral (E1M6) Yellow",
     "connects_to_hub":False,
     "episode":1,
     "connections":[
        {"target":"The Cathedral (E1M6) Green","pro":False},
        {"target":"The Cathedral (E1M6) Main","pro":False},
        {"target":"The Cathedral (E1M6) Main Fly","pro":False}]},
    {"name":"The Cathedral (E1M6) Green",
     "connects_to_hub":False,
     "episode":1,
     "connections":[
        {"target":"The Cathedral (E1M6) Yellow","pro":False},
        {"target":"The Cathedral (E1M6) Main Fly","pro":False}]},
    {"name":"The Cathedral (E1M6) Main Fly",
     "connects_to_hub":False,
     "episode":1,
     "connections":[{"target":"The Cathedral (E1M6) Main","pro":False}]},

    # The Crypts (E1M7)
    {"name":"The Crypts (E1M7) Main",
     "connects_to_hub":True,
     "episode":1,
     "connections":[
        {"target":"The Crypts (E1M7) Yellow","pro":False},
        {"target":"The Crypts (E1M7) Green","pro":False}]},
    {"name":"The Crypts (E1M7) Blue",
     "connects_to_hub":False,
     "episode":1,
     "connections":[
        {"target":"The Crypts (E1M7) Yellow","pro":False},
        {"target":"The Crypts (E1M7) Main","pro":False}]},
    {"name":"The Crypts (E1M7) Yellow",
     "connects_to_hub":False,
     "episode":1,
     "connections":[
        {"target":"The Crypts (E1M7) Main","pro":False},
        {"target":"The Crypts (E1M7) Green","pro":False},
        {"target":"The Crypts (E1M7) Blue","pro":False}]},
    {"name":"The Crypts (E1M7) Green",
     "connects_to_hub":False,
     "episode":1,
     "connections":[
        {"target":"The Crypts (E1M7) Yellow","pro":False},
        {"target":"The Crypts (E1M7) Main","pro":False}]},

    # Hell's Maw (E1M8)
    {"name":"Hell's Maw (E1M8) Main",
     "connects_to_hub":True,
     "episode":1,
     "connections":[]},

    # The Graveyard (E1M9)
    {"name":"The Graveyard (E1M9) Main",
     "connects_to_hub":True,
     "episode":1,
     "connections":[
        {"target":"The Graveyard (E1M9) Yellow","pro":False},
        {"target":"The Graveyard (E1M9) Green","pro":False},
        {"target":"The Graveyard (E1M9) Blue","pro":False}]},
    {"name":"The Graveyard (E1M9) Blue",
     "connects_to_hub":False,
     "episode":1,
     "connections":[{"target":"The Graveyard (E1M9) Main","pro":False}]},
    {"name":"The Graveyard (E1M9) Yellow",
     "connects_to_hub":False,
     "episode":1,
     "connections":[{"target":"The Graveyard (E1M9) Main","pro":False}]},
    {"name":"The Graveyard (E1M9) Green",
     "connects_to_hub":False,
     "episode":1,
     "connections":[{"target":"The Graveyard (E1M9) Main","pro":False}]},

    # The Crater (E2M1)
    {"name":"The Crater (E2M1) Main",
     "connects_to_hub":True,
     "episode":2,
     "connections":[{"target":"The Crater (E2M1) Yellow","pro":False}]},
    {"name":"The Crater (E2M1) Yellow",
     "connects_to_hub":False,
     "episode":2,
     "connections":[
        {"target":"The Crater (E2M1) Main","pro":False},
        {"target":"The Crater (E2M1) Green","pro":False}]},
    {"name":"The Crater (E2M1) Green",
     "connects_to_hub":False,
     "episode":2,
     "connections":[{"target":"The Crater (E2M1) Yellow","pro":False}]},

    # The Lava Pits (E2M2)
    {"name":"The Lava Pits (E2M2) Main",
     "connects_to_hub":True,
     "episode":2,
     "connections":[{"target":"The Lava Pits (E2M2) Yellow","pro":False}]},
    {"name":"The Lava Pits (E2M2) Yellow",
     "connects_to_hub":False,
     "episode":2,
     "connections":[
        {"target":"The Lava Pits (E2M2) Green","pro":False},
        {"target":"The Lava Pits (E2M2) Main","pro":False}]},
    {"name":"The Lava Pits (E2M2) Green",
     "connects_to_hub":False,
     "episode":2,
     "connections":[
        {"target":"The Lava Pits (E2M2) Main","pro":False},
        {"target":"The Lava Pits (E2M2) Yellow","pro":False}]},

    # The River of Fire (E2M3)
    {"name":"The River of Fire (E2M3) Main",
     "connects_to_hub":True,
     "episode":2,
     "connections":[
        {"target":"The River of Fire (E2M3) Yellow","pro":False},
        {"target":"The River of Fire (E2M3) Blue","pro":False},
        {"target":"The River of Fire (E2M3) Green","pro":False}]},
    {"name":"The River of Fire (E2M3) Blue",
     "connects_to_hub":False,
     "episode":2,
     "connections":[{"target":"The River of Fire (E2M3) Main","pro":False}]},
    {"name":"The River of Fire (E2M3) Yellow",
     "connects_to_hub":False,
     "episode":2,
     "connections":[{"target":"The River of Fire (E2M3) Main","pro":False}]},
    {"name":"The River of Fire (E2M3) Green",
     "connects_to_hub":False,
     "episode":2,
     "connections":[{"target":"The River of Fire (E2M3) Main","pro":False}]},

    # The Ice Grotto (E2M4)
    {"name":"The Ice Grotto (E2M4) Main",
     "connects_to_hub":True,
     "episode":2,
     "connections":[
        {"target":"The Ice Grotto (E2M4) Green","pro":False},
        {"target":"The Ice Grotto (E2M4) Yellow","pro":False}]},
    {"name":"The Ice Grotto (E2M4) Blue",
     "connects_to_hub":False,
     "episode":2,
     "connections":[{"target":"The Ice Grotto (E2M4) Green","pro":False}]},
    {"name":"The Ice Grotto (E2M4) Yellow",
     "connects_to_hub":False,
     "episode":2,
     "connections":[
        {"target":"The Ice Grotto (E2M4) Main","pro":False},
        {"target":"The Ice Grotto (E2M4) Magenta","pro":False}]},
    {"name":"The Ice Grotto (E2M4) Green",
     "connects_to_hub":False,
     "episode":2,
     "connections":[
        {"target":"The Ice Grotto (E2M4) Main","pro":False},
        {"target":"The Ice Grotto (E2M4) Blue","pro":False}]},
    {"name":"The Ice Grotto (E2M4) Magenta",
     "connects_to_hub":False,
     "episode":2,
     "connections":[{"target":"The Ice Grotto (E2M4) Yellow","pro":False}]},

    # The Catacombs (E2M5)
    {"name":"The Catacombs (E2M5) Main",
     "connects_to_hub":True,
     "episode":2,
     "connections":[{"target":"The Catacombs (E2M5) Yellow","pro":False}]},
    {"name":"The Catacombs (E2M5) Blue",
     "connects_to_hub":False,
     "episode":2,
     "connections":[{"target":"The Catacombs (E2M5) Green","pro":False}]},
    {"name":"The Catacombs (E2M5) Yellow",
     "connects_to_hub":False,
     "episode":2,
     "connections":[
        {"target":"The Catacombs (E2M5) Green","pro":False},
        {"target":"The Catacombs (E2M5) Main","pro":False}]},
    {"name":"The Catacombs (E2M5) Green",
     "connects_to_hub":False,
     "episode":2,
     "connections":[
        {"target":"The Catacombs (E2M5) Blue","pro":False},
        {"target":"The Catacombs (E2M5) Yellow","pro":False},
        {"target":"The Catacombs (E2M5) Main","pro":False}]},

    # The Labyrinth (E2M6)
    {"name":"The Labyrinth (E2M6) Main",
     "connects_to_hub":True,
     "episode":2,
     "connections":[
        {"target":"The Labyrinth (E2M6) Blue","pro":False},
        {"target":"The Labyrinth (E2M6) Yellow","pro":False},
        {"target":"The Labyrinth (E2M6) Green","pro":False}]},
    {"name":"The Labyrinth (E2M6) Blue",
     "connects_to_hub":False,
     "episode":2,
     "connections":[{"target":"The Labyrinth (E2M6) Main","pro":False}]},
    {"name":"The Labyrinth (E2M6) Yellow",
     "connects_to_hub":False,
     "episode":2,
     "connections":[{"target":"The Labyrinth (E2M6) Main","pro":False}]},
    {"name":"The Labyrinth (E2M6) Green",
     "connects_to_hub":False,
     "episode":2,
     "connections":[{"target":"The Labyrinth (E2M6) Main","pro":False}]},

    # The Great Hall (E2M7)
    {"name":"The Great Hall (E2M7) Main",
     "connects_to_hub":True,
     "episode":2,
     "connections":[
        {"target":"The Great Hall (E2M7) Yellow","pro":False},
        {"target":"The Great Hall (E2M7) Green","pro":False}]},
    {"name":"The Great Hall (E2M7) Blue",
     "connects_to_hub":False,
     "episode":2,
     "connections":[{"target":"The Great Hall (E2M7) Yellow","pro":False}]},
    {"name":"The Great Hall (E2M7) Yellow",
     "connects_to_hub":False,
     "episode":2,
     "connections":[
        {"target":"The Great Hall (E2M7) Blue","pro":False},
        {"target":"The Great Hall (E2M7) Main","pro":False}]},
    {"name":"The Great Hall (E2M7) Green",
     "connects_to_hub":False,
     "episode":2,
     "connections":[{"target":"The Great Hall (E2M7) Main","pro":False}]},

    # The Portals of Chaos (E2M8)
    {"name":"The Portals of Chaos (E2M8) Main",
     "connects_to_hub":True,
     "episode":2,
     "connections":[]},

    # The Glacier (E2M9)
    {"name":"The Glacier (E2M9) Main",
     "connects_to_hub":True,
     "episode":2,
     "connections":[
        {"target":"The Glacier (E2M9) Yellow","pro":False},
        {"target":"The Glacier (E2M9) Blue","pro":False},
        {"target":"The Glacier (E2M9) Green","pro":False}]},
    {"name":"The Glacier (E2M9) Blue",
     "connects_to_hub":False,
     "episode":2,
     "connections":[{"target":"The Glacier (E2M9) Main","pro":False}]},
    {"name":"The Glacier (E2M9) Yellow",
     "connects_to_hub":False,
     "episode":2,
     "connections":[{"target":"The Glacier (E2M9) Main","pro":False}]},
    {"name":"The Glacier (E2M9) Green",
     "connects_to_hub":False,
     "episode":2,
     "connections":[{"target":"The Glacier (E2M9) Main","pro":False}]},

    # The Storehouse (E3M1)
    {"name":"The Storehouse (E3M1) Main",
     "connects_to_hub":True,
     "episode":3,
     "connections":[
        {"target":"The Storehouse (E3M1) Yellow","pro":False},
        {"target":"The Storehouse (E3M1) Green","pro":False}]},
    {"name":"The Storehouse (E3M1) Yellow",
     "connects_to_hub":False,
     "episode":3,
     "connections":[{"target":"The Storehouse (E3M1) Main","pro":False}]},
    {"name":"The Storehouse (E3M1) Green",
     "connects_to_hub":False,
     "episode":3,
     "connections":[{"target":"The Storehouse (E3M1) Main","pro":False}]},

    # The Cesspool (E3M2)
    {"name":"The Cesspool (E3M2) Main",
     "connects_to_hub":True,
     "episode":3,
     "connections":[{"target":"The Cesspool (E3M2) Yellow","pro":False}]},
    {"name":"The Cesspool (E3M2) Blue",
     "connects_to_hub":False,
     "episode":3,
     "connections":[{"target":"The Cesspool (E3M2) Green","pro":False}]},
    {"name":"The Cesspool (E3M2) Yellow",
     "connects_to_hub":False,
     "episode":3,
     "connections":[
        {"target":"The Cesspool (E3M2) Main","pro":False},
        {"target":"The Cesspool (E3M2) Green","pro":False}]},
    {"name":"The Cesspool (E3M2) Green",
     "connects_to_hub":False,
     "episode":3,
     "connections":[
        {"target":"The Cesspool (E3M2) Blue","pro":False},
        {"target":"The Cesspool (E3M2) Main","pro":False},
        {"target":"The Cesspool (E3M2) Yellow","pro":False}]},

    # The Confluence (E3M3)
    {"name":"The Confluence (E3M3) Main",
     "connects_to_hub":True,
     "episode":3,
     "connections":[
        {"target":"The Confluence (E3M3) Green","pro":False},
        {"target":"The Confluence (E3M3) Yellow","pro":False}]},
    {"name":"The Confluence (E3M3) Blue",
     "connects_to_hub":False,
     "episode":3,
     "connections":[{"target":"The Confluence (E3M3) Green","pro":False}]},
    {"name":"The Confluence (E3M3) Yellow",
     "connects_to_hub":False,
     "episode":3,
     "connections":[{"target":"The Confluence (E3M3) Main","pro":False}]},
    {"name":"The Confluence (E3M3) Green",
     "connects_to_hub":False,
     "episode":3,
     "connections":[
        {"target":"The Confluence (E3M3) Main","pro":False},
        {"target":"The Confluence (E3M3) Blue","pro":False},
        {"target":"The Confluence (E3M3) Yellow","pro":False}]},

    # The Azure Fortress (E3M4)
    {"name":"The Azure Fortress (E3M4) Main",
     "connects_to_hub":True,
     "episode":3,
     "connections":[
        {"target":"The Azure Fortress (E3M4) Green","pro":False},
        {"target":"The Azure Fortress (E3M4) Yellow","pro":False}]},
    {"name":"The Azure Fortress (E3M4) Yellow",
     "connects_to_hub":False,
     "episode":3,
     "connections":[{"target":"The Azure Fortress (E3M4) Main","pro":False}]},
    {"name":"The Azure Fortress (E3M4) Green",
     "connects_to_hub":False,
     "episode":3,
     "connections":[{"target":"The Azure Fortress (E3M4) Main","pro":False}]},

    # The Ophidian Lair (E3M5)
    {"name":"The Ophidian Lair (E3M5) Main",
     "connects_to_hub":True,
     "episode":3,
     "connections":[
        {"target":"The Ophidian Lair (E3M5) Yellow","pro":False},
        {"target":"The Ophidian Lair (E3M5) Green","pro":False}]},
    {"name":"The Ophidian Lair (E3M5) Yellow",
     "connects_to_hub":False,
     "episode":3,
     "connections":[{"target":"The Ophidian Lair (E3M5) Main","pro":False}]},
    {"name":"The Ophidian Lair (E3M5) Green",
     "connects_to_hub":False,
     "episode":3,
     "connections":[{"target":"The Ophidian Lair (E3M5) Main","pro":False}]},

    # The Halls of Fear (E3M6)
    {"name":"The Halls of Fear (E3M6) Main",
     "connects_to_hub":True,
     "episode":3,
     "connections":[{"target":"The Halls of Fear (E3M6) Yellow","pro":False}]},
    {"name":"The Halls of Fear (E3M6) Blue",
     "connects_to_hub":False,
     "episode":3,
     "connections":[
        {"target":"The Halls of Fear (E3M6) Yellow","pro":False},
        {"target":"The Halls of Fear (E3M6) Cyan","pro":False}]},
    {"name":"The Halls of Fear (E3M6) Yellow",
     "connects_to_hub":False,
     "episode":3,
     "connections":[
        {"target":"The Halls of Fear (E3M6) Blue","pro":False},
        {"target":"The Halls of Fear (E3M6) Main","pro":False},
        {"target":"The Halls of Fear (E3M6) Green","pro":False}]},
    {"name":"The Halls of Fear (E3M6) Green",
     "connects_to_hub":False,
     "episode":3,
     "connections":[
        {"target":"The Halls of Fear (E3M6) Yellow","pro":False},
        {"target":"The Halls of Fear (E3M6) Main","pro":False},
        {"target":"The Halls of Fear (E3M6) Cyan","pro":False}]},
    {"name":"The Halls of Fear (E3M6) Cyan",
     "connects_to_hub":False,
     "episode":3,
     "connections":[
        {"target":"The Halls of Fear (E3M6) Yellow","pro":False},
        {"target":"The Halls of Fear (E3M6) Main","pro":False}]},

    # The Chasm (E3M7)
    {"name":"The Chasm (E3M7) Main",
     "connects_to_hub":True,
     "episode":3,
     "connections":[{"target":"The Chasm (E3M7) Yellow","pro":False}]},
    {"name":"The Chasm (E3M7) Blue",
     "connects_to_hub":False,
     "episode":3,
     "connections":[]},
    {"name":"The Chasm (E3M7) Yellow",
     "connects_to_hub":False,
     "episode":3,
     "connections":[
        {"target":"The Chasm (E3M7) Main","pro":False},
        {"target":"The Chasm (E3M7) Green","pro":False},
        {"target":"The Chasm (E3M7) Blue","pro":False}]},
    {"name":"The Chasm (E3M7) Green",
     "connects_to_hub":False,
     "episode":3,
     "connections":[{"target":"The Chasm (E3M7) Yellow","pro":False}]},

    # D'Sparil'S Keep (E3M8)
    {"name":"D'Sparil'S Keep (E3M8) Main",
     "connects_to_hub":True,
     "episode":3,
     "connections":[]},

    # The Aquifier (E3M9)
    {"name":"The Aquifier (E3M9) Main",
     "connects_to_hub":True,
     "episode":3,
     "connections":[{"target":"The Aquifier (E3M9) Yellow","pro":False}]},
    {"name":"The Aquifier (E3M9) Blue",
     "connects_to_hub":False,
     "episode":3,
     "connections":[]},
    {"name":"The Aquifier (E3M9) Yellow",
     "connects_to_hub":False,
     "episode":3,
     "connections":[
        {"target":"The Aquifier (E3M9) Green","pro":False},
        {"target":"The Aquifier (E3M9) Main","pro":False}]},
    {"name":"The Aquifier (E3M9) Green",
     "connects_to_hub":False,
     "episode":3,
     "connections":[
        {"target":"The Aquifier (E3M9) Yellow","pro":False},
        {"target":"The Aquifier (E3M9) Main","pro":False},
        {"target":"The Aquifier (E3M9) Blue","pro":False}]},

    # Catafalque (E4M1)
    {"name":"Catafalque (E4M1) Main",
     "connects_to_hub":True,
     "episode":4,
     "connections":[{"target":"Catafalque (E4M1) Yellow","pro":False}]},
    {"name":"Catafalque (E4M1) Yellow",
     "connects_to_hub":False,
     "episode":4,
     "connections":[
        {"target":"Catafalque (E4M1) Green","pro":False},
        {"target":"Catafalque (E4M1) Main","pro":False}]},
    {"name":"Catafalque (E4M1) Green",
     "connects_to_hub":False,
     "episode":4,
     "connections":[{"target":"Catafalque (E4M1) Main","pro":False}]},

    # Blockhouse (E4M2)
    {"name":"Blockhouse (E4M2) Main",
     "connects_to_hub":True,
     "episode":4,
     "connections":[
        {"target":"Blockhouse (E4M2) Yellow","pro":False},
        {"target":"Blockhouse (E4M2) Green","pro":False},
        {"target":"Blockhouse (E4M2) Blue","pro":False}]},
    {"name":"Blockhouse (E4M2) Yellow",
     "connects_to_hub":False,
     "episode":4,
     "connections":[
        {"target":"Blockhouse (E4M2) Main","pro":False},
        {"target":"Blockhouse (E4M2) Balcony","pro":False},
        {"target":"Blockhouse (E4M2) Lake","pro":False}]},
    {"name":"Blockhouse (E4M2) Green",
     "connects_to_hub":False,
     "episode":4,
     "connections":[{"target":"Blockhouse (E4M2) Main","pro":False}]},
    {"name":"Blockhouse (E4M2) Blue",
     "connects_to_hub":False,
     "episode":4,
     "connections":[{"target":"Blockhouse (E4M2) Main","pro":False}]},
    {"name":"Blockhouse (E4M2) Lake",
     "connects_to_hub":False,
     "episode":4,
     "connections":[{"target":"Blockhouse (E4M2) Balcony","pro":False}]},
    {"name":"Blockhouse (E4M2) Balcony",
     "connects_to_hub":False,
     "episode":4,
     "connections":[]},

    # Ambulatory (E4M3)
    {"name":"Ambulatory (E4M3) Main",
     "connects_to_hub":True,
     "episode":4,
     "connections":[
        {"target":"Ambulatory (E4M3) Blue","pro":False},
        {"target":"Ambulatory (E4M3) Yellow","pro":False},
        {"target":"Ambulatory (E4M3) Green","pro":False},
        {"target":"Ambulatory (E4M3) Green Lock","pro":False}]},
    {"name":"Ambulatory (E4M3) Blue",
     "connects_to_hub":False,
     "episode":4,
     "connections":[
        {"target":"Ambulatory (E4M3) Yellow","pro":False},
        {"target":"Ambulatory (E4M3) Green","pro":False}]},
    {"name":"Ambulatory (E4M3) Yellow",
     "connects_to_hub":False,
     "episode":4,
     "connections":[{"target":"Ambulatory (E4M3) Main","pro":False}]},
    {"name":"Ambulatory (E4M3) Green",
     "connects_to_hub":False,
     "episode":4,
     "connections":[{"target":"Ambulatory (E4M3) Main","pro":False}]},
    {"name":"Ambulatory (E4M3) Green Lock",
     "connects_to_hub":False,
     "episode":4,
     "connections":[
        {"target":"Ambulatory (E4M3) Green","pro":False},
        {"target":"Ambulatory (E4M3) Main","pro":False}]},

    # Sepulcher (E4M4)
    {"name":"Sepulcher (E4M4) Main",
     "connects_to_hub":True,
     "episode":4,
     "connections":[]},

    # Great Stair (E4M5)
    {"name":"Great Stair (E4M5) Main",
     "connects_to_hub":True,
     "episode":4,
     "connections":[{"target":"Great Stair (E4M5) Yellow","pro":False}]},
    {"name":"Great Stair (E4M5) Blue",
     "connects_to_hub":False,
     "episode":4,
     "connections":[{"target":"Great Stair (E4M5) Green","pro":False}]},
    {"name":"Great Stair (E4M5) Yellow",
     "connects_to_hub":False,
     "episode":4,
     "connections":[
        {"target":"Great Stair (E4M5) Main","pro":False},
        {"target":"Great Stair (E4M5) Green","pro":False}]},
    {"name":"Great Stair (E4M5) Green",
     "connects_to_hub":False,
     "episode":4,
     "connections":[
        {"target":"Great Stair (E4M5) Blue","pro":False},
        {"target":"Great Stair (E4M5) Yellow","pro":False}]},

    # Halls of the Apostate (E4M6)
    {"name":"Halls of the Apostate (E4M6) Main",
     "connects_to_hub":True,
     "episode":4,
     "connections":[{"target":"Halls of the Apostate (E4M6) Yellow","pro":False}]},
    {"name":"Halls of the Apostate (E4M6) Blue",
     "connects_to_hub":False,
     "episode":4,
     "connections":[{"target":"Halls of the Apostate (E4M6) Green","pro":False}]},
    {"name":"Halls of the Apostate (E4M6) Yellow",
     "connects_to_hub":False,
     "episode":4,
     "connections":[
        {"target":"Halls of the Apostate (E4M6) Main","pro":False},
        {"target":"Halls of the Apostate (E4M6) Green","pro":False}]},
    {"name":"Halls of the Apostate (E4M6) Green",
     "connects_to_hub":False,
     "episode":4,
     "connections":[
        {"target":"Halls of the Apostate (E4M6) Yellow","pro":False},
        {"target":"Halls of the Apostate (E4M6) Blue","pro":False}]},

    # Ramparts of Perdition (E4M7)
    {"name":"Ramparts of Perdition (E4M7) Main",
     "connects_to_hub":True,
     "episode":4,
     "connections":[{"target":"Ramparts of Perdition (E4M7) Yellow","pro":False}]},
    {"name":"Ramparts of Perdition (E4M7) Blue",
     "connects_to_hub":False,
     "episode":4,
     "connections":[{"target":"Ramparts of Perdition (E4M7) Yellow","pro":False}]},
    {"name":"Ramparts of Perdition (E4M7) Yellow",
     "connects_to_hub":False,
     "episode":4,
     "connections":[
        {"target":"Ramparts of Perdition (E4M7) Main","pro":False},
        {"target":"Ramparts of Perdition (E4M7) Green","pro":False},
        {"target":"Ramparts of Perdition (E4M7) Blue","pro":False}]},
    {"name":"Ramparts of Perdition (E4M7) Green",
     "connects_to_hub":False,
     "episode":4,
     "connections":[{"target":"Ramparts of Perdition (E4M7) Yellow","pro":False}]},

    # Shattered Bridge (E4M8)
    {"name":"Shattered Bridge (E4M8) Main",
     "connects_to_hub":True,
     "episode":4,
     "connections":[{"target":"Shattered Bridge (E4M8) Yellow","pro":False}]},
    {"name":"Shattered Bridge (E4M8) Yellow",
     "connects_to_hub":False,
     "episode":4,
     "connections":[
        {"target":"Shattered Bridge (E4M8) Main","pro":False},
        {"target":"Shattered Bridge (E4M8) Boss","pro":False}]},
    {"name":"Shattered Bridge (E4M8) Boss",
     "connects_to_hub":False,
     "episode":4,
     "connections":[]},

    # Mausoleum (E4M9)
    {"name":"Mausoleum (E4M9) Main",
     "connects_to_hub":True,
     "episode":4,
     "connections":[{"target":"Mausoleum (E4M9) Yellow","pro":False}]},
    {"name":"Mausoleum (E4M9) Yellow",
     "connects_to_hub":False,
     "episode":4,
     "connections":[{"target":"Mausoleum (E4M9) Main","pro":False}]},

    # Ochre Cliffs (E5M1)
    {"name":"Ochre Cliffs (E5M1) Main",
     "connects_to_hub":True,
     "episode":5,
     "connections":[{"target":"Ochre Cliffs (E5M1) Yellow","pro":False}]},
    {"name":"Ochre Cliffs (E5M1) Blue",
     "connects_to_hub":False,
     "episode":5,
     "connections":[{"target":"Ochre Cliffs (E5M1) Yellow","pro":False}]},
    {"name":"Ochre Cliffs (E5M1) Yellow",
     "connects_to_hub":False,
     "episode":5,
     "connections":[
        {"target":"Ochre Cliffs (E5M1) Main","pro":False},
        {"target":"Ochre Cliffs (E5M1) Green","pro":False},
        {"target":"Ochre Cliffs (E5M1) Blue","pro":False}]},
    {"name":"Ochre Cliffs (E5M1) Green",
     "connects_to_hub":False,
     "episode":5,
     "connections":[{"target":"Ochre Cliffs (E5M1) Yellow","pro":False}]},

    # Rapids (E5M2)
    {"name":"Rapids (E5M2) Main",
     "connects_to_hub":True,
     "episode":5,
     "connections":[{"target":"Rapids (E5M2) Yellow","pro":False}]},
    {"name":"Rapids (E5M2) Yellow",
     "connects_to_hub":False,
     "episode":5,
     "connections":[
        {"target":"Rapids (E5M2) Main","pro":False},
        {"target":"Rapids (E5M2) Green","pro":False}]},
    {"name":"Rapids (E5M2) Green",
     "connects_to_hub":False,
     "episode":5,
     "connections":[
        {"target":"Rapids (E5M2) Yellow","pro":False},
        {"target":"Rapids (E5M2) Main","pro":False}]},

    # Quay (E5M3)
    {"name":"Quay (E5M3) Main",
     "connects_to_hub":True,
     "episode":5,
     "connections":[
        {"target":"Quay (E5M3) Yellow","pro":False},
        {"target":"Quay (E5M3) Green","pro":False},
        {"target":"Quay (E5M3) Blue","pro":False}]},
    {"name":"Quay (E5M3) Blue",
     "connects_to_hub":False,
     "episode":5,
     "connections":[{"target":"Quay (E5M3) Main","pro":False}]},
    {"name":"Quay (E5M3) Yellow",
     "connects_to_hub":False,
     "episode":5,
     "connections":[{"target":"Quay (E5M3) Main","pro":False}]},
    {"name":"Quay (E5M3) Green",
     "connects_to_hub":False,
     "episode":5,
     "connections":[
        {"target":"Quay (E5M3) Main","pro":False},
        {"target":"Quay (E5M3) Cyan","pro":False}]},
    {"name":"Quay (E5M3) Cyan",
     "connects_to_hub":False,
     "episode":5,
     "connections":[{"target":"Quay (E5M3) Main","pro":False}]},

    # Courtyard (E5M4)
    {"name":"Courtyard (E5M4) Main",
     "connects_to_hub":True,
     "episode":5,
     "connections":[
        {"target":"Courtyard (E5M4) Kakis","pro":False},
        {"target":"Courtyard (E5M4) Blue","pro":False}]},
    {"name":"Courtyard (E5M4) Blue",
     "connects_to_hub":False,
     "episode":5,
     "connections":[{"target":"Courtyard (E5M4) Main","pro":False}]},
    {"name":"Courtyard (E5M4) Kakis",
     "connects_to_hub":False,
     "episode":5,
     "connections":[{"target":"Courtyard (E5M4) Main","pro":False}]},

    # Hydratyr (E5M5)
    {"name":"Hydratyr (E5M5) Main",
     "connects_to_hub":True,
     "episode":5,
     "connections":[{"target":"Hydratyr (E5M5) Yellow","pro":False}]},
    {"name":"Hydratyr (E5M5) Blue",
     "connects_to_hub":False,
     "episode":5,
     "connections":[{"target":"Hydratyr (E5M5) Green","pro":False}]},
    {"name":"Hydratyr (E5M5) Yellow",
     "connects_to_hub":False,
     "episode":5,
     "connections":[
        {"target":"Hydratyr (E5M5) Main","pro":False},
        {"target":"Hydratyr (E5M5) Green","pro":False}]},
    {"name":"Hydratyr (E5M5) Green",
     "connects_to_hub":False,
     "episode":5,
     "connections":[
        {"target":"Hydratyr (E5M5) Main","pro":False},
        {"target":"Hydratyr (E5M5) Yellow","pro":False},
        {"target":"Hydratyr (E5M5) Blue","pro":False}]},

    # Colonnade (E5M6)
    {"name":"Colonnade (E5M6) Main",
     "connects_to_hub":True,
     "episode":5,
     "connections":[
        {"target":"Colonnade (E5M6) Yellow","pro":False},
        {"target":"Colonnade (E5M6) Blue","pro":False}]},
    {"name":"Colonnade (E5M6) Blue",
     "connects_to_hub":False,
     "episode":5,
     "connections":[{"target":"Colonnade (E5M6) Main","pro":False}]},
    {"name":"Colonnade (E5M6) Yellow",
     "connects_to_hub":False,
     "episode":5,
     "connections":[
        {"target":"Colonnade (E5M6) Main","pro":False},
        {"target":"Colonnade (E5M6) Green","pro":False}]},
    {"name":"Colonnade (E5M6) Green",
     "connects_to_hub":False,
     "episode":5,
     "connections":[{"target":"Colonnade (E5M6) Yellow","pro":False}]},

    # Foetid Manse (E5M7)
    {"name":"Foetid Manse (E5M7) Main",
     "connects_to_hub":True,
     "episode":5,
     "connections":[{"target":"Foetid Manse (E5M7) Yellow","pro":False}]},
    {"name":"Foetid Manse (E5M7) Blue",
     "connects_to_hub":False,
     "episode":5,
     "connections":[{"target":"Foetid Manse (E5M7) Yellow","pro":False}]},
    {"name":"Foetid Manse (E5M7) Yellow",
     "connects_to_hub":False,
     "episode":5,
     "connections":[
        {"target":"Foetid Manse (E5M7) Main","pro":False},
        {"target":"Foetid Manse (E5M7) Green","pro":False},
        {"target":"Foetid Manse (E5M7) Blue","pro":False}]},
    {"name":"Foetid Manse (E5M7) Green",
     "connects_to_hub":False,
     "episode":5,
     "connections":[
        {"target":"Foetid Manse (E5M7) Yellow","pro":False},
        {"target":"Foetid Manse (E5M7) Main","pro":False}]},

    # Field of Judgement (E5M8)
    {"name":"Field of Judgement (E5M8) Main",
     "connects_to_hub":True,
     "episode":5,
     "connections":[]},

    # Skein of D'Sparil (E5M9)
    {"name":"Skein of D'Sparil (E5M9) Main",
     "connects_to_hub":True,
     "episode":5,
     "connections":[
        {"target":"Skein of D'Sparil (E5M9) Blue","pro":False},
        {"target":"Skein of D'Sparil (E5M9) Yellow","pro":False},
        {"target":"Skein of D'Sparil (E5M9) Green","pro":False}]},
    {"name":"Skein of D'Sparil (E5M9) Blue",
     "connects_to_hub":False,
     "episode":5,
     "connections":[{"target":"Skein of D'Sparil (E5M9) Main","pro":False}]},
    {"name":"Skein of D'Sparil (E5M9) Yellow",
     "connects_to_hub":False,
     "episode":5,
     "connections":[{"target":"Skein of D'Sparil (E5M9) Main","pro":False}]},
    {"name":"Skein of D'Sparil (E5M9) Green",
     "connects_to_hub":False,
     "episode":5,
     "connections":[{"target":"Skein of D'Sparil (E5M9) Main","pro":False}]},
]