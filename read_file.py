from validate_email import validate_email
import sys
import os
import csv

# Holds a list of potential configurations for an email address
# ie {first_name}{last_initial} would be anshulj for anshul jain



email_configs_file= "find_email/configs.txt"
email_configs = []

def load_configs():
  global email_configs
  this_dir, this_filename = os.path.split(__file__)
  path = os.path.join(this_dir, email_configs_file)
  with open(path) as f:
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

  if len(sys.argv) != 3:
  	print "ERROR: wrong number of args"
  	sys.exit(1)

  load_configs()
  file_name = sys.argv[1]
  output_file_name = sys.argv[2]

  with open(file_name, 'rb') as csvfile:
  	leads = csv.reader(csvfile, delimiter=',')
  	with open(output_file_name, 'wb') as csvof:
  	  of = csv.writer(csvof, delimiter=',')
  	  for row in leads:
  		first_name, last_name = row[1].split()
  		domain = row[4]
  		row[3] = find_email(first_name, last_name, domain)
  		of.writerow(row)
  		print first_name + " " + last_name + " from " + row[0] + " found"





