# Gitlab cheatsheet by Ehsan Shirzadi

### How to reset root password?
First start Rails console and it takes a few minutes:
```
gitlab-rails console
```
In console put these commands:
```
user = User.find_by_username 'root'
user.password = 'secret_pass'
user.password_confirmation = 'secret_pass'
user.send_only_admin_changed_your_password_notification!
user.save!
```
More info here: https://docs.gitlab.com/ce/security/reset_user_password.html#reset-your-root-password


Email: Ehsan.Shirzadi@Gmail.com
Web: www.ehsanshirzadi.com
