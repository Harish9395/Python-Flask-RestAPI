class AppService:

    def __init__(self):

        self.tasks = [
            {
                "id": 1,
                "name": "task1",
                "description": "This is task 1"
            },
            {
                "id": 2,
                "name": "task2",
                "description": "This is task 2"
            },
            {
                "id": 3,
                "name": "task3",
                "description": "This is task 3"
            }
        ]


    def get_tasks(self):

        return self.tasks


    def create_task(self, task):

        new_id = len(self.tasks) + 1

        new_task = {
            "id": new_id,
            "name": task,
            "description": f"This is {task}"
        }

        self.tasks.append(new_task)

        return new_task


    def update_task(self, request_task):

        for task in self.tasks:

            if task["id"] == request_task["id"]:

                task.update(request_task)

                return task


        return {
            "message": "task id not found"
        }


    def delete_task(self, request_task_id):

        for task in self.tasks:

            if task["id"] == request_task_id:

                self.tasks.remove(task)

                return {
                    "message": "task deleted",
                    "tasks": self.tasks
                }


        return {
            "message": "task id not found"
        }
