import os
import pathlib
from flask import Flask, redirect, session, request, render_template, abort
from google_auth_oauthlib.flow import Flow
from google.oauth2 import id_token
import google.auth.transport.requests

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Set a secret key for session management

# Google OAuth2 setup
web = {'client_id': 'client_id'}  # Replace with your Google client ID
GOOGLE_CLIENT_ID = web['client_id']
client_secrets_file = os.path.join(pathlib.Path(__file__).parent, ".client_secrets.json")  # Path to your secrets file

flow = Flow.from_client_secrets_file(
    client_secrets_file=client_secrets_file,
    scopes=["https://www.googleapis.com/auth/userinfo.profile", "https://www.googleapis.com/auth/userinfo.email", "openid"],
    redirect_uri="https://www.sd3aiotclassserver.online/callback"  # Replace with your production callback URL
)

# Session decorator to require authentication
def login_is_required(function):
    def wrapper(*args, **kwargs):
        if "google_id" not in session:
            return redirect('/login')  # Redirect to login if not authenticated
        else:
            return function(*args, **kwargs)
    return wrapper

# Home page with login button
@app.route("/")
@login_is_required
def index():
    return render_template("index.html", user_name=session['name'])  # Render a page after login

# Login route
@app.route("/login")
def login():
    authorization_url, state = flow.authorization_url()
    session["state"] = state
    return render_template("login.html")  # Render login page

@app.route("/login_redirect")
def login_redirect():
    authorization_url, state = flow.authorization_url()
    session["state"] = state
    return redirect(authorization_url)

# Callback route to handle OAuth response
@app.route("/callback")
def callback():
    flow.fetch_token(authorization_response=request.url)

    if not session["state"] == request.args["state"]:
        abort(500)  # State mismatch, possible CSRF attack

    credentials = flow.credentials
    request_session = flow.authorized_session()
    token_request = google.auth.transport.requests.Request(session=request_session)

    # Get user info
    id_info = id_token.verify_oauth2_token(
        id_token=credentials._id_token,
        request=token_request,
        audience=GOOGLE_CLIENT_ID
    )

    # Save user information in session
    session["google_id"] = id_info.get("sub")
    session["name"] = id_info.get("name")
    session["google_token"] = credentials._id_token

    return redirect("/")  # Redirect to home after successful login

# Logout route
@app.route("/logout")
def logout():
    session.clear()  # Clear the session
    return redirect("/login")  # Redirect to login after logout

if __name__ == "__main__":
    app.run(debug=True)
