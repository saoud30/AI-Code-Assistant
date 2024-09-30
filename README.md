# 🖥️ Versatile Code Assistant

Versatile Code Assistant is an AI-powered tool that helps you generate code and answer programming-related questions. It supports multiple programming languages and allows users to switch between **Code Generation** and **Conversation** modes.

This project leverages the **Groq API** for generating code based on user inputs. The application is built using **Streamlit**, allowing it to be run as a web application.

## 🌟 Features

- Generate code in different programming languages (Python, C, C++).
- Choose from various versions of languages like Python, GCC, etc.
- Engage in conversation mode to ask programming-related questions.
- Clean and responsive user interface with both text input and chat-based interactions.
- Streamlit-powered web app with Groq API integration.

---

## 🛠️ Technologies Used

- **Python**: Core language for the app.
- **Streamlit**: Web framework for building the user interface.
- **Groq API**: Used to handle AI-based code generation and conversation.
- **dotenv**: For managing environment variables securely.

---

## 🚀 How to Run the Project

### Prerequisites

- Python 3.7+
- [Groq API Key](https://groq.com/) (You'll need to sign up and get your API key)
- Git

### Step-by-Step Instructions

1. **Clone the Repository**

   Open your terminal and clone the repository:

   ```bash
   git clone https://github.com/your-username/AI-Code-Assistant.git

2. Navigate to the project directory: 
    ```bash
    cd app.py
    ```

3. Install requirements: 
    ```bash
    pip install -r requirements.txt
    ```    

4. Run the app: 
    ```bash
    streamlit run app.py
    ```

This command will launch the app locally in your default web browser. The app will be accessible at http://localhost:8501.

## 📖 Usage

### 1. Code Generation Mode
- **Step 1**: Choose Code Generation mode from the mode selector.
- **Step 2**: Enter a specific prompt describing the code you need.
- **Step 3**: Select the desired programming language (e.g., Python, C, C++).
- **Step 4**: Choose the language version.
- **Step 5**: Click **Generate Response** and wait for the code to be generated.

### 2. Conversation Mode
- **Step 1**: Select Conversation mode from the mode selector.
- **Step 2**: Enter a question or prompt about programming.
- **Step 3**: Click **Generate Response** to get answers related to your question.
- **Step 4**: Alternatively, you can use the chat input at the bottom for a more conversational experience.

## 💻 Example Prompts

Here are some examples of prompts you can use:

### Code Generation Mode:
- **Python Prompt**: "Generate Python code to read a CSV file and calculate the sum of a column."
- **C++ Prompt**: "Write C++ code that implements a binary search algorithm."

### Conversation Mode:
- "What is the difference between a list and a tuple in Python?"
- "How does memory management work in C++?"

## 🛡️ Environment Variables

The application uses the following environment variables, managed securely through the `.env` file:

- **GROQ_API_KEY**: Your Groq API key for accessing the code generation and conversation services.

Make sure to never expose your API key in the source code or public repositories. Use the `.env` file and ensure it's listed in `.gitignore`.

## 🎯 Future Enhancements

- Support for more programming languages, such as Java, JavaScript, Ruby, Go, and more.
- Add user authentication (e.g., using OAuth) to allow users to save their preferences, history, and favorite code snippets.
- Integrate code formatting and linting features to ensure that generated code adheres to style guides and best practices.
- Provide a sandbox environment to run the generated code directly within the app, allowing users to see the output immediately.
- Create a library of commonly used code snippets that users can easily access and insert into their code generation prompts.
- Add a toggle for dark mode or customizable themes to improve user experience.
- Automatically generate documentation for the code snippets based on comments and code structure, making it easier for users to understand the generated code.
- Develop plugins for popular IDEs (like VSCode, PyCharm) that allow users to access the assistant's features directly within their coding environment.
- Allow users to create and save custom prompt templates for common tasks, making it easier to generate code.


## 🤝 Contributing

Contributions are welcome! If you'd like to contribute, feel free to open a pull request or issue.

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/feature-name`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/feature-name`).
5. Open a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🌟 Acknowledgements

This project is powered by the Groq API and Streamlit framework.

## 📧 Contact

For any queries, feel free to reach out to me:

- **GitHub**: Saoud30
- **Email**: mohdhashimansari30@gmail.com
