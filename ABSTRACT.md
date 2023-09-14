As the authors of **Strawberry dataset for object detection** discuss, addressing labor shortages in the context of open-field strawberry production is a pressing concern. Introducing robotic solutions holds promise for round-the-clock field operations with minimal human oversight, offering long-term security to strawberry farmers. The paper, which this dataset was collected for, focuses on the critical aspect of detecting garden strawberries to guide a strawberry harvesting robot efficiently. A real-time implementation of a strawberry and peduncle detection system, designed to operate on an edge device, is presented. The paper discusses the prerequisites for the vision system, hardware and model selection, training procedures, and results achieved.

Strawberries are produced in Finland on approximately 4,000 hectares, yielding an annual average of 15 million kg of strawberries. To manage this extensive cultivation, an estimated 15,000 to 20,000 foreign strawberry pickers are employed in Finland annually (Migri 2021). Recruiting these foreign workers is a laborious and complex process, involving bureaucratic hurdles, regulatory compliance, and significant expenses for accommodation and occupational health care. Moreover, communication challenges, cultural differences, and varying work paces pose additional difficulties.

The authors suggest that strawberry farmers often struggle to predict the quality of work provided by seasonal laborers. Introducing a harvesting robot could enhance predictability and efficiency, potentially allowing for continuous, minimally supervised fieldwork. Such automation would mitigate personnel-related risks and ensure long-term operational stability for strawberry farmers.

Developing a robotic solution capable of replacing human labor in horticultural production necessitates a precise and rapid perception system. This is crucial for tasks such as harvesting blueberries, peppers, and tomatoes in the agricultural sector.

The decision to grasp the strawberry's peduncle imposed specific requirements on the vision system:

1. Continuous Tracking: The method must continuously select, locate, and track a single strawberry as the camera approaches it.

2. Peduncle Identification: Once the camera is within 10-50 centimeters of the strawberry, the vision system must consistently identify the peduncle connected to the strawberry in every frame, even when the camera is in motion.

3. Distance Estimation: The system should calculate the estimated distance from the camera to the peduncle once it is detected.

4. Continuous Detection: While the cutter approaches to grasp the peduncle, the vision system must maintain detection of the peduncle in each frame.

5. Optimal Approach Angle: The system should determine a suitable approach angle to the berry. The camera, attached to the cutter, can be rotated around the strawberry to find this ideal angle.

The authors selected the YOLOv5 object detection model, considering its real-time performance, low memory footprint, quick training, and compatibility with NVIDIA TensorRT for real-time inference. This choice was driven by both computational constraints and project time limitations, enabling efficient development and deployment on the target device.