Project Description- 
This project is a Event Management System called montclair connect. Its purpose is for event scheduling. A user can create a event that will also send Email and SMS notifications to communicate any changes as well as any cancellations.
Its backend consists of using Django for backend and HTML/CSS for the frontend with DBsqlite being used for storing user information (ie: emails,phone numbers, Event info, passwords etc) Users and Admins have differing permissions (views in django).
Admins can remove events and provide a reason (note) for removing the event.
The user can only create their own events as well as remove their own events. 
The event consists of the time date and place fields that the user can enter,
In addition the system will check if there are any conflicting date and times so a user cant mass create events within a minute time span (ie spam).
