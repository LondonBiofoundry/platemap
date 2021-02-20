from ..plate import Plate


def add_volume(
    destination_plate: Plate,
    destination_well: str,
    volume: float,
    volume_id: str,
    volume_concentration: int = None,
):
    """Add volume to a well of a plate object

    Args:
        destination_plate (Plate): target plate in which volume will be added to,
        destination_well (str): target well in which volume will be added to,
        volume (float): volume of liquid to add to the specified well,
        volume_id (str): identifier of liquid to be added to specified well,
        volume_concentration (int): concentraion of liquid to be added to specified well,

    Raises:
        ValueError: if volume well added exceeds well capacity
    """
    if (
        destination_plate[destination_well]["total_volume"] + volume
        <= destination_plate.well_volume
    ):
        destination_plate.set_well_volume(
            destination_well,
            float(destination_plate[destination_well]["total_volume"] + volume),
        )
        if volume_id in destination_plate[destination_well]["composition"]:
            new_volume = (
                destination_plate[destination_well]["composition"][volume_id]["volume"]
                + volume
            )
            destination_plate.update_well_composition(
                destination_well, new_volume, volume_id
            )
        else:
            destination_plate.update_well_composition(
                destination_well, volume, volume_id
            )
    else:
        raise ValueError(
            f"attempted to exceed plate: {destination_plate.id} with capacity ({destination_plate.well_volume}) "
            f"by adding {volume} nanoliters to already present {destination_plate[destination_well]['total_volume']} "
            f"at plate location {destination_well}"
        )
