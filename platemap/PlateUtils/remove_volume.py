from ..plate import Plate


def remove_volume(
    target_plate: Plate,
    target_well: str,
    volume: int,
):
    """Remove volume from a well of a plate object

    Args:
        target_plate (Plate): target plate in which volume will be removed from,
        target_well (str): target well in which volume will be removed from,
        volume (float): volume of liquid to add to the specified well,

    Raises:
        ValueError: if volume well added passes well deadspace
    """
    if target_plate[target_well]["total_volume"] - volume >= target_plate.deadspace:
        for item in target_plate[target_well]["composition"]:
            volume_removed = (
                volume / target_plate[target_well]["total_volume"]
            ) * target_plate[target_well]["composition"][item]["volume"]
            new_volume = (
                target_plate[target_well]["composition"][item]["volume"]
                - volume_removed
            )
            print(new_volume)
            target_plate.update_well_composition(target_well, new_volume, item)
        target_plate.set_well_volume(
            target_well,
            target_plate[target_well]["total_volume"] - volume,
        )
    else:
        raise ValueError(
            f"attempted to subtract volume from plate: {target_plate.id} with deadspace ({target_plate.deadspace}) "
            f"by removing {volume} nanoliters to already present {target_plate[target_well]['total_volume']} "
            f"at plate location {target_well}"
        )
