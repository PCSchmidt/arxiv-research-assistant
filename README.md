# Research Assistant App

This Django-based web application serves as a Research Assistant, allowing users to search for academic papers using the arXiv API, summarize them, interact with the content through a chat interface, view the full PDF of selected papers, and generate word clouds for paper summaries.

## Current Features

1. **ArXiv Paper Search**: Users can search for research papers using keywords.
2. **Paper Summaries**: The app displays summaries of selected papers.
3. **Chat Interface**: Users can ask questions about the papers using a chat interface powered by the Claude AI model.
4. **PDF Viewer**: Users can view the full PDF of selected papers directly in the browser.
5. **Word Cloud Generation**: Users can generate and view word clouds for paper summaries.

## Planned Features

1. **Knowledge Graph**: Create and display a knowledge graph representing the paper's content and relationships.

## Project Structure

```
arxiv_app/
│
├── research_assistant/    # Main Django project directory
│   ├── __init__.py
│   ├── settings.py        # Project settings
│   ├── urls.py            # Main URL configuration
│   └── wsgi.py
│
├── arxiv_search/          # Django app for arXiv search functionality
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py          # Defines the Paper model
│   ├── views.py           # View functions for search, summary, chat, PDF viewer, and word cloud
│   ├── urls.py            # URL patterns for the app
│   └── templates/         # HTML templates
│       └── arxiv_search/
│           ├── index.html
│           ├── search_results.html
│           ├── paper_summary.html
│           ├── pdf_viewer.html
│           └── wordcloud.html
│
├── static/                # Static files (CSS, JavaScript)
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── main.js
│
├── manage.py              # Django management script
├── requirements.txt       # Project dependencies
└── README.md              # This file
```

## Setup and Installation

1. Clone the repository
2. Create a virtual environment and activate it
3. Install the required packages: `pip install -r requirements.txt`
4. Set up your environment variables, including the `ANTHROPIC_API_KEY` for Claude AI
5. Run migrations: `python manage.py migrate`
6. Start the development server: `python manage.py runserver`

## Path to Completion

To complete the project with the planned features, follow these steps:

1. ~~**PDF Viewer Integration**~~ (Completed)
   - ~~Implement a PDF viewer using a library like PDF.js~~
   - ~~Update the `paper_summary` view to fetch and serve the PDF file~~
   - ~~Create a new template for displaying the PDF~~

2. ~~**Word Cloud Generation**~~ (Completed)
   - ~~Install and configure a word cloud generation library (wordcloud)~~
   - ~~Create a new view and URL for generating word clouds~~
   - ~~Implement word cloud generation logic using paper content~~
   - ~~Display the generated word cloud on a separate page~~

3. **Knowledge Graph Creation**
   - Research and choose an appropriate library for knowledge graph generation
   - Create a new view and URL for generating knowledge graphs
   - Implement logic to extract key concepts and relationships from paper content
   - Generate and display the knowledge graph on the paper summary page

4. **UI/UX Improvements**
   - Enhance the user interface to incorporate the new features
   - Ensure responsive design for various device sizes
   - Implement loading indicators for asynchronous operations

5. **Testing and Optimization**
   - Write unit tests for new functionality
   - Perform thorough testing of all features
   - Optimize performance, especially for resource-intensive operations like PDF rendering and graph generation

6. **Documentation**
   - Update this README with detailed information on new features
   - Create user documentation explaining how to use all features of the application

7. **Deployment**
   - Prepare the application for production deployment
   - Set up a production-ready database
   - Configure static file serving for production
   - Deploy the application to a suitable hosting platform

By following this path, you'll be able to transform the current Research Assistant app into a comprehensive tool that not only searches and summarizes papers but also provides advanced features like PDF viewing, word clouds, and knowledge graphs.

## Using the PDF Viewer

To view the PDF of a paper:
1. Search for a paper using the search functionality.
2. Click on a paper title to view its summary.
3. On the paper summary page, click the "View PDF" link.
4. The PDF will open in a new tab, allowing you to read the full paper directly in your browser.

Note: The PDF viewer uses PDF.js to render PDFs in the browser, ensuring compatibility across different devices and platforms.

## Using the Word Cloud Generator

To generate and view a word cloud for a paper:
1. Search for a paper using the search functionality.
2. Click on a paper title to view its summary.
3. On the paper summary page, click the "View Word Cloud" link.
4. A new page will open, displaying the generated word cloud for the paper's summary.

The word cloud provides a visual representation of the most frequent words in the paper's summary, giving you a quick overview of the main topics and themes of the paper.# arxiv-research-assistant
