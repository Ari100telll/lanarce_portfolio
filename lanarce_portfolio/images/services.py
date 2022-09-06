from django.contrib.auth import get_user_model

from lanarce_portfolio.images.models import Image
from lanarce_portfolio.portfolios.models import Portfolio
from lanarce_portfolio.utils.common import model_update

User = get_user_model()


def create_image(
        *,
        portfolio: Portfolio,
        name: str,
        description: str,
        file,
) -> Image:
    image = Image.objects.create(
        portfolio=portfolio,
        name=name,
        description=description,
        file=file
    )
    return image


def update_image(
        *,
        image: Image,
        **image_details,
) -> Image:
    updated_image, _ = model_update(
        instance=image,
        fields=list(image_details.keys()),
        data=image_details
    )

    return updated_image


def delete_image(
        *,
        image: Image,
) -> None:
    image.delete()
