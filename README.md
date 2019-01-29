**Welcome to the Unmanned Surface Vehicle - Automation Capstone Repo!**

The following document assumes you have a fresh install of Ubuntu 18.04. Also, by this point, you should have git account and have access to the git repo. If you have any pending updates from Ubuntu, please do them before going through this guide.

**Notes:**
All commands will be done through terminal.
When using sudo, you may be asked to enter your password. Terminal does not show the characters you type in for your password. Enter your password whem prompted.
If when installing any of the following instructions show up, follow all instructions.

**1. Obtain pip for python3** <br />
sudo apt install python3-pip <br />

**2. Obtain numpy, scipy, matplotlib, jupyter** <br />
pip3 install numpy scipy matplotlib jupyter <br />

**3. Installing git** <br />
sudo apt-get update <br />
sudo apt-get install git <br />

**4. Setting up git username and email** <br />
git config --global user.name "Your name goes here" <br />
git config --global user.email "Your email goes here" <br />

**5. Generate id_rsa.pub key file** <br />
ssh-keygen -t rsa -b 4096 -C "your_email@domain.com" <br />

You will get the following output: <br />
*Generating public/private rsa key pair.* <br />
*Enter file in which to save the key (/home/username/.ssh/id_rsa):* <br />
Press enter. <br />

*Enter passphrase (empty for no passphrase):* <br />
Press enter. <br />

*Enter same passphrase again:* <br />
Press enter. <br />

After pressing enter you will see a key randomart image. At this point, your key has been created. <br />

**Note**: If ssh doesn't work, you probably don't have it installed. Run the following in terminal and then generate your key file using the code above.

sudo apt-get install openssh-server

**6. Give Rohit your id_rsa.pub key file** <br />
Navigate to your home directory from the file explorer. If you do not see any files that have a "." in front of them, press ctrl+h to view hidden files. You should see a .ssh folder. Open that folder and find your "id_rsa.pub" file. Send this file to Rohit. Wait for Rohit to add your key to the repo. Without this, you will not be able to use the remote repo. 

**DO NOT CONTINUE UNTIL ROHIT GIVES YOU THE GO-AHEAD**

**7. Create directory for remote repo.** <br />
cd ~ <br />
mkdir usvmac <br />
cd ./usvmac <br />
git init <br />
git remote add origin git@github.com:USVMcMaster/usv-dcs.git <br />

**8. Make your own personal branch and clone master** <br />
git checkout -b "name of your new branch" <br />
git checkout "name of your new brach <br />
git pull origin master <br />

**9. Make test file** <br />
touch "yourname.txt" <br />
git add "yourname.txt" <br />
git commit "yourname.txt" <br />

**Note**: After writing the commit line and pressing enter, it will open a nano file in terminal. Write your commit comment here (can be anything, keep it professional). Press ctrl+x and then y and then enter. This will save the commit message.

**10. Push to YOUR branch** <br />
git push origin "name of your new branch" <br />

Congrats, you have done your first push to github.

**Note: Under no circumstances should you be on the master branch. DO NOT PUSH TO MASTER.** <br />
**PUSHING TO MASTER WILL LEAD TO REMOVAL FROM PROJECT AND TEAM.**
