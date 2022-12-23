from starlite import Controller, get

from icon_rhizome_dev.constants import API_PREFIX
from icon_rhizome_dev.models.governance import Validator


class AppGovernanceController(Controller):
    """
    A controller for routes relating to ICON governance.
    """

    path = f"/governance"

    @get(path="/")
    async def get_validators(self) -> list[Validator]:
        """
        Returns information about all ICON validators.
        """
        return
