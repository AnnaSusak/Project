from utils import db_action, DBAction


class Task:
    id: int
    name: str
    description: str
    output: str

    def __init__(self, task_id: int, name: str, description: str, output: str):
        self.id = task_id
        self.name = name
        self.description = description
        self.output = output

    def save(self, id: int, name_val: str, description_val: str, output_val: str):
        db_action(
            '''
            update tasks set name=?, description=?, output=? where id=?
            ''',
            (name_val, description_val, output_val, id),
            DBAction.commit,
        )


def get_task(task_id: int) -> Task:
    db_task = db_action(
        '''
        select * from tasks where id=?
        ''',
        (task_id,),
        DBAction.fetchone
    )

    task = Task(db_task[0], db_task[1], db_task[2], db_task[3])
    return task
