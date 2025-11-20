from fastapi import APIRouter
from schemas import STaskAdd, STask, STaskId
from repository import TaskRepository

router = APIRouter(prefix="/tasks", tags=["Tasks"])


@router.post("")
async def add_task(task: STaskAdd) -> STaskId:
    task_id = await TaskRepository.add_one(task)
    return STaskId(ok=True, task_id=task_id)


@router.get("")
async def get_tasks() -> list[STask]:
    tasks = await TaskRepository.find_all()
    return tasks
