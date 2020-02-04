from geoalchemy2.shape import from_shape
from shapely.geometry import Point

from skylines.model import Airport


def merzbrueck(**kwargs):
    return Airport(
        name="Aachen Merzbruck",
        icao="EDKA",
        country_code="DE",
        altitude=189,
        location_wkt=from_shape(Point(6.186389, 50.823056), srid=4326),
        frequency=122.875,
        runway_len=520,
        runway_dir=80,
        surface="asphalt",
        type="airport",
    ).apply_kwargs(kwargs)


def meiersberg(**kwargs):
    return Airport(name=u"Meiersberg", country_code="DE").apply_kwargs(kwargs)
