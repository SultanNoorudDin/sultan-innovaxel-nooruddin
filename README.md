# URL-SHortener
## api description
Method | URL | Description
POST | /shorten/ | Create a new short URL
GET | /urls/ | List all shortened URLs
GET | /urls/<id>/ | Retrieve details of a URL
PUT | /urls/<id>/update/ | Update a URL
DELETE | /urls/<id>/delete/ | Delete a URL
GET | /<shortcode>/ | Redirect to original URL
