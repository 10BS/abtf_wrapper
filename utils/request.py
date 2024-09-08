from typing import Optional, Literal

import requests
from pydantic import validate_call
from requests import Response


@validate_call()
def make_request(
    method: Literal["GET", "POST", "PATCH"],
    base_url: str,
    url: str,
    headers: Optional[dict] = None,
    params: Optional[dict] = None,
    data: Optional[dict | list] = None,
    json: Optional[dict | list] = None,
    output: Literal["raw", "txt", "json"] | None = "raw",
) -> Response | str | dict:
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
