# github_repo_visualizer

make structure.md, workflow.mermaid, readme summary, key insights & original problem & solution & results

goal is to make a pretty nice visualisation/information breakdown of a github repo which i can later add to the newsletter for trending repos

1. clone repo - 
2. make source tree of repo 
3. iterate over files from source tree and make one line desc
4. in the case a specific folder does not contain relevant files like node modules files, folder with examples then skip it and add a short max 5 words description. 
5. in the case its a file which is not relevant like readme or gitignore skip it
6. return final structure

dont overcomplicate things. see it as an 


1. in the first step get the whole structure and remove all files and folders where the AI thinks its not relevant. only the relevant files and folders are left
2. now get the content from this files with an max depth of X tokens and add all to one file
3. take the original source tree and add take the first chunk of whole content file and add short descripions to each file
4. repeat as long there are no chunks left 