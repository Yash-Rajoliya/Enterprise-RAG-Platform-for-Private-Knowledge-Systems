from .registry import PROMPTS


def get_prompt(name):
    return PROMPTS[name]