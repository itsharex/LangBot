from __future__ import annotations

import openai

from . import chatcmpl
from .. import requester
from ....core import app


@requester.requester_class("siliconflow-chat-completions")
class QwenChatCompletions(chatcmpl.OpenAIChatCompletions):
    """Qwen ChatCompletion API 请求器"""

    client: openai.AsyncClient

    requester_cfg: dict

    def __init__(self, ap: app.Application):
        self.ap = ap

        self.requester_cfg = self.ap.provider_cfg.data['requester']['qwen-chat-completions']
