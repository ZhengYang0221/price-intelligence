import { useEffect, useState } from "react";

function App() {
  const [status, setStatus] = useState("loading");

  useEffect(() => {
    fetch("http://localhost:8000/health")
      .then(res => res.json())
      .then(data => setStatus(data.status))
      .catch(() => setStatus("error"));
  }, []);

  return (
    <div style={{ padding: "2rem" }}>
      <h1>Price Intelligence</h1>
      <p>Backend health: {status}</p>
    </div>
  );
}

export default App;
