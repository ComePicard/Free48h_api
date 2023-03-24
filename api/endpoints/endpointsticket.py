from datetime import datetime
from typing import Any

from fastapi import Path, HTTPException, Depends, APIRouter
from pydantic import BaseModel, constr, Field

from api.dao.daoticket import get_ticket_by_id, add_ticket, edit_ticket, delete_ticket, get_ticket_by_email, \
    assign_support_to_ticket

router = APIRouter(tags=["Ticket"])


def valid_ticket_from_path(
        ticket_id: int = Path(ge=1, description="L'identifiant du ticket", example=4)
) -> dict[str, Any]:
    found_ticket = get_ticket_by_id(ticket_id=ticket_id)
    if found_ticket is None:
        raise HTTPException(
            status_code=404,
            detail=f"Le ticket d'identifiant {ticket_id!r} n'a pas été trouvé"
        )
    return found_ticket


class CreateTicketModel(BaseModel):
    content: constr(strip_whitespace=True, min_length=1) = Field(..., description="Le message du ticket")
    sender_id: int = Field(None, description="Identifiant de l'expéditeur du ticket")
    support_id: int | None = Field(None, description="Identifiant du support qui a prend le ticket en charge")
    category_id: int = Field(None, description="Identifiant de la category du ticket")
    status_id: int = Field(None, description="Identifiant du status du ticket")


class EditTicketModel(CreateTicketModel):
    ticket_id: int = Field(None, description="Identifiant du ticket")


class TicketModel(CreateTicketModel):
    ticket_id: int = Field(None, description="Identifiant du ticket")
    date_creation: datetime = Field(..., description="Date de création du ticket",
                                    example="2022-10-04T12:39:19.291694+00:00")


class SupportEditModel(BaseModel):
    support_id: int = Field(None, description="Identifiant du support")


@router.get('/ticket/{ticket_id}', response_model=TicketModel, summary="Affiche un ticket")
def get_ticket(
        ticket=Depends(valid_ticket_from_path)
):
    """
    # Get Ticket

    Affiche un ticket avec son identifiant
    """
    return ticket


@router.get('/ticket_email/{email}', response_model=TicketModel, summary="Affiche un ticket avec son email")
def get_ticket_email(
        email: str = Path()
):
    """
    # Get Ticket Email

    Affiche un ticket avec son email
    """
    return get_ticket_by_email(email=email)


@router.post('/ticket', response_model=TicketModel, summary="Créer un ticket")
def post_ticket(
        CreateTicket: CreateTicketModel
):
    """
    # Post Ticket

    Créer un ticket
    """
    return add_ticket(
        content=CreateTicket.content,
        sender_id=CreateTicket.sender_id,
        support_id=CreateTicket.support_id,
        category_id=CreateTicket.category_id,
        status_id=CreateTicket.status_id,
    )


@router.put('/ticket/{ticket_id}', response_model=TicketModel, summary="Edite un ticket")
def put_ticket(
        UpdateTicket: EditTicketModel,
        ticket=Depends(valid_ticket_from_path)
):
    """
    # Put Ticket

    Edite un ticket
    """
    return edit_ticket(
        ticket_id=ticket['ticket_id'],
        content=UpdateTicket.content,
        sender_id=UpdateTicket.sender_id,
        support_id=UpdateTicket.support_id,
        category_id=UpdateTicket.category_id,
        status_id=UpdateTicket.status_id,
    )


@router.patch('/ticket/{ticket_id]', response_model=TicketModel, summary="Édite le support affilié au ticket")
def patch_ticket_support(
        UpdateSupport: SupportEditModel,
        ticket=Depends(valid_ticket_from_path)
):
    """
    # Patch Ticket Support

    Edite le support affilié au ticket
    """
    return assign_support_to_ticket(support_id=UpdateSupport.support_id, ticket_id=ticket['id'])


@router.delete('/ticket/{ticket_id}', summary="Supprime un ticket")
def del_ticket(
        ticket=Depends(valid_ticket_from_path)
):
    """
    # Del Ticket

    Supprime le ticket
    """
    delete_ticket(ticket_id=ticket['ticket_id'])
