from .config import settings
from .handlers import error_handler, print_handler
from pydrinker_gcp.routes import SubscriptionRoute

provider_options = {
    "options": {
        "deadline": settings.SUBSCRIPTION_RETRY_TIMEOUT,
        "max_messages": settings.MAX_MESSAGES_PER_PULL,
        "timeout": settings.SUBSCRIPTION_TIMEOUT,
    }
}

routes = (
    SubscriptionRoute(
        project_id=settings.PROJECT_ID,
        subscription_id=settings.SUBSCRIPTION_ID,
        provider_options=provider_options,
        handler=print_handler,
        error_handler=error_handler,
    ),
)
