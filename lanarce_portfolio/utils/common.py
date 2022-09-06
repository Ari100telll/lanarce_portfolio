from typing import Any, Dict, List, Tuple, TypeVar

from django.db import models

DjangoModelType = TypeVar("DjangoModelType", bound=models.Model)


def model_update(
    *,
    instance: DjangoModelType,
    fields: List[str],
    data: Dict[str, Any],
) -> Tuple[DjangoModelType, bool]:
    has_updated = False

    for field in fields:
        if field not in data:
            continue

        if getattr(instance, field) != data[field]:
            has_updated = True
            setattr(instance, field, data[field])

    if has_updated:
        instance.full_clean()
        instance.save(update_fields=fields)

    return instance, has_updated
