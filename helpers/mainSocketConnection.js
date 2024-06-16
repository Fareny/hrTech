import { io } from 'socket.io-client';

class SocketService {
    constructor() {
        this.socket = null;
        this.isConnected = false;
    }

    async connect(url) {
        if (!this.socket) {
            return new Promise((resolve, reject) => {
                this.socket = io(url, {
                    transports: ['websocket'],
                    reconnectionAttempts: 5
                });

                this.socket.on('connect', () => {
                    this.isConnected = true;
                    console.log('Connected to socket server');
                    resolve(this.socket);
                });

                this.socket.on('connect_error', (error) => {
                    console.error('Connection error:', error);
                    this.isConnected = false;
                    reject(error);
                });
            });
        } else {
            return Promise.resolve(this.socket);
        }
    }

    disconnect() {
        if (this.socket) {
            this.socket.disconnect();
            this.socket = null;
            this.isConnected = false;
        }
    }

    sendEvent(event, data) {
        if (this.socket) {
            this.socket.emit(event, data);
        }
    }

    onEvent(event, callback) {
        if (this.socket) {
            this.socket.on(event, callback);
        }
    }

    offEvent(event, callback) {
        if (this.socket) {
            this.socket.off(event, callback);
        }
    }
}

export default new SocketService();
