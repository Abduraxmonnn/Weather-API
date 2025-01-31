from typing import Union

from django.db import models


class ColorCodesManager(models.Manager):
    def get_color_code(self, value: Union[int, float], category: str) -> str:
        """
        Returns the hex code for the given value and category.
        If no match is found, returns a default color (e.g., '#000000').
        """
        color_code = self.filter(
            start_point__lte=value,
            end_point__gte=value,
            category=category
        ).last()

        return color_code
