from ..plate import Plate


def find_well(
    target_plate: Plate,
    target_volume_id: str,
    target_volume: int,
):
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
