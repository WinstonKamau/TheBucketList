'''A module that contains a class that stores a bucket (key) and an activity list(value)'''
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
            self.list_items.update( {item_added:self.activity_list})
    def update_bucket(self,old_item , new_item):
        if new_item !=  "" and isinstance (new_item , str):
            old_item_activity_list = self.list_items.get (old_item)
            self.list_items.pop(old_item)
            self.list_items.update( {new_item:old_item_activity_list})
    def delete_bucket(self , deletable_bucket):
        self.list_items.pop(deletable_bucket)
    def view_bucket(self):
        return self.bucket_name
    def create_activity(self , bucket_name , item_added):
        if item_added !=  "" and isinstance (item_added , str):
            for key in self.list_items:
                if key == bucket_name:
                    temporary_list = self.list_items[key]
                    temporary_list.append(item_added)
                    self.list_items[key] = temporary_list
    def delete_activity(self, bucket_name , activity_chosen):
        self.list_items[bucket_name].remove (activity_chosen)
    def update_activity(self, bucket_name , old_activity , new_activity):
        if new_activity !=  "" and isinstance (new_activity , str):
            counter = 0
            while counter < len(self.list_items[bucket_name]):
                if self.list_items[bucket_name][counter] == old_activity:
                    self.list_items[bucket_name][counter] = new_activity
                counter +=1
    def read_activity_list():
        return self.activity_list
                
        
        
        
