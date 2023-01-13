import httpx


class HttpClient:
    def __init__(self) -> None:
        pass

    @staticmethod
    async def get(
        url: str,
        headers: dict = None,
        timeout: float = 10.0,
        retries=2,
    ):
        async with httpx.AsyncClient(
            timeout=timeout, transport=httpx.AsyncHTTPTransport(retries=retries)
        ) as client:
            response = await client.get(url, headers=headers)
            response.raise_for_status
            return response