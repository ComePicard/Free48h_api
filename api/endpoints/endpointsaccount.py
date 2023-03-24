from typing import Any

from fastapi import Path, HTTPException, APIRouter, Depends
from pydantic import BaseModel, constr, Field

from api.dao.daoaccount import get_account_by_id, get_all_account, get_account_by_email, add_account, edit_account, \
    delete_account

router = APIRouter(tags=["Account"])


def valid_account_from_path(
        account_id: int = Path(ge=1, description="L'identifiant du compte", example=4)
) -> dict[str, Any]:
    found_account = get_account_by_id(id=account_id)
    if found_account is None:
        raise HTTPException(
            status_code=404,
            detail=f"Le compte d'identifiant {account_id!r} n'a pas été trouvé"
        )
    return found_account


class CreateAccountModel(BaseModel):
    firstname: constr(strip_whitespace=True, min_length=1) = Field(..., description="Le prénom du compte",
                                                                   example="John")
    lastname: constr(strip_whitespace=True, min_length=1) = Field(..., description="Le nom du compte", example="Doe")
    email: constr(strip_whitespace=True, min_length=1) = Field(..., description="L'email du compte",
                                                               example="johndoe@mail.com")
    password: constr(strip_whitespace=True, min_length=1) = Field(..., description="Le mot de passe du compte",
                                                                  example="johndoe123")
    role_id: int = Field(None, description="Le rôle du compte", example="1")


class AccountModel(CreateAccountModel):
    id: int = Field(None, description="Identifiant du compte", example="1")


@router.get('/accounts', response_model=list[AccountModel], summary="Affiche tous les comptes")
def get_accouts():
    """
    # Get Accounts

    Affiche tous les comptes
    """
    return get_all_account()


@router.get('/account/{account_id}', response_model=AccountModel, summary="Affiche un compte")
def get_account(
        account=Depends(valid_account_from_path)
):
    """
    # Get Account

    Affiche un compte avec son identifiant
    """
    return account


@router.get('/account_email/{email}', response_model=AccountModel, summary="Affiche un compte avec son email")
def get_account_email(
        email: str = Path()
):
    """
    # Get Account Email

    Affiche le compte associé à l'email
    """
    return get_account_by_email(email=email)


@router.post('/account', response_model=AccountModel, summary="Crée un compte")
def post_account(
        CreateAccount: CreateAccountModel
):
    """
    # Post Account

    Crée un compte
    """
    return add_account(
        firstname=CreateAccount.firstname,
        lastname=CreateAccount.lastname,
        email=CreateAccount.email,
        password=CreateAccount.password,
        role_id=CreateAccount.role_id,
    )


@router.put('/account/{account_id}', response_model=AccountModel, summary="Edite un compte")
def put_account(
        EditAccount: AccountModel,
        account=Depends(valid_account_from_path)
):
    """
    # Put Account

    Met à jour un account
    """
    return edit_account(
        id=account['id'],
        firstname=EditAccount.firstname,
        lastname=EditAccount.lastname,
        email=EditAccount.email,
        password=EditAccount.password,
        role_id=EditAccount.role_id,
    )


@router.delete('/account/{account_id}', summary="Supprime un compte")
def del_account(
        account=Depends(valid_account_from_path)
):
    """
    # Del Account

    Supprime un compte
    """
    delete_account(id=account['id'])
