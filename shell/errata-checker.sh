#!/bin/ksh
# Description :
#  A simple script designed to run from crontab to check for new syspatchs.

# Set the following :
# Where to send email report to
email_rcpt="admin@basstech.net"
# end settings

applied_errata=`/usr/sbin/syspatch -l`
obsd_version=`sysctl kern.osrelease | cut -c 16-18`
mail_body="/tmp/errata-chk"

echo "----------------------------------------------------------------" > $mail_body
echo "Checking new patches for $obsd_version" >> $mail_body
echo "----------------------------------------------------------------" >> $mail_body
echo "Available patches upstream :" >> $mail_body
errata=`/usr/sbin/syspatch -c`
if [ $? != 0 ]; then
  printf "$errata\n" >> $mail_body
else
  printf "No new patches to install\n" >> $mail_body
fi
echo "----------------------------------------------------------------" >> $mail_body
echo "Applied patches :" >> $mail_body
printf "$applied_errata\n" >> $mail_body
echo "----------------------------------------------------------------" >> $mail_body

cat $mail_body | mail -s "OpenBSD patches check report" $email_rcpt

rm $mail_body
