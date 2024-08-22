# Predictive Maintenance for Turbofan Engines

This project demonstrates a predictive maintenance model for turbofan engines. The project includes a Flask web application that allows users to input features from turbofan engine data and predict the Remaining Useful Life (RUL) of the engine. The project includes feature importance visualization and comparison of predictions vs. true values.

## Features
- Predict RUL based on different datasets (FD001, FD002, FD003, FD004)
- Visualize feature importance for each prediction
- Compare predicted vs. true RUL values

## Installation

### Local Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/my_project.git
   cd my_project
   ```

2. Create a virtual environment and activate it:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python app.py
   ```

5. Open a web browser and go to `http://localhost:8080`.

### Docker Deployment
1. Build the Docker image:
   ```bash
   docker build -t turbofan-predictor .
   ```

2. Run the Docker container:
   ```bash
   docker run -p 8080:8080 turbofan-predictor
   ```

3. Access the application at `http://localhost:8080`.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- This project is based on data from the NASA Prognostics Data Repository.
- Special thanks to the authors of the C-MAPSS datasets for their contributions to predictive maintenance research.
