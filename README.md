## Welcome to our Habitat for Humanity Class Project for CSC 425 Database Management Systems

The project itself, codename White Iverson is presented by the team Post Malone Fan Club consisting of Jordan Barge and Juan Valencia

## Initial Design Proposal

### Project Description
We are creating a Warehouse Inventory Management System with a project management and donation built on top of it. This will be in the form of a dynamic website.  This system will be built with a main page to direct traffic between volunteers and donors. These individual pages will allow the user to sign up with their email address and then depending on the log in will be taken to different pages. The volunteer page will display active projects, completed projects, and proposed projects, as well as a button to propose a project. The active project page allows you to see the details of the project, the other members of the project, and other information correlated with the project itself. If you are the project lead for that project you also get the ability to add items to that project itself with an inventory search and checkout. This allows the user to create and populate the project tables themselves. There you can also approve members and control more aspects of the project. The other side of the website has the donation sign up, log in, and donate page where users can see the items they’ve donated in the past, add new items to donate, and see where their contributions ended up.

### Technical Project Description
The language we are using primarily is [Python 3.7](https://www/python.org/). The web framework we are using for the backend is [Django version 2.1.2](https://www.djangoproject.com/). Our front end will be Dynamic Python and HTML provided by Django's API and CSS3 for styling.

### Entity Relationship Diagram
To be added later...

### Assumptions Made
Based on the current requirements and existing information, some assumptions were made in the creation and implementation of the Warehouse Inventory System (Codename White Iverson). For the health of the client and server layer of our system we also made some assumptions.

**Website-Related:**
- Some users will be site administrators, and these users can impersonate other users if needed.
- Users will login and have certain access granted to them based on their status as a project lead for certain projects.
- There are 2 primary user distinctions in logging in: Volunteers (Project members) and Donors (Businesses and Individuals).
- When signing up, Users will be prompted to use a valid email as their username.

**Business Rule Related:**
- Someone will have to do a preliminary inventory count to add the existing items into the system
- Admin have the power to directly manipulate the inventory tables when needed
- Projects will be proposed with items, materials, and people needed and then accepted when certain requirements are met.
- Projects will have a zip code related to them so that users can find the closest projects to them.
- A singular centralized warehouse is assumed to be the only warehouse available. If more warehouses are added this will require a small manipulation of the existing schema
- Donors can donate as a company or as an individual
- Donors can add an approximate retail value of the individual items they are donating or not
- Donors can see their past donations

### Proposed Schedule
 Date | Item 
 --- | --- 
 Oct 17 | First Presentation Completed 
 Oct 25 | Data Models Created 
 Oct 25 | First Page Created 
 Nov 4  | Start Progress Report 
 Nov 8  | Login, Donations, Volunteer Pages Finished 
 Nov 8  | Skeleton of other pages done 
 Nov 13 | Written Progress Report 
 Dec 2  | Final Presentation completed 
 Dec 3  | Team Report completed 
 Dec 4  | Final Project Presentation 
 Dec 5  | Individual Reports Completed 
 Dec 6  | All reports Due 
### Team Member Assignments

 Juan | Jordan 
 ------------- | ------------- 
 Pick Language to use | Create and Manage Project Schedule 
 Pick DBMS to use | Create Entity Relationship Diagram 
 Create Relational Schema Diagram | Populate Database when needed 
 Present First Presentation | In Charge of Documentation 
 Keep Personal notes on DBMS | 
 In charge of DBMS Implementation | 
 In charge of Application Implementation | Do majority of Final Presentation 
 Manage GitHub Repository for Project | Type up progress report 
 | Manage Extraneous Files 

| Shared |
| ---------- |
| Create SQL Schema and Relationships |
| Design and create necessary queries |
| Implement Application Program |
| Document Project |
| Create Project Summaries |
