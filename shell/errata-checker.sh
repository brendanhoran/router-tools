#!/bin/ksh
# Description :
#  A simple script designed to run from crontab to check for new errata.

obsd_version=`sysctl kern.osrelease | cut -c 16-18 | tr -d '.'`
# Where to send email report to
email_rcpt="brendan@horan.hk"


errata=`links -dump http://www.openbsd.org/errata$obsd_version.html | grep FIX`
applied_errata=`ls -l /root/patches/$obsd_version/ | awk '{print $9}'`
mail_body="/tmp/errata-chk"

echo "----------------------------------------------------------------" > $mail_body
echo "Checking errata for $obsd_version" >> $mail_body
echo " " >> $mail_body
echo "----------------------------------------------------------------" >> $mail_body
echo "Available errata patches upstream :" >> $mail_body
echo " " >> $mail_body
printf "$errata\n" >> $mail_body
echo " " >> $mail_body
echo "----------------------------------------------------------------" >> $mail_body
echo "Applied errata patches locally :" >> $mail_body
printf "$applied_errata\n" >> $mail_body
echo "----------------------------------------------------------------" >> $mail_body

cat $mail_body | mail -s "OpenBSD errata check report" $email_rcpt

rm $mail_body
