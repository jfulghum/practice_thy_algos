
Users can:
    * create hypertexts (clickable hyperlink embedded in text)

Maybe
--------
Users can:
    * set a color theme (front-end feature)
    
API Signatures
    
createLink(url, text) -> link_id
getLink(url) -> http_redirect
updateLink(link_id, url, text) -> link_id
deleteLink(link_id) -> boolean
listLinks(user_id) -> Link[]


setTheme(buttonStyle, backgroundStyle, 
        backgroundImage, ...etc...) -> void

Very broadly speaking, the stored data are dictionaries of Object-to-HyperLink for each user
so any schema matching that format will be acceptable.

Relational because every link has the same schema.
-- OR --
Document because links are such small data, we can store all of a user's
links and metadata in an array in a single document and avoid joins altogether.

Which type of database(s) would you use and what would each of them store?

Describe the tables and columns.

User Table
ID
Email
Hashed password
Date Created

Links Table
ID
User ID
URL
Title
Description
Date Created
Number of Clicks
Platform

Platform Table:
ID 
Platform URL
Icon


Purpose(s) of each service
--------------------------------
LinkTreeService
    * Handles CRUD operations for links
    * stores/retrieves images associated with each link



