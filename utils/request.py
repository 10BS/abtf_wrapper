from typing import Optional, Any, TypeAlias, Literal

import requests
from pydantic import validate_call
from requests import Response

JSON: TypeAlias = Any


@validate_call()
def make_request(
    method: Literal["GET", "POST"],
    base_url: str,
    headers: dict,
    url: str,
    params: Optional[dict] = None,
    data: Optional[dict | list] = None,
    json: Optional[dict | list] = None,
    output: Literal["raw", "txt", "json"] = "raw",
) -> Response | str | JSON:
    response: Response = requests.request(
        method=method,
        url=base_url + url,
        params=params,
        data=data,
        json=json,
        headers=headers,
    )
    if response.ok:
        if output == "raw":
            return response
        elif output == "txt":
            return response.text
        elif output == "json":
            return response.json()
    else:
        print(response.raise_for_status())
