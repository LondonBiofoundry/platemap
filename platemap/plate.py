import uuid
import string
from typing import Literal, TypedDict, List, Dict
import math


class Composition_Item(TypedDict):
    volume: int
    concentration: int


class Contents(TypedDict):
    id: str
    total_volume: int
    composition: dict[str, Composition_Item]


class Plate:
    """Class for Plate objects.

    Generate a structure to handle plates and contents of wells

    Attributes:
        size (int): Number of wells within the plate.
        id (str): Unique identification of the plate object.
        deadspace (int): Volume of unaccessable / unreachable liquid within each well
        rows (list): row labels within plate e.g. ['A','B'...]
        columns (list): column labels within plate e.g. [1,2,3,4...]
        well_volume (int): volume of liquid within each well
    """

    def __init__(
        self,
        size: int,
        id: str = uuid.uuid4(),
        deadspace: int = None,
        rows: int = None,
        columns: int = None,
        well_volume: int = None,
    ):
        """Initiation object of Plate objects.

        Plate can be initiated which just size without rows and columns if size
        is of regular 2:3 ratio one of [6, 24, 96, 384, 1536]

        Args:
            size (int): Number of wells within the plate.
            id (str): Unique identification of the plate object.
            deadspace (int): Volume of unaccessable / unreachable liquid within each well
            rows (int): number of rows within the plate
            columns (int): number of columns within the plate
            well_volume (int): volume of liquid within each well

        Raises:
            ValueError: If rows or columns is a not a postive integer, or if rows and columns are
                not supplied and size is not regular 2:3 ratio.
        """
        self.size = size
        self.id = id
        self.deadspace = deadspace
        self.rows = rows
        self.columns = columns
        self.well_volume = well_volume
        self._test_input_validity()
        if rows:
            self.rows = [i for i in string.ascii_uppercase[:rows]]
        else:
            self.rows = [
                i for i in string.ascii_uppercase[: int(math.sqrt(self.size * (2 / 3)))]
            ]
        if columns:
            self.columns = [i for i in range(1, columns + 1)]
        else:
            self.columns = [
                i for i in range(1, int(math.sqrt(self.size * (3 / 2))) + 1)
            ]
        self.wells = [
            letter + str(number) for number in self.columns for letter in self.rows
        ]
        self.contents: Contents = {
            key: {"id": key, "total_volume": 0.0, "composition": {}}
            for key in self.wells
        }

    def __getitem__(self, k):
        """Return e.g. well A1's dict when calling myplate["A1"]."""
        return self.contents[k]

    def set_well_id(self, well: str, id: str):
        """Set id of individual wells"""
        self.contents[well]["id"] = id

    def set_well_volume(self, well: str, volume: int):
        """Set volume of individual wells"""
        self.contents[well]["total_volume"] = volume

    def update_well_composition(
        self, well: str, volume: int, volume_id: str, volume_concentration: int = None
    ):
        """Update composition of individual wells"""
        self.contents[well]["composition"].update(
            {volume_id: {"volume": volume, "concentration": volume_concentration}}
        )

    def _test_input_validity(self):
        if (
            self.size not in [6, 24, 96, 384, 1536]
            and self.rows == None
            and self.columns == None
        ):
            raise ValueError(
                "Plate size must be one of [6, 24, 96, 384, 1536] if rows and columns arent specified"
            )
        if self.columns:
            if self.columns <= 0:
                raise ValueError("Please use positive integer for columns")
        if self.rows:
            if self.rows <= 0:
                raise ValueError("Please use positive integer for rows")
