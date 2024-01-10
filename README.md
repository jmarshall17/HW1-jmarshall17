# Homework 1 

## Problem Two: github submission

1.   Sign up for github. ~~and report your username to gradescope.  We will authorize you to receive the materials on github-classroom.~~ Follow the link https://classroom.github.com/a/TzScN0eH to get access to the homework-template-repository.
2.    You will get a copy of the homework template (in github-classroom) that you control. 
3.    Clone your repository to your laptop.  This is a command like `git clone 'https://github.com/DATA120/HW1-WIN24-bobwang43'` You now control your copy of the classroom repository on github-classroom and another copy on your laptop.
4.    Add a text file called "scavenger.txt" that contains your answers to the scavenger hunt to the repository directory.  Add this file to the repostitory and commit your changes.  This is a step something like `git add scavenger.txt` and `git commit -m "Added scavenger hunt answers, read 'em and weep."`  
6.    Add a picture of a cat ("cat.jpg" or "cat.webp" might be good choices for file names here) to your repostiory and commit your changes on your laptop.
7.    Add an executable python script that produces the output "Hello, world!" when executed in the autograder environment.  (Not to be too creative, but "helloworld.py"?)  (Ugh-oh, what if it works on your laptop but not in the autograder environment?  Fix it.)
8.    Update your github-classroom repository (that you control) with your changes.   This is a command like  `git push origin main`

9.  When you are finished, use "submit from github" button to share your gihtub-classroom repostiroy with gradescope.

Don't stress out about following the rules, for this assignment we won't be scrutinizing your git history, just find out how to make it all happen.  Here we are using github as a means to distribute assignment materials and collect completed assignments.  What are we looking for?  Three files, one with answers, one with pointy ears, and one which invokes the python interpreter to do a very stereotypical thing in a programming class.  

## Scavenger hunt items

### Problem Zero: CS Accounts
Sign up for a CS account at https://account-request.cs.uchicago.edu/account/requests. If you need
help using SSH, please visit https://howto.cs.uchicago.edu/remote_access.

### Problem One: Terminal Scavenger Hunt
On your laptop, collect the following scraps of information. Be sure to document the command-
s/steps that you’ve used for each problem.
1. What is your unix username?
2. What is the full path of your home directory?
3. What is the full path of your Downloads directory?
4. Download the DATA120 syllabus to your computer. Now, check how many files are in your
Downloads directory using the command line. (Hint: adding "| wc -l" to the end of a
command counts the number of lines in its output and otherwise ignores the contents)
5. How much hard drive space is used by all the files in Downloads? (Hint: du )
6. Save the DATA120 syllabus in a different, memorable location (consider creating a new di-
rectory for all DATA120 materials). What does your prompt look like? Will it change if you
change directories?
7. What do you see if you run echo $PATH?
8. Does your $PATH contain any directories in your user directory? Reminder: user directory
and home directory are synonymous.
9. Find the most recently modified or created file in your Downloads using the command line,
and find its full path.
10. The command "which python" returns the path of the system’s default python. Where is
that?
11. "ls -FG /" produces a directory listing of the root of the filesystem. Does anything look
familiar?
12. Use SSH to log in to the CS linux cluster linux.cs.uchicago.edu.
13. Find the md5 hash of a local file not larger than 1Mb and that doesn’t have anything personal
or sensitive in it. You should be able to use the syllabus as this file.
14. Use SCP to copy the file to the CS server. Confirm that the local file on the CS server has
the same md5 hash.
15. Use ls -l to confirm that you have created a file on your account on the server. You can
delete it if you like.

Everything that follows is generic gihtub instructional content you may find helpful.

# :wave: The Basics of GitHub 

## 🤓 Course overview and learning outcomes 

The goal of this course is to give you a brief introduction to GitHub. We’ll also provide you with materials for further learning and a few ideas to get you started on our platform. 🚀

## :octocat: Git and GitHub

Git is a **distributed Version Control System (VCS)**, which means it is a useful tool for easily tracking changes to your code, collaborating, and sharing. With Git you can track the changes you make to your project so you always have a record of what you’ve worked on and can easily revert back to an older version if need be. It also makes working with others easier—groups of people can work together on the same project and merge their changes into one final source!

GitHub is a way to use the same power of Git all online with an easy-to-use interface. It’s used across the software world and beyond to collaborate and maintain the history of projects.

GitHub is home to some of the most advanced technologies in the world. Whether you're visualizing data or building a new game, there's a whole community and set of tools on GitHub that can get you to the next step. This course starts with the basics of GitHub, but we'll dig into the rest later.

## :octocat: Understanding the GitHub flow 

The GitHub flow is a lightweight workflow that allows you to experiment and collaborate on your projects easily, without the risk of losing your previous work.

### Repositories

A repository is where your project work happens--think of it as your project folder. It contains all of your project’s files and revision history.  You can work within a repository alone or invite others to collaborate with you on those files.

### Cloning 

When a repository is created with GitHub, it’s stored remotely in the ☁️. You can clone a repository to create a local copy on your computer and then use Git to sync the two. This makes it easier to fix issues, add or remove files, and push larger commits. You can also use the editing tool of your choice as opposed to the GitHub UI. Cloning a repository also pulls down all the repository data that GitHub has at that point in time, including all versions of every file and folder for the project! This can be helpful if you experiment with your project and then realize you liked a previous version more. 
To learn more about cloning, read ["Cloning a Repository"](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository). 

