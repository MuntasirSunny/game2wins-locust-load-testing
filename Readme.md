# Game2wins Load Testing

This project uses Locust to simulate user traffic to the Game2Wins website and its APIs.

## Overview

The `game2wins.py` script defines two types of users for load testing:

1.  **WebsiteUser**: Simulates users browsing the main Game2Wins website.
2.  **ApiUser**: Simulates API traffic to the game2wins CMS endpoints.

## Prerequisites

- Python 3.x
- pip

## Setup

1.  **Create a virtual environment:**

    ```bash
    python -m venv myenv
    ```

    # or,
    ```bash
    python3 -m venv myenv
    ```
    # Initiating virtual Environment:
    source myenv/bin/activate

    # Deactivate Virtual Environment: 
    deactivate


2.  **Activate the virtual environment:**

    - On macOS and Linux:
      ```bash
      source myenv/bin/activate
      ```
    - On Windows:
      ```bash
      .\myenv\Scripts\activate
      ```

3.  **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

## Running the Load Test

1.  **Start Locust:**

    Once the setup is complete, you can start the Locust load test with the following command:

    ```bash
    locust -f game2wins.py
    ```

2.  **Open the Locust web interface:**

    Open your web browser and go to [http://localhost:8089](http://localhost:8089).

3.  **Configure and start the test:**

    - Enter the number of users to simulate.
    - Enter the spawn rate (users to start per second).
    - Click "Start swarming" to begin the test.
