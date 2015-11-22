from validate_email import validate_email
import sys
# List of configurations
# {first_name}{last_initial}

# Holds a list of potential configurations for an email address
# ie {first_name}{last_initial} would be anshulj for anshul jain
email_configs_file= "configs.txt"
email_configs = []

def load_configs():
  global email_configs
  with open(email_configs_file) as f:
    # use split lines to ignore \n char at end of lines
    email_configs = f.read().splitlines()
    return email_configs

def get_email_from_config(config, first_name, last_name):
  email = config
  email = email.replace("{first_name}", first_name)
  if first_name: email = email.replace("{first_initial}", first_name[0])
  email = email.replace("{last_name}", last_name)
  if last_name: email = email.replace("{last_initial}", last_name[0])
  return email

def find_email(first_name, last_name, company_domain):
  for config in email_configs:
    email = get_email_from_config(config, first_name, last_name) + "@" + company_domain
    # print "trying email: " + email
    try:
      if validate_email(email, verify=True):
        #print "success"
        return email
    except:
      print "error on " + email
    #print "email not valid"
  return None

if __name__ == "__main__":
  if len(sys.argv) < 4:
    #print "ERROR: find_email expects 4 arguments, only " + str(len(sys.argv)) + " received"
    sys.exit(1)

  load_configs()
  email = find_email(sys.argv[1], sys.argv[2], sys.argv[3])

  if email:
    print email
  else:
    print "email not found"
