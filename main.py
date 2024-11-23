task={}

class Task:
      
    def __init__(self,title,index_task,is_active=False):
        self.is_active = is_active
        self.title = title
        self.index_task = index_task
        
    
    def add_task(self):
        task[self.index_task] = {"title":self.title,"is_active":self.is_active}
    def remove_task(self, index_task):
        task.pop(index_task)
    def mark_is_active(self):
        self.is_active = True
    
    def string(self):
        if(self.is_active):
            status = "completed"
            return status
        else:
             status = "not completed"
             return status
#add on task
task1 = Task("brosser les dents",1)
task1.add_task()
task2 = Task("Mediter",2)
task2.add_task()
task3 = Task("deepwork",3)
task3.add_task()
#delete on task
# task3.remove_task(2)

print(task)
