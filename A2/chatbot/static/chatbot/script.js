document.addEventListener('DOMContentLoaded', function() {
    const chatBox = document.getElementById('chat-box');
    const userInput = document.getElementById('user-input');
    const sendBtn = document.getElementById('send-btn');
    const clearBtn = document.getElementById('clear-btn');
    
    function appendMessage(sender, message, timestamp) {
        const messageDiv = document.createElement('div');
        messageDiv.classList.add('message');
        messageDiv.classList.add(sender === 'user' ? 'user-message' : 'bot-message');
        
        const timeSpan = document.createElement('span');
        timeSpan.classList.add('timestamp');
        timeSpan.textContent = timestamp;
        
        messageDiv.innerHTML = `${message}<br>`;
        messageDiv.appendChild(timeSpan);
        
        chatBox.appendChild(messageDiv);
        chatBox.scrollTop = chatBox.scrollHeight;
    }
    
    function sendMessage() {
        const message = userInput.value.trim();
        if (message === '') return;
        
        const now = new Date();
        const timestamp = now.toLocaleTimeString();
        
        // Display user message
        appendMessage('user', message, timestamp);
        userInput.value = '';
        
        // Send to server and get response
        fetch('/get-response/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-CSRFToken': getCookie('csrftoken'),
            },
            body: `message=${encodeURIComponent(message)}`
        })
        .then(response => response.json())
        .then(data => {
            appendMessage('bot', data.response, data.timestamp);
        })
        .catch(error => {
            console.error('Error:', error);
            appendMessage('bot', "Sorry, I'm having trouble responding right now.", new Date().toLocaleTimeString());
        });
    }
    
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
    
    function clearChat() {
        chatBox.innerHTML = '';
    }
    
    // Event listeners
    sendBtn.addEventListener('click', sendMessage);
    userInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            sendMessage();
        }
    });
    clearBtn.addEventListener('click', clearChat);
});