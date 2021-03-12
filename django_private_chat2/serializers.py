from .models import DialogUser, Dialog, Message, TextMessage, MessageModel, DialogsModel
from datetime import datetime
from typing import Callable
import json
import dataclasses


def serialize_dialog_user(d: DialogUser, datetime_formatter: Callable[[datetime], str]) -> str:
    obj = {"id": d.id, "was_online": datetime_formatter(d.was_online) if d.was_online else None,
           "is_online": d.is_online}
    return json.dumps(obj)


def serialize_dialog(d: Dialog) -> str:
    return json.dumps({"id": d.id, "between": (d.creator.id, d.opponent.id)})


def serialize_text_message(m: TextMessage, datetime_formatter: Callable[[datetime], str]) -> str:
    obj = {
        "dialog_id": m.dialog_id,
        "data": m.data,
        "msg_id": m.msg_id,
        "sent_by": m.sent_by.id,
        "sent_at": datetime_formatter(m.sent_at),
        "was_read": m.was_read
    }
    return json.dumps(obj)


def serialize_message_model(m: MessageModel):
    obj = {
        "id": m.id,
        "text": m.text,
        "sent": int(m.created.timestamp()),
        "edited": int(m.modified.timestamp()),
        "read": m.read,
        "file": m.file.path if m.file else None,
        "sender": m.sender.pk,
        "recipient": m.recipient.pk
    }
    return obj


def serialize_dialog_model(m: DialogsModel):
    obj = {
        "id": m.id,
        "created": int(m.created.timestamp()),
        "modified": int(m.modified.timestamp()),
        "user1": m.user1.pk,
        "user2": m.user2.pk
    }
    return obj
