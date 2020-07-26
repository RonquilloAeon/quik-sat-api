import httpx

"""
{
    "FALCON 9 DEB" : {
        "name": "FALCON 9 DEB",
        "catalog_number": 12345
        "classification": "U",
    }
}
"""
SATELLITES = {}


def _load_satellites(data: str):
    satellite_data = [d.strip() for d in data.split("\r\n") if d != ""]
    satellite_data = [
        satellite_data[i : i + 3] for i in range(0, len(satellite_data), 3)
    ]

    for satellite in satellite_data:
        line_1 = satellite[1].split(" ")
        name = (satellite[0],)
        catalog_number = line_1[1][:5]
        classification = line_1[1][-1:]

        SATELLITES[name] = {
            "name": name,
            "catalog_number": catalog_number,
            "classification": classification,
        }


async def get_satellites(path: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(path)

        _load_satellites(response.text)
