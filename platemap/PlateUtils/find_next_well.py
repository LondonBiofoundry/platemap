from ..plate import Plate


def find_well(
    target_plate: Plate,
    target_volume_id: str,
    target_volume: int,
):
    """Finds the next available well for a specific reagent-id that has sufficient volume defined by the third input argument.

    Args:
        target_plate (Plate): The target plate to analyse.
        target_volume_id (str): The regaent ID that you are looking for.
        target_volume (int): The volume that you are looking to take.

    """
    try:
        return list(
            filter(
                lambda x: target_plate[x]["composition"][target_volume_id]["volume"]
                >= (target_plate.deadspace + target_volume),
                list(
                    filter(
                        lambda x: target_volume_id in target_plate[x]["composition"],
                        target_plate.wells,
                    )
                ),
            )
        )[0]
    except:
        return 0
