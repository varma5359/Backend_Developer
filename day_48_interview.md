# Day 48: Interview Guide — Password Management, Password Reset and Secure Password Storage

**Related class notes:** [Day 48 notes](day_48_notes.md)  
**Approved mini-project:** Password Recovery System  
**Level:** Beginner to Intermediate

## How to use this guide
Treat password questions as security questions. Explain the risk, the Django API and the safe workflow. Never use real credentials in interview demonstrations.

## 1. Core technical questions

### Q1. Why should passwords be hashed?
**Answer:** A database should not store the original readable password. Django stores an encoded password hash and verifies a submitted candidate against it. This reduces the impact of a database exposure compared with storing plain-text passwords.

### Q2. What is the difference between hashing and encryption?
**Answer:** Hashing is designed to be one-way and is used for password verification. Encryption is reversible with the correct key and is used when the original data must be recovered.

### Q3. What is a salt?
**Answer:** A salt is random data used as part of a password hashing process. It helps ensure that identical passwords do not produce identical stored hash values.

### Q4. What does set_password() do?
**Answer:** It prepares a password hash using Django's configured password hasher and places the encoded value on the user instance. The instance must then be saved to persist the change.

### Q5. What does check_password() do?
**Answer:** It verifies a candidate password against the stored encoded value and returns a Boolean. It does not reveal or decrypt the original password.

### Q6. Why is direct assignment to user.password unsafe?
**Answer:** It bypasses Django's password-setting workflow and can store a raw value that cannot be verified through the normal authentication system. Use create_user(), set_password() or built-in forms.

### Q7. What are password validators?
**Answer:** They are configured rules that decide whether a proposed new password is acceptable. Django provides validators for minimum length, common passwords, numeric-only passwords and similarity to user attributes.

### Q8. What does validate_password() do?
**Answer:** It runs the configured password validators and raises ValidationError when the candidate does not satisfy the policy.

### Q9. What is the difference between password change and password reset?
**Answer:** Password change is normally used by an authenticated user who can provide the current password. Password reset is used when the user cannot sign in and needs a time-limited recovery link.

### Q10. What does PasswordChangeForm validate?
**Answer:** It checks the current password and validates the new password and confirmation using Django's password validation behavior.

### Q11. What does PasswordResetView do?
**Answer:** It accepts an account email and starts the reset workflow. Django generates reset instructions using a time-sensitive token and sends the email through the configured email backend.

### Q12. What does the console email backend do?
**Answer:** It prints email content to the development terminal rather than delivering it to a real mailbox. It is useful for local testing only.

### Q13. What is a password reset token?
**Answer:** It is a time-sensitive value used by Django to validate a password reset link. Anyone who obtains a valid link may be able to reset the account, so the link must be protected.

### Q14. Why should reset responses not reveal whether an email exists?
**Answer:** Revealing account existence allows attackers to enumerate registered email addresses. A neutral confirmation message avoids confirming whether an eligible account was found.

### Q15. What is update_session_auth_hash() used for?
**Answer:** It updates the current session's authentication hash after a password change so the current user can remain signed in. Custom password-change implementations must handle this deliberately.

## 2. Debugging questions

### Q16. Password reset email does not appear.
**Answer:** Check EMAIL_BACKEND, runserver terminal, user email address, account eligibility and reset form submission. With the console backend, the message appears in the server terminal, not an inbox.

### Q17. Reset link is invalid.
**Answer:** It may have been copied incompletely, expired, already used, or invalidated by an account-state/password change. Request a new link rather than editing the token.

### Q18. New password is rejected.
**Answer:** Read the validator messages. Check minimum length, common password, numeric-only and similarity rules. Do not remove validators just to make a weak test password pass.

### Q19. User is signed out after reset.
**Answer:** Password reset can invalidate existing sessions because the authentication hash changes. This is a security behavior. PasswordChangeView handles the current session differently from a reset workflow.

## 3. Scenario questions

### Q20. A developer emails a forgotten password to the user.
**Answer:** This is unsafe. The application should not be able to recover the original password. Send a time-limited reset link that lets the user choose a new password.

### Q21. A reset link is pasted into a public support ticket.
**Answer:** Treat the link as compromised. Request a new reset link and do not share reset tokens publicly.

### Q22. A production application uses console email backend.
**Answer:** Console backend is for development. Production requires a trusted email provider, secure credentials, TLS, delivery monitoring and secret management.

## 4. Mini-project discussion — Password Recovery System

Demonstrate:
1. Password hash verification.
2. Password change while signed in.
3. Reset request page.
4. Console email output.
5. Valid reset link.
6. Invalid or expired link behavior.
7. Verification that the new password works.
8. Proof that the old password no longer works.

## 5. Readiness checklist

- [ ] I can explain hashing versus encryption.
- [ ] I can explain set_password() and check_password().
- [ ] I can explain password validators.
- [ ] I can explain password change and reset.
- [ ] I can explain reset tokens and email backend.
- [ ] I can explain session behavior after password changes.
- [ ] I can demonstrate Password Recovery System safely.

**Related notes:** [Day 48 class notes](day_48_notes.md)
