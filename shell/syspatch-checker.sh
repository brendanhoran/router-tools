#!/bin/ksh
# Description :
#  A simple script designed to run from crontab to check for new syspatchs.

# Set the following :
# Where to send email report to
email_rcpt=""


applied_patches=`/usr/sbin/syspatch -l`
obsd_version=`sysctl kern.osrelease | cut -c 16-18`
mail_body="/tmp/patches-chk"

echo "----------------------------------------------------------------" > $mail_body
echo "Checking new patches for $obsd_version" >> $mail_body
echo "----------------------------------------------------------------" >> $mail_body
echo "Available patches upstream :" >> $mail_body
sys_patches=`/usr/sbin/syspatch -c`
if [ -n "$sys_patches" ]; then
  printf "$sys_patches\n" >> $mail_body
else
  printf "No new patches to install\n" >> $mail_body
fi
echo "----------------------------------------------------------------" >> $mail_body
echo "Applied patches :" >> $mail_body
printf "$applied_patches\n" >> $mail_body
echo "----------------------------------------------------------------" >> $mail_body

cat $mail_body | mail -s "OpenBSD patches check report" $email_rcpt

rm $mail_body
