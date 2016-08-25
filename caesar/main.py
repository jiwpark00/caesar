import webapp2
from caesar import encrypt

page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>Caesar</title>
</head>
<body>
"""

page_footer = """
</body>
</html>
"""

class Index(webapp2.RequestHandler):
    def get(self):
        edit_header = "<h1>Caesar</h1>"

        text_form = """
        <form action="/encrypted" method="post">
            <textarea name="textarea" style="height:150px; width:400px" placeholder="Enter your text here"></textarea>
            <br>
            <input type="submit" value="Submit">
        </form>
        """
        body_content = edit_header + text_form
        response = page_header + body_content + page_footer
        self.response.write(response)

class EncryptedView(webapp2.RequestHandler):
    def post(self):
        edit_header = "<h1>Caesar</h1>"
        textarea = self.request.get("textarea")
        answer = encrypt(textarea,13)
        body_content = edit_header + answer
        response = page_header + body_content + page_footer
        self.response.write(response)

app = webapp2.WSGIApplication([
    ('/', Index),
    ('/encrypted',EncryptedView)
], debug=True)
