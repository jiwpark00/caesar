import webapp2
from caesar import encrypt
import cgi

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
        <textarea type="text" name="textarea" style="height:150px; width:400px" placeholder="Enter your text here"></textarea>
        <br>
        <label>
        Number of positions to rotate?
        </label>
        <input type="text" name="rotateCount"></input>
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
        rotateCount = self.request.get("rotateCount")
        rotateCountInt = int(rotateCount)
        answer = encrypt(cgi.escape(textarea,quote=True),rotateCountInt)
        encrypt_form = """
        <form method="post">
        <textarea name="encryptedarea" style="height:150px; width:400px">{0}</textarea>
        <br>
        </input>
        </form>
        """.format(answer)

        body_content = edit_header +  encrypt_form
        response = page_header + body_content + page_footer
        self.response.write(response)

app = webapp2.WSGIApplication([
    ('/', Index),
    ('/encrypted',EncryptedView)
], debug=True)
