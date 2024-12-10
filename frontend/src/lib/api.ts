const API_BASE_URL = 'http://localhost:8000';
const WS_BASE_URL = 'ws://localhost:8000';

export interface Column {
  id?: string;
  name: string;
  extraction_key?: string;  // Optional since it's generated server-side
}

export interface Row {
  id: string;
  website: string;
  data: Record<string, string | number | boolean | null>;
}

export interface GridData {
  columns: Column[];
  rows: Row[];
}

export interface WebSocketMessage {
  type: 'update' | 'error';
  data?: GridData;
  error?: string;
}

export const api = {
  async getData(): Promise<GridData> {
    const response = await fetch(`${API_BASE_URL}/api/data`);
    if (!response.ok) {
      throw new Error('Failed to fetch data');
    }
    return response.json();
  },

  async addColumn(name: string): Promise<void> {
    const response = await fetch(`${API_BASE_URL}/api/columns`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ name }),
    });
    if (!response.ok) {
      throw new Error('Failed to add column');
    }
  },

  async addRow(website: string): Promise<void> {
    const response = await fetch(`${API_BASE_URL}/api/rows`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ website }),
    });
    if (!response.ok) {
      throw new Error('Failed to add row');
    }
  },

  async clearColumns(): Promise<void> {
    const response = await fetch(`${API_BASE_URL}/api/columns`, {
      method: 'DELETE',
    });
    if (!response.ok) {
      throw new Error('Failed to clear columns');
    }
  }
};

export class WebSocketClient {
  private ws: WebSocket | null = null;
  private reconnectTimeoutId: number | null = null;

  constructor(private onMessage: (data: WebSocketMessage) => void) {}

  connect() {
    if (this.ws) return;

    this.ws = new WebSocket(`${WS_BASE_URL}/ws/updates`);

    this.ws.onmessage = (event) => {
      try {
        const data = JSON.parse(event.data) as WebSocketMessage;
        this.onMessage(data);
      } catch (error) {
        console.error('Failed to parse WebSocket message:', error);
      }
    };

    this.ws.onclose = () => {
      this.ws = null;
      this.scheduleReconnect();
    };

    this.ws.onerror = (error) => {
      console.error('WebSocket error:', error);
      this.ws?.close();
    };
  }

  private scheduleReconnect() {
    if (this.reconnectTimeoutId) return;
    this.reconnectTimeoutId = window.setTimeout(() => {
      this.reconnectTimeoutId = null;
      this.connect();
    }, 5000);
  }

  disconnect() {
    if (this.reconnectTimeoutId) {
      window.clearTimeout(this.reconnectTimeoutId);
      this.reconnectTimeoutId = null;
    }
    this.ws?.close();
    this.ws = null;
  }
}
