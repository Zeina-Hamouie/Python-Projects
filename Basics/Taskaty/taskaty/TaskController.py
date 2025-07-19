from tabulate import tabulate
from .Task import Task
from datetime import datetime, date
from argparse import Namespace

class TaskController:
    def __init__(self,file_name):
        self.file_name=file_name

    def parse_date(self, date_str):
        try:
            # صيغة ISO: 2025-07-22
            return date.fromisoformat(date_str)
        except ValueError:
            try:
                # صيغة DD-MM-YYYY
                return datetime.strptime(date_str, "%d-%m-%Y").date()
            except ValueError:
                print(f"⚠️ تنسيق تاريخ غير مدعوم: {date_str}")
                return None

    def add_task(self,args):
        #1 start_date
        if not args.start_date: #تتحقق من عدم وجود التاريخ
            now = date.today().isoformat()
            args.start_date =now

        # 2 Task
        task=Task(args.title,args.description,args.start_date,args.end_date,args.done)

        with open(self.file_name,'a')as file:
            file.write(str(task)+'\n')

    def list_tasks(self):
        unfinished_task =[]
        with open(self.file_name,'r') as file:
            for line in file:
                title,description,start_date,end_date,done=line.split(',')
                end_date= None if end_date=='None' else end_date
                done =False if done.strip('\n') =='False' else True
                if done:
                    continue
                unfinished_task.append({'title':title,'description':description,'start_date':start_date,'end_date':end_date})

        return unfinished_task

    def list_all_tasks(self):
        tasks= []
        with open(self.file_name, 'r') as file:
            for line in file:
                title, description, start_date, end_date, done = line.split(',')
                end_date = None if end_date == 'None' else end_date
                done = False if done.strip('\n') == 'False' else True
                tasks.append({'title': title, 'description': description, 'start_date': start_date, 'end_date': end_date,'done':done})

        return tasks

    def due_date(self,start,end):
        start_date = self.parse_date(start)
        end_date = self.parse_date(end)

        if start_date and end_date:
            delta = end_date - start_date
            return f"{delta.days} days left"
        else:
            return "❌ تاريخ غير صالح"

        # start_date = date.fromisoformat(start)
        # end_date = date.isoformat(end)
        # date_delta = end_date-start_date
        # return f'{date_delta.days} days left'

    def print_table(self,tasks):
        formatted_tasks = []
        for number,task in enumerate(tasks,1):
            if task['start_date'] and task['end_date']:
                due_date=self.due_date(task['start_date'],task['end_date'])
            else:
                due_date ='Open'
            formatted_tasks.append({'no.':number,**task,'due_date':due_date})
        print(tabulate(formatted_tasks,headers='keys'))

    def display(self,args):
        all_tasks =self.list_all_tasks()
        unchecked_tasks =self.list_tasks()
        if not all_tasks:
            print('there is no file. To add a task use add<task>')
            return
        if args.all:
            self.print_table(all_tasks)
        else:
            if unchecked_tasks:
                self.print_table(unchecked_tasks)
            else:
                print('All tasks are checked!')

    def check_task(self,args):
        index =args.task
        tasks =self.list_all_tasks()
        if index<= 0 or index> len(tasks):
            print(f'Task number{index} does not exit!')
            return
        tasks[index-1]['done']=True
        with open(self.file_name,'w') as file:
            for task in tasks:
                self.add_task(Namespace(**task))

    def remove(self,args):
        tasks = self.list_all_tasks()
        if args.task:
            index = args.task
        else:
            index = len(tasks)
        if index <= 0 or index > len(tasks):
            print(f'Task number{index} does not exit!')
            return
        tasks.pop(index - 1)
        with open(self.file_name, 'w') as file:
            for task in tasks:
                self.add_task(Namespace(**task))

    def reset(self,*args):
        with open(self.file_name, 'w') as file:
            file.write('')
            print('you deleted all tasks')
