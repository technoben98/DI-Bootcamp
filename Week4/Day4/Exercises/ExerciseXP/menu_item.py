from executor import Executor

class MenuItem:
    def __init__(self, name: str, price: int) -> None:       
        self.item_name = name
        self.price = price
        self.table_name = 'Menu_Items'

    def save(self):
        query = f"insert into {self.table_name}(item_name, item_price) values ('{self.item_name}', {self.price})"
   
        Executor.run_commit(query)
        return query
    
    def delete(self):
        query = f"delete from {self.table_name} where item_name='{self.item_name}' and item_price={self.price}"
 
        Executor.run_commit(query)
        return query
    
    def update(self, new_name: str|None = None, new_price: str|None = None):
        n_name = new_name if new_name is not None else self.item_name
        n_price = new_price if new_price is not None else self.price

        query = f"update {self.table_name} set item_name='{n_name}', item_price={n_price} where "
        query += f"item_name='{self.item_name}' and item_price={self.price}"

        Executor.run_commit(query)
        return query
    

if __name__ == '__main__':
    item = MenuItem('Falafel', 5)
    item.save()
    print(item.update(new_name='BurgerXL', new_price=15))
    item.delete()