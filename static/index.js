document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('sendButton').addEventListener('click', sendMessage);
    document.getElementById('messageInput').addEventListener('keypress', function(event) {
        if (event.key === 'Enter') {
            event.preventDefault();
            sendMessage();
        }
    });
});

async function sendMessage() {
    const messageInput = document.getElementById('messageInput');
    const message = messageInput.value.trim();
    if (!message) return;

    addMessageToChat('You', message);

    const responseElement = document.createElement('div');
    responseElement.className = 'message bot-message';
    responseElement.innerHTML = `
        <div class="message-content">
            <div class="typing">
                <div class="typing-animation"></div>
                <div class="typing-animation"></div>
                <div class="typing-animation"></div>
            </div>
        </div>
    `;
    document.getElementById('chat-box').appendChild(responseElement);
    document.getElementById('chat-box').scrollTop = document.getElementById('chat-box').scrollHeight;

    try {
        const response = await fetch('/api/chatbot', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ message })
        });

        if (response.ok) {
            const data = await response.json();
            setTimeout(() => {
                responseElement.innerHTML = `
                    <div class="message-content">
                        <div class="message-text">${data.message}</div>
                        <img class="avatar bot-avatar" src="https://img.icons8.com/ios-filled/50/000000/bot.png" alt="Bot">
                    </div>
                `;
            }, 1000); // Simulate typing delay
        } else {
            responseElement.innerHTML = 'Error: ' + response.statusText;
        }
    } catch (error) {
        responseElement.innerHTML = 'Error: ' + error.message;
    }

    messageInput.value = '';
}

function addMessageToChat(sender, message) {
    const chatBox = document.getElementById('chat-box');
    const messageElement = document.createElement('div');
    messageElement.className = sender === 'You' ? 'message user-message' : 'message bot-message';
    messageElement.innerHTML = `
        <div class="message-content">
            ${sender === 'You' ? `<img class="avatar user-avatar" src="https://img.icons8.com/ios-filled/50/000000/user.png" alt="User">` : ''}
            <div class="message-text">${message}</div>
            ${sender === 'Bot' ? `<img class="avatar bot-avatar" src="https://img.icons8.com/ios-filled/50/000000/bot.png" alt="Bot">` : ''}
        </div>
    `;
    chatBox.appendChild(messageElement);
    chatBox.scrollTop = chatBox.scrollHeight;
}