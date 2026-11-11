# Day 50: Interview Guide — Authorization, Permissions and Role-Based Access

**Related class notes:** [Day 50 notes](day_50_notes.md)  
**Approved mini-project:** Role-Based Employee Portal  
**Level:** Intermediate

## How to use this guide
For every scenario, identify the user, required permission, object ownership rule and expected HTTP response. Explain why a template-only check is insufficient.

## 1. Core technical questions

### Q1. What is authorization?
**Answer:** Authorization decides what an authenticated user may do or which resources they may access. It is separate from authentication, which verifies identity.

### Q2. What are Django's default model permissions?
**Answer:** Django creates add, change, delete and view permissions for models. A permission string includes the app label and model codename, such as profiles.change_employee.

### Q3. What does has_perm() do?
**Answer:** It checks whether a user has a specified permission and returns a Boolean. Permissions can be assigned directly or through groups.

### Q4. What is a Django Group?
**Answer:** A group is a collection of users. Permissions assigned to the group are available to its members, which simplifies role-based administration.

### Q5. Why use groups instead of assigning every permission individually?
**Answer:** A group lets an administrator assign a permission policy once and apply it to many users. New members inherit the group's permissions, and access can be removed by changing membership.

### Q6. What does permission_required do?
**Answer:** It is a decorator that protects a function-based view by checking whether the current user has a required permission.

### Q7. What is PermissionRequiredMixin?
**Answer:** It provides permission checking for class-based views. The required permission is declared through the permission_required attribute.

### Q8. What does raise_exception=True do?
**Answer:** It raises PermissionDenied when the required permission is absent, resulting in a 403 response through Django's error handling.

### Q9. What is least privilege?
**Answer:** Give a user only the access required to perform their responsibilities. Do not make ordinary users superusers for convenience.

### Q10. Why is hiding a button not authorization?
**Answer:** A user can manually type the URL or send a request. The server-side view must enforce permission and ownership checks.

### Q11. What is object-level authorization?
**Answer:** It decides whether a user may access a specific record, such as their own profile or an employee in their department. A model permission alone may not be enough.

### Q12. What is the difference between 403 and 404?
**Answer:** 403 means the server refuses access. 404 means the resource was not found or is intentionally concealed. The application should choose its behavior consistently.

## 2. Code and debugging questions

### Q13. Why might has_perm() return False?
**Answer:** Check the app label, codename, group membership, direct permissions, migration state and whether the user is the account you intended to test.

### Q14. Why can a superuser hide a permission bug?
**Answer:** Django treats superusers as having all permissions. Test with ordinary accounts to verify group and permission configuration.

### Q15. A template hides an edit link but direct URL access still works. What is missing?
**Answer:** The view is missing a server-side permission or ownership check. Template conditions are presentation logic, not the security boundary.

## 3. Scenario questions

### Q16. HR staff can edit jobs but should edit only their own jobs.
**Answer:** Use a model permission to establish the general capability, then check object ownership in the view before updating the specific job.

### Q17. A student can view another student's profile by changing an ID.
**Answer:** The view trusts an unscoped object ID. Retrieve the record through the current user's ownership relation or enforce a suitable object-level policy.

### Q18. A user has delete permission unexpectedly.
**Answer:** Inspect all groups and direct permissions assigned to the user. Remove unnecessary grants and test again with an ordinary account.

## 4. Mini-project discussion — Role-Based Employee Portal

Demonstrate:
1. Role matrix.
2. Group creation.
3. Permission assignment.
4. User membership.
5. Backend view protection.
6. Direct URL denial.
7. Ownership restriction.
8. Tests for allowed and denied users.

## 5. Readiness checklist

- [ ] I can explain authentication versus authorization.
- [ ] I can identify default model permissions.
- [ ] I can create groups and assign permissions.
- [ ] I can protect function-based and class-based views.
- [ ] I understand least privilege and ownership checks.
- [ ] I can test direct URL access.
- [ ] I can demonstrate Role-Based Employee Portal.

**Related notes:** [Day 50 class notes](day_50_notes.md)
