from ..plate import Plate
from .add_volume import add_volume
import math


def assign_source_wells(
    plate: Plate, input_dict: dict[str, float], fill_to: int = None
):
    useable_liquid_per_well = (
        fill_to - plate.deadspace if fill_to else plate.well_volume - plate.deadspace
    )
    well_index = 0
    for item in input_dict:
        for well_needed in range(
            math.ceil(
                input_dict[item]
                / (
                    fill_to - plate.deadspace
                    if fill_to
                    else plate.well_volume - plate.deadspace
                )
            )
        ):
            plate.set_well_id(plate.wells[well_index], item)
            add_volume(
                plate,
                plate.wells[well_index],
                fill_to if fill_to else plate.well_volume,
                item,
            )
            well_index += 1
