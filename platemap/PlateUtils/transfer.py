from ..plate import Plate
from .remove_volume import remove_volume
from .add_volume import add_volume


def transfer(
    source_plate: Plate,
    source_well: str,
    destination_plate: Plate,
    destination_well: str,
    volume: int,
):
    """Transfer volume from one well within a plate object to another well within a plate object

    Args:
        source_plate (Plate): source plate in which volume will be taken from,
        source_well (str): source well in which volume will be taken from,
        destination_plate (Plate): target plate in which volume will be added to,
        destination_well (str): target well in which volume will be added to,
        volume (float): volume of liquid to add to the specified well,

    Raises:
        ValueError: if volume in destination well added exceeds well capacity or volume in source
            well will drop below deadspace
    """
    if (
        destination_plate[destination_well]["total_volume"] + volume
        <= destination_plate.well_volume
    ):
        if source_plate[source_well]["total_volume"] - volume >= source_plate.deadspace:
            for item in source_plate[source_well]["composition"]:
                add_volume(
                    destination_plate,
                    destination_well,
                    (
                        source_plate[source_well]["composition"][item]["volume"]
                        / source_plate[source_well]["total_volume"]
                    )
                    * volume,
                    item,
                    source_plate[source_well]["composition"][item]["concentration"],
                )
            remove_volume(source_plate, source_well, volume)
        else:
            raise ValueError(
                f"attempted to subtract volume from plate: {source_plate.id} with deadspace ({source_plate.deadspace}) "
                f"by removing {volume} nanoliters to already present {source_plate[source_well]['total_volume']} "
                f"at plate location {source_well}"
            )
    else:
        raise ValueError(
            f"attempted to exceed plate: {destination_plate.id} with capacity ({destination_plate.well_volume}) "
            f"by adding {volume} nanoliters to already present {destination_plate[destination_well]['total_volume']} "
            f"at plate location {destination_well}"
        )
