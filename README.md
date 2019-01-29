Welcome to the Unmanned Surface Vehicle - Automation Capstone Repo!

The following document assumes you have a fresh install of Ubuntu 18.04 and that you have a working internet connection. Also, by this point, you should have git account and have access to the git repo. If you have any pending updates from Ubuntu, please do them before going through this guide.

**Notes:**
All commands will be done through terminal.
When using sudo, you may be asked to enter your password. Terminal does not show the characters you type in for your password. Enter your password whem prompted.
If when installing any of the following instructions show up, follow all instructions.

**1. Obtain pip for python3**
sudo apt install python3-pip

**2. Obtain numpy, scipy, matplotlib, jupyter**
pip3 install numpy scipy matplotlib jupyter

**3. Installing git**
sudo apt-get update
sudo apt-get install git

**4. Setting up git username and email**
git config --global user.name "Your name goes here"
git config --global user.email "Your email goes here"

**5. Generate id_rsa.pub key file**
ssh-keygen -t rsa -b 4096 -C "your_email@domain.com"

You will get the following output:
*Generating public/private rsa key pair.*
*Enter file in which to save the key (/home/rohit/.ssh/id_rsa):*
Press enter.

*Enter passphrase (empty for no passphrase):*
Press enter.

*Enter same passphrase again:*
Press enter.

After pressing enter you will see a key randomart image. At this point, your key has been created.

**Note**: If ssh doesn't work, you probably don't have it installed. Run the following in terminal and then generate your key file using the code above.

sudo apt-get install openssh-server

**6. Give Rohit your id_rsa.pub key file**
Navigate to your home directory from the file explorer. If you do not see any files that have a "." in front of them, press ctrl+h to view hidden files. You should see a .ssh folder. Open that folder and find your "id_rsa.pub" file. Send this file to Rohit. Wait for Rohit to add your key to the repo. Without this, you will not be able to use the remote repo. 

**DO NOT CONTINUE UNTIL ROHIT GIVES YOU THE GO-AHEAD**

**7. Create directory for remote repo.**
cd ~
mkdir usvmac
cd ./usvmac
git init
git remote add origin git@github.com:USVMcMaster/usv-dcs.git
git pull origin master

**8. Make your own personal branch and clone master**
git checkout -b "name of your new branch"
git checkout "name of your new brach

**9. Make test file**
touch "yourname.txt"
git add "yourname.txt"
git commit "yourname.txt"

**Note**: After writing the commit line and pressing enter, it will open a nano file in terminal. Write your commit comment here (can be anything, keep it professional). Press ctrl+x and then y and then enter. This will save the commit message.

**10. Push to YOUR branch**
git push origin "name of your new branch"

Congrats, you have done your first push to github.
