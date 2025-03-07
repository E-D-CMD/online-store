const socket = io();

button.addEventListener('click', () => {
    const message = input.value.trim();
    if (message) {
        socket.emit('message', message);
        input.value = '';
    }
});

socket.on('message', (msg) => {
    const newMessage = document.createElement('div');
    newMessage.textContent = msg;
    messages.appendChild(newMessage);
});
