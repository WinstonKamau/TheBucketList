import unittest
from app import model
from app.model import Users
from app.model import BucketList

class UserToBucketListActivitiesTest(unittest.TestCase):
    def test_creation_of_a_bucket_object(self):
        model.users.clear()
        Users().create_user("s", "s@gmail.com", "s", "s")
        Users().create_user("t", "t@gmail.com", "t", "t")
        Users().create_user("u", "u@gmail.com", "u", "u")
        Users().login_user("u@gmail.com", "u")
        BucketList().create_bucket("Travel")
        print(model.users[0].user_bucket)
        print(model.users[1].user_bucket)
        print(model.users[2].user_bucket)
        self.assertEqual(BucketList().create_bucket("Travel"), True)
    def test_creation_of_many_users(self):
        #Not sure that this method will work on calling the users list
        model.users.clear()
        Users().create_user("s", "s@gmail.com", "s", "s")
        Users().create_user("t", "t@gmail.com", "t", "t")
        Users().create_user("u", "u@gmail.com", "u", "u")
        Users().login_user("u@gmail.com", "u")
        self.assertEqual(model.user_id, 2)
        Users().login_user("t@gmail.com", "t")
        self.assertEqual(model.user_id, 1)
        Users().login_user("s@gmail.com", "s")
        self.assertEqual(model.user_id, 0)
    def test_bucket_returned(self):
        model.users.clear()
        Users().create_user("s", "s@gmail.com", "s", "s")
        Users().login_user("s@gmail.com", "s")
        BucketList().create_bucket("Travel")
        self.assertEqual(BucketList().view_bucket()[0].bucket_name, "Travel")
        Users().create_user("t", "t@gmail.com", "t", "t")
        Users().login_user("t@gmail.com", "t")
        BucketList().create_bucket("Family")
        BucketList().create_bucket("Mosodo")
        self.assertEqual(BucketList().view_bucket()[1].bucket_name, "Mosodo")
        BucketList().edit_bucket(0, "Mion")
        self.assertEqual(BucketList().view_bucket()[0].bucket_name, "Mion")
        BucketList().delete_bucket(0)
        self.assertEqual(BucketList().view_bucket()[0].bucket_name, "Mosodo")
        self.assertEqual(len(BucketList().view_bucket()), 1)
        BucketList().create_activity(0, "fkslk")
        self.assertEqual(BucketList().view_bucket()[0].activity_list[0], "fkslk")
        BucketList().edit_activity(0, 0, "kkkk")
        self.assertEqual(BucketList().view_bucket()[0].activity_list[0], "kkkk")
        BucketList().create_activity(0, "opop")
        BucketList().create_activity(0, "pppp")
        BucketList().delete_activity(0,1)
        self.assertEqual(BucketList().view_bucket()[0].activity_list[1], "pppp")

if __name__ == '__main__':
    unittest.main()