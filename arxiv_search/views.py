import ssl
import requests
import xml.etree.ElementTree as ET
import io
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Paper
from django.conf import settings
import os
from anthropic import Anthropic
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import base64
import spacy
import networkx as nx

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Disable SSL verification (use with caution)
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

def index(request):
    return render(request, 'arxiv_search/index.html')

def search_results(request):
    query = request.GET.get('query', '')
    if query:
        # arXiv API endpoint
        url = f'http://export.arxiv.org/api/query?search_query=all:{query}&start=0&max_results=10'
        
        # Make a GET request to the arXiv API
        response = requests.get(url)
        
        # Parse the XML response
        root = ET.fromstring(response.content)
        
        # Extract relevant information from the XML
        results = []
        for entry in root.findall('{http://www.w3.org/2005/Atom}entry'):
            title = entry.find('{http://www.w3.org/2005/Atom}title').text
            summary = entry.find('{http://www.w3.org/2005/Atom}summary').text
            link = entry.find('{http://www.w3.org/2005/Atom}id').text
            arxiv_id = link.split('/abs/')[-1]
            results.append({'title': title, 'summary': summary, 'link': link, 'arxiv_id': arxiv_id})
        
        return render(request, 'arxiv_search/search_results.html', {'results': results, 'query': query})
    else:
        return render(request, 'arxiv_search/search_results.html')

def paper_summary(request, paper_id):
    # Check if paper is already in database
    paper = Paper.objects.filter(arxiv_id=paper_id).first()
    if not paper:
        try:
            # Fetch the paper details from arXiv API
            url = f'http://export.arxiv.org/api/query?id_list={paper_id}'
            response = requests.get(url)
            root = ET.fromstring(response.content)
            
            entry = root.find('{http://www.w3.org/2005/Atom}entry')
            title = entry.find('{http://www.w3.org/2005/Atom}title').text
            summary = entry.find('{http://www.w3.org/2005/Atom}summary').text
            
            # Save to database
            paper = Paper.objects.create(arxiv_id=paper_id, title=title, summary=summary)
        except Exception as e:
            # Log the error (you might want to use proper logging here)
            print(f"Error processing paper {paper_id}: {str(e)}")
            # Return an error message to the user
            context = {
                'error_message': f"An error occurred while processing the paper: {str(e)}",
                'paper_id': paper_id,
                'query': request.GET.get('query', '')
            }
            return render(request, 'arxiv_search/error.html', context)

    context = {
        'paper': paper,
        'query': request.GET.get('query', '')
    }
    return render(request, 'arxiv_search/paper_summary.html', context)

def pdf_viewer(request, paper_id):
    paper = Paper.objects.get(arxiv_id=paper_id)
    pdf_url = f'https://arxiv.org/pdf/{paper_id}.pdf'
    context = {
        'paper': paper,
        'pdf_url': pdf_url
    }
    return render(request, 'arxiv_search/pdf_viewer.html', context)

def generate_wordcloud(request, paper_id):
    paper = Paper.objects.get(arxiv_id=paper_id)
    
    # Generate word cloud
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(paper.summary)
    
    # Create a plot
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    
    # Save the plot to a buffer
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    
    # Encode the image to base64
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
    
    context = {
        'paper': paper,
        'wordcloud_image': image_base64
    }
    return render(request, 'arxiv_search/wordcloud.html', context)

def generate_knowledge_graph(request, paper_id):
    paper = Paper.objects.get(arxiv_id=paper_id)
    
    # Process the text with spaCy
    doc = nlp(paper.summary)
    
    # Create a graph
    G = nx.Graph()
    
    # Add nodes and edges
    for sent in doc.sents:
        for token in sent:
            if token.dep_ in ('nsubj', 'nsubjpass', 'dobj', 'pobj'):
                G.add_edge(token.head.text, token.text)
    
    # Create a plot
    plt.figure(figsize=(16, 10))
    pos = nx.spring_layout(G, k=0.5, iterations=50)
    
    # Draw nodes
    nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=3000, alpha=0.8)
    
    # Draw edges
    nx.draw_networkx_edges(G, pos, edge_color='gray', width=1, alpha=0.5)
    
    # Draw labels
    nx.draw_networkx_labels(G, pos, font_size=8, font_weight='bold')
    
    # Remove axis
    plt.axis('off')
    
    # Save the plot to a buffer
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png', dpi=300, bbox_inches='tight')
    buffer.seek(0)
    
    # Encode the image to base64
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
    
    context = {
        'paper': paper,
        'knowledge_graph_image': image_base64
    }
    return render(request, 'arxiv_search/knowledge_graph.html', context)

@csrf_exempt
def chat(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_message = data['message']
        paper_id = data['paper_id']
        
        # Retrieve the paper summary from the database
        paper = Paper.objects.get(arxiv_id=paper_id)
        
        # Prepare the prompt for Claude
        prompt = f"""Human: Given the following paper title and summary, please answer the user's question:

Paper title: {paper.title}
Summary: {paper.summary}

User question: {user_message}
"""
        
        # Call Claude API
        client = Anthropic(api_key=settings.ANTHROPIC_API_KEY)
        response = client.completions.create(
            model="claude-2.1",
            prompt=prompt,
            max_tokens_to_sample=300
        )
        
        ai_response = response.completion
        
        return JsonResponse({'response': ai_response})