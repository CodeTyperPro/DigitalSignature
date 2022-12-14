[Application of Discrete Models](https://canvas.elte.hu/courses/31709) > [Assignments](https://canvas.elte.hu/courses/31709/assignments) > Digital Signature

![](Aspose.Words.80b8cf06-f67c-4f55-b5e8-1439dd625bb7.001.png)

Name: **MARTINS Alfredo** | Neptune-code: **HEIOPO**

*ELTE, Budapest 18/12/2022*

**Digital Signatures**

**OVERVIEW**

*Figure 1. Image from Simplilearn, 2022*

![](Aspose.Words.80b8cf06-f67c-4f55-b5e8-1439dd625bb7.002.png)![Asymmetric\_Key](Aspose.Words.80b8cf06-f67c-4f55-b5e8-1439dd625bb7.003.png)***Cryptography*** is the science of *encrypting* and *decrypting* information to prevent unauthorized access. The decryption process should be known to both sender and the receiver. There are two types of encryption, **symmetric** and **asymmetric**. Symmetric key cryptography uses the same key for encryption and decryption, which is not our focus. The given topic, *Digital Signatures,* relies on asymmetric key cryptography because of the fact that *is uses a pair of two different keys*, **public key** (for encryption) and **private key** (for decryption).

Briefly, *Digital signatures* are mechanisms ***to determine authenticity*** of a document file. They are one of the main aspects of ensure security and ***integrity*** of data that was recorded into a ***BlockChain***. Similar to the handwritten signature in the physical world. Digital signatures are used to bind a person or entity to digital data. There are two main types of implementation of Digital signatures:

1) **RSA (Rivest–Shamir–Adleman Algorithm);**
1) **DSA (Digital Signature Algorithm).**

**So far so good, I have introduced the topic, now let’s jump right in to the requirements!**

**PROBLEM STATEMENT**

For a sake of simplicity, let denote:

***Jack*** = sender | ***Mary*** = receiver | ***m = original message*** | ***m’ = modified message*** | **JK (-) = Jack’s private key** | **JK (+) = Jack’s public key**

Jack and Mary are communication through an insecure channel (third-part can listen to this communication). If Jack wants to send “10$” to Mary, there is a big chance that this communication is catched by a “Hacker”, and he changes the message saying that Jack wants to send “1000$” to Mary. In case it happens, there might have a huge problem between Jack and Mary! With that being said, since there will be contradiction between them, i.e., Jack says he didn’t send 1000$ but, 10$ instead, and Mary will say Jack sent 1000$. So, they will have to verify the source and integrity of the message, so that Mary is not carried to justice. However, a question arrives. How to verify the source and integrity of the message?


**DETAILS OF THE SOLUTION**

**Main idea:** Jack wants to send a digitally signed document/message to Mary. He wants to prove that he is the owner of that message. In order to do that, Jack will use his private key to digitally sign the document and Mary will have the responsibility to verify that signature and check that It was Jack that encrypted It.** 

**m = “Hey, Mary! I sent you 10$”.**

**Simple Oversimplification of Digital Signature for message “m”:**

1) Jack signs m by encrypting with his private key JK (-), creating a digitally signed message, JK (-) (m). He is the only one who has this private key, It’s secret!
1) Suppose Mary receives the message m, with signature: m and JK (-) (m).
1) Mary verifies m signed by Jack by applying JK (+) to JK (-) (m), then checks JK (+) (JK (-) (m)) = m;
1) If the performed key unlocks the message, then, whoever signed “m” must have used JK (-).

On this way, Mary thus verifies that:

- Jack signed m;
- No one else signed m;
- Bob signed m and not m’;
- Data integrity is fulfilled.

**No repudiation:**

Mary can take m, and signature PK (-) to count and prove signed m.

Now that we know how to prove the ownership of the message, a new huge problem comes. What If Jack wants to send a bit document of gigabytes of size? 

Well, the message/document that Jack sends can have any length/size, either it is very long or too short, RSA algorithm would cause problems with computational efficiency (split message up, sign multiple bits and then it might be reordered), giving attacks opportunity to NINJAS. This idea would not work properly for some cases, therefore, It’s a good ideia to use a scheme that will work however long m is or however short m is.

The solution for this problem is the insertion of Hash Function H, in this example SHA-256 will be used to create message digest. As we can notice, on this way Jack can send m of any length and turn into a length of exactly 250 bits which would help a lot the encryption process.

Since 250 is quite short, a padding might also be added to the message digest.

Jack has no idea what the output of the Hash Function is going to be. It can be very small like in BlockChain, which would lead to a security risk. Then, to avoid this risk, a padding or any mechanism must be used, and after this we can encrypt using the private key. Same process must be done in Mary’s side.
**


**Last but not least, to add more security, a PSSR id added.**

**# Probabilistic signature scheme of RSA.**

Also, It’s recommended to register a public key in a **Public Key Certification Authority (CA)**.

**Certification Authority (CA):** *binds public key to particular entity, E*.

**BlockChain**: *collection of records linked with each other, strongly resistant to alteration and protected using cryptography.*

