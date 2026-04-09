So the Idea is, I will be writing a blog on how when a coding IDE or agent calls the webpage tool. And the webpage can do prompt injection to make the Agent perform malicious action. This is a blog for awareness. To make people understand that, giving unknown links to the Agents can go south.

So first will be that webpage.

The webpage will have A documentation to build a langgraph, or something. Now somewhere in the html or script, we ll use some malicious prompt. That would be to discover api keys and passwords. For sake of safety of my machine, it will look at the folder im running the copoilot chat from, and one step outside it. To get access to files outside the workspace, itll run a python script on bash. This will be the injection.



Ill be deploying above website. Now for the blog, there will be a folder called Test here. Ill open copilot inside that folder. Now, ill ask copilot to build one agent, or something thats around the doc. and give it the url. itll goto that url. And primpt gets injected. IDE is made to run a script to discover apikeys env file inside this folder, and one folder outside this. Which is root. of this project. 


And that will be the blog.