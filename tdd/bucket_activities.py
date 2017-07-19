bucket_name = ""
activity_list = []
list_items = { bucket_name : activity_list}
class BucketActivities(object):
    def __init__(self):
        self.list_items = list_items
        self.bucket_name = bucket_name
        self.activity_list = activity_list
    def create_bucket(self, item_added):
        if item_added !=  "" and isinstance (item_added , str):
            self.list_items.pop(self.bucket_name)
            self.list_items.update( {item_added:self.activity_list})
        else:
            raise ValueError
    def update_bucket(self,old_item , new_item):
        if new_item !=  "" and isinstance (new_item , str):
            self.list_items.pop(old_item)
            self.list_items.update( {new_item:self.activity_list})
    def delete_bucket(self):
        self.list_items = { bucket_name : activity_list}
    def view_bucket(self):
        return self.bucket_name
    def create_activity(self , item_added):
        if item_added !=  "" and isinstance (item_added , str):
             for item in self.activity_list:
                if item.lower() == item_added.lower():
                    raise ValueError
                else:
                    self.activity.list.append(item_added)
    def delete_activity(self, activity_chosen):
        self.activity_list.remove (activity_chosen)
    def update_activity(self, old_activity , new_activity):
        if new_activity !=  "" and isinstance (new_activity , str):
            counter = 0
            while counter < len(self.activity_list):
                if self.activity_list[counter] == old_activity:
                    self.activity_list[counter] = new_activity
                counter +=1
    def read_activity_list():
        return self.activity_list
                
        
        
        
