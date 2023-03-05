# Flask Webapp - Dashboard Tutorial
This webapp will be an example of how to create a Dashboard using Flask. 

### Topics Covered:   
* Virtual Environment
* Flask Webapp Folder Structure
* Front-End   
    * HTML _(Hyper-Text Markup Language)_ - The layout of the different views
    * CSS _(Cascade Style Sheet)_ - The styling of the layouts (e.g. custom colors, shapes, sizes, etc.), including styling frameworks
    * JS _(Javascript)_ - Programmed functionality of the views when interacted with by the user (e.g. clicks, drags, etc.)
* Back-End
    * Database - Storage/Recovery
    * JS _(Javascript)_ - Interacting with the Database
    * Python Flask methods 

## Objective:   
___
To illustrate a realworld Webapp use case for a small business.

## Functional Requirements:
___
1. Have a way to add and remove barbers (admin)
2. The main dashboard should list clients with different states:   
   2a. Arrived   
   2b. Late   
   2c. In the chair
3. The main dashboard should also list the barbers with different states:   
   3a. Booked   
   3b. Cutting   
   3c. Unavailable   
   3d. Open (Taking Walk-In's)   
   > NOTE : The main dashboard should include barber name & chair position
4. Each barber name on the main dashboard will be clickable, and that click
   should provide that barber's dedicated dashboard, including:   
   * Current Day's availability
   * Current Status (see #3)

The webapp will include the following views:   
* admin view
* main dashboard view
* barber dashboard view

