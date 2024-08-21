class PlannerService:
    def create_backlog(self, tasks):
        # Create a backlog with the provided list of tasks
        backlog = []
        for task in tasks:
            backlog.append(task)
        return backlog
