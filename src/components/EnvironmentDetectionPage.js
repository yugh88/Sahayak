import React from "react";

function EnvironmentDetectionPage() {
  return (
    <div className="environment-detection-page">
      <h1>Environment Detection</h1>
      <div className="camera-feed">
        <p>Camera feed here (CV backend integration required).</p>
      </div>
      <div className="output">
        <h3>Detected Object:</h3>
        <p>Object text will appear here...</p>
      </div>
    </div>
  );
}

export default EnvironmentDetectionPage;