# 361_Microservice
Code for CS 361 Microservice for random movie selection microservice.

COMMUNICATION CONTRACT

I. Requesting Data

A user of the microservice may REQUEST data from the microservice by changing the first line of the specified text file to "run". The user must also write to the same text file in lines below the "run" line with any number of arrays of feature options, with one array per line, and with each item in each array separated by the "^" symbol. 

For example, a user could request random movie attributes by changing the designated text file to:
```sample_request
run
action^drama^dark comedy
Cher^Johnny Depp^Kira Knightly
great^good^ok^fair^bad
```

II. Receiving Data

A user of the microservice may RECEIVE data from the microservice by reading from the same text file that was used to request data. The data received will be a selection of one item from each line below the "run" line of the request; thus, each choice gets its own line in the return text file.

For example, a user might receive the following after giving the sample request from above:
```sample_receipt
dark comedy
Cher
good
```

III. UML Sequence Diagram

![Sequence Diagram_ ATM Transferal](https://user-images.githubusercontent.com/61097283/199132824-a0f2b063-b988-4ad6-a2e4-6990691bce0c.jpg)
