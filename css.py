body {
  font-family: Arial, sans-serif;
  background: #f5f5f5;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

.chat-container {
  width: 400px;
  background: white;
  border-radius: 12px;
  box-shadow: 0px 4px 10px rgba(0,0,0,0.2);
  display: flex;
  flex-direction: column;
  overflow: hidden;
}

.chat-box {
  padding: 10px;
  height: 400px;
  overflow-y: auto;
  border-bottom: 1px solid #ddd;
}

.user-message {
  text-align: right;
  margin: 5px;
  padding: 8px;
  background: #007bff;
  color: white;
  border-radius: 8px;
  display: inline-block;
}

.bot-message {
  text-align: left;
  margin: 5px;
  padding: 8px;
  background: #eaeaea;
  border-radius: 8px;
  display: inline-block;
}

.input-container {
  display: flex;
  border-top: 1px solid #ddd;
}

input {
  flex: 1;
  padding: 10px;
  border: none;
  outline: none;
}

button {
  padding: 10px;
  border: none;
  background: #007bff;
  color: white;
  cursor: pointer;
}
