'''A module that contains a class that stores a bucket (key) and an activity list(value)'''
bucket_name = ""
activity_list = []
list_items = {bucket_name : activity_list}
class BucketActivities(object):
    ''' A class that reads , creates , updates and deletes bucket lists and activities'''
    def __init__(self):
        '''Creating instance variables for the class bucket activities'''
        self.list_items = list_items
        self.bucket_name = bucket_name
        self.activity_list = activity_list
    def create_bucket(self, item_added):
        '''A method that creates a bucket list'''
        if item_added != "" and isinstance(item_added, str):
            self.list_items.update({item_added:self.activity_list})
    def update_bucket(self, old_item, new_item):
        '''A method that updates a bucket list'''
        if new_item != "" and isinstance(new_item, str):
            old_item_activity_list = self.list_items.get(old_item)
            self.list_items.pop(old_item)
            self.list_items.update({new_item:old_item_activity_list})
    def delete_bucket(self, deletable_bucket):
        '''A method that deletes a bucket list'''
        self.list_items.pop(deletable_bucket)
    def view_bucket(self):
        '''A method that views a bucket list'''
        return self.bucket_name
    def create_activity(self, bucket_name_provided, item_added):
        '''A method that creates an activity'''
        if item_added != "" and isinstance(item_added, str):
            for key in self.list_items:
                if key == bucket_name_provided:
                    temporary_list = self.list_items[key]
                    temporary_list.append(item_added)
                    self.list_items[key] = temporary_list
    def delete_activity(self, bucket_name_provided, activity_chosen):
        '''A method that deletes an activity'''
        self.list_items[bucket_name_provided].remove(activity_chosen)
    def update_activity(self, bucket_name_provided, old_activity, new_activity):
        '''A method that updates an activity'''
        if new_activity != "" and isinstance(new_activity, str):
            counter = 0
            while counter < len(self.list_items[bucket_name]):
                if self.list_items[bucket_name_provided][counter] == old_activity:
                    self.list_items[bucket_name_provided][counter] = new_activity
                counter += 1
    def read_activity_list(self):
        '''A method that reads an acitivity list'''
        return self.activity_list
