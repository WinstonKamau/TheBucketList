'''A test file for testing the views method.  '''
import unittest
from app import views
from app import app


class ViewTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_register_get(self):
        response = self.app.get('/Register')
        self.assertEqual(response.status_code, 200)
    
    def test_register_post(self):
        response = self.app.post('/Register',
                                 data=dict(
                                     username_register="example",
                                     useremail_register="example@email.com",
                                     password_register="password",
                                     confirm_new_password="password"))
        self.assertEqual(response.status_code, 302)

    def test_similar_email(self):
        response_1 = self.app.post('/Register',
                                   data=dict(
                                   username_register="example",
                                   useremail_register="example@email.com",
                                   password_register="password",
                                   confirm_new_password="password"))
        response_2 = self.app.post('/Register',
                                   data=dict(
                                   username_register="example2",
                                   useremail_register="example@email.com",
                                   password_register="password",
                                   confirm_new_password="password"))
        self.assertIn(b"example@email.com is already registered", response_2.data)

    def test_similar_name(self):
        self.app.post('/Register', data=dict(
                                             username_register="example",
                                             useremail_register="example@email.com",
                                             password_register="password",
                                             confirm_new_password="password"))
        response_2 = self.app.post('/Register',
                                   data=dict(
                                   username_register="example",
                                   useremail_register="example2@email.com",
                                   password_register="password",
                                   confirm_new_password="password"))
        self.assertIn(b"example is already registered", response_2.data)

    def test_different_passwords(self):
        response_1 = self.app.post('/Register',
                                   data=dict(
                                   username_register="example",
                                   useremail_register="example@email.com",
                                   password_register="password",
                                   confirm_new_password="password2"))
        self.assertIn(b"Ensure that all fields have been inserted and that the passwords are the same!", response_1.data)

    def test_login_get(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_login_post(self):
        self.app.post('/Register',
                            data=dict(
                            username_register="e-login",
                            useremail_register="e-login@email.com",
                            password_register="passworde",
                            confirm_new_password="passworde"))

        response_2 = self.app.post('/',
                            data=dict(
                            user_email_login="e-login@email.com",
                            password_login="passworde"
                            ))
        self.assertEqual(response_2.status_code, 302)

    def test_invalid_login(self):
        response = self.app.post('/',
                    data=dict(
                    user_email_login="non-login@email.com",
                    password_login="password-non"
                    ))
        self.assertIn(b"Invalid email / password!", response.data)

    def test_create_bucketlist(self):
        response = self.app.get('/CreateBucketList')
        self.assertEqual(response.status_code, 200)

    def test_empty_duplicate_bucketlist(self):
        self.app.post('/Register', data=dict(
                                             username_register="example3",
                                             useremail_register="example3@email.com",
                                             password_register="password3",
                                             confirm_new_password="password3"))
        self.app.post('/',
                            data=dict(
                            user_email_login="example3@email.com",
                            password_login="password3"
                            ))
        response = self.app.post('/CreateBucketList',
                                 data=dict(
                                 bucketlistcreated="Bucket1"
                                ))
        self.assertEqual(response.status_code, 302)
        empty_response = self.app.post('/CreateBucketList',
                            data=dict(
                            bucketlistcreated=""
                        ))
        self.assertIn(b"Ensure that the bucket name is not an empty word!",
                      empty_response.data)
        duplicate_response = self.app.post('/CreateBucketList',
                            data=dict(
                            bucketlistcreated="Bucket1"
                        ))
        self.assertIn(b"already exists in the bucket list!",
                      duplicate_response.data)

    def test_view_bucketlist(self):
        self.app.post('/Register', data=dict(
                                        username_register="example7",
                                        useremail_register="example7@email.com",
                                        password_register="password7",
                                        confirm_new_password="password7"))
        self.app.post('/',
                            data=dict(
                            user_email_login="example7@email.com",
                            password_login="password7"
                            ))
        view_response = self.app.get('/ViewBucketList')
        empty_prompt = "You currently have no bucketlists on the bucket list,"
        empty_prompt += " press the create new bucket list button to create a new bucket!"
        self.assertIn(b"You currently have no bucketlists on the bucket list,", view_response.data)
        self.assertIn(b" press the create new bucket list button to create a new bucket!", view_response.data)
        post_view_response = self.app.post('/ViewBucketList')
        self.assertEqual(post_view_response.status_code, 302)

    def test_edit_bucketlist(self):
        self.app.post('/Register', data=dict(
                                             username_register="example4",
                                             useremail_register="example4@email.com",
                                             password_register="password4",
                                             confirm_new_password="password4"))
        self.app.post('/',
                            data=dict(
                            user_email_login="example4@email.com",
                            password_login="password4"
                            ))
        self.app.post('/CreateBucketList',
                      data=dict(
                      bucketlistcreated="TrialBucket"
                     ))
        response = self.app.get('/EditBucketList/0')
        self.assertEqual(response.status_code,200)
        self.assertIn(b"TrialBucket", response.data)
        edit_response0 = self.app.post('/EditBucketList/0',
                                 data=dict(
                                 new_name="TrialBucket"
                     ))
        self.assertIn(b"already exists in the bucket list!", edit_response0.data)
        edit_response1 = self.app.post('/EditBucketList/0',
                                 data=dict(
                                 new_name=""
                     ))
        self.assertIn(b"Bucket cannot be replaced with an empty string!", edit_response1.data)
        edit_response2 = self.app.post('/EditBucketList/0',
                                 data=dict(
                                 new_name="ExchangeBucket"
                     ))
        self.assertEqual(edit_response2.status_code, 302)
        view_response = self.app.get('ViewBucketList')
        self.assertIn(b"ExchangeBucket", view_response.data)

    def test_delete_bucket(self):
        self.app.post('/Register', data=dict(
                                             username_register="example4",
                                             useremail_register="example4@email.com",
                                             password_register="password4",
                                             confirm_new_password="password4"))
        self.app.post('/',
                            data=dict(
                            user_email_login="example4@email.com",
                            password_login="password4"
                            ))
        self.app.post('/CreateBucketList',
                      data=dict(
                      bucketlistcreated="TrialBucket"
                     ))
        response = self.app.get('/DeleteBucketList/0')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"TrialBucket", response.data)
        view_response0 = self.app.get('/ViewBucketList')
        self.assertIn(b"TrialBucket", view_response0.data)
        delete_response = self.app.post('DeleteBucketList/0')
        self.assertEqual(delete_response.status_code, 302)
        view_response1 = self.app.get('/ViewBucketList')
        self.assertNotIn(b"TrialBucket", view_response1.data)

    def test_naming(self):
        self.app.post('/Register', data=dict(
                                             username_register="example5",
                                             useremail_register="example5@email.com",
                                             password_register="password5",
                                             confirm_new_password="password5"))
        self.app.post('/',
                            data=dict(
                            user_email_login="example5@email.com",
                            password_login="password5"
                            ))
        view_response = self.app.get('/ViewBucketList')
        self.assertIn(b"EXAMPLE5&#39;s", view_response.data)

    def test_view_activity(self):
        self.app.post('/Register', data=dict(
                                        username_register="example6",
                                        useremail_register="example6@email.com",
                                        password_register="password6",
                                        confirm_new_password="password6"))
        self.app.post('/',
                            data=dict(
                            user_email_login="example6@email.com",
                            password_login="password6"
                            ))
        self.app.post('/CreateBucketList',
                data=dict(
                bucketlistcreated="TrialBucket2"
                ))
        response = self.app.get('/ViewActivities/0')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"TrialBucket2",response.data)
        self.assertIn(b"You currently have no activities on the activity list, ", response.data)

    def test_add_activity(self):
        self.app.post('/Register', data=dict(
                                        username_register="example8",
                                        useremail_register="example8@email.com",
                                        password_register="password8",
                                        confirm_new_password="password8"))
        self.app.post('/',
                            data=dict(
                            user_email_login="example8@email.com",
                            password_login="password8"
                            ))
        self.app.post('/CreateBucketList',
                data=dict(
                bucketlistcreated="TrialBucket3"
                ))
        add_activity_response = self.app.get('/AddActivities/0')
        self.assertIn(b"New Activity Name", add_activity_response.data)
        self.assertIn(b"Exit to ActivityList", add_activity_response.data)
        add_response = self.app.post('/AddActivities/0', data=dict(
                                        theActivity="activity1"))
        self.assertEqual(add_response.status_code, 302)
        view_activity_response = self.app.get('/ViewActivities/0')
        self.assertIn(b"activity1", view_activity_response.data)
        add_response0 = self.app.post('/AddActivities/0', data=dict(
                                theActivity="activity1"))
        self.assertIn(b" already exists in the activity list!", add_response0.data)
        add_response1 = self.app.post('/AddActivities/0', data=dict(
                                theActivity=""))
        self.assertIn(b"Ensure that the activity inserted is not an empty string!", add_response1.data)

    def test_edit_activity(self):
        self.app.post('/Register', data=dict(
                                        username_register="example9",
                                        useremail_register="example9@email.com",
                                        password_register="password9",
                                        confirm_new_password="password9"))
        self.app.post('/',
                            data=dict(
                            user_email_login="example9@email.com",
                            password_login="password9"
                            ))
        self.app.post('/CreateBucketList',
                data=dict(
                bucketlistcreated="TrialBucket4"
                ))
        self.app.post('/AddActivities/0', data=dict(
                                        theActivity="activity1"))
        edit_get_response = self.app.get('/EditActivity/0x0')
        self.assertIn(b"activity1", edit_get_response.data)
        edit_response1 = self.app.post('/EditActivity/0x0', 
                                       data=dict(
                                        new_activity=""
                                    ))
        self.assertIn(b"An activity cannot be replaced with an empty string", edit_response1.data)
        edit_response2 = self.app.post('/EditActivity/0x0', 
                                data=dict(
                                new_activity="activity1"
                            ))
        self.assertIn(b" already exists in the activity list", edit_response2.data)

    def test_delete_activity(self):
        self.app.post('/Register', data=dict(
                                        username_register="example10",
                                        useremail_register="example10@email.com",
                                        password_register="password10",
                                        confirm_new_password="password10"))
        self.app.post('/',
                            data=dict(
                            user_email_login="example10@email.com",
                            password_login="password10"
                            ))
        self.app.post('/CreateBucketList',
                data=dict(
                bucketlistcreated="TrialBucket5"
                ))
        self.app.post('/AddActivities/0', data=dict(
                                theActivity="activity1"))
        delete_get_response = self.app.get('/DeleteActivity/0x0')
        self.assertEqual(delete_get_response.status_code, 200)
        delete_post_response = self.app.post('/DeleteActivity/0x0')
        self.assertEqual(delete_post_response.status_code, 302 )

    def test_logout(self):
        logout_response = self.app.get('/Logout')
        self.assertEqual(logout_response.status_code, 302)

if __name__ == '__main__':
    unittest.main()






    


        
        
        
         

        
        
        
        
        
        
        
        


