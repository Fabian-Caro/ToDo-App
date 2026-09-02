from features.tasks.commands.delete_task.request import DeleteTaskRequest
from infrastructure.database.unit_of_work import UnitOfWork


def execute(delete_task_request: DeleteTaskRequest) -> bool:
    
    with UnitOfWork() as uow:
        task = uow.tasks.get_by_id(delete_task_request.id)
        
        if task is None:
            return False
        
        uow.tasks.delete(task)
        uow.commit()
        
        return True
        