# **Django Rest Api**

### **What is Rest Api**
REST is acronym for REpresentational State Transfer. It is architectural style for distributed hypermedia systems ans was first presented by Roy Fielding in 2000 in his famous dissertation.

Like any other architectural style, REST also does have it’s own principles which must be satisfied if an interface needs to be referred as RESTful. These principles are listed below:
1. **Client–server** – By separating the user interface concerns from the data storage concerns, we improve the portability of the user interface across multiple platforms and improve scalability by simplifying the server components.

1. **Stateless** – Each request from client to server must contain all of the information necessary to understand the request, and cannot take advantage of any stored context on the server. Session state is therefore kept entirely on the client.

1. **Cacheable** – Cache constraints require that the data within a response to a request be implicitly or explicitly labeled as cacheable or non-cacheable. If a response is cacheable, then a client cache is given the right to reuse that response data for later, equivalent requests.
1.  **Uniform interface** – By applying the software engineering principle of generality to the component interface, the overall system architecture is simplified and the visibility of interactions is improved. In order to obtain a uniform interface, multiple architectural constraints are needed to guide the behavior of components. REST is defined by four interface constraints: identification of resources; manipulation of resources through representations; self-descriptive messages; and, hypermedia as the engine of application state.
1. **Layered system** – The layered system style allows an architecture to be composed of hierarchical layers by constraining component behavior such that each component cannot “see” beyond the immediate layer with which they are interacting.
1. **Code on demand (optional)** – REST allows client functionality to be extended by downloading and executing code in the form of applets or scripts. This simplifies clients by reducing the number of features required to be pre-implemented.

In other words suppose you are the owner of a website like twitter. Now after building the site you decided to make a mobile application for it, or even
a desktop application. Now what you need to do is worry about how to connect with the database of the website with the mobile application. How to integrate the website database and the application database and make communications between their data. So what you did is design a separate database for the mobile application and after that designed another database for the desktop application and fetched data from there. Now this redundancy doesnt
feel right. What if we could transfer the data from our website and save it in our application.
We cannot just save website data on something like a thumb drive for example. What we can do is transform the data in a transferrable state like JSON.
If we can do that then we can move around this json data between our mobile application or desktop application without designing separate databases for
them. This representational(for example: JSON) state  transferring is called REST and web APIs built with this architecture is called REstful web service.
