# Artificial-Intelligence
Here I will continuously upload my activities &amp; Tasks related to AI.


## My approuch in Installing ROS (Robot Operating System) on Ubuntu with steps and links .
![ros](https://user-images.githubusercontent.com/67114907/91162855-55cad480-e6d5-11ea-9692-e7652f8ba8cb.jpg)

To install ROS in our computer we need first to install the Linux based Ubuntu operating system and run it on top of our Windows OS.
Even though ROS can be made to run on other Linux based operating systems,
it works best with Ubuntu based operating systems.

Let us follow my way in installing it in the next three simple steps ..

## 1st STEP : Installing VirtualBox
![virtualbox-61](https://user-images.githubusercontent.com/67114907/91163539-63cd2500-e6d6-11ea-8d55-f17cf82ebda2.png)

VirtualBox lets us run Ubuntu on your Windows machine, 
which is a key requirement for ROS
To Install VirtualBox ,
we need to dawoloud virtualbox from the internet then installing it .The installation process of it is pretty straightforward (Next..Next..).
Download VirtualBox 
```
 https://www.virtualbox.org/wiki/Downloads
 ```
 
## Snd STEP :downloading  Ubuntu OS
2-After,we already have VirtualBox  installed on my machine. In order to create
a new virtual machine,click on the new icon to download our Ubuntu OS.

2- After clicking on the new icon , we need to choose the name(e.g. ROS) ,type (e.g.Linux),and version (e.g.,64-bit).

3-NEXT,Choose the RAM ,It is recmmonded to share a little about half of the RAM with the client OS.

4-NEXT,as it is without any changes in VDI AND We'll go with virtualbox disk image for the default file type. A dynamically allocated disk file.

5-NEXT,This is where we can enter the size of your virtual hard disk
Before we start our OS, we must first choose the ISO file that we need to download for
the mount image. 

To do that, click on the settings icon. Select storage, click on the CD icon under controller then choose the file that u sholud download it from the next link .
```
downloading  Ubuntu OS link :https://ubuntu.com/download/desktop
```

6- Now, we can click on start.Then, choosing our harddisk .

7-click on Install Ubuntu, click on Continue. 

8-choose erase disk and install Ubuntu.

9-Choose your time zone. 

10-Click on Continue. Choose your keyboard layout.

11-Fill in your username, password, your computer name and then continue. 

12-Once the installation process is complete we can restart it.

13- now our new Ubuntu OS is ready to use.

![Third step- installation  of ROS](https://user-images.githubusercontent.com/67114907/91164364-962b5200-e6d7-11ea-8ecf-1a98314e316c.jpeg)

2nd Step' done successfully )

## 3rd step :installation process of ROS

1- after virtual box installation, we  have to install the latest open the
packages to keep your system up to date.

To achieve this,Open a new terminal using the key combinations control alt and  D then type the command sudo AAPT update.

2- After that let's open a browser and head to Rascon adek installation wiki
to make our machine accept packages from Rause packages index.

We would have to set up our sources not list simply copy paste the command from Ross Wiki.
Similarly set up your keys by copying the next command
update.
Your Debian package is indexed by running sudo APD update again.

3- We are given with three options for us installation.
we will choose the desktop option .
Then we need to follow the steps On 
```
ROS website : http://wiki.ros.org/kinetic/Installation/Ubuntu
```
Congratulations,, We have successfully installed ROS.
THANK U )
