from abc import ABC

from entities.entity import Entity


class ImmovableEntity(Entity, ABC):
    pass

# class Wall(ImmovableEntity):
#     def __init__(self):
