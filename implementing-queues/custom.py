from dataclasses import dataclass

@dataclass
class Message:
    event: str

wipers = Message("Windshield wipers turned on")
hazard_lights = Message("Hazard lights turned on")

print(wipers < hazard_lights)