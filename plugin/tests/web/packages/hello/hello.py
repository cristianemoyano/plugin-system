from dataclasses import dataclass
from typing import Any, Protocol


@dataclass
class HelloPlugin:

    class Meta:
        plugin_name: str = 'hello'
        plugin_uri: str = 'N/A'
        plugin_description: str = 'Hello World Plugin'
        version: str = '0.0.3'
        author: str = 'cmoyano'
        license: str = 'N/A'

    @staticmethod
    def register_activation_hook() -> None:
        print(f"register_activation_hook: {HelloPlugin.Meta.plugin_name}")

    @staticmethod
    def register_deactivation_hook() -> None:
        print(f"register_deactivation_hook: {HelloPlugin.Meta.plugin_name}")

    @staticmethod
    def register_uninstall_hook() -> None:
        print(f"register_uninstall_hook: {HelloPlugin.Meta.plugin_name}")

def register() -> Protocol:
    return HelloPlugin


class InternalHooks:
    GET_CARD_TITLE: str = 'get_card_title'
    GET_CARD_TEXT: str = 'get_card_text'
    GET_CARD_SMALL_TEXT: str = 'get_card_small_text'

# Actions

def get_card_title_callback() -> None:
    return 'A title from hello plugin '

def get_card_text_callback() -> None:
    return 'A card text from hello plugin'

def get_card_small_text_callback() -> None:
    return 'A smal text from hello plugin'



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
