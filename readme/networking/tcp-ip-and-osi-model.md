# TCP/IP and OSI model

**Overview of Networking Models: TCP/IP and OSI**

In the early days of computing, devices from different manufacturers were unable to communicate because they utilized proprietary, incompatible networking designs. The development of standardized networking models solved this by creating a common language for devices to connect and share data.

**The TCP/IP Model**

* The **TCP/IP model** (or stack) is the industry standard used for modern networking.
* It acts as a collection of rules and guidelines that govern how systems are designed to communicate.
* To simplify the complexity of network functions, the model is divided into layers, with each layer handling specific protocols (e.g., Physical, Data Link, Network, Transport, and Application).

**The OSI Model**

* The **OSI model** (_Open Systems Interconnect_) consists of seven layers. While it was once intended to be the primary standard, it was ultimately surpassed by TCP/IP in practical adoption.
* Despite this, the OSI model remains the universal reference point used by engineers for daily communication and troubleshooting.
* Engineers frequently refer to the specific layers (e.g., "Layer 7" for Application, "Layer 3" for Network) when discussing or diagnosing networking issues.

**Key Differences and Terminology**

* While the models share similar concepts for the lower levels (Physical, Data Link, Network, and Transport), the OSI model separates the Application layer into three distinct layers: Application, Presentation, and Session.
* In the real world, network professionals typically map these extra OSI layers into the broader "Application" layer of the TCP/IP stack but continue to use OSI terminology for technical discussions.

**Memorization Tips**

* To remember the seven layers of the OSI model, use mnemonic devices:
  * From top to bottom: "All People Seem To Need Data Processing."
  * From bottom to top: "Please Do Not Throw Sausage Pizza Away."
  *

While the real world primarily utilizes the **TCP/IP model**, the **OSI model** is often used as a reference framework to visualize the process of data moving between devices.



**The Layers of Data Transmission**

* **Application Layer (Layer 7):** This is where user-facing applications (like web browsers) initiate communication using protocols such as **HTTPS**. The computer takes the user's request and prepares it to travel down through the protocol stack.
* **Transport Layer (Layer 4):** This layer dictates how data is moved. It primarily uses **TCP** (reliable, connection-oriented) or **UDP** (fast, less reliable). For web traffic, **Port 443** is typically used for secure **HTTPS** connections. A data unit at this layer is known as a **segment**.
* **Network Layer (Layer 3):** This layer handles **IP addresses** and routing. Routers use this information to determine the path the data needs to take to reach its destination. A data unit at this layer is called a **packet**.
* **Data Link Layer (Layer 2):** This layer deals with **MAC addresses** and physical hardware like switches. It ensures the data gets to the next physical stop on the network path. A data unit at this layer is called a **frame**.

**Key Concepts**

* **Encapsulation:** As data moves from the Application layer down to the Physical layer, each layer adds its own header information (like an envelope inside an envelope) to ensure the data is correctly handled and routed.
* **De-encapsulation:** When a device receives a frame, it performs the reverse process. It strips away the headers layer by layer to interpret the information contained in the packet, segment, and eventually the application data.
* **The Physical Path:** Data travels as electrical or optical signals across hardware components (cables, switches, and routers) until it reaches the final destination server, where the process is reversed so the original application request can be read.

<br>
