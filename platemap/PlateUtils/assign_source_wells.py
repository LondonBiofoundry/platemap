from ..plate import Plate
from .add_volume import add_volume
import math
from typing import Dict


def assign_source_wells(
    plate: Plate,
    input_dict: Dict[str, float],
    fill_to: int = None,
    alternate_wells=False,
):
    """Assign source wells to a plate on bulk through a dictionary of input reagent id's and their respective volumes.

    Args:
        plate (Plate): target plate in which to fill with reagents from the input_dict,
        input_dict (Dict[str, float]): A dictionary of reagent names and their corresponding volumes,
        fill_to (Dict[str, float]): Amount to fill to in each well. If None, fill to the maximum volume.
        alternate_wells (boolean): Whether to use every other well in the plate. Sometimes useful for 384 well plates.

    """
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
            if not alternate_wells:
                plate.set_well_id(plate.wells[well_index], item)
                add_volume(
                    plate,
                    plate.wells[well_index],
                    fill_to if fill_to else plate.well_volume,
                    item,
                )
            else:
                plate.set_well_id(plate.wells[well_index * 2], item)
                add_volume(
                    plate,
                    plate.wells[well_index * 2],
                    fill_to if fill_to else plate.well_volume,
                    item,
                )
            well_index += 1