**Hashing:** *process of scrambling a piece of information or data beyond recognition. Hash functions are used to convert input into hash value (digest)*.

**HASH FUNCTION PROPERTIES**

- Many to 1;
- Produces fixed-size message digest (***fingerprint***);
- Given message digest x, computationally infeasible to find m such that x = H(m).

**PROPERTIES OF DIGITAL SIGNATURES**

![](Aspose.Words.80b8cf06-f67c-4f55-b5e8-1439dd625bb7.004.png)Confidentially | Unforgeable | Authenticity | Can't be modified once sent | Not reusable | Prevent repudiation | Ownership | Immutability. 


Figure 2 (Digital Signatures and Digital Certificates, 2019)
![](Aspose.Words.80b8cf06-f67c-4f55-b5e8-1439dd625bb7.005.png)**

**RSA**

**Step 1 - Key Generation**

1) Consider two large prime numbers, p and q;
1) Compute n = p\*q;
1) ϕn=p-1\*q-1, where ϕn is Euler’s Totient Function;
1) Choose a small number e, coprime to n and ϕn, i.e. , ( gcd(ϕn, e) = 1 and gcd(n,  e) = 1), where 1 < e < ϕn;
1) Select a number d so that e\*d mod ϕn = 1.

**Step 2 – Encryption and Decryption:**

If the plaintext is, encrypted cipher-text c is calculated as:

c =me mod n

Under similar assumptions, the plaintext can be calculated using the following expression:

m = cd mod n

*Please, check the example at the end of this report.*

**TEST CASES WHICH VALIDATE THE SOLUTION**



|**Sign text**|
| :-: |
|**#**|**Text**|**Private key**|**Response**|
|1||||
|2||||
|3||||
|4||||
|5||||


|**Verify signature**|
| :-: |
|**#**|**Text**|**Signature**|**Public key**|**Response**|
|1|||||
|2|||||
|3|||||
|4|||||
|5|||||

Please, check the sage-math script in the link: https://github.com/CodeTyperPro/DigitalSignature/blob/master/Digital\_Signature.ipynb



**EXAMPLES:**

**RSA – Key Generation:**

1) Two prime numbers, p=3 and q=5
1) n = p\*q = 3\*5 = 15  => n = 15
1) ϕn=p-1\*q-1=3-1\*5-1=8=> ϕn=8
1) Assume e such that gcd(ϕn, e) = 1 and gcd(n,  e) = 1), where 1 < e < ϕn

e = 3, because:

gcd3, 8= 1,gcd5, 8= 1,gcd(7, 8) = 1

1) Find d:

e\*d mod ϕn = 1

3\*d mod 8 = 1

Consider  d = 3,

3\*3 mod 8 = 1

9 mod 8 = 1

1 = 1

d = 3


private  key = {e, n} = {3, 15}

public key = {d, n} = {3, 15}

**Encryption:**

Consider plaintext m = “B” => m = H(“B”) = 8

c =me mod n

c =83 mod 15

c =512 mod 15

c =2

**Descryption**

m = cd mod n

m = 23 mod 15

m = 8 mod 15

m = 8

Therefore, the algorithm works.
**


**REFERENCES**

W. Trappe and L. C. Washington. Introduction to Cryptography with Coding Theory. Pearson Prentice Hall, Upper Saddle River, New Jersey, USA, 2nd edition, 2006.

T. H. Cormen, C. E. Leiserson, R. L. Rivest, and C. Stein. Introduction to Algorithms. The MIT Press, USA, 2nd edition, 2001.

A. J. Menezes, P. C. van Oorschot, and S. A. Vanstone. Handbook of Applied Cryptography. CRC Press, Boca Raton, FL, USA, 1996.

D. R. Stinson. Cryptography: Theory and Practice. Chapman & Hall/CRC, Boca Raton, USA, 3rd edition, 2006.

NGUYEN, M. V. Number Theory and the RSA Public Key Cryptosystem. Sage Math, 2022. Disponivel em: <https://doc.sagemath.org/html/en/thematic\_tutorials/numtheory\_rsa.html>. Acesso em: 14 dez. 2022.

WHAT is Cryptography And How Does It Protect Data? Simplilearn, 12 dez. 2022. Disponivel em: <https://www.simplilearn.com/tutorials/cryptography-tutorial/what-is-cryptography>. Acesso em: 21 2022 2022.

Along the references, there following videos are to be mentioned as well:

- <https://www.youtube.com/watch?v=JR4_RBb8A9Q>
- <https://youtu.be/stsWa9A3sOM>
- <https://www.youtube.com/watch?v=stsWa9A3sOM&list=PLTd6ceoshprcUyoyOQ_2dCvr5GPi5w_T7&index=7>
- <https://youtu.be/ANsg4wIQFn4>
- <https://www.youtube.com/watch?v=AQDCe585Lnc>
- <https://www.youtube.com/watch?v=yubzJw0uiE4&t=181s>
- <https://www.youtube.com/watch?v=s22eJ1eVLTU>
- <https://www.youtube.com/watch?v=-0slxSL9B6A>
- <https://www.youtube.com/watch?v=OBdEhSPoDaY>

