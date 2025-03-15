from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from app.models import Project, User
from app.schemas import ProjectCreate
from app.database import get_session
from app.auth import get_current_user

router = APIRouter()

@router.get("/")
def get_projects(
    user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    projects = session.exec(select(Project)).all()
    return projects

@router.post("/")
def create_project(
    project_data: ProjectCreate,
    user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    if user.role != "admin":
        raise HTTPException(status_code=403, detail="Not authorized")

    new_project = Project(name=project_data.name, description=project_data.description, owner_id=user.id)
    session.add(new_project)
    session.commit()
    session.refresh(new_project)
    return new_project

@router.put("/{project_id}")
def update_project(
    project_id: int,
    project_data: ProjectCreate,
    user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    if user.role != "admin":
        raise HTTPException(status_code=403, detail="Not authorized")

    project = session.get(Project, project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    project.name = project_data.name
    project.description = project_data.description
    session.commit()
    session.refresh(project)
    return project

@router.delete("/{project_id}")
def delete_project(
    project_id: int,
    user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    if user.role != "admin":
        raise HTTPException(status_code=403, detail="Not authorized")

    project = session.get(Project, project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    session.delete(project)
    session.commit()
    return {"message": "Project deleted successfully"}
