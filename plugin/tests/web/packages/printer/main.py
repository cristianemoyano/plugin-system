from dataclasses import dataclass
from typing import Any, Protocol
import logging

logger: logging.Logger = logging.getLogger(__name__)


@dataclass
class PrinterPlugin:

    class Meta:
        plugin_name: str = 'printer'
        plugin_uri: str = 'N/A'
        plugin_description: str = 'Printer Plugin'
        version: str = '1.0.0'
        author: str = 'cmoyano'
        license: str = 'N/A'

    @staticmethod
    def register_activation_hook() -> None:
        logger.debug(f"register_activation_hook: {PrinterPlugin.Meta.plugin_name}")

    @staticmethod
    def register_deactivation_hook() -> None:
        logger.debug(f"register_deactivation_hook: {PrinterPlugin.Meta.plugin_name}")

    @staticmethod
    def register_uninstall_hook() -> None:
        logger.debug(f"register_uninstall_hook: {PrinterPlugin.Meta.plugin_name}")


def register() -> Protocol:
    return PrinterPlugin



class InternalHooks:
    GET_CARD_TITLE: str = 'get_card_title'
    GET_CARD_TEXT: str = 'get_card_text'
    GET_CARD_SMALL_TEXT: str = 'get_card_small_text'

# Actions

def get_card_title_callback() -> None:
    return 'A title from printer plugin'

def get_card_text_callback() -> None:
    return 'A card text from printer plugin'

def get_card_small_text_callback() -> None:
    return 'A smal text from printer plugin'



def add_actions() -> list[dict[str, Any]]:
    return [
        {
            'hook_name': InternalHooks.GET_CARD_TITLE,
            'callback': get_card_title_callback,
            'priority': 10,
        },
        {
            'hook_name': InternalHooks.GET_CARD_TEXT,
            'callback': get_card_text_callback,
            'priority': 10,
        },
                {
            'hook_name': InternalHooks.GET_CARD_SMALL_TEXT,
            'callback': get_card_small_text_callback,
            'priority': 10,
        },
    ]
