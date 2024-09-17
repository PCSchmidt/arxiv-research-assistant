# Research Assistant App

This Django-based web application serves as a Research Assistant, allowing users to search for academic papers using the ArXiv API, summarize them, interact with the content through a chat interface, view the full PDF of selected papers, generate word clouds for paper summaries, and create knowledge graphs representing the paper's content and relationships.

## Current Features

1. **ArXiv Paper Search**: Users can search for research papers using keywords.
2. **Paper Summaries**: The app displays summaries of selected papers.
3. **Chat Interface**: Users can ask questions about the papers using a chat interface powered by the Claude AI model.
4. **PDF Viewer**: Users can view the full PDF of selected papers directly in the browser.
5. **Word Cloud Generation**: Users can generate and view word clouds for paper summaries.
6. **Knowledge Graph Creation**: Users can view knowledge graphs representing the paper's content and relationships.

## Setup and Installation

1. Clone the repository
2. Create a virtual environment and activate it
3. Install the required packages: `pip install -r requirements.txt`
4. Create a `.env` file in the root directory and add the following:
   ```
   SECRET_KEY=your_secret_key_here
   OPENAI_API_KEY=your_openai_api_key_here
   ANTHROPIC_API_KEY=your_anthropic_api_key_here
   ```
5. Run migrations: `python manage.py migrate`
6. Start the development server: `python manage.py runserver`

## Usage

1. **Search for Papers**: 
   - Go to the home page and enter your search query.
   - Click on a paper title to view its summary.

2. **View Paper Summary**:
   - On the paper summary page, you'll see options to view the PDF, generate a word cloud, and create a knowledge graph.

3. **PDF Viewer**:
   - Click "View PDF" on the paper summary page.
   - The PDF will open in a new tab, allowing you to read the full paper.
   - Use the "Back to Paper Summary" button to return to the summary page.

4. **Word Cloud Generation**:
   - Click "View Word Cloud" on the paper summary page.
   - A new page will open, displaying the generated word cloud for the paper's summary.

5. **Knowledge Graph**:
   - Click "View Knowledge Graph" on the paper summary page.
   - A new page will open, showing the generated knowledge graph representing key concepts and relationships in the paper.

6. **Chat Interface**:
   - On the paper summary page, use the chat interface to ask questions about the paper.
   - The AI-powered assistant will provide answers based on the paper's content.

## Troubleshooting

If you encounter any issues:

1. Ensure all required packages are installed and up to date.
2. Check that your `.env` file contains the necessary API keys and secret key.
3. Make sure you've applied all migrations.
4. Clear your browser cache if you're experiencing front-end issues.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).

