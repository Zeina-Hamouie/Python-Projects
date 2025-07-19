from argparse import ArgumentParser
from .TaskController import TaskController


def main():

    controller =TaskController('tasks.txt')
    #انشاء نسخة من الصنف ArgumentParser
    # ثم نضيف الوسائط
    # نطلب من التابع parse_args() تحديد الوسائط و تحويلها ال namespacee
    # الذي يمكن الاستفادة منه بالحصول على قيم المدخلة من المستخدم
    #<class 'argparse.ArgumentParser'>
    parser =ArgumentParser(description='Simple ClI task manager')

    #  <class 'argparse._SubParsersAction'>
    subparsers =parser.add_subparsers()#يعيد كائن له تابع واحد فقط add_parser

    # <class 'argparse.ArgumentParser'>
    add_task =subparsers.add_parser('add',help='Add to the given task')
    add_task.add_argument('title',help='title of the task',type=str)
    add_task.add_argument('-d','--description',help='short description of the task',type=str,default=None)
    add_task.add_argument('-s', '--start_date', help='Date to begin the task', type=str, default=None)
    add_task.add_argument('-e', '--end_date', help='Date to end the task', type=str, default=None)
    add_task.add_argument( '--done', help='check whether the task done or not',default=False)
    add_task.set_defaults(func=controller.add_task)

    list_tasks = subparsers.add_parser('list', help='list unfinished tasks')
    list_tasks.add_argument('-a','--all',help='list all the tasks',action='store_true')
    list_tasks.set_defaults(func=controller.display)

    check_task = subparsers.add_parser('check', help='check the given task')
    check_task.add_argument('-t','--task',help='number of the task to be done,if not specified,last task will be romved',type=int)
    check_task.set_defaults(func=controller.check_task)

    remove = subparsers.add_parser('remove', help='remove a task')
    remove.add_argument('-t','--task',help='the task to be removed(Number)',type=int)
    remove.set_defaults(func=controller.remove)

    reset = subparsers.add_parser('reset', help='Remove all tasks')
    reset.set_defaults(func=controller.reset)
    # تحويل التطبيق الى تطبيق في سطر الأوامر
    args = parser.parse_args()
    args.func(args)


if __name__=='__main__':
    main()