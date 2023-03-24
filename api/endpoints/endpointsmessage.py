from datetime import datetime
from typing import Any

from fastapi import Path, HTTPException, APIRouter, Depends
from pydantic import BaseModel, constr, Field

from api.dao.daoaccount import get_account_by_id
from api.dao.daomessage import get_all_message, get_message_by_ticket_id, add_message, edit_message, delete_message, \
    get_message_by_account_email

router = APIRouter(tags=["Message"])


def valid_message_from_path(
        message_id: int = Path(ge=1, description="L'identifiant du message", example=4)
) -> dict[str, Any]:
    found_message = get_account_by_id(id=message_id)
    if found_message is None:
        raise HTTPException(
            status_code=404,
            detail=f"Le message d'identifiant {message_id!r} n'a pas été trouvé"
        )
    return found_message


class CreateMessageModel(BaseModel):
    content: constr(strip_whitespace=True, min_length=1) = Field(..., description="Le contenu du message !")
    sender_id: int = Field(None, description="L'identifiant de l'émetteur du message", example="1")
    ticket_id: int = Field(None, description="L'identifiant du ticket du message associé", example="1")


class EditMessageModel(CreateMessageModel):
    id: int = Field(None, description="Identifiant du compte", example="1")


class MessageModel(CreateMessageModel):
    id: int = Field(None, description="Identifiant du compte", example="1")
    date_creation: datetime = Field(None, description="Date de création du message",
                                    example="2022-10-04T12:39:19.291694+00:00")


@router.get('/messages', response_model=list[MessageModel], summary="Affiche tous les messages")
def get_messages():
    """
    # Get Messages

    Affiche tous les messages
    """
    return get_all_message()


@router.get('/message/{message_id}', response_model=MessageModel, summary="Affiche un message")
def get_message(
        message=Depends(valid_message_from_path)
):
    """
    # Get Message

    Affiche un message avec son identifiant
    """
    return message


@router.get('/message_ticket/{ticket_id}', response_model=list[MessageModel],
            summary="Affiche les messages d'un ticket")
def get_message_ticket(
        ticket_id: int = Path()
):
    """
    # Get Message Ticket

    Affiche les messages liés à un ticket
    """
    return get_message_by_ticket_id(ticket_id=ticket_id)


@router.get('/message_account/{email}', response_model=list[MessageModel],
            summary="Affiche les messages d'un account")
def get_message_account(
        email: int = Path()
):
    """
    # Get Account Email

    Affiche les messages liés à un account
    """
    return get_message_by_account_email(email=email)


@router.post('/message', response_model=MessageModel, summary="Crée un compte")
def post_message(
        CreateMessage: CreateMessageModel
):
    """
    # Post Message

    Crée un message
    """
    return add_message(
        content=CreateMessage.content,
        sender_id=CreateMessage.sender_id,
        ticket_id=CreateMessage.ticket_id,
    )


@router.put('/message/{message_id}', response_model=MessageModel, summary="Edite un compte")
def put_account(
        EditAccount: EditMessageModel,
        message=Depends(valid_message_from_path)
):
    """
    # Put Message

    Met à jour un message
    """
    return edit_message(
        id=message['id'],
        content=EditAccount.content,
        sender_id=EditAccount.sender_id,
        ticket_id=EditAccount.ticket_id,
    )


@router.delete('/message/{message_id}', summary="Supprime un message")
def del_message(
        message=Depends(valid_message_from_path)
):
    """
    # Del message

    Supprime un message
    """
    delete_message(id=message['id'])
