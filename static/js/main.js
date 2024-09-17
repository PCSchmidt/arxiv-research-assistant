console.log("Research Assistant app is running!");

function sendMessage() {
    const userInput = document.getElementById('user-input');
    const chatMessages = document.getElementById('chat-messages');
    
    if (userInput.value.trim() === '') return;
    
    // Add user message to chat
    chatMessages.innerHTML += `<p><strong>You:</strong> ${userInput.value}</p>`;
    
    // Send request to backend
    fetch('/chat/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: JSON.stringify({
            message: userInput.value,
            paper_id: document.body.dataset.paperId
        })
    })
    .then(response => response.json())
    .then(data => {
        // Add AI response to chat
        chatMessages.innerHTML += `<p><strong>AI:</strong> ${data.response}</p>`;
    })
    .catch(error => console.error('Error:', error));
    
    userInput.value = '';
}

// Function to get CSRF token
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}