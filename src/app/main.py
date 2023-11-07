import fastapi
from fastapi import Body


TASKS = [
    {'task_id': 1, 'description': 'aaaa', 'status': 'new'},
    {'task_id': 2, 'description': 'bbbb', 'status': 'in_progress'},
    {'task_id': 3, 'description': 'cccc', 'status': 'done'},
    {'task_id': 4, 'description': 'dddd', 'status': 'done'},
    {'task_id': 5, 'description': 'ffff', 'status': 'new'},
    {'task_id': 6, 'description': 'gggg', 'status': 'new'}
]

router = fastapi.APIRouter(prefix="/api")


@router.get("/tasks")
def get_all_tasks():
    return TASKS


@router.get("/tasks/{task_id}")
def get_task(task_id :int):
    for task in TASKS:
        if task.get('task_id') == task_id:
            return task


@router.get("/tasks/")
def get_task_by_status(status:str):
    tasks_by_status = []
    for task in TASKS:
        if task.get('status') == status.lower():
            tasks_by_status.append(task)
    return tasks_by_status
    

@router.get("/task/{id}")
def get_issue(id :int):
    return {'id': id, 'task_description' : 'description', 'status' : 'done'}


@router.post("/tasks/create_task")
def create_task(new_task=Body()):
    TASKS.append(new_task)
    return new_task


app = fastapi.FastAPI()
app.include_router(router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run('main:app', reload=True)
