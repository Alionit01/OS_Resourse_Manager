
🛠 OS Resource Manager
Hey there! 👋
This is a simple project I made to understand how operating systems manage resources like CPU, memory, and I/O. It’s not too fancy — just a fun way to simulate and play around with OS concepts like scheduling, resource allocation, and process management.

📌 What This Does
Simulates how an OS handles different resources (CPU, memory, etc.)

You can try out basic scheduling logic like round-robin

Tracks which "process" is using what and shows logs

Good for learning or messing around with how these systems work under the hood

🔧 How to Set It Up
1. Clone the repo
bash
Copy
Edit
git clone https://github.com/Alionit01/OS_Resourse_Manager.git
cd OS_Resourse_Manager
2. (Optional but recommended) Create a virtual environment
bash
Copy
Edit
python -m venv venv
# activate it:
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
3. Install required Python libraries
bash
Copy
Edit
pip install -r requirements.txt
If there's no requirements.txt, just do:

bash
Copy
Edit
pip install psutil tabulate
▶️ How to Run It
Just run the main file like this:

bash
Copy
Edit
python main.py
There might be config options you can change (like CPU count, memory size, etc.). Those are usually in a config file (like configs/default.json) if you want to experiment with different setups.

🧠 Why I Made This
It was a course project and honestly, I was trying to get a better grasp on how operating systems actually handle multiple things at once. Reading theory was cool, but building this helped a lot more. I kept it simple enough to tinker with feel free to fork it and mess around.

💡 Ideas to Add (Maybe Later)
Better UI (right now it’s mostly command line)

Add deadlock detection

Visualize resource usage with graphs

Try new scheduling techniques

🙌 Contributing
If you’re learning too and want to add stuff, go for it! Open a pull request or suggest changes. I’m open to ideas.

📄 License
MIT — feel free to use or change anything.

