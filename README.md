This is my project for a Help Desk ticketing system.

This system includes python codes for submitting tickets, reviewing tickets, as well as responding, close, and re-open available tickets. 

This system also have an UI using tkinter module for the whole program. 

To navigate through the code:
1. Main.py --> is where to run the whole code
2. Complain_UI.py --> a code for UI on complain menu, this code will execute a UI for user to create and submit a ticket
3. Review_UI.py --> a code for UI on Review menu, this code will also create a UI for user to review all ticket submitted, open ticket details, respond to it, close, and re-open.
4. Statistic_UI.py --> a code for a pop-up window showing the statistic of how many ticket, open ticket, and closed ticket available on the system
5. Class.py --> is where I divide and define Ticket classes as well as all of the function to create and modify tickets.
6. Ticket_list_py --> contains a class for hashmap feature and this is how I store all my ticketing details.
7. Window_update.py --> contains a function to refresh my UI.

To run and test the code:
1. Run Main.py
2. go to complain menu
3. fill all the blank spaces with value matching the template. (you can use anything for staff ID, but you can't submit the ticket if something left blank)
4. submit the ticket and repeat as many times.
5. go to review menu (here you can see every ticket submitted)
6. if the you can't find a specific ticket, you can start typing on the boxes to search a specific ticket available. You can also try using a dropdown menu on status search bar to see all ticket that has the same status.
7. you can select a ticket simply by clicking on it and see details of the ticket by clicking open  (this should pop a window up displaying ticket id, name, and content of the ticket in read only)
8. by clicking respond button, it will give you a blank text box to write a respond to the ticket and a submit button to submit the respond (you cant leave the respond as blank)
9. you can close a ticket with responded as status by simply selecting the ticket and click close ticket button
10. you can also re-open a ticket with closed status by the same way using Re-Open ticket button. This will send you back to complain menu but with filled and read only data except for the content/description (it will fill up with the old content but you can change it or not at all) and re-submit the ticket. This will make the ticket status as Re-open
11. Open, responded, and Re-open ticket is counted as Open ticket and closed is counted as Closed ticket in the statistic window. (please bear in mind that the window is not auto refresh, to refresh the statistic you click on the statistic menu again to pop up a new window that shows updated statistic).
