from typing import Optional, Any, TypeAlias, Literal

import requests
from pydantic import validate_call
from requests import Response

JSON: TypeAlias = Any


@validate_call
def make_request(
        method: Literal["GET", "POST"],
        base_url: str,
        headers: dict,
        url: str,
        params: Optional[dict] = None,
        data: Optional[dict | list] = None,
        mode: Literal["raw", "txt", "json"] = "raw",
) -> Response | str | JSON:
    response: Response = requests.request(
        method=method,
        url=base_url + url,
        params=params,
        data=data,
        headers=headers,
    )
    if response.ok:
        if mode == "raw":
            return response
        elif mode == "txt":
            return response.text
        elif mode == "json":
            return response.json()
    else:
        print(response.raise_for_status())
