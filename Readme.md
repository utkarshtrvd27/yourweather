# FRONTEND
## Steps to Run the Frontend Application

1. **Install Dependencies**  
    Navigate to the project directory and run the following command to install the required dependencies:
    ```bash
    npm install
    ```

2. **Start the Development Server**  
    Use the following command to start the development server:
    ```bash
    npm start
    ```

3. **Access the Application**  
    Open your web browser and go to `http://localhost:5500` to view the application.

4. **Build for Production**  
    To create a production build, run:
    ```bash
    npm run build
    ```

5. **Serve the Production Build**  
    Use a static server to serve the production build, or deploy it to your preferred hosting platform.




# BACKEND
## Steps to Run the Backend Application

1. **Set Up a Virtual Environment**  
    Navigate to the backend project directory and create a virtual environment:
    ```bash
    python -m venv venv
    ```

2. **Activate the Virtual Environment**  
    Activate the virtual environment using the following command:
    - On Windows:
      ```bash
      venv\Scripts\activate
      ```
    - On macOS/Linux:
      ```bash
      source venv/bin/activate
      ```

3. **Install Dependencies**  
    Install the required Python packages by running:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set Up Environment Variables**  
    Create a `.env` file in the backend directory and add the necessary environment variables. For example:
    ```properties
    FLASK_APP=app.py
    FLASK_ENV=development
    TOMORROW_API_KEY=<your_API_key>
    OPENWEATHER_API_KEY=<your_API_key>
    ```

    Flask will automatically load the `.env` file when you run the application.

5. **Run the Application**  
    Start the Flask development server:
    ```bash
    flask run
    ```

6. **Access the API**  
    Open your web browser or API client and go to `http://127.0.0.1:5000` to interact with the backend API.