from executor import Executor

class MenuManager:

    def __init__(self) -> None:
        self.table_name = 'Menu_Items'

    def all(self):
        query = f"select * from {self.table_name}"
        out = Executor.run_fetch(query)
        return out
    
    def get_by_name(self, name: str):
        query = f"select * from {self.table_name} where item_name='{name}'"
        out = Executor.run_fetch(query, many=False)
        return out
    
if __name__ == '__main__':
    manage = MenuManager()
    print(manage.all())
    print(manage.get_by_name('BurgerXL'))