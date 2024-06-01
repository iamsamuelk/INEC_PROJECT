## INEC_PROJECT

Welcome to the INEC_PROJECT, a FastAPI-based web application for viewing and managing election results for polling units and LGAs (Local Government Areas). The portal allows users to view individual polling unit results, view summed total results for an LGA, and add new results for polling units.

### Project Features

- **View Results for a Polling Unit:** Users can select a polling unit and view its results.
- **View Summed Total Results for an LGA:** Users can select an LGA and view the summed total results of all polling units under it.
- **Add New Polling Unit Results:** Users can add new results for a polling unit via a form submission.

### Live Demo

The project is hosted at: [INEC Project](https://inec-project.onrender.com/)

### Tech Stack

- **Backend:** FastAPI
- **Database:** PostgreSQL
- **Frontend:** HTML, CSS, Jinja2 Templates
- **Hosting:** Render

### Getting Started

#### Prerequisites

- Python 3.11.5
- PostgreSQL database

#### Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/iamsamuelk/INEC_PROJECT.git
   cd INEC_PROJECT
   ```

2. **Create and activate a virtual environment:**

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

4. **Set up the database:**

   Update the `SQLALCHEMY_DATABASE_URL` in `main.py` with your PostgreSQL database URL.

5. **Run the application:**

   ```sh
   uvicorn main:app --reload
   ```

   The application will be available at `http://127.0.0.1:8000`.

### Usage

1. **Home Page:**

   Visit the home page at `http://127.0.0.1:8000/`. You will see links to view polling unit results, LGA results, and add new polling unit results.

2. **View Polling Unit Results:**

   - Click on "View Results for a Polling Unit".
   - Select a polling unit from the dropdown and view its results.

3. **View LGA Results:**

   - Click on "View Summed Total Results for an LGA".
   - Select an LGA from the dropdown and view the summed total results of all polling units under it.

4. **Add New Polling Unit Results:**

   - Click on "Add New Polling Unit Results".
   - Fill out the form with the polling unit unique ID, party abbreviation, party score, and entered by user information.
   - Submit the form to add the new results.


### Acknowledgements

This project was developed to manage and display election results for polling units and LGAs. Special thanks to BINCOM for giving this as a project and the FastAPI community for their support and resources.


For any questions or issues, please open an issue on the GitHub repository or contact the maintainer.


Enjoy using the INEC_PROJECT!