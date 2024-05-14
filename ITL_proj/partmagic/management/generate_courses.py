import random
import string
from django.utils import timezone
from partmagic.models import Pubs

def random_string(length):
    """Generate a random string of a specified length"""
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

def add_pubs():
    courses = [
  "A Scalable Framework for Parallel Deep Learning on Heterogeneous Clusters",
  "Leveraging Natural Language Processing for Improved Bug Detection in Code",
  "Towards Explainable AI: Interpretable Machine Learning for Medical Diagnosis",
  "Enhancing Network Security with Blockchain-based Trust Management Systems",
  "Optimizing Performance of Real-Time Object Detection on Edge Devices",
  "A Comparative Study of Deep Learning Architectures for Image Segmentation",
  "Federated Learning for Privacy-Preserving Mobile Healthcare Applications",
  "Investigating the Ethical Implications of Algorithmic Bias in Social Media",
  "Human-in-the-Loop Reinforcement Learning for Robot Manipulation Tasks",
  "A Novel Approach to Anomaly Detection in High-Dimensional Network Traffic Data",
  "The Impact of Cloud Computing on Scalability and Cost-Efficiency in Scientific Research",
  "Towards Explainable Recommendation Systems: Understanding User Preferences",
  "Privacy-Enhancing Techniques for Secure Data Aggregation in the Internet of Things",
  "Developing Conversational AI Agents for Customer Service Applications",
  "Exploring the Potential of Quantum Computing for Drug Discovery and Materials Science",
  "A Survey of Graph Neural Networks for Complex Network Analysis",
  "Real-Time Visual Question Answering with Multimodal Embeddings",
  "Generating Realistic and Diverse Synthetic Data for Machine Learning Applications",
  "Decentralized Applications (DApps) on Blockchain: Opportunities and Challenges",
  "The Role of AI in Personalized Education: Adaptive Learning Systems",
  "Investigating Explainable Reinforcement Learning for Autonomous Vehicles",
  "A Framework for Continuous Integration and Delivery (CI/CD) in Machine Learning Projects",
  "Bridging the Gap Between Theory and Practice: Deep Learning for Natural Language Processing",
  "Evaluating the Fairness of Machine Learning Models in High-Stakes Applications",
  "The Emerging Landscape of Explainable AI for Cybersecurity Applications",
  "Leveraging Big Data Analytics for Improved Supply Chain Optimization",
  "Enhancing Software Reliability Through Automated Testing Techniques",
  "The Future of Human-Computer Interaction: Brain-Computer Interfaces (BCIs)",
  "Developing Secure and Efficient Routing Protocols for Large-Scale Networks",
  "A Comprehensive Survey of Deep Reinforcement Learning Algorithms"
]
    names = [
  "Evelyn Jones",
  "Noah Miller",
  "Sophia Garcia",
  "William Brown",
  "Olivia Davis",
  "Liam Hernandez",
  "Ava Thomas",
  "Matthew Johnson",
  "Isabella Jackson",
  "Ethan Moore",
  "Mia Robinson",
  "Alexander Clark",
  "Emily Lewis",
  "Benjamin Walker",
  "Charlotte Allen",
  "Daniel Young",
  "Harper Wilson",
  "Joseph Martin",
  "Amelia King",
  "Michael Wright",
  "Evelyn Lopez",
  "Noah Lee",
  "Sophia Hernandez",
  "William Gonzalez",
  "Olivia Harris",
  "Liam Scott",
  "Ava Miller",
  "Matthew Garcia",
  "Isabella Walker",
  "Ethan Anderson"
]
    computer_science_topics = [
  "Algorithmic Complexity Analysis",
  "Web Application Security",
  "Introduction to Database Systems",
  "Computer Vision Techniques",
  "Natural Language Processing Applications",
  "Machine Learning for Anomaly Detection",
  "Parallel and Distributed Computing Systems",
  "Software Design Principles and Patterns",
  "Human-Computer Interaction Design",
  "Cybersecurity Threats and Countermeasures",
  "Programming Languages for System Development",
  "Fundamentals of Compiler Design",
  "Operating System Concepts and Design",
  "Computer Networks and Communication Protocols",
  "Introduction to Bioinformatics",
  "Artificial Intelligence Search Algorithms",
  "Robotics and Motion Planning",
  "Software Engineering Methodologies",
  "Big Data Analytics and Processing",
  "Cloud Computing Architectures",
  "Ethical Considerations in Artificial Intelligence",
  "Formal Languages and Automata Theory",
  "Distributed File Systems and Storage",
  "Type Theory and Programming Languages",
  "Computer Graphics Algorithms and Techniques",
  "Software Testing and Quality Assurance Practices",
  "High-Performance Computing Architectures",
  "Natural Language Processing for Chatbots",
  "Explainable Artificial Intelligence (XAI) Techniques",
  "Quantum Computing Algorithms and Applications"
]



    for _ in range(30):
        auth = names[_]
        pub_title = courses[_]
        topic = computer_science_topics[_]
        pub_date = timezone.now() # You can adjust this to generate random dates if needed

        pub = Pubs(auth=auth, pub_title=pub_title, topic=topic, pub_date=pub_date)
        pub.save()

if __name__ == "__main__":
    add_pubs()
