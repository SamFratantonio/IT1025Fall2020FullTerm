# Executive Summary
The goal of this lab is to learn about different networking protocols and how they apply to programming and cyber security. 
# Internet Architecture

## Internet Protocol
* What is an IP address and what is the difference between IPv4 and IPv6? 
  * An IP address is a unique identifier assigned to each device on a computer network. IPV4 uses 32 bit addresses and IPV6 uses 128. This means IPV6 has much more possible addresses and it is highly unlikely we'll run out, as we have with IPV4 before.
* Find the IP address of your computer by typing ipconfig at the command prompt (refer back to the "Operating Systems" module for details.) 
  Take a screenshot of the command without including the IP address to show your success, name the file ipconfig and upload to the lab folder on GitHub. 
* What is ICANN and how do they contribute to the global Internet? They help keep a standard in the DNS and make sure everything is done smoothly, they also help with other identification protocols in the architecture of the internet.

## TCP/IP

#### Review the first article and answer these questions:
* What is the responsibility of TCP/IP? 
  * To send packets over a network from one device to another.
* Explain how the client-server model applies to TCP/IP. 
  * The way TCP works is one device initiates a connection and the target recieves it. In this way the device that initiates would be the client and the one that listens for/accepts TCP sockets would be the server.

#### Review the second article and answer these questions:
Review the section of the article aligning the post office with protocol stacks.  
* Why are layers important to changing technology? 
  * Because when it's in layers and everything is organized from top to bottom, meaning everything is fundamentally built on top of everything below it, it makes it easier to change things without changing literally everything. 
* What types of applications run on the "application" layer?
   * The ones that the user actually interacts with. For example HTTP is an application layer protocol whereas TCP is a transport layer protocol. So they are not on the same level so to speak, HTTP uses TCP. Your browser that you're using to read this is on the application layer of things. 

# Internet Security
#### Watch the video and answer these questions:
* What is HTTP and how does it support the client-server model? 
   * HTTP means hypertext transfer protocol. It is the application layer protocol used by websites/browsers, the browser is the client and the web server is the server. 
* Explain the protocols that secure HTTP uses to protect data.  
   * HTTPS encrypts the data and uses SSL which makes it harder to intercept. 

#### Review the following article: Securing Your Web Browser 
* Why should you secure your browser? 
   * To protect your privacy because a large amount of information can be found on your browser alone. Especially since browsers are so customizable and serve such a general purpose that security vulnerabilities are going to happen, especially if you use 3rd party software like browser extensions. 
* Explain one of the risks described in the article. 
  * The fact that websites leave cookies on your browser, cookies are files left by websites to save certain data, said cookies could be picked up by any other website if the proper measures are not taken, which could be a problem if that cookie is a username and password, as they often are.
 
# Conclusion
Include your conclusion here...
This lab was helpful in explaining how different networking protocols work as well as how to use certain ones to make things more secure.
