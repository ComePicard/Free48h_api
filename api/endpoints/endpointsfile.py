from typing import Any

from fastapi import Path, HTTPException, APIRouter, Depends
from pydantic import BaseModel, constr, Field

from api.dao.daofile import *

router = APIRouter(tags=["File"])


def valid_file_from_path(
        file_id: int = Path(ge=1, description="L'identifiant du file", example=4)
) -> dict[str, Any]:
    found_file = get_file_by_id(id=file_id)
    if found_file is None:
        raise HTTPException(
            status_code=404,
            detail=f"Le fichier d'identifiant {file_id!r} n'a pas été trouvé"
        )
    return found_file


class CreateFileModel(BaseModel):
    link: constr(strip_whitespace=True, min_length=1) = Field(..., description="Le lien du fichier !")
    ticket_id: int = Field(None, description="L'identifiant du ticket du fichier associé", example="1")


class FileModel(CreateFileModel):
    id: int = Field(None, description="Identifiant du compte", example="1")


@router.get('/files', response_model=list[FileModel], summary="Affiche tous les fichiers")
def get_files():
    """
    # Get Files

    Affiche tous les fichiers
    """
    return get_all_file()


@router.get('/file/{file_id}', response_model=FileModel, summary="Affiche un fichier")
def get_file(
        file=Depends(valid_file_from_path())
):
    """
    # Get File

    Affiche un fichier avec son identifiant
    """
    return file


@router.get('/file_ticket/{ticket_id}', response_model=list[FileModel],
            summary="Affiche les fichiers d'un ticket")
def get_file_ticket(
        ticket_id: int = Path()
):
    """
    # Get File Ticket

    Affiche les fichiers liés à un ticket
    """
    return get_file_by_ticket_id(ticket_id=ticket_id)


@router.post('/file', response_model=FileModel, summary="Crée un fichier")
def post_file(
        CreateFile: CreateFileModel
):
    """
    # Post File

    Crée un fichier
    """
    return add_file(
        link=CreateFile.link,
        ticket_id=CreateFile.ticket_id,
    )


@router.put('/file/{file_id}', response_model=FileModel, summary="Edite un fichier")
def put_file(
        EditFile: FileModel,
        file=Depends(valid_file_from_path)
):
    """
    # Put File

    Met à jour un file
    """
    return edit_file(
        id=file['id'],
        link=EditFile.link,
        ticket_id=EditFile.ticket_id,
    )


@router.delete('/file/{file_id}', summary="Supprime un file")
def del_file(
        file=Depends(valid_file_from_path)
):
    """
    # Del file

    Supprime un file
    """
    delete_file(id=file['id'])
