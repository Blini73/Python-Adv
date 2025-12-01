from pydantic import Settings


class Setting(Settings):
    app_name: str
    admin_email: str
    items_per_user: int = 50

settings = Setting()