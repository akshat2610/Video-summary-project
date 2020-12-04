function validate_signin(form){
  var fail = validate_username(form.username.value);
  fail += validate_password(form.password.value);
  if (fail.length !== 0){
    alert(fail);
    return false;
  }
  else return true;
}

function validate_signup(form){
  var fail = validate_username(form.username.value);
  fail += validate_password(form.password.value);

  if (form.password.value !== form.password_reenter.value)
    fail += 'Passwords do not match';

  if (fail.length !== 0){
    alert(fail);
    return false;
  }
  else return true;
}

function validate_username(username){
  if (username.length < USERNAME_MIN_LENGTH || username.length > USERNAME_MAX_LENGTH)
    return 'Username length must be between ' + USERNAME_MIN_LENGTH + ' and ' + USERNAME_MAX_LENGTH + '\n';
  if (/[^a-zA-Z0-9_-]/.test(username))
    return 'Username can only contain a-z, A-Z, 0-9, - and _\n';

  return '';
}

function validate_password(password){
  if (password.length < PASSWORD_MIN_LENGTH)
    return 'Password too short';
  if (!/[a-z]/.test(password) || ! /[A-Z]/.test(password) ||!/[0-9]/.test(password))
    return 'Password must contain at least 1 lowercase letter, 1 uppercase letter, and 1 number\n';

  return '';
}

const USERNAME_MIN_LENGTH = 5;
const USERNAME_MAX_LENGTH = 10;
const PASSWORD_MIN_LENGTH = 8;
const MIN_ALLOWED_AGE = 18;
const MAX_ALLOWED_AGE = 120;
