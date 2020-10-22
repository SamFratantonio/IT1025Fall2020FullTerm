# Executive Summary
The goal of this lab is to understand the basics of cryptography and the different types of encryption algorithms and how they work, as well as what they are/aren't good for and how they can be applied to cybersecurity.

# Cybersecurity and Encryption

* Imagine you are part of the Amazon.com online chat. Explain how each component of the security triad would impact your job
    * You'd have to make sure all of the accounts are password protected and the architecture behind it has no weaknesses, you'd also have to limit access to the servers that house everything, as all of the data is on there. Not only would you have to make sure everything is secure, you'd also have to do routine checks to make sure there have been no breaches. It would be a good idea to require the users to use a complex password.
* Identify three daily tasks that require authentication. Explain how each one could be converted to multi-factor authentication
   * Unlocking my phone: It could require a password as well as a fingerprint
   
   * Clocking in at work: Also, require a password and the biometrics, instead of one or the other
   
   * Using credit card: Should always require a PIN and your name.
   
* Explain ACL and RBAC. What are the advantages and disadvantages of each?
   * RBAC is where you have a list of roles and each role has certain permissions, ACL is where each user is specific and has their own set of permissions.
   RBAC is easier for larger systems but ACL is more specific and in some ways more secure.
* Explain the interaction of ciphertext, a public key and a private key
   * A public key and a private key are linked in such a way that anything encrypted with the public key and only be decrypted with the private key and vice versa. 
   This is useful so you can share your public key and keep your private key secret. 
* Explain why we need public key cryptography.
   * So people don't need to create a new algorithm every time they want to encrypt something and have it be secure.

## Cryptography
* Type a message in the "Caesar Cipher Exploration box and turn the wheel to encrypt your message.
Then explain the encryption here: 
   * Turning the wheel changes the letter each "original" letter corresponds  with, so turning it once would make A = B, B = C, etc.

* Type a message in the "Frequency Fingerprint Exploration" box and a) Explain the result.
b) Would it be different for different languages? 
   * It shows a graph of how many times each letter was typed, it would most likely be different for other languages, especially those that are not based on latin.

* What is a "Polyalphabetic cipher?"
Type a message in the "Polyalphabetic Exploration" box as well as a shift word.
Explain the result.
   * It converts the letters to numbers based on their position in the alphabet, then it adds each number from the corresponding number in the shift word, to decrypt it you do the opposite and subtract it to get the original. 

## Brute Force
* What is Brute-Force and how does it relate to Kerckhoffs's principle?
    * A brute force attack is when you try every possible combination for a password until one of them works, in cryptography this would mean trying every possible key until one of them decrypts it successfully. Brute force attacks are not practical and take a long time, if the key is long enough it will literally take centuries to try all of them. This is where Kerckhoffs's principle comes in, the principle states that a system should be secure even if every aspect of how it works is public knowledge. This implies that the algorithm should be mathematically sound and impossible reverse engineer. If a system had a constant key then it could be reverse engineered to decrypt anything, this is why asymmetric encryption is better. That way you can know exactly how it works and still not be able to do anything about it. 

# Conclusion
Summarize how this lab was useful to you and what you learnt that really interested you!
I found the part on cryptography to be quite interesting and useful because understanding these concepts is essential in today's world if you're going to be a programmer as the applications you'll be making need to be secure, especially if it involves two users communicating over it. 
