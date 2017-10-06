#!/bin/sh

echo "pushing resume automatically."

git pull origin master
git add resume.md

if [ $# -gt 0 ]
then 
    git commit -m "$*"
    git push origin master
else
    echo ""
    echo "No arguments"
    echo "Comment of commiting will be \"updated resume using shellscript.\""
    echo "Do you continue? (y/n)"
    read ANSWER
    if [ "$ANSWER" == "y" ]
    then
        git commit -m "updated resume using shellscript."
        git push origin master
        open -a "/Applications/Google Chrome.app" https://github.com/OnizukaLab/tashiKANI_resumes/blob/master/takebayashi_yuto/resume.md
    else
        echo "Please enter the message to commit"
    fi
fi
