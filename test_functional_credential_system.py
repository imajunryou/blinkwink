import os

import pytest
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    """Create a Firefox webdriver before each test; close it when done"""
    driver = webdriver.Firefox()

    yield driver

    driver.close()

# Ima navigates to the site and is taken to the main page.

def test_site_access(driver):
    driver.get("http://localhost:5000")  # How to abstract out the URI?
    assert driver.title == "Blinkwink and you're gone."

# Using their desktop, they see a row of options at the top, with a pulldown menu on the left side, containing more options.

# Using a smaller screen, all of the options are collapsed into the menu, with the options that made up the visible section being presented first in the menu.

# The available options include a login option.

# Ima clicks the login option and is taken to a login page.

# The login page contains the same header menu, and a login form.

# The form contains a field for a username, a field for a password, a link in case Ima has forgotten their credentials, and a link in case Ima hasn't registered an account yet.

# Below these options is a sign-in button.

# Ima attempts to enter a username, having not yet created an account.  They then press the sign-in button.  Ima is informed that either the username or password is incorrect, and that they should check their credentials and try again.

# Ima's username remains filled in the form, despite the appearance of this message.

# Ima deletes the username, and enters a password instead, followed by again pressing the sign-in button.  Ima is again informed that either the username or password is incorrect, and that they should check their credentials and try again.

# Ima's password field is emptied after this occurs, leaving the form blank.

# Ima enters both a username and a password, and presses the sign-in button.  Ima is once again presented with the message that either their username or password is incorrect, and that they should check their credentials and try again.

# Ima presses the "Forgot Password" link.  This takes them to a new page, with a simpler form.  The header menu is present on this page as well.

# Ima sees a form with a field for an email address, and a submit button.  Ima also sees two more links; there is a link back to the login page, and a second link to the registration page.

# Ima clicks the submit button, without entering an email address.  They are shown a message informing them that they must enter a valid email address first.

# Ima enters an invalid email address, and presses the submit button.  They are again shown a message informing them that they must enter a valid email address first.  The form is cleared in the process.

# Ima enters a valid email address that does not correspond with a known user, namely their own email address, and then presses the submit button.  Ima is taken back to the login page, this time with a message informing them that if the given email is associated with an account, it will receive an email with a link in need of clicking.

# Ima selects the option to register, from the login page, and is taken to a new page.  This page has the same header menu, and also contains a form for registering a new account.

# The form consists of a field for email, a confirmation field, a password field, and a confirmation field for the password as well.  There is also a submit button, and two links.  One link returns to the login page, and the other navigates to the forgot password page.  All fields are marked as required.

# Ima enters an invalid email in the first field, and attempts to submit the form.  All fields are highlighted and a message appears informing Ima that there are required fields which do not have valid data in them.  The invalid email field is unchanged.

# Ima enters a valid email in the first field, and attempts to submit the form.  The remaining empty fields are highlighted, and the same message appears.  The email remains filled out.

# Ima removes the valid email and enters an invalid email in the email confirmation field.  As they begin typing, the confirmation field highlights, and a message appears above it informing Ima that the email does not match the original (empty) field.

# They then press submit.  All fields again highlight, and the same message again appears.  The confirmation email field remains filled out.

# Ima enters a valid email in the email confirmation field.  As they begin typing, there is the same message above the field about mismatched emails, and the field highlights.

# Ima presses submit.  All fields are highlighted, and the same message appears.  The confirmation email field remains filled out.

# Ima enters an invalid email in both email fields.  As the confirmation field has information entered it is highlighted as before.  Once the confirmation field matches the first field, such that they both have the same invalid email, the highlighting and message disappear.

# Ima presses submit.  All four fields are highlighted, and the message appears again.  The email fields are unchanged.

# Ima enters an invalid email in the first slot and a valid email in the second slot.  As they enter the info in the confirmation field, it again highlights as not matching the first field.

# Ima presses submit, and all four fields are highlighted, and the message again appears.  The email fields are unchanged.

# Ima enters valid emails corresponding to an existing user in both fields, and presses submit.  The password fields are highlighted, and the same message again appears, with the emails unchanged.

# Ima enters valid existing emails in both fields, and enters an invalid password in the first password field.  Ima presses submit, and the same message about invalid fields appears with the emails unchanged, but the password removed.

# Ima enters valid existing emails in both fields, and also enters invalid, but matching, passwords in both password fields.  Ima presses submit.  A message about the password not being valid is shown, listing the specific rules that were violated.  The invalid passwords are removed, but the emails remain.

# Ima enters valid existing emails in both fields, and also enters valid, but not matching, passwords in both password fields.  The confirmation password is highlighted, and a message appears above its field about the mismatch.  Ima clicks submit.  A message about invalid fields is shown, with the passwords being removed.

# Ima enters valid, matching passwords, but removes the emails entirely, and clicks submit.  A message about invalid fields is shown, with the passwords being removed.

# Ima enters valid, matching, emails that already exists in the system, and valid matching passwords, and then clicks submit.  A message appears informing ima that the chosen email is already in use.  The passwords are removed.

# Ima enters valid, matching, emails that do not exist in the system, and valid matching passwords, and clicks submit.  Ima is taken to a confirmation screen with a message informing them that a confirmation email was sent.

