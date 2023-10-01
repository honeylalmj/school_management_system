# School Management System

This is a simple Python project for a school management system that allows you to maintain student exam data for different exam terms. You can add student information, enter marks for subjects, view student data, and calculate total marks for individual terms and for the entire year.

## Features

- Add student data including exam term, student name, and marks for English, Maths, and Science.
- View student data for a specific term.
- Calculate total marks for individual terms and for the entire year.
- Data storage and handling using JSON.
- Option to run the project as an executable (.exe) file on Windows.

## Getting Started

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-username/school-management-system.git
   cd school-management-system
   ```

2. Run the project:

   ```bash
   python school_management_system.py
   ```
### Running in a Virtual Environment

You can run this project within a virtual environment to manage its dependencies and isolate it from your system's global Python environment. Here are the steps to set up and run the project in a virtual environment:

1. Create a virtual environment (replace `venv` with your preferred environment name):

   ```bash
   python -m venv venv
   ```

2. Activate the virtual environment:

   - On Windows:

    ``` bash
     venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```bash
     source venv/bin/activate
     ```

Running the project within a virtual environment ensures that its dependencies do not interfere with your system-wide Python packages, making it easier to manage and maintain the project.

3. Follow the on-screen prompts to add, view, or calculate total marks for students.

## Usage

- When you run the project, you'll be presented with a menu that allows you to add student data, view data for a specific term, calculate total marks, and exit the program.

- You can customize the data structure by adding more subjects or terms to suit your requirements.

## File Structure

- `school_management_system.py`: The main Python script for the school management system.
- `data.json`: JSON file for storing student data.
- `school_management_system.exe`: Executable file for running the project on Windows.

## Contributing

If you'd like to contribute to this project, please open an issue or create a pull request. Contributions are welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```
