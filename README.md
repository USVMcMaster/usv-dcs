**Welcome to the Unmanned Surface Vehicle - Automation Capstone Repo!**

**1. Obtain pip for python3** <br />
sudo apt install python3-pip <br />

**2. Obtain python dependancies** <br />
pip3 install numpy pyserial inputs <br />

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

**6. Add your id_rsa.pub key file to your git account** <br />
Settings >> SSH and GPG keys >> New SSH key

**7. Request collaborator status from admin** <br />

**Wait until you're added as a collaborator!**

**8. Create directory for the repo.** <br />
cd ~ <br />
mkdir usvmac <br />
cd ./usvmac <br />
git init <br />
git remote add origin git@github.com:USVMcMaster/usvmac.git <br />
