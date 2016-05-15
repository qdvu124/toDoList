Following are the account infos:

ADMIN INFO:

User Name: admin
Password: @Test12345
First Name: Ad
Last Name: min
Email: admin@Masta.com
Birthday 01/01/1954
Country: Vietnam
Secret Hint: Who Am I?
Secret Answer: Admin
TEST USER INFO:

User Name: testuser1
Password: @Test12345
First Name: Test
Last Name: User
Email: testuser1@Masta.com
Birthday 05/16/1957
Country: Vietnam
Secret Hint: Who Am I?
Secret Answer: Testuser1

YOUR ACCOUNT (if you want to use)

User Name: monead
Password: @Test12345
First Name: David
Last Name: Read
Email: dread@skidmore.edu
Birthday 01/01/1962
Country: Vietnam
Secret Hint: Where do I work in 2016?
Secret Answer: Skidmore College

===========================================================================================================================================================

admin account is important because it is the only account that can use the Generate Servlet/ Generate Pseudo Members in the View Page 

your user "monead" is a normal account, so if you want to generate pseudo users, you have to use the admin account

===========================================================================================================================================================

Following, I listed out features and some notices about them:

1. Refactor program to use Prepared Statement Singleton accepting (varargs)
2. Handle Exception Duplicated User and Email when creating new user (involve finding out the error code 1062 and deal with it)
3. Encode/Sanitize output in JSP page -> Prevent XSS
4. Have the user use CAPTCHA:
Create user requires CAPTCHA.
Login after the second failed attempts ->user needs to use CAPTCHA, if he logs in with the right CAPTCHA and wrong password, his user is locked
5. Modify Log to use report level "info, debug, warn, error, fatal" accordingly
6. CSRF Token generator for Edit/Delete/Add member form and manage this using a filter
7. Have an authentication filter to check user's authentication status
8. Have No Cache filter to prevent use to back to Memberlist page after logging out
9. User Redirect and Forward with consideration to prevent user from going back to login page after sign in (So the work flow is: Login->Forward Login Servlet-> Forward to Member List Servlet -> Redirect to Memberlist page --> This prevent user from submitting the login form again using Refresh form browser)
10. Get rid of some unnecessary uses of the controller() method, instead, use doPost() and doGet() as needed!
11. Mitigating Race Condition Vulnerability 
12. A system of turning tools into singleton and put parameters into the servlet parameters in web.xml
for example: encryption infos, database infos, workload for password hasher, number of failed login attempts allowed before sending CAPTCHA to user login
13. You can view "Database Generator Query/DbTableSetup.txt" to generate the table used for this project in the database
14. Use hybrid encryption to encrypt user's secret (which is used to reset user's password if his account is locked)
15. An offensive-enough error message system
16. Use Enum for Constant used throughout the web-app
17. Improved user UI using API (Date/ Color/ Country Picker and Bootstrap)
18. Error Page added
19. Use mailto: to make Contact form to administrator
20. When clicking Edit member, does not redirect to another page but use the same form as the Add form
21. Split saving from logout servlet, now when you click Save in the Member List page, member List instance is persisted and a new one is fetched from the database
22. Intense Input Validator system

Some are for security, some are for professionalism and trying to simulate production line quality, some are for sake of aesthetics. 


USE CASE:

User related:
1. Login
2. Create user
3. Unlock locked user (try to log in with wrong password a lot of times, hit the CAPTCHA right then use the wrong password would lead to your account locked)
4. Recover user-> reset password
5. Log out

Member related:
1. Add member
2. Edit member
3. Delete
4. Save
5. View Map (Notice the red button on top right corner of the Member List page)


IF YOU ARE admin, play with generate pseudo users and remove them afterwards