# After seeing the confirmation screen, Ima returns to the registration page and attempts to reregister with the same valid email and password.  When Ima clicks submit, a message appears informing Ima that the email is already in use.

# When Ima receives the confirmation email, they click the "Cancel" link within.  This marks them as "Cancelled" in the database.  Ima then attempts to log in, and is informed that their credentials are not correct.  Ima then attempts to recover a password, and is informed that if the account exists, an email will be sent.  Ima gets no such email.  Ima then attempts to reregister the account and is able to.

# Before clicking anything in the email, Ima tries to log in.  They encounter a message about the account being unconfirmed, and needing to check their email.  They are informed that if they misplaced the confirmation email, they'll need to wait a day and reregister.

# Before clicking anything in the email, Ima attempts to use the "Forgot Password" interface.  They receive an "Unconfirmed account" message.

# Before clicking anything in the email, Ima attempts to reregister the account.  They receive an "Email in use" message.

# Ima waits until the email expires, at which time they are marked as "expired" in the database.

# With an expired email, Ima attempts to confirm the email.  This leads to a message about how the email expired and that they'll need to reregister, and confirm the email within the given time frame.

# With an expired email, Ima attempts to cancel the email.  This leads to the same "email expired" message.

# With an expired email, Ima attempts to log in, and is given the "Invalid credentials" message.

# With an expired email, Ima attempts to recover the password, and is given the "If the account exists, a recovery email will be sent" message.

# With an expired email, Ima attempts to reregister, and is able to.  An unexpired email is sent.

# With the new unexpired email, Ima clicks to confirm the email.  Ima is taken to the login page with a "Sucessful confirmation" message.

# After confirming the email, Ima is able to log in.

# Once logged in, Ima is taken to the main page.  The header menu has its "login" option changed to a "logout" option.

# Once logged in, Ima logs out of the account.  They are taken to the login page.

# Ima attempts to reset their password.  They receive a password recovery email with a deadline, and a confirmation link.

# Ima allows the password recovery email to expire, and attempts to log in.  They are allowed in without issue.  Ima logs out again.

# Ima attempts to recover their password again, and once more receives a recovery email.  Ima then attempts to recover their email again, without touching the first email.  A second email is sent.  Ima then clicks the link in the first email, and receives an "email expired" message.

# Ima clicks the link in the valid reset email, and is taken to a password entry page.  Ima declines to enter a password, and instead attempts to log in.  They successfully log in.

# Ima resets their password, confirms the email, and enters invalid passwords.  They receive an "Invalid password" message listing what rules are not followed.

# Ima resets their password, confirms the email, and enters valid mismatched passwords.  They receive an "Invalid fields" message, and the passwords are cleared.

# Ima resets their password, confirms the email, and enters valid passwords.  They are logged in, taken to the main page.  Ima logs out.

# After resetting their password, Ima attempts to log in with the original password, and receives an "Invalid credentials" message.

# After resetting their password, Ima attempts to log in with the new password, and is allowed in.  Ima then logs out again.

# Ima attempts to log in with invalid passwords, repeatedly.  After 5 attempts, they are locked out for an indicated period of time.

# Ima attempts to log in with invalid password after a lock, and receives an "account locked" message.

# Ima attempts to log in with valid password after a lock, and receives an "account locked" message.

# Ima waits for the lock to expire, and then uses the valid password.  They are allowed in.  They log out again.

# Ima attempts to login repeatedly with invalid passwords until they are locked out for another time period again.  Ima waits for the time period to elapse.  Ima proceeds to log in repeatedly with invalid passwords again until they are locked out.  This time the message states that they will need to reset their password to unlock their account, after time has elapsed.

# After fully locking the account, Ima tries to log in with correct credentials.  Ima gets an "Account locked" message.

# After fully locking the account, Ima tries to reregister the account.  Ima receives an "email in use" message.

# After fully locking the account, Ima tries to reset the password, and gets a confirmation email about the reset.

# With the account fully locked, and a reset requested, Ima confirms the reset email.  They are taken to the password page.  Instead of entering a password, Ima attempts to log in, instead, and receives an "Account locked" message.

# With a full lock, and a pw reset request confirmed, Ima attempts to reregister instead, and is given an "Email in use" message.

# With a full lock, and a pw reset request confirmed, Ima attempts to reset password again, before actually finishing the first reset.  They receive a second email.  The link simply takes them back to the password page.  Attempting to enter the password from the first attempt works fine.  Resetting their password takes them to the main page with their password reset, nullifying any time left on the lockout timer.  Ima logs out.

# Ima attempts to navigate to a restricted page, while not logged in.  They are redirected to the login page, with a message saying that they must log in to access that page.

# Ima logs in, and then attempts to navigate to a restricted page.  They are shown the page.  Ima remains logged in.  Ima navigates to another page, and is still logged in.  Ima logs out.

# Ima attempts to logout while already logged out, but the option is not available on the menu.  Ima remembers the url, anyway, and enters it.  They are redirected to the login page, with a message about already being logged out.

# Ima sees the "login" option on the header menu.  Ima proceeds to log in.  The "login" option becomes a "logout" option instead.  Ima logs out.

# Ima logs in, and then logs out.  Upon logout, they are taken to the login page.
