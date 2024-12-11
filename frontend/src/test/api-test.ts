import { api, WebSocketClient } from '../lib/api';

async function testAPI() {
  try {
    // Test getData
    console.log('Testing getData...');
    const data = await api.getData();
    console.log('getData result:', data);

    // Test addColumn
    console.log('\nTesting addColumn...');
    await api.addColumn({
      name: 'Test Column',
      extraction_key: 'test_key'
    });
    console.log('Column added successfully');

    // Test addRow
    console.log('\nTesting addRow...');
    await api.addRow('https://example.com');
    console.log('Row added successfully');

    // Test WebSocket
    console.log('\nTesting WebSocket connection...');
    const ws = new WebSocketClient((data) => {
      console.log('WebSocket message received:', data);
    });
    ws.connect();

    // Keep connection open for a few seconds to test updates
    await new Promise(resolve => setTimeout(resolve, 5000));
    ws.disconnect();
    console.log('WebSocket test completed');

  } catch (error) {
    console.error('Test failed:', error);
  }
}

testAPI();