### Committing and pushing
**Committing** and **pushing** are how you can add the changes you made on your local machine to the remote repository in GitHub. That way your instructor and/or teammates can see your latest work when you’re ready to share it. You can make a commit when you have made changes to your project that you want to “checkpoint.” You can also add a helpful **commit message** to remind yourself or your teammates what work you did (e.g. “Added a README with information about our project”).

Once you have a commit or multiple commits that you’re ready to add to your repository, you can use the push command to add those changes to your remote repository. Committing and pushing may feel new at first, but we promise you’ll get used to it 🙂

## 💻 GitHub terms to know 

### Repositories 
We mentioned repositories already, they are where your project work happens, but let’s talk a bit more about the details of them! As you work more on GitHub you will have many repositories which may feel confusing at first. Fortunately, your ["GitHub dashboard"](https://docs.github.com/en/github/setting-up-and-managing-your-github-user-account/about-your-personal-dashboard) helps to easily navigate to your repositories and see useful information about them. Make sure you’re logged in to see it!

Repositories also contain **README**s. You can add a README file to your repository to tell other people why your project is useful, what they can do with your project, and how they can use it. We are using this README to communicate how to learn Git and GitHub with you. 😄 
To learn more about repositories read ["Creating, Cloning, and Archiving Repositories](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/about-repositories) and ["About README's"](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/about-readmes). 

### Branches
You can use branches on GitHub to isolate work that you do not want merged into your final project just yet. Branches allow you to develop features, fix bugs, or safely experiment with new ideas in a contained area of your repository. Typically, you might create a new branch from the default branch of your repository—main. This makes a new working copy of your repository for you to experiment with. Once your new changes have been reviewed by a teammate, or you are satisfied with them, you can merge your changes into the default branch of your repository.
To learn more about branching, read ["About Branches"](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/about-branches).

### Forks
A fork is another way to copy a repository, but is usually used when you want to contribute to someone else’s project. Forking a repository allows you to freely experiment with changes without affecting the original project and is very popular when contributing to open source software projects!
To learn more about forking, read ["Fork a repo"](https://docs.github.com/en/github/getting-started-with-github/fork-a-repo)

### Pull requests
When working with branches, you can use a pull request to tell others about the changes you want to make and ask for their feedback. Once a pull request is opened, you can discuss and review the potential changes with collaborators and add more changes if need be. You can add specific people as reviewers of your pull request which shows you want their feedback on your changes! Once a pull request is ready-to-go, it can be merged into your main branch.
To learn more about pull requests, read ["About Pull Requests"](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/about-pull-requests). 


### Issues
Issues are a way to track enhancements, tasks, or bugs for your work on GitHub. Issues are a great way to keep track of all the tasks you want to work on for your project and let others know what you plan to work on. You can also use issues to tell a favorite open source project about a bug you found or a feature you think would be great to add!

For larger projects, you can keep track of many issues on a project board. GitHub Projects help you organize and prioritize your work and you can read more about them [in this "About Project boards document](https://docs.github.com/en/github/managing-your-work-on-github/about-project-boards). You likely won’t need a project board for your assignments, but once you move on to even bigger projects, they’re a great way to organize your team’s work!
You can also link together pull requests and issues to show that a fix is in progress and to automatically close the issue when someone merges the pull request.
To learn more about issues and linking them to your pull requests, read ["About Issues"](https://docs.github.com/en/github/managing-your-work-on-github/about-issues). 

### Your user profile

Your profile page tells people the story of your work through the repositories you're interested in, the contributions you've made, and the conversations you've had. You can also give the world a unique view into who you are with your profile README. You can use your profile to let future employers know all about you! 
To learn more about your user profile and adding and updating your profile README, read ["Managing Your Profile README"](https://docs.github.com/en/github/setting-up-and-managing-your-github-profile/managing-your-profile-readme). 

### Using markdown on GitHub 

You might have noticed already, but you can add some fun styling to your issues, pull requests, and files. ["Markdown"](https://guides.github.com/features/mastering-markdown/) is an easy way to style your issues, pull requests, and files with some simple syntax. This can be helpful to organize your information and make it easier for others to read. You can also drop in gifs and images to help convey your point!
To learn more about using GitHub’s flavor of markdown, read ["Basic Writing and Formatting Syntax"](https://docs.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax). 

## 📚  Resources 
* [A short video explaining what GitHub is](https://www.youtube.com/watch?v=w3jLJU7DT5E&feature=youtu.be) 
* [Git and GitHub learning resources](https://docs.github.com/en/github/getting-started-with-github/git-and-github-learning-resources) 
* [Understanding the GitHub flow](https://guides.github.com/introduction/flow/)
* [How to use GitHub branches](https://www.youtube.com/watch?v=H5GJfcp3p4Q&feature=youtu.be)
* [Interactive Git training materials](https://githubtraining.github.io/training-manual/#/01_getting_ready_for_class)
* [GitHub's Learning Lab](https://lab.github.com/)
* [Education community forum](https://education.github.community/)
* [GitHub community forum](https://github.community/)



